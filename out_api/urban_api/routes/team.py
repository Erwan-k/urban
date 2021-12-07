from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
from random import choice,shuffle
import requests
import json
from time import time

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

team_post_args = reqparse.RequestParser()
team_post_args.add_argument("token",type=str,required=True)
team_post_args.add_argument("ref_match",type=int,required=True)
team_post_args.add_argument("position",type=str,required=True)
team_delete_args = reqparse.RequestParser()
team_delete_args.add_argument("token",type=str,required=True)
team_delete_args.add_argument("ref_match",type=int,required=True)

class team(Resource):
	def post(self): #rejoindre_un_match
		body = team_post_args.parse_args()
		[token,ref_match,position] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token exite et je récupère l'adresse mail du player.
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ =\""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token specifiee n'est pas connue de notre bdd"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ =\""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que le match existe
		if True:
			mycursor.execute("SELECT count(*) FROM `Match` WHERE reference = "+str(ref_match))
			if not mycursor.fetchall()[0][0]:
				return {"retour":"Le match référencé n'a pas été trouvé"}

		#Je vérifie que le joueur n'est pas déjà inscrit à ce match
		if True:
			mycursor.execute("SELECT count(*) FROM Team WHERE ref_match = "+str(ref_match)+" AND ref_player = \""+adresse_mail+"\"")
			if mycursor.fetchall()[0][0]:
				return {"retour":"Le joueur est déjà inscrit à ce match"}

		#Je vérifie que les places dans la team choisie sont disponibles
		if True:
			mycursor.execute("SELECT count(*) FROM Team WHERE ref_match = "+str(ref_match)+" AND team_color = \""+position+"\"")
			if mycursor.fetchall()[0][0] >= 5:
				return {"retour":"Navré, l'équipe choisie est déjà complète."}

		#J'inscris le joueur au match
		if True:
			ajouter_Team(ref_match,adresse_mail,position,int(time()),mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

	def delete(self): #se_desinscrire_d_un_match
		body = team_delete_args.parse_args()
		[token,ref_match] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		#Je vérifie que le token exite et je récupère l'adresse mail du player.
		if True:
			mycursor.execute("SELECT count(*) FROM Token WHERE token_ =\""+token+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"le token specifiee n'est pas connue de notre bdd"}
			mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ =\""+token+"\"")
			adresse_mail = mycursor.fetchall()[0][0]

		#Je vérifie que le match existe
		if True:
			mycursor.execute("SELECT count(*) FROM `Match` WHERE reference = "+str(ref_match))
			if not mycursor.fetchall()[0][0]:
				return {"retour":"Le match référence n'existe pas"}

		#Je vérifie que mon joueur est bien inscrit au match
		if True:
			mycursor.execute("SELECT count(*) FROM Team WHERE ref_match = "+str(ref_match)+" AND ref_player = \""+adresse_mail+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"Le joueur est déjà desinsicrit de ce match"}

		#Je desisncris mon joueur du match
		if True:
			#J'enregistre la couleur de sa team au passage
			mycursor.execute("SELECT team_color FROM Team WHERE ref_match = "+str(ref_match)+" AND ref_player = \""+adresse_mail+"\"")
			couleur = mycursor.fetchall()[0][0]
			mycursor.execute("DELETE FROM Team WHERE ref_match = "+str(ref_match)+" AND ref_player = \""+adresse_mail+"\"")
			mydb.commit()

		#Je regarde si un joueur de la fil d'attente peut alors jouer
		if True:
			mycursor.execute("SELECT count(*) FROM Team WHERE ref_match = "+str(ref_match)+" AND  team_color != \"rouge\" AND team_color != \"bleu\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"Ok"}

		#J'opère pour permettre à mon remplacant de jouer
		if True:
			#Je récupère le joueur de la liste d'attente qui s'est inscrit en premier
			mycursor.execute("SELECT ref_player FROM Team WHERE ref_match = "+str(ref_match)+" AND  team_color != \"rouge\" AND team_color != \"bleu\" ORDER BY date LIMIT 1")
			joueur = mycursor.fetchall()[0][0]
			#Je place ce joueur à la place de celui qui s'est desinscrit
			mycursor.execute("UPDATE Team SET team_color = \""+couleur+"\" WHERE ref_match = "+str(ref_match)+" AND ref_player = \""+joueur+"\"")
			mdyb.commit()

		#J'envoie un mail à mon remplacant
		if True:
			obj = "Une place s'est libérée !"
			#envoyer_email("Un joueur s'est désisncrit du match de ***** à ***** à l'adresse : ***** pour lequel vous étiez sur la liste supplémentaire. Vous êtes donc promu joueur titulaire de l'équipe *****",obj,adresse_mail)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}
