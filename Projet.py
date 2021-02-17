# much love ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask, render_template, Response, request, redirect, url_for,send_file
from flask_bootstrap import Bootstrap
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from crontab import CronTab
import json
import csv
import os
import sys
import random
import io
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
            row = str(donnees[i]['name'])+';'+str(donnees[i]['quote']['EUR']['price'])+';'+str(donnees[i]['quote']['EUR']['percent_change_24h'])+';'+str(donnees[i]['quote']['EUR']['percent_change_1h'])+';'+str(donnees[i]['last_updated'])+';'+str(donnees[i]['symbol'])+ '\n'
            csv.write(row)
        csv.close()
    incr=4*(i+1)
    
    return render_template('index.html', data=importhtml, incr=incr)

#Je return le incr, mais je ne m'en sers plus dans la partie suivante donc on peut s'en servir pour ce qu'on veut
#ou l'enlever aussi si jamais il nous sert à rien

# @app.route('/SomeFunction')
# def SomeFunction():
#     print('In SomeFunction')
#     return "Nothing"

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)


#Rechangez en 127.0.0.1 ou enlevez simplement la partie host=''
#Mais comme ça on peut émuler sur réseau local un petit serveur

# ==============================================================================