# much love ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask, render_template, Response, request, redirect, url_for,send_file
from flask_bootstrap import Bootstrap
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import os
import sys
import random
import io
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time 

app = Flask(__name__)

# ==============================================================================
# FLASK
api_key = os.getenv("API_KEY")

if not api_key:
    print("API_KEY variable missing ")
    sys.exit(1)
    
lim=15


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {'start': '1', 'limit': lim, 'convert': 'EUR'}
headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': api_key }
session = Session()
session.headers.update(headers)
new = 2
try:
    response = session.get(url, params=parameters)
    data = response.json()
    donnees = data['data']
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

@app.route('/')
def index():
    importhtml = []
    #os.remove('data.csv')
    for i in range(0, lim):
        nomcrypto=str("csv/"+donnees[i]['symbol']+".csv")
        with open(nomcrypto, "a") as csv:
            importhtml.append(str("Crypto currency n° "+str(i+1)+" from CMC analysis : "+donnees[i]['name']))
            importhtml.append(str("Currency's price : "+str(donnees[i]['quote']['EUR']['price'])+'euros.'))
            importhtml.append(str('Percent change last 24hours : '+str(donnees[i]['quote']['EUR']['percent_change_24h'])+'%.'))
            importhtml.append(str('Percent change last hour : '+str(donnees[i]['quote']['EUR']['percent_change_1h'])+'%.'))
            row = str(donnees[i]['name'])+';'+str(donnees[i]['quote']['EUR']['price'])+';'+str(donnees[i]['last_updated'])+';'+str(donnees[i]['symbol'])+ '\n'
            csv.write(row)
        csv.close()
    incr=4*(i+1)
    
    return render_template('index.html', data=importhtml, incr=incr)


@app.route('/chart')
def chart():
    labels = []
    data = []
    for i in range(0, lim):
        nomcrypto=str("csv/"+donnees[i]['symbol']+".csv")
        with open(nomcrypto, "r") as file:  # on open les fichiers csv ici
            csv_reader=csv.reader(file)     # on lit le contenu du fichier csv ouvert juste avant, définit par la boucle for au début (ligne 75)
            for row in csv_reader:          # on parse chaque ligne du fichier
                lignes=str(row).split(';')  # on split les éléments avec le caractère `;` définit plus haut dans le code
                #for ligne in lignes:        # LA C LA MERDE
                                            # Il faut pouvoir récupérer les éléments individuellement, pour les push dans le return
                tab = []        
                for ligne in lignes:  
                    tab.append(ligne)
                #print(tab)
                val1=tab[0]
                val2=tab[1]
                val3=tab[2]
                val4=tab[3]  

                val1=val1.replace("['", "")
                val3=val3.replace("T", " | ")
                val3=val3.replace("Z", "")
                val4=val4.replace("']", "")
                #print(val3)
                labels.append(val3) #insérer date pour axe x   
                data.append(val2) #insérer prix pour axe y
                #labels = json.dumps(labels)  # C'est sensé permettre 
                #data = json.dumps(data)
    return render_template('chart.html', labels = labels, data = data) #crypto_name=crypto_name

#Je return le incr, mais je ne m'en sers plus dans la partie suivante donc on peut s'en servir pour ce qu'on veut
#ou l'enlever aussi si jamais il nous sert à rien

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000/chart")
    app.run(debug=True, host='localhost')


#Rechangez en 127.0.0.1 ou enlevez simplement la partie host=''
#Mais comme ça on peut émuler sur réseau local un petit serveur

# ==============================================================================