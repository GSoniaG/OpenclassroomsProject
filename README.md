# OpenclassroomsProject
Projet : Utilisez les bases de Python pour l'analyse de marché
Client : analyste marketing chez Books Online
1.	Description du projet :
  Les analystes marketing chez Books Online, une importante librairie en ligne spécialisée dans les livres d'occasion, dans le cadre de leurs fonctions,  suivent manuellement les prix des livres d'occasion sur les sites web de leurs concurrents, ce qui se révèle fastidieux.
  Le projet consiste à automatiser ces analyses pour extraire les informations tarifaires d’un revendeur de livres en ligne  Books to Scrape, qui se déclinera sous la forme d'une application exécutable à la demande visant à récupérer diverses données, dont les prix, au moment de son exécution, et ceci via un programme (un scraper) développé en Python.
2.	environnement à utiliser : Python
3.	Pré-requis
  3.1.	Python : langage de programmation interprété et orienté objet
  3.2.	Jupyter notebook : interface de programmation interactive (sections en langage naturel et des sections en langage informatique)
4.	Installation : 
  4.1.	Python : langage de programmation interprété et orienté objet. 
    Installer Python sous Windows, sous Mac et Linux Python est déjà installé. 
    Sous Windows : sous internet aller sur le site de Python à l'adresse python.org/downloads pour installer Python
    Installer la version 3.x.x. (Cochez la case Add Python 3.5 to PATH (Ajouter Python 3.5 au PATH pour exécuter Python directement depuis l'invite de commandes)).
  4.2.	Jupyter notebook : interface de programmation interactive (sections en langage naturel et des sections en langage informatique). Pour lancer Jupyter tapez jupyter notebook sous l’invite de commande du PC.
5.	ETL : extract transform load
  5.1.	Extraction des données du site  :  import requests
    Dans Python, la bibliothèque* requests récupère la page web du site analysé :
    url = 'http://books.toscrape.com'
      (*ensemble logiciel de modules (classes (types d'objets), fonctions, constantes, …)
5.2.	Transformation : from bs4 import BeautifulSoup
    bs4 est une bibliothèque Python d'analyse syntaxique de documents HTML et XML.
    Les données de la page web étudiée (un livre particulier par ex) sont récupérées ou parsées (parcourir le contenu d'une page web pour en extraire des éléments) et les informations obtenues peuvent être traitées et/ou sauvegardées. 
5.3.	Load : 
  5.3.1.	import csv
    Création d’un fichier csv par catégorie de livres (50 catégories sur le site web) contenant n livres avec les données à analyser 
    o	product_page_url
    o	universal_ product_code (upc)
    o	title
    o	price_including_tax
    o	price_excluding_tax
    o	number_available
    o	product_description
    o	category
    o	review_rating
    o	image_url
  5.3.2.	 création d’un fichier image.png par de la page de couverture de chaque livre (1000 livres sur le site web)
6.	Lancement du programme
  6.1.	Lancer le programme Python : Python Projet 2 - analyse marketing Books Online
  6.2.	Le programme Python accède au site web https://books.toscrape.com
  6.3.	Import des bibliothèques pour :
    6.3.1.	 Accéder à une page web
    6.3.2.	 Parser une page web : récupérer les données livres avec les balises html
    6.3.3.	 Créer un fichier .png : photo de la page de couverture du livre (1000 livres toute catégorie comprise)
    6.3.4.	 Créer un fichier .csv : 1 fichier .csv par catégorie (50 catégories), chaque ligne du fichier .csv correspond à un livre avec ses données (titre, prix, …)
  6.4.	Le programme Python contient un programme principal qui appelle des fonctions de traitement des données
  6.5.	Il parcourt toutes les pages web catégorie par catégorie 
  6.6.	Il crée un fichier nom_catégorie.csv par catégorie et dans chaque fichier .csv il mémorise les données de chaque livre (une ligne d’un fichier csv contient les données d’un livre pour une catégorie donnée ) : 50 fichiers .csv
  6.7.	Il crée un fichier .png par livre qui est une photo de la page de couverture du livre : 1000 livres
7.	Diagramme avec https://www.draw.io/
8.	Déroulé du programme Python avec Excel
9.	Le programme Python génère au final :
  9.1.	Les 50 fichiers .csv : 1 fichier .csv par catégorie
  9.2.	Extrait des 1000 fichiers .png : 1 fichier image par livre dans l’ordre alphabétique
