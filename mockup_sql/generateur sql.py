

from random import choice

sql1 = "INSERT INTO `Player` (`adresse_mail`,`mdp`,`lastname`,`firstname`,`age`,`avatar`) VALUES (\"&1\",\"&2\",\"&3\",\"&4\",&5,&6);"
sql2 = "INSERT INTO `Match` (`reference`,`adresse`,`day`,`hour`,`organisateur`) VALUES (&1,\"&2\",\"&3\",\"&4\",\"&5\");"
sql3 = "INSERT INTO `Team` (`ref_match`,`ref_player`,`team_color`,`date`) VALUES (&1,\"&2\",\"&3\",&4);"

noms = ["Aaron", "Abdon", "Abel", "Abelin", "Abondance", "Abraham", "Absalon", "Acace", "Achaire", "Achille", "Adalard", "Adalbald", "Adalbert", "Adalric", "Adam", "Adegrin", "Adel", "Adelin", "Andelin", "Adelphe", "Adam", "Adjutor", "Adolphe", "Adonis", "Adon", "Adrien", "Agapet", "Agathange", "Agathon", "Agilbert", "Agnan", "Aignan", "Agrippin", "Aimable", "Alain", "Alban", "Albin", "Aubin", "Albert", "Albertet", "Alcibiade", "Alcide", "Alcime", "Aldonce", "Aldric", "Aleaume", "Alexandre", "Alexis", "Alix", "Alliaume", "Aleaume", "Almine", "Almire", "Alphonse", "Alpinien", "Amalric", "Amaury", "Amandin", "Amant", "Ambroise", "Amiel", "Amour", "Anastase", "Anatole", "Ancelin", "Andoche", "Andoche", "Ange", "Angelin", "Angilbe", "Anglebert", "Angoustan", "Anicet", "Anne", "Annibal", "Ansbert", "Anselme", "Anthelme", "Antheaume", "Anthime", "Antide", "Antoine", "Antonius", "Antonin", "Apollinaire", "Apollon", "Aquilin", "Arcade", "Archambaud", "Archambeau", "Archange", "Archibald", "Arian", "Ariel", "Ariste", "Aristide", "Armand", "Armel", "Armin", "Arnould", "Arnaud", "Arolde", "Arthaud", "Arthur", "Ascelin", "Athanase", "Aubry", "Audebert", "Audouin", "Audran", "Audric", "Auguste", "Augustin", "Aurian", "Auxence", "Axel", "Aymard", "Aymeric", "Aymon", "Aymond", "Balthazar", "Baptiste", "Basile", "Bastien", "Baudouin", "Benjamin", "Bernard", "Bertrand", "Blaise", "Bon", "Boniface", "Bouchard", "Brice", "Brieuc", "Bruno", "Brunon", "Calixte", "Calliste", "Camille", "Camillien", "Candide", "Caribert", "Carloman", "Cassandre", "Cassien", "Charles", "Charlemagne", "Childebert", "Christian", "Christodule", "Christophe", "Chrysostome", "Clarence", "Claude", "Claudien", "Clotaire", "Constance", "Constant", "Constantin", "Corentin", "Cyprien", "Cyriaque", "Cyrille", "Cyril", "Damien", "Daniel", "David", "Delphin", "Denis", "Didier", "Dimitri", "Dominique", "Dorian", "Edgard", "Edmond", "Emmanuel", "Enguerrand", "Esprit", "Ernest", "Eubert", "Eudes", "Eudoxe", "Eustache", "Fabien", "Fabrice", "Falba", "Ferdinand", "Fiacre", "Firmin", "Flavien", "Flodoard", "Florent", "Florentin", "Florestan", "Florian", "Foulques", "Francisque", "Franciscus", "Francs", "Fulbert", "Fulcran", "Fulgence", "Gabin", "Gabriel", "Garnier", "Gaston", "Gaspard", "Gatien", "Gaud", "Gautier", "Geoffroy", "Georges", "Gerbert", "Germain", "Gervais", "Ghislain", "Gilbert", "Gilles", "Girart", "Gislebert", "Gondebaud", "Gonthier", "Gontran", "Gonzague", "Gui", "Guillaume", "Gustave", "Guy", "Guyot", "Hardouin", "Hector", "Henri", "Herbert", "Herluin", "Hilaire", "Hildebert", "Hincmar", "Hippolyte", "Hubert", "Hugues", "Innocent", "Isabeau", "Isidore", "Jacques", "Japhet", "Jason", "Jean", "Jeannel", "Jeannot", "Joachim", "Joanny", "Job", "Jocelyn", "Johan", "Jonas", "Jonathan", "Joseph", "Josse", "Josselin", "Jourdain", "Jude", "Jules", "Julien", "Juste", "Justin", "Lambert", "Landry", "Laurent", "Lazare", "Leu", "Loup", "Leufroy", "Lionel", "Longin", "Lorrain", "Lorraine", "Lothaire", "Louis", "Loup", "Luc", "Lucas", "Lucien", "Ludolphe", "Ludovic", "Macaire", "Malo", "Mamert", "Marc", "Marceau", "Marcel", "Marcelin", "Marius", "Marseille", "Martial", "Martin", "Mathurin", "Matthias", "Mathias", "Matthieu", "Maugis", "Maurice", "Mauricet", "Maxence", "Maxime", "Maximilien", "Mayeul", "Melchior", "Mence", "Merlin", "Michel", "Morgan", "Nathan", "Narcisse", "Nestor", "Nestor", "Nicolas", "Norbert", "Normand", "Normands", "Octave", "Odilon", "Odon", "Oger", "Olivier", "Oury", "Parfait", "Pascal", "Paterne", "Patrice", "Paul", "Perceval", "Philibert", "Philippe", "Pie", "Pierre", "Pierrick", "Prosper", "Quentin", "Raoul", "Raymond", "Renaud", "Reybaud", "Richard", "Robert", "Roch", "Rodolphe", "Rodrigue", "Roger", "Roland", "Romain", "Romuald", "Rome", "Ronan", "Roselin", "Salomon", "Samuel", "Savin", "Savinien", "Scholastique", "Serge", "Sidoine", "Sigebert", "Sigismond", "Simon", "Sixte", "Stanislas", "Stephan", "Sylvain", "Sylvestre", "Tanguy", "Taurin", "Thibault", "Thibert", "Thierry", "Thomas", "Titien", "Tonnin", "Toussaint", "Trajan", "Tristan", "Turold", "Tim", "Ulysse", "Urbain", "Valentin", "Venance", "Venant", "Venceslas", "Vianney", "Victor", "Victorien", "Victorin", "Vigile", "Vincent", "Vital", "Vitalien", "Vivien", "Waleran", "Wandrille", "Xavier", "Yves", "Zacharie"]
nom_ = ["Candide", "Fulcran", "Melchior", "Nestor", "Odon", "Aymard", "Simon", "Patrice", "Mayeul", "Marcel", "Lazare", "Flodoard", "Georges", "Jude", "Urbain", "Anglebert", "Antonius", "Angoustan", "Ange", "Thierry", "Loup", "Normand", "Maxime", "Leu", "Vincent", "Ernest", "Ariel", "Alban", "Romain", "Job", "Ghislain", "Olivier", "Jeannel", "Corentin", "Pascal"]

