# eduardo.ch

[![Join the chat at https://gitter.im/HE-Arc/eduardo](https://badges.gitter.im/HE-Arc/eduardo.svg)](https://gitter.im/HE-Arc/eduardo?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Site d'achat et vente en ligne basé sur ricardo.ch

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
