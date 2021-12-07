from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
from random import choice,shuffle
import requests
import json
from time import time
import datetime


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

match_get_args = reqparse.RequestParser()
match_get_args.add_argument("token",type=str,required=True)
match_post_args = reqparse.RequestParser()
match_post_args.add_argument("token",type=str,required=True)
match_post_args.add_argument("date",type=str,required=True)
match_post_args.add_argument("heure",type=str,required=True)
match_post_args.add_argument("adresse",type=str,required=True)
match_put_args = reqparse.RequestParser()
match_put_args.add_argument("token",type=str,required=True)
match_put_args.add_argument("ref_match",type=int,required=True)
match_put_args.add_argument("date",type=str,required=True)
match_put_args.add_argument("heure",type=str,required=True)
match_put_args.add_argument("adresse",type=str,required=True)
match_delete_args = reqparse.RequestParser()
match_delete_args.add_argument("token",type=str,required=True)
match_delete_args.add_argument("ref_match",type=int,required=True)
match2_get_args = reqparse.RequestParser()
match2_get_args.add_argument("token",type=str,required=True)
match2_delete_args = reqparse.RequestParser()
match2_delete_args.add_argument("token",type=str,required=True)
match2_delete_args.add_argument("ref_match",type=int,required=True)

class match(Resource):
	def get(self): #recuperer_la_liste_des_matchs_et_participants
		body = match_get_args.parse_args()
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

		#Je récupère et formate les informations demandées
		if True:
			mycursor.execute("SELECT reference,adresse,day,hour,organisateur FROM `Match`")
			resultat = [{"reference":i[0],"adresse":i[1],"day":i[2],"hour":i[3],"organisateur":i[4]} for i in mycursor.fetchall()]

			sortie = []
			for i in range(len(resultat)):

				s = {}
				s["ref"] = resultat[i]["reference"]
				s["am_i_origin"] = 0
				if resultat[i]["organisateur"] == adresse_mail:
					s["am_i_origin"] = 1

				mycursor.execute("SELECT ref_player,team_color,date FROM Team WHERE ref_match = "+str(resultat[i]["reference"]))
				stock =  [{"ref_player":i[0],"team_color":i[1],"date":i[2]} for i in mycursor.fetchall()]

				nbr_rouge,nbr_bleu,nbr_liste_supp = 0,0,0
				for j in stock:
					if j["team_color"] == "rouge":
						nbr_rouge += 1
					elif j["team_color"] == "bleu":
						nbr_bleu += 1
					else:
						nbr_liste_supp += 1
				s["nbr_rouge"] = nbr_rouge
				s["nbr_bleu"] = nbr_bleu
				s["nbr_attente"] = nbr_liste_supp

				s["day"] = resultat[i]["day"]
				s["hour"] = resultat[i]["hour"]
				s["adresse"] = resultat[i]["adresse"]

				joueurs = []
				for j in stock:
					mycursor.execute("SELECT firstname,lastname,avatar FROM Player WHERE adresse_mail = \""+j["ref_player"]+"\"")
					[firstname,lastname,avatar] = mycursor.fetchall()[0]
					stock2 = {}
					stock2["adresse_mail"] = j["ref_player"]
					stock2["firstname"] = firstname
					stock2["lastname"] = lastname
					stock2["avatar"] = avatar
					stock2["equipe"] = j["team_color"]
					stock2["date"] = j["date"]

					joueurs += [stock2]

				s["joueurs"] = joueurs

				sortie += [s]

		mycursor.close()
		mydb.close()

		return {"retour":"ok","valeur":sortie}
	def post(self): #creer_un_match
		body = match_post_args.parse_args()
		[token,date,heure,adresse] = [body[i] for i in body]
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
			#date
			try:
				[j,m,a] = [int(i) for i in date.split('/')]
				datetime.datetime(a,m,j)
			except ValueError:
				return {"retour":"La date renseignée n'existe pas."}
			#heure
			try:
				[h,m] = [int(i) for i in heure.split("h")]
				if not (0 <= h < 24) or not (0 <= m <60):
					return {"retour":"L'heure renseignée n'est pas conforme."}
			except:
				return {"retour":"L'heure renseignée n'est pas conforme."}

		#Je crée le match
		if True:
			mycursor.execute("SELECT count(*) FROM `Match`")
			if not mycursor.fetchall()[0][0]:
				reference = 0
			else:
				mycursor.execute("SELECT max(reference) FROM `Match`")
				reference = mycursor.fetchall()[0][0] + 1

			ajouter_Match(reference,adresse,date,heure,adresse_mail,mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}
	def put(self): #modifier_un_match
		body = match_put_args.parse_args()
		[token,ref_match,date,heure,adresse] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		if True:
			#Je vérifie que le token exite et je récupère l'adresse mail du player.
			if True:
				mycursor.execute("SELECT count(*) FROM Token WHERE token_ =\""+token+"\"")
				if not mycursor.fetchall()[0][0]:
					return {"retour":"le token specifiee n'est pas connue de notre bdd"}
				mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ =\""+token+"\"")
				adresse_mail = mycursor.fetchall()[0][0]

			#Je vérifie que les informations transmises soient conformes
			if True:
				if len(date):
					try:
						[j,m,a] = [int(i) for i in date.split('/')]
						datetime.datetime(a,m,j)
					except ValueError:
						return {"retour":"La date renseignée n'existe pas."}
				if len(heure):
					try:
						[h,m] = [int(i) for i in heure.split("h")]
						if not (0 <= h < 24) or not (0 <= m <60):
							return {"retour":"L'heure renseignée n'est pas conforme."}
					except:
						return {"retour":"L'heure renseignée n'est pas conforme."}

			#Je modifie les informations voulues
			if True:
				if len(date):
					mycursor.execute("UPDATE `Match` SET day = \""+date+"\" WHERE reference = "+str(ref_match))
					mydb.commit()
				if len(heure):
					mycursor.execute("UPDATE `Match` SET hour = \""+heure+"\" WHERE reference = "+str(ref_match))
					mydb.commit()
				if len(adresse):
					mycursor.execute("UPDATE `Match` SET adresse = \""+adresse+"\" WHERE reference = "+str(ref_match))
					mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}
	def delete(self): #supprimer_un_match
		body = match_delete_args.parse_args()
		[token,ref_match] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		if True:
			#Je vérifie que le token exite et je récupère l'adresse mail du player.
			if True:
				mycursor.execute("SELECT count(*) FROM Token WHERE token_ =\""+token+"\"")
				if not mycursor.fetchall()[0][0]:
					return {"retour":"le token specifiee n'est pas connue de notre bdd"}
				mycursor.execute("SELECT adresse_mail FROM Token WHERE token_ =\""+token+"\"")
				adresse_mail = mycursor.fetchall()[0][0]

			#Je supprime le match et les inscriptions associées.
			if True:
				mycursor.execute("DELETE FROM `Match` WHERE reference = "+str(ref_match))
				mycursor.execute("DELETE FROM Team WHERE ref_match = "+str(ref_match))
				mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

