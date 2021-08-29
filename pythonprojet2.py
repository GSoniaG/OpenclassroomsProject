# extraire les données livres d'une même catégorie (avec plusieurs pages) et pour toutes les catégories
# données livres dans un csv par catégorie avec import csv , 1 livre par ligne
# 1 fichier par image.png
# ---------------------------------------------------------------------------- OK ---------------------------------------

import requests 
from bs4 import BeautifulSoup
import csv
import urllib.request

list_results =[]

def export_image(image_url,title): # export picture file csv
    reponse = urllib.request.urlopen(image_url)
    image = reponse.read()
    coupe_title = ['(','/']
    coupe_title0 = '('
    coupe_title1 = '/'
    title_image = title    
    for i in coupe_title:
        if title.find(coupe_title0)>0 :
            long_titre = len(title)
            title_image = title[:title.find(coupe_title0)]   
        if title.find(coupe_title1)>0 :
            long_titre = len(title)
            title_image = title[:title.find(coupe_title1)]
    transTable = title_image.maketrans('?*"#:',"     ","") 
    title_image = title_image.translate(transTable)
    nom_imagePng = title_image +'.png'
    with open(nom_imagePng, "wb") as file:
        file.write(image)

def export_csv():
    categorie = format(href)[25:-11]+'.csv'
    print('======  categorie export_csv : ',categorie,'===========================================')
    with open (categorie,'w',newline="") as result:
        writer = csv.writer(result,delimiter=",")
        writer.writerow(('product_page_url','universal_product_code','title','price_including_tax',
                         'price_excluding_tax','number_available','category',
                         'review_rating','nbre_etoile','image_url','product_description'))
        for row in list_results:
            columns = [c.strip() for c in row.strip(', ').split(',')]
            writer.writerow(columns)

def livres(links):
    url = links
    response = requests.get(url)
    response.encoding = "UTF-8" # ajout Arthur
    if response :
        soup = BeautifulSoup(response.text,"html.parser")
        product_page_url = url
        universal_product_code = soup.find('table', {'class':'table table-striped'}).find('td').text
        
        title = soup.find ('div', {'class':'col-sm-6 product_main'}).find('h1').text
        title = title.replace(',','')
        print('title livres : ',title,)
        
        product_information = soup.find_all('td') 
        universal_product_code = product_information[0].text # code UPC
        price_excluding_tax = product_information[2].text.replace('£', '')
        price_including_tax = product_information[3].text.replace('£', '')          
        #price_excluding_tax = product_information[2].text.replace('Â£', '') 
        #price_including_tax = product_information[3].text.replace('Â£', '') 
        number_available = product_information[5].text  
        
        product_description =''
        soup = BeautifulSoup(response.content)
        product_description = soup.find_all('p')[3].text 
        transTable = product_description.maketrans("àâäéèêëîïôöùûüç•’—!#$%^“”,", "aaaeeeeiioouuuc           ","") 
        product_description = product_description.translate(transTable)
        product_description = product_description.replace('  ',' ')
        product_description = product_description.replace('.',' . ')
        
        category = soup.find('ul', {'class':'breadcrumb'}).find_all('a')[2].text
        review_rating = soup.find_all('tr')[6].find('td').text 
        
        nbre_etoile = soup.find ('div', {'class':'col-sm-6 product_main'}).find_all('p')[2]
        nbre_etoile = str(nbre_etoile)   
        nombre = ('Zero','One','Two','Three','Four','Five')
        for n in nombre:
            etoile = nbre_etoile.find(n)
            if etoile > 0:
                resultat = n
                resultat = str(nombre.index(resultat))
        
        extract_html = str(soup.find_all('img'))
        extract_html = str(soup.find('img'))
        debut_image_url = "http://books.toscrape.com/"
        select_extract = 'src="../../'
        indice_url = extract_html.find(select_extract)+10
        image_extraite = extract_html[indice_url:-3]
        image_url = image_extraite
        image_url = debut_image_url + image_url 
        
        export_image(image_url,title)
        
        final_result = product_page_url  + ',' +  universal_product_code  + ',' +  title  + ',' +  price_including_tax  + ',' +  price_excluding_tax  + ',' +  number_available + ',' +   category  + ',' +  review_rating  + ',' + resultat + ',' + image_url + ',' + product_description + '\n'
        list_results.append(final_result)

def traitement_page():
    link = soup.find_all('h3')
    for h3 in link:
        livre = []
        links = []
        a = h3.find('a')
        livre = a['href'][8:]
        links = 'https://books.toscrape.com/catalogue' + livre
        livres(links)

#début du programme -----------------------------------------------------
url = 'http://books.toscrape.com' # url du site 
response = requests.get(url) 

if response.ok:
    soup = BeautifulSoup(response.text,"html.parser")
    for categories in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
        href = categories.a.get('href')
        url = "https://books.toscrape.com/{}".format(href)
        response = requests.get(url) # 1ère catégorie 
        if response.ok :
            soup = BeautifulSoup(response.text,"html.parser")
            traitement_page()
            page_suivante = soup.find('li', class_='next')          
            no_page = 2
            index = "index.html"
            while page_suivante is not None:
                complement = "page-"+str(no_page)+".html"
                url = url.replace(index, complement) 
                response = requests.get(url) 
                soup = BeautifulSoup(response.text,"html.parser")
                page_suivante = soup.find('li', class_='next')
                traitement_page()
                index = complement
                no_page = no_page + 1
            export_csv()
            list_results =[]

            
