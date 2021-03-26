# Dependencies
from flask import Flask, render_template, Response, request, redirect, url_for,send_file
from apscheduler.schedulers.background import BackgroundScheduler
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import os
import sys

# FLASK Application
app = Flask(__name__)
scheduler = BackgroundScheduler()

# API KEY
api_key = os.getenv("API_KEY")

if not api_key:
    print("API_KEY variable missing ")
    sys.exit(1)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/chart')
def chart():
    lim=15
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start': '1', 'limit': lim, 'convert': 'EUR'}
    headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': api_key }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = response.json()
        donnees = data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        
    for i in range(0, lim):
        nomcrypto=str("csv/"+donnees[i]['symbol']+".csv")
        os.remove(nomcrypto)
        with open(nomcrypto, "w") as csvfile:
            row = str(donnees[i]['name'])+';'+str(donnees[i]['quote']['EUR']['price'])+';'+str(donnees[i]['last_updated'])+';'+str(donnees[i]['symbol'])+ '\n'
            csvfile.write(row)
        csvfile.close()
        
    tab = []
    labels = []
    data = []
    name = []
    symbol = []    
    
    for i in range(0, lim):
        nomcrypto=str("csv/"+donnees[i]['symbol']+".csv")
        
        with open(nomcrypto, "r") as file:  # on open les fichiers csv ici
            csv_reader=csv.reader(file)     # on lit le contenu du fichier csv ouvert juste avant, définit par la boucle for au début (ligne 75)
            print()
            count=0
            for row in csv_reader:          # on parse chaque ligne du fichier
                         
                lignes=str(row).split(';')  # on split les éléments avec le caractère `;` définit plus haut dans le code
                   
                for ligne in lignes:  
                    tab.append(ligne)
                    
                val1=tab[0]
                val2=tab[1]
                val3=tab[2]
                val4=tab[3]  

                val1=val1.replace("['", "")
                val3=val3.replace("T", " | ")
                val3=val3.replace("Z", "")
                val4=val4.replace("']", "")

                labels.append(val3) #insérer date pour axe x   
                data.append(val2) #insérer prix pour axe y
                name.append(val1)
                symbol.append(val4)

                count+=1
                
    return render_template('chart.html', labels = labels, data = data, lim=lim, count=count, name=name, symbol=symbol) 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled task', func = chart, trigger = 'interval', seconds = 3600 )
    scheduler.start()
    app.run(debug=True, host='localhost')
