# OpenclassroomsProject

Books Online market Analyse : monitoring of book prices at "Books to Scrape" (online book reseller)

## 1 - Project installation : <br/>
### Virtual environment "env2" (set of project-specific Python packages) : <br/>
- create a virtual environment with the venv Python module (to create and manage virtual environments with Python version 3.7.1)<br/>
- python command : -m venv <environment name> (<environment name> = env2 in this project) <br/>

## Installation of python packages :<br/>
pip install -r requirements.txt<br/>

## 2 - Description of the project : <br/>
- Track book prices at Books to Scrape, an online book reseller <br/>
- Save the books data in a CSV file by category, a separate CSV file for each category of books <br/>
- Download and save the image file of each Product page (png file)<br/>
## 3 - ETL Proces : <br/>
- Web data extraction : extract <br/>
 REQUESTS <br/>
 url : link of the page to scrape <br/>
 http protocol for communication with a server, method (or get request) of requests to obtain a response that contains a web page (response object)<br/>
- Transform : transformation <br/>
 beautifulsoup bs4 <br/>
 transform (parse) the HTML into a BeautifulSoup object <br/>
 result of html content (parsed or extract information) and retrieve the data books <br/>
- Load : data loading <br/>
 creation of csv and png files<br/>

## 4- Python script to launch : <br/>
 pythonprojet2.py
