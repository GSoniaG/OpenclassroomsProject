# OpenclassroomsProject

Analyse marketing chez Books Online : suivi des prix des livres chez "Books to Scrape"(revendeur de livres en ligne)

## installation du projet :
environnement virtuel "env2" (ensemble de paquets Python propres au projet) :
 créer un environnement virtuel avec le module Python venv (pour créer et gérer des environnements virtuels avec version Python 3.7.1)
 commande python : -m venv <environment name> (<environment name> = env2 dans ce projet)
activer l'environnement : 
 exécutez source env/bin/activate  
 sous Windows  : env/Scripts/activate.bat

installation des paquets python :
pip install -r requirements.txt

descriptif du projet : 
suivre les prix des livres chez Books to Scrape, un revendeur de livres en ligne
Enregistrer les données livres dans un fichier CSV par catégorie, un fichier CSV distinct pour chaque catégorie de livres
télécharger et enregistrer le fichier image de chaque page Produit
processus ETL : 
Extraction de données web : extract
 requests
  url : lien de la page à scraper
  protocole http de communication avec un serveur, méthode (ou requête get) de requests pour obtenir une réponse qui contient une page web (objet response)
Transform : transformation
 beautifulsoup bs4
  transforme (parse) le HTML en objet BeautifulSoup
  résultat du contenu html (parsé ou extraire des informations) et récupérer les données livres
Load : chargement des données
  création des fichiers csv et png

script python "pythonprojet2.py" : C:\Users\sggue\projects\projet2\env2

lancer le programme python : C:\Users\sggue\projects\projet2\env2>pythonprojet2.py
