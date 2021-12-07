# Urban API
Urban API is an open source API to organise a football match

## Specifications
Organize a football match with two teams (rouge and bleu) of 5 players each
If both teams are complete, a player is allowed to join a "waiting list"

## Data
* Player : adresse_mail, mdp, lastname, firstname, age, avatar
* Match : reference, adresse, day, hour, organisateur
* Team : ref_match, ref_player, team_color, date
* Token : adresse_mail, token_
* Adresse_mail_non_verif : adresse_mail, code
* Changement_de_mot_de_passe : adresse_mail, code

## Routes
* user/post : subscribe
* mail_code/get : ask for a new confirmation mail
* mail_code/delete : verify your mail
* password_code/post : ask for a code received by mail that will allow you to change your password
* password/put : allow you to change your password using the referenced code
* password2/put : allow you to change your password using your older password
* login/get : log in and get a token
* account/get : get your account information
* account/put : modify your account information
* match/get : get a list of all matches and participants
* match/post : create a new match
* match/put : modify a match informations
* match/delete : delete a match information
* match2/get : get a list of all matches you are in
* match2/delete : delete a match you organised which does not count any players
* team/post : join a match
* team/delete : leave a match

## Basics Fonctionalities
* As a new player I can : subscribe, verify my mail, ask for a new confimation mail if needed, change my password using my mail or my older password.
* As a player I can get a list of all matches proposed showing how full they are.
* As an organisator I can create a match, modify it or even delete it. The delete fuction is meant to be down and get replaced by a "delete only if there is no playe".
* As a player I can join matches, get a list of all matches I joined and leave them.
" As a player I can join a "waiting list" if both rouge and bleu teams are full. If a player leave one of those teams, I will automatically be asigned to his position and receive a mail that will let me know about it.

## How does it works ?
* commande.bat commands will build the containers, run the containers and show the api logs
* the docker-compose.yml describes : urban_api (a rest python-flask api), urban_front (a React frontend), api_mail_sender (another flask api meant to send mails), db (a database built from official image mysql:5.7) and dbadmin (a phpmyadmin service that allows us to operate more easily on our databse)
* in order to test the flask api you will find ./out_api/urban_api/test.py which is a python script that requests the api but you will also find mockup_sql/dump.sql to populate the database, making the testing easier (this .sql file is generated from the python script next to it)

## What's next ?

I am looking forward to :
* add a decorator that will stop a url from requesting more than 100 times within 5 minutes
* build the front service
* deploy this service on my server
* get this app reachable on urban.erwankerbrat.com
* deploy this app on amazon web services

