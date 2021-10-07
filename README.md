# OpenclassroomsProject

Analyse marketing chez Books Online : suivi des prix des livres chez "Books to Scrape"(revendeur de livres en ligne)

## Installation du projet : <br/>
### Environnement virtuel "env2" (ensemble de paquets Python propres au projet) : <br/>
- créer un environnement virtuel avec le module Python venv (pour créer et gérer des environnements virtuels avec version Python 3.7.1)<br/>
- commande python : -m venv <environment name> (<environment name> = env2 dans ce projet) <br/>

## Installation des paquets python :<br/>
pip install -r requirements.txt<br/>

## Descriptif du projet : <br/>
- Suivre les prix des livres chez Books to Scrape, un revendeur de livres en ligne <br/>
- Enregistrer les données livres dans un fichier CSV par catégorie, un fichier CSV distinct pour chaque catégorie de livres <br/>
- Télécharger et enregistrer le fichier image de chaque page Produit (fichier png) <br/>
## Processus ETL : <br/>
- Extraction de données web : extract <br/>
 requests <br/>
  url : lien de la page à scraper <br/>
  protocole http de communication avec un serveur, méthode (ou requête get) de requests pour obtenir une réponse qui contient une page web (objet response) <br/>
- Transform : transformation <br/>
 beautifulsoup bs4 <br/>
  transforme (parse) le HTML en objet BeautifulSoup <br/>
  résultat du contenu html (parsé ou extraire des informations) et récupérer les données livres <br/>
- Load : chargement des données <br/>
  création des fichiers csv et png <br/>

## Script python à lancer : <br/>
 pythonprojet2.py
