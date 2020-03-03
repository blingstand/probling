# Probling

## Description

Probling est une application développée dans l'objectif de répondre à un projet openclassroom pour le parcours Python. Vous la trouverez [ici](https://peaceful-garden-24014.herokuapp.com/)

Elle se présente sous forme de tchat. L'utilisateur est amenée à entrer une question sur un lieu. L'application analyse la question posée et donne une réponse si elle y arrive. 

Elle est développée en utilisant Flask et est déployée grâce à Heroku. 

## Mode d'emploi

### Linux
* Ouvrez le terminal puis tapez
* mkdir new_file
* cd new_file
* git init
* git clone https://github.com/blingstand/probling.git
* virtualenv env -p votre_version_de_python
* source env/bin/activate
* pip install -r requirements.txt
* python app.py # le serveur est lancé, rendez vous à cette adresse : http://127.0.0.1:5000/

## Partie développeur

Ce projet utilise python 3.8.0 et flask 1.1.1 [plus d'information](https://github.com/blingstand/probling/blob/master/requirements.txt)

## Comment lancer les tests : 

Les tests réalisés se lancent avec pytest, cependant il y a une spécificté. Pour tester le parcours utilisateur j'ai écrit des tests dans app/tests/test_us.py donc si vous lancez : 

* pytest/app/tests/test_us.py


Vous n'allez tester QUE le parcours utilisateur, soient 6 fonctions pour plus d'une minute. J'ai trouvé ça long (mais néanmoins nécessaire dans le cadre de ma formation). J'ai donc créé une alternative qui est de lancer le serveur puis de lancer l'autre test app/tests/test_apipro7.py : 

* python app.py #le serveur démarre
* pytest/app/tests/test_apipro7.py

**Cette methode présente l'avantage d'être exhaustive et plus rapide**.