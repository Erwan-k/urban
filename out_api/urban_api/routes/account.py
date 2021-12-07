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

account_get_args = reqparse.RequestParser()
account_get_args.add_argument("token",type=str,required=True)
account_put_args = reqparse.RequestParser()
account_put_args.add_argument("token",type=str,required=True)
account_put_args.add_argument("lastname",type=str,required=True)
account_put_args.add_argument("firstname",type=str,required=True)
account_put_args.add_argument("age",type=int,required=True)
account_put_args.add_argument("avatar",type=int,required=True)

class account(Resource):
	def get(self): #recuperer_ses_infos_perso
		body = account_get_args.parse_args()
		[token] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token exite et je récupère l'adresse mail du player.
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ =\""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token specifiee n'est pas connue de notre bdd"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ =\""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je récupère les informations de mon joueur
		if True:
			mycursor.execute("SELECT lastname,firstname,age,avatar FROM Player WHERE adresse_mail = \""+adresse_mail+"\"")
			[lastname,firstname,age,avatar] = mycursor.fetchall()[0]
			s = {"nom":lastname,"prenom":firstname,"age":age,"avatar":avatar}

		mycursor.close()
		mydb.close()

		return {"retour":"ok","valeur":s}
	def put(self): #modifier_une_info_perso
		body = account_put_args.parse_args()
		[token,lastname,firstname,age,avatar] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token exite et je récupère l'adresse mail du player.
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ =\""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token specifiee n'est pas connue de notre bdd"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ =\""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que les informations transmises sont conformes
		if True:
			if age != -1:
				if not (6 < int(age) < 100) :
					return {"retour":"l'age renseigné n'est pas valide"}
			if avatar != -1:
				if not [0,1,2].count(avatar):
					return {"retour":"l'avatar renseigné n'est pas connu"}

		#Je modifie les informatiosn souhaités
		if True:
			if len(lastname):
				mycursor.execute("UPDATE Player SET lastname = \""+lastname+"\" WHERE adresse_mail = \""+adresse_mail+"\"")
				mydb.commit()
			if len(firstname):
				mycursor.execute("UPDATE Player SET firstname = \""+firstname+"\" WHERE adresse_mail = \""+adresse_mail+"\"")
				mydb.commit()
			if age != -1:
				mycursor.execute("UPDATE Player SET age = "+str(age)+" WHERE adresse_mail = \""+adresse_mail+"\"")
				mydb.commit()
			if avatar != -1:
				mycursor.execute("UPDATE Player SET avatar = "+str(avatar)+" WHERE adresse_mail = \""+adresse_mail+"\"")
				mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

