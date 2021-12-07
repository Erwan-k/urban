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

login_get_args = reqparse.RequestParser()
login_get_args.add_argument("adresse_mail",type=str,required=True)
login_get_args.add_argument("mdp",type=str,required=True)

class login(Resource):
	def get(self): #se_connecter
		body = login_get_args.parse_args()
		[adresse_mail,mdp] = [body[i] for i in body]
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

		#Je vérifie que le mot de passe est le bon.
		mycursor.execute("SELECT count(*) FROM Player WHERE adresse_mail = \""+adresse_mail+"\" AND mdp = \""+mdp+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"le mot de passe specifie n'est pas le bon"}

		#Je supprime les enventuels anciens token.
		mycursor.execute("DELETE FROM Token WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		#Je génére un token et l'enregistre dans la table token.
		lettres = list("abcdefghijklmnopqrstuvwxyz")
		nombres = list("0123456789")
		caracteres = list("éè_àù")
		n_l,n_n,n_c = choice(range(5,8)),choice(range(3,6)),choice(range(1,3))
		token = [choice(lettres) for i in range(n_l)]+[choice(nombres) for i in range(n_n)]+[choice(caracteres) for i in range(n_c)]
		shuffle(token)
		token = "".join(token)
		ajouter_Token(adresse_mail,token,mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok","token":token}