class match2(Resource):
	def get(self): #recuperer_la_liste_de_mes_matchs
		body = match2_get_args.parse_args()
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

		#Je récupère la liste des matchs
		if True:
			mycursor.execute("SELECT ref_match FROM Team WHERE ref_player = \""+adresse_mail+"\"")
			resultat = [i[0] for i in mycursor.fetchall()]

			sortie = []
			for i in range(len(resultat)):
				s = {}
				s["ref_match"] = str(resultat[i])
				#Je récupère les informations du match
				mycursor.execute("SELECT adresse,day,hour,organisateur FROM `Match` WHERE reference = "+str(resultat[i]))
				[adresse,day,hour,organisateur] = mycursor.fetchall()[0]
				#Je récupère l'adresse des participants
				mycursor.execute("SELECT ref_player FROM Team WHERE ref_match = "+str(resultat[i])+" AND team_color = \"rouge\"")
				joueurs_rouges = [j[0] for j in mycursor.fetchall()]
				mycursor.execute("SELECT ref_player FROM Team WHERE ref_match = "+str(resultat[i])+" AND team_color = \"bleu\"")
				joueurs_bleus = [j[0] for j in mycursor.fetchall()]
				mycursor.execute("SELECT ref_player,date FROM Team WHERE ref_match = "+str(resultat[i])+" AND team_color != \"rouge\" AND team_color != \"bleu\"")
				joueurs_attente = mycursor.fetchall()
				joueurs_attente = [[i[1],i[0]] for i in joueurs_attente]
				joueurs_attente.sort()
				joueurs_attente.reverse()
				joueurs_attente = [i[0] for i in joueurs_attente]
				#Je récupère des informations chez les participants
				stock = []
				for j in joueurs_rouges:
					mycursor.execute("SELECT lastname,firstname,age,avatar FROM Player WHERE adresse_mail = \""+j+"\"")
					[lastname,firstname,age,avatar] = mycursor.fetchall()[0]
					stock += [{"nom":lastname,"prenom":firstname,"age":age,"avatar":avatar}]
				s["equipe_rouge"] = stock
				stock = []
				for j in joueurs_bleus:
					mycursor.execute("SELECT lastname,firstname,age,avatar FROM Player WHERE adresse_mail = \""+j+"\"")
					[lastname,firstname,age,avatar] = mycursor.fetchall()[0]
					stock += [{"nom":lastname,"prenom":firstname,"age":age,"avatar":avatar}]
				s["equipe_bleue"] = stock
				stock = []
				for j in range(len(joueurs_attente)):
					mycursor.execute("SELECT lastname,firstname,age,avatar FROM Player WHERE adresse_mail = \""+joueurs_attente[j][0]+"\"")
					[lastname,firstname,age,avatar] = mycursor.fetchall()[0]
					stock += [{"nom":lastname,"prenom":firstname,"age":age,"avatar":avatar,"ordre":j}]
				s["fil_attente"] = stock

				sortie += [s]

		mycursor.close()
		mydb.close()

		return {"retour":"ok","valeur":sortie}
	def delete(self): #supprimer_un_match_sans_participant
		body = match2_delete_args.parse_args()
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
				return {"retour":"le match référencé n'existe pas"}

		#Je vérifie que le player est l'organisateur à l'origine de ce match
		if True:
			mycursor.execute("SELECT count(*) FROM `Match` WHERE reference = "+str(ref_match)+" AND organisateur = \""+adresse_mail+"\"")
			if not mycursor.fetchall()[0][0]:
				return {"retour":"vous n'etes pas à l'origine de l'oganisation du match référencé"}

		#Je vérifie qu'il n'y a pas de participants à ce match
		if True:
			mycursor.execute("SELECT count(*) FROM Team WHERE ref_match = "+str(ref_match))
			if mycursor.fetchall()[0][0]:
				return {"retour":"on ne peut pas supprimer un match ou il y a dejà des inscrits"}

		#Je supprime le match
		if True:
			mycursor.execute("DELETE FROM `Match` WHERE reference = "+str(ref_match))
			mydb.commit()

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}

