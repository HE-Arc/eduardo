# eduardo.ch

[![Join the chat at https://gitter.im/HE-Arc/eduardo](https://badges.gitter.im/HE-Arc/eduardo.svg)](https://gitter.im/HE-Arc/eduardo?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Site d'achat et vente en ligne basé sur ricardo.ch

## Environnement de développement
Installer l'environnement : 
1. Commande `pip install virtualenv`
2. Créer un environnement avec `virtualenv <nom_env>`
3. Démarrer l'environnement avec `<nom_env>\Scripts\activate.bat`
4. Il devrait être écrit (<nom_env>) sur la console
5. Il sera surement nécessaire de ré-installer les paquets nécessaires sur l'environnement (Django, django-crispy-forms, mysqlclient etc...)

## Démarrage serveur
1. Ouvrir la console dans le dossier de `manage.py`
2. Lancer `python manage.py runserver`
3. Ouvrir localhost:8000

## Migrations
Modifications d'un model:
* Modif dans 'models.py'
* Commande `python manage.py makemigrations` permet de créer le migrations correspondant aux changements
* Commande `python manage.py migrate` applique les migrations

## Tuto entier
[Tuto Django - ResistanceApp](https://github.com/HE-Arc/demo-django-resistance-app)

## Capistrano 
[Cours Capistrano](https://slides.com/osaris/deploiement-applis-web-2018?token=Ca2YfhZy#/17)