organisateurs = {}
organisateurs["Ariel"] = ["7/12/2021"]
organisateurs["Aymard"] = ["2/12/2021"]
organisateurs["Nestor"] = ["21/12/2021","6/12/2021"]
organisateurs["Antonius"] = ["5/12/2021","19/12/2021","13/12/2021","8/12/2021"]
organisateurs["Vincent"] = ["6/12/2021","21/12/2021","14/12/2021","4/12/2021"]

s = ""
s += "DELETE FROM `Player`;\n"
s += "DELETE FROM `Match`;\n"
s += "DELETE FROM `Team`;\n\n"
s+= sql1.replace("&1","kerbrat.erwan@gmail.com").replace("&2","mdpARI1").replace("&3","Kerbrat").replace("&4","Erwan").replace("&5","25").replace("&6","0")+"\n"

mail_orga = {}
noms_associes = {}
#Ajout des Players
for i in nom_:
    nom,prenom,age,avatar,mdp = choice(nom_),i,str(choice(range(20,50))),str(choice([0,1,2])),"".join([choice("abcdefghijklmnopqrstuvwxyz") for j in range(6)])
    noms_associes[prenom] = nom
    adresse_mail = nom+"."+prenom+"@gmail.com"
    s += sql1.replace("&1",adresse_mail).replace("&2",mdp).replace("&3",nom).replace("&4",prenom).replace("&5",age).replace("&6",avatar)+"\n"
    if i in organisateurs:
        mail_orga[i] = adresse_mail
s+="\n"
    
#Ajout des Match
compteur = 0
for i in organisateurs:
    for j in organisateurs[i]:
        compteur+=1
        heure = str(choice(range(8,24)))+"h"+choice(["00","15","30","45"])
        s += sql2.replace("&1",str(compteur)).replace("&2","37 rue de Paris, Saint-Germain en Laye").replace("&3",j).replace("&4",heure).replace("&5",i)+"\n"
s+="\n"
    
#Ajout des participants
compteur,compteur2 = 0,0
for i in organisateurs:
    for j in organisateurs[i]:
        compteur+=1
        joueurs = [i]
        for k in range(choice([10,10,10,10,11,12,13,8])-1):
            joueur = choice(nom_)
            while joueur in joueurs:
                joueur = choice(nom_)
            joueurs += [joueur]
            
        for k in range(len(joueurs)):
            compteur2 += 1
            adresse = noms_associes[joueurs[k]]+"."+joueurs[k]+"@gmail.com"
            if k < 5: 
                s += sql3.replace("&1",str(compteur)).replace("&2",adresse).replace("&3","bleu").replace("&4",str(compteur2))+"\n"
            elif k<10:
                s += sql3.replace("&1",str(compteur)).replace("&2",adresse).replace("&3","rouge").replace("&4",str(compteur2))+"\n"
            else:
                s += sql3.replace("&1",str(compteur)).replace("&2",adresse).replace("&3","supplémentaire").replace("&4",str(compteur2))+"\n"
s += "\n"
   
del(i,j,k,sql1,sql2,sql3,mdp,prenom,nom,joueur,joueurs,age,avatar,compteur,heure)




























