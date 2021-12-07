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

password_put_args = reqparse.RequestParser()
password_put_args.add_argument("adresse_mail",type=str,required=True)
password_put_args.add_argument("code",type=str,required=True)
password_put_args.add_argument("nouveau_mdp",type=str,required=True)
password2_put_args = reqparse.RequestParser()
password2_put_args.add_argument("adresse_mail",type=str,required=True)
password2_put_args.add_argument("ancien_mdp",type=str,required=True)
password2_put_args.add_argument("nouveau_mdp",type=str,required=True)

class password(Resource):
	def put(self): #changer_son_mot_de_passe_a_l_aide_d_un_code
		body = password_put_args.parse_args()
		[adresse_mail,code,nouveau_mdp] = [body[i] for i in body]
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

		#Je vérifie que le format du nouveau mot_de_passe est valide.
		if len(nouveau_mdp) <= 6:
			return {"retour":"le mot de passe doit faire au moins 6 caractères"}

		#Je vérifie qu'un code ait bien été enregistré.
		mycursor.execute("SELECT count(*) FROM Changement_de_mot_de_passe WHERE adresse_mail = \""+adresse_mail+"\"")
		if not mycursor.fetchall()[0][0]:
			return {"retour":"aucune demande de changement de mot de passe n'a été trouvée dans notre BDD"}

		#Je vérifie que le code correspond puis je le supprime de Changement_de_mot_de_passe.
		mycursor.execute("SELECT code FROM Changement_de_mot_de_passe WHERE adresse_mail = \""+adresse_mail+"\"")
		code_dans_la_table = mycursor.fetchall()[0][0]
		if code_dans_la_table != code:
			return {"retour":"le code spécifié n'est pas bon"}

		mycursor.execute("DELETE FROM Changement_de_mot_de_passe WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		#Je modifie le mot_de_passe dans la table professeur.
		mycursor.execute("UPDATE Player SET mdp = \""+nouveau_mdp+"\" WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class password2(Resource):
	def put(self): #changer_son_mot_de_passe_a_l_aide_de_l_ancien
		body = password2_put_args.parse_args()
		[adresse_mail,ancien_mdp,nouveau_mdp] = [body[i] for i in body]
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

		#Je vérifie que le format du nouveau mot_de_passe est valide.
		if len(nouveau_mdp) <= 6:
			return {"retour":"le mot de passe doit faire au moins 6 caractères"}

		#Je vérifie que l'ancien mot_de_passe est le bon.
		mycursor.execute("SELECT mdp FROM Player WHERE adresse_mail = \""+adresse_mail+"\"")
		mdp_dans_la_table = mycursor.fetchall()[0][0]
		if mdp_dans_la_table != ancien_mdp:
			return {"retour":"le code spécifié n'est pas bon"}

		#Je change le mot_de_passe.
		mycursor.execute("UPDATE Player SET mdp = \""+nouveau_mdp+"\" WHERE adresse_mail = \""+adresse_mail+"\"")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

