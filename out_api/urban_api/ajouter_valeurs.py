def ajouter_Token(adresse_mail,token_,mycursor,mydb):
	val = (adresse_mail,token_)
	try:
		mycursor.execute("INSERT INTO Token (adresse_mail,token_) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Player(adresse_mail,mdp,lastname,firstname,age,avatar,mycursor,mydb):
	val = (adresse_mail,mdp,lastname,firstname,age,avatar)
	try:
		mycursor.execute("INSERT INTO Player (adresse_mail,mdp,lastname,firstname,age,avatar) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Match(reference,adresse,day,hour,organisateur,mycursor,mydb):
	val = (reference,adresse,day,hour,organisateur)
	try:
		mycursor.execute("INSERT INTO `Match` (reference,adresse,day,hour,organisateur) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Team(ref_match,ref_player,team_color,date,mycursor,mydb):
	val = (ref_match,ref_player,team_color,date)
	try:
		mycursor.execute("INSERT INTO Team (ref_match,ref_player,team_color,date) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Adresse_mail_non_verif(adresse_mail,code,mycursor,mydb):
	val = (adresse_mail,code)
	try:
		mycursor.execute("INSERT INTO Adresse_mail_non_verif (adresse_mail,code) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

def ajouter_Changement_de_mot_de_passe(adresse_mail,code,mycursor,mydb):
	val = (adresse_mail,code)
	try:
		mycursor.execute("INSERT INTO Changement_de_mot_de_passe (adresse_mail,code) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

