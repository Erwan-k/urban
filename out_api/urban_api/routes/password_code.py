from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
from random import choice,shuffle
import requests
import json

def getMysqlConnection():
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
	return mydb

def mycursor_execute(sql,mycursor):
	try:
		mycursor.execute(sql)
		return {"statut":True}
	except Exception as e:
		return {"statut":False,"erreur":e}

def mycursor_fetchall(mycursor):
	try:
		s = mycursor.fetchall()
		return {"statut":True,"retour":s}
	except Exception as e:
		return {"statut":False,"erreur":e}

def mydb_commit(mydb):
	try:
		mydb.commit()
		return {"statut":True}
	except Exception as e:
		return {"statut":False,"erreur":e}

def envoyer_email(contenu,objet,adresse_mail):
	x = requests.post("http://api_mail_sender:5003/fonction_1", data = {'adresse_mail_receveur': adresse_mail,'objet':objet,'contenu_mail':contenu})
	retour = json.loads(x.text)

from ajouter_valeurs import *

password_code_post_args = reqparse.RequestParser()
password_code_post_args.add_argument("adresse_mail",type=str,required=True)

class password_code(Resource):
	def post(self): #demander_un_code_pour_changer_son_mot_de_passe
		body = password_code_post_args.parse_args()
		[adresse_mail] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse mail existe dans la table player.
		mycursor.execute("SELECT count(*) FROM Player WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse_mail n'existe plus dans la table Adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail n'a pas été vérifiée"}

		#Je vérifie qu'un code n'existe pas déjà.
		mycursor.execute("SELECT count(*) FROM Changement_de_mot_de_passe WHERE adresse_mail = \""+adresse_mail+"\"")

		#Si oui, je le récupère et le renvoie par mail.
		if mycursor.fetchall()[0][0]:

			mycursor.execute("SELECT code FROM Changement_de_mot_de_passe WHERE adresse_mail = \""+adresse_mail+"\"")
			code = mycursor.fetchall()[0][0]
			obj = "Reception d'un code pour changer de mot de masse"
			#envoyer_email("Pour changer votre mot de passe, veuillez renseigner le code : "+code+" à la page http://neo.erwankerbrat.com/gestion_mdp",obj,adresse_mail)

		#Si non, j'en crée un et l'envoie par mail.
		else:
			lettres = list("abcdefghijklmnopqrstuvwxyz")
			nombres = list("0123456789")
			caracteres = list("éè_àù")
			n_l,n_n,n_c = choice(range(5,8)),choice(range(3,6)),choice(range(1,3))
			code = [choice(lettres) for i in range(n_l)]+[choice(nombres) for i in range(n_n)]+[choice(caracteres) for i in range(n_c)]
			shuffle(code)
			code = "".join(code)

			ajouter_Changement_de_mot_de_passe(adresse_mail,code,mycursor,mydb)
			obj = "Reception d'un code pour changer de mot de masse"
			envoyer_email("Pour changer votre mot de passe, veuillez renseigner le code : "+code,obj,adresse_mail)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

