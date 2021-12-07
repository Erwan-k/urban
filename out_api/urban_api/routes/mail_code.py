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

mail_code_get_args = reqparse.RequestParser()
mail_code_get_args.add_argument("adresse_mail",type=str,required=True)
mail_code_delete_args = reqparse.RequestParser()
mail_code_delete_args.add_argument("code",type=str,required=True)

class mail_code(Resource):
	def get(self): #demander_un_nouvel_email_de_confirmation
		body = mail_code_get_args.parse_args()
		[adresse_mail] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que l'adresse mail existe dans la table player.
		mycursor.execute("SELECT count(*) FROM Player WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail specifiee n'est pas connue de notre bdd"}

		#Je vérifie que l'adresse mail existe toujours dans la table Adresse_mail_non_verif.
		mycursor.execute("SELECT count(*) FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"l'adresse mail est déjà vérifiée"}

		#Je récupère le code et le renvoie par mail.
		mycursor.execute("SELECT code FROM Adresse_mail_non_verif WHERE adresse_mail = \""+adresse_mail+"\"")
		code = mycursor.fetchall()[0][0]

		obj = "Vérification d'adresse mail"
		envoyer_email("Pour vérifier votre adresse mail, veuillez renseigner le code : "+code,obj,adresse_mail)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}
			
	def delete(self): #verifier_son_adresse_mail
		body = mail_code_delete_args.parse_args()
		[code] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le code existe dans la table et le supprime dans ce cas.
		mycursor.execute("DELETE FROM Adresse_mail_non_verif WHERE code = \""+code+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}


