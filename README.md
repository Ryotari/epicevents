# epicevents
Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.
Il s'agit d'une API réalisée avec Django pour EpicEvents, une entreprise fictive d'evenementiel.  
L'application permet de gérer des clients, contrats et événements via une API REST et une interface d'administration.

## Installation & lancement

Commencez tout d'abord par installer Python.  
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/Ryotari/epicevents.git
```
Créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Installez ensuite les packages requis:
```
pip install -r requirements.txt
```
Ensuite, placez vous à la racine du projet (là ou se trouve le fichier manage.py), puis effectuez les migrations pour initialiser la base de données:
```
python manage.py makemigrations
```
Puis: 
```
python manage.py migrate
```
Il ne vous reste plus qu'à lancer le serveur: 
```
python manage.py runserver
```
