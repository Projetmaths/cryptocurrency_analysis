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
import random
import io
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

app = Flask(__name__)

# ==============================================================================
# FLASK

lim=15

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {'start': '1', 'limit': lim, 'convert': 'EUR'}
headers = {'Accepts': 'application/json',
 'X-CMC_PRO_API_KEY': '4aaaa51e-2ac2-48ce-8e75-a49c61efeb33', }

session = Session()
session.headers.update(headers)
new = 2
try:
    response = session.get(url, params=parameters)
    data = response.json()

    #print(data) #-> print absolument TOUT donc c'est bien pour voir les tuples mais c'est tout c:
    #print(data) #-> print absolument TOUT donc c'est bien pour voir les tuples mais c'est tout c:
    # print("Sentence describing what you want to tell : ", data['data'])
    donnees = data['data']
    # donnees[n] -> donne l'item classé au rang 'cmc_rank'=n+1
    # donnees[i]['data_you_want_to_print'] -> print la colonne 'data_you_want_to_print'
    # de l'item i (au rang 0 ce sera la colonne 'blabla' du BTC, et etc)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

@app.route('/')
def index():
    importhtml = []
    os.remove('data.csv')
    with open("data.csv", "a") as csv:

        for i in range(0, lim):
            importhtml.append(str("Crypto currency n° "+str(i+1)+" from CMC analysis : "+donnees[i]['name']))
            importhtml.append(str("Currency's price : "+str(donnees[i]['quote']['EUR']['price'])+'euros.'))
            importhtml.append(str('Percent change last 24hours : '+str(donnees[i]['quote']['EUR']['percent_change_24h'])+'%.'))
            importhtml.append(str('Percent change last hour : '+str(donnees[i]['quote']['EUR']['percent_change_1h'])+'%.'))
            row = str(donnees[i]['name'])+';'+str(donnees[i]['quote']['EUR']['price'])+';'+str(donnees[i]['quote']['EUR']['percent_change_24h'])+';'+str(donnees[i]['quote']['EUR']['percent_change_1h'])+';'+str(donnees[i]['last_updated'])+';'+str(donnees[i]['symbol'])+ '\n'
            csv.write(row)
    incr=4*(i+1)
    csv.close()

    return render_template('index.html', data=importhtml, incr=incr)

#Je return le incr, mais je ne m'en sers plus dans la partie suivante donc on peut s'en servir pour ce qu'on veut
#ou l'enlever aussi si jamais il nous sert à rien

# @app.route('/SomeFunction')
# def SomeFunction():
#     print('In SomeFunction')
#     return "Nothing"

@app.route('/visualize')
def visualize():
    with open("data.csv","r") as csv_reader:
        df = pd.read_csv(csv_reader)
        sns.barplot(df)
        plt.plot()

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)


#Rechangez en 127.0.0.1 ou enlevez simplement la partie host=''
#Mais comme ça on peut émuler sur réseau local un petit serveur

# ==============================================================================