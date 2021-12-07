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

user_post_args = reqparse.RequestParser()
user_post_args.add_argument("adresse_mail",type=str,required=True)
user_post_args.add_argument("mdp",type=str,required=True)
user_post_args.add_argument("lastname",type=str,required=True)
user_post_args.add_argument("firstname",type=str,required=True)
user_post_args.add_argument("age",type=int,required=True)
user_post_args.add_argument("avatar",type=int,required=True)

class user(Resource):
	def post(self): #s_inscrire
		body = user_post_args.parse_args()
		[adresse_mail,mdp,lastname,firstname,age,avatar] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le joueur n'est pas déjà enregistré
		mycursor.execute("SELECT count(*) FROM Player WHERE adresse_mail = \""+adresse_mail+"\"")
		resultat1 = mycursor.fetchall()[0][0]
		if resultat1:
			return {"retour":"l'adresse mail est déjà enregistrée'"}

		#Je vérifie que le format des informations renseignées est conforme.
		if not adresse_mail.count("@"):
			return {"retour":"l'adresse mail n'est pas conforme"}
		cut = adresse_mail.split("@")
		if not len(cut[0]) or not len(cut[-1]):
			return {"retour":"l'adresse mail n'est pas conforme"}

		if len(mdp) <= 6:
			return {"retour":"le mot de passe doit faire au moins 6 caractères"}
		if [lastname,firstname].count(""):
			return {"retour":"Le nom ou le prenom est vide"}
		if not (6 < age < 100) :
			return {"retour":"l'age renseigné n'est pas valide"}
		if not [0,1,2].count(avatar):
			return {"retour":"l'avatar renseigné n'est pas connu"}

		#Je crée un code que j'envoie par mail et l'enregistre dans la table Adresse_mail_non_verif.
		lettres = list("abcdefghijklmnopqrstuvwxyz")
		nombres = list("0123456789")
		caracteres = list("éè_àù")
		n_l,n_n,n_c = choice(range(5,8)),choice(range(3,6)),choice(range(1,3))
		code = [choice(lettres) for i in range(n_l)]+[choice(nombres) for i in range(n_n)]+[choice(caracteres) for i in range(n_c)]
		shuffle(code)
		code = "".join(code)

		#Envoie par mail 
		obj = "Vérification d'adresse mail"
		envoyer_email("Pour vérifier votre adresse mail, veuillez renseigner le code : "+code,obj,adresse_mail)
		ajouter_Adresse_mail_non_verif(adresse_mail,code,mycursor,mydb)

		#J'ajoute une ligne à la table professeur.
		ajouter_Player(adresse_mail,mdp,lastname,firstname,age,avatar,mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

