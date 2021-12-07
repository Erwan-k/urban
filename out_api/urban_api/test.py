import requests
url = "http://127.0.0.1:1241/"

def testeur(route,type_,arguments):
	global url
	if type_ == "get":
		response = requests.get(url+route,arguments)
	if type_ == "put":
		response = requests.put(url+route,arguments)
	if type_ == "post":
		response = requests.post(url+route,arguments)
	if type_ == "delete":
		response = requests.delete(url+route,arguments)
	return response.json()


##############################   user   ##############################

if False: #S'inscrire
    s = testeur("user","post",{"adresse_mail":"erwan.kerbrat@edu.devinci.fr",
                               "mdp":"mdpAIR1",
                               "lastname":"Kerbrat",
                               "firstname":"Erwan",
                               "age":25,
                               "avatar":0})
    print(s)

##############################   mail_code   ##############################

if False: #Demander un nouvel email de confirmation
    s = testeur("mail_code","get",{"adresse_mail":"erwan.kerbrat@edu.devinci.fr"})
    print(s)
    
if False: #Vérifier son adresse mail
    pass
    #s = testeur("mail_code","delete",{"code":"azeaze"})
    #print(s)
    #Ca ne fonctionne pas car requests.delete ne prend pas d'arguments
    #C'est peut-être parce que c'est pas censé en prendre mais postman accepte d'en envoyer et ca fonctionne
    #On doit surement faire différement pour un delete, mais alors que fait postman ?
    #Il faudrait surement ne pas demander de RequestParser, passer par un paramètre donné dans l'url
    #et faire en sorte qu'on puisse appeler la route avec un delete et un parameetre dans l'url
    #tout en pouvant appeller la route avec le get sans paramètre dans l'url

    #Pour le moment je fais avec postman : http://127.0.0.1:1241/mail_code {"code":"l8èv950kfàxu"}

##############################   login   ##############################

if False: #Se connecter
    s = testeur("login","get",{"adresse_mail":"erwan.kerbrat@edu.devinci.fr",
                               "mdp":"mdpAIR1"})
    print(s)
    
##############################   account   ##############################

if False:#modifier_une_info_perso
    s = testeur("account","put",{"token":"7j8ahi0éc97",
                                 "lastname":"",
                                 "firstname":"Erwan",
                                 "age":-1,
                                 "avatar":-1})
    print(s)

if False: #recuperer_ses_infos_perso
    s = testeur("account","get",{"token":"7j8ahi0éc97"})
    print(s)

##############################   password_code   ##############################

if False: #demander_un_code_pour_changer_son_mot_de_passe
    s = testeur("password_code","post",{"adresse_mail":"erwan.kerbrat@edu.devinci.fr"})
    print(s)

##############################   password   ##############################

if False: #demander_un_code_pour_changer_son_mot_de_passe
    s = testeur("password","put",{"adresse_mail":"erwan.kerbrat@edu.devinci.fr",
                                  "code":"bmqj_è03v58",
                                  "nouveau_mdp":"mdpAIR2"})
    print(s)

if False: #demander_un_code_pour_changer_son_mot_de_passe
    s = testeur("password2","put",{"adresse_mail":"erwan.kerbrat@edu.devinci.fr",
                                   "ancien_mdp":"mdpAIR2",
                                   "nouveau_mdp":"mdpAIR1"})
    print(s)

##############################   match   ##############################

if False: #recuperer_la_liste_des_matchs_et_participants
    s = testeur("match","get",{"token":"7j8ahi0éc97"})
    print(s)

if False: #creer_un_match
    s = testeur("match","post",{"token":"7j8ahi0éc97",
                                "date":"8/12/2021",
                                "heure":"9h00",
                                "adresse":"37 rue de Paris"})
    print(s)

if False: #modifier_un_match
    s = testeur("match","put",{"token":"7j8ahi0éc97",
                               "ref_match":13,
                               "date":"32/12/2021",
                               "heure":"",
                               "adresse":""})
    print(s)

if False: #supprimer_un_match
    pass
    #http://127.0.0.1:1241/match
    #{"token":"7j8ahi0éc97","ref_match":13}    

if False: #recuperer_la_liste_de_mes_matchs
    s = testeur("match2","get",{"token":"7j8ahi0éc97"})
    print(s)

if False:
    pass
    #http://127.0.0.1:1241/match2
    #{"token":"7j8ahi0éc97","ref_match":13}  

##############################   team   ##############################

if False: #rejoindre_un_match
    s = testeur("team","post",{"token":"7j8ahi0éc97",
                               "ref_match":13,
                               "position":"rouge"})
    print(s)

if False: #se_desinscrire_d_un_match
    pass
    #http://127.0.0.1:1241/team
    #{"token":"7j8ahi0éc97","ref_match":13}


























