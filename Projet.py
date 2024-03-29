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
scheduler = BackgroundScheduler(daemon=True)

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
    lim=5
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
        with open(nomcrypto, "a") as csvfile:
            row = str(donnees[i]['name'])+';'+str(donnees[i]['quote']['EUR']['price'])+';'+str(donnees[i]['last_updated'])+';'+str(donnees[i]['symbol'])+ '\n'
            csvfile.write(row)
        csvfile.close()
    labels = []
    data = []
    
    prix_btc = []
    date_btc = []

    prix_ada = []
    date_ada = []

    prix_bch = []
    date_bch = []

    prix_bnb = []
    date_bnb = []

    prix_doge = []
    date_doge = []

    prix_dot = []
    date_dot = []

    prix_eth = []
    date_eth = []

    prix_link = []
    date_link = []

    prix_ltc = []
    date_ltc = []

    prix_luna = []
    date_luna = []

    prix_klay = []
    date_klay = []

    prix_theta = []
    date_theta = []

    prix_uni = []
    date_uni = []

    prix_usdc = []
    date_usdc = []

    prix_usdt = []
    date_usdt = []

    prix_wbtc = []
    date_wbtc = []

    prix_xlm = []
    date_xlm = []

    prix_xrp = []
    date_xrp = []

    prix_fil = []
    date_fil = []


    name = []
    symbol = []    
    for i in range(0, lim):
        nomcrypto=str("csv/"+donnees[i]['symbol']+".csv")
        with open(nomcrypto, "r") as file:  # on open les fichiers csv ici
            csv_reader=csv.reader(file)     # on lit le contenu du fichier csv ouvert juste avant, définit par la boucle for au début (ligne 75)
            count=0
            for row in csv_reader:          # on parse chaque ligne du fichier       
                lignes=str(row).split(';')  # on split les éléments avec le caractère `;` définit plus haut dans le code
                
                tab = []   
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
                name.append(val1) #insérer nom
                symbol.append(val4) #insérer acronyme
                
                
                if tab[0] == "['Bitcoin":
                    prix_btc.append(val2)
                    date_btc.append(val3)
                    
                if tab[0] == "['Cardano":
                    prix_ada.append(val2)
                    date_ada.append(val3)
                    
                if tab[0] == "['Bitcoin Cash":
                    prix_bch.append(val2)
                    date_bch.append(val3)
                
                if tab[0] == "['Binance Coin":
                    prix_bnb.append(val2)
                    date_bnb.append(val3)
                
                if tab[0] == "['Dogecoin":
                    prix_doge.append(val2)
                    date_doge.append(val3)
                
                if tab[0] == "['Polkadot":
                    prix_dot.append(val2)
                    date_dot.append(val3)

                if tab[0] == "['Ethereum":
                    prix_eth.append(val2)
                    date_eth.append(val3)
                
                if tab[0] == "['Chainlink":
                    prix_link.append(val2)
                    date_link.append(val3)
                
                if tab[0] == "['Litecoin":
                    prix_ltc.append(val2)
                    date_ltc.append(val3)
                
                if tab[0] == "['Terra":
                    prix_luna.append(val2)
                    date_luna.append(val3)

                if tab[0] == "['Klaytn":
                    prix_klay.append(val2)
                    date_klay.append(val3)

                if tab[0] == "['Theta":
                    prix_theta.append(val2)
                    date_theta.append(val3)

                if tab[0] == "['Uniswap":
                    prix_uni.append(val2)
                    date_uni.append(val3)

                if tab[0] == "['USD Coin":
                    prix_usdc.append(val2)
                    date_usdc.append(val3)

                if tab[0] == "['Tether":
                    prix_usdt.append(val2)
                    date_usdt.append(val3)

                if tab[0] == "['Wrapped Bitcoin":
                    prix_wbtc.append(val2)
                    date_wbtc.append(val3)

                if tab[0] == "['Stellar":
                    prix_xlm.append(val2)
                    date_xlm.append(val3)

                if tab[0] == "['XRP":
                    prix_xrp.append(val2)
                    date_xrp.append(val3)

                if tab[0] == "['Filecoin":
                    prix_fil.append(val2)
                    date_fil.append(val3)

                count+=1         

              
    return render_template('chart.html', labels = labels, data = data,  lim=lim, count=count, name=name, symbol=symbol, prix_btc = prix_btc, date_btc = date_btc, prix_ada = prix_ada, date_ada = date_ada , prix_bch = prix_bch, date_bch = date_bch, prix_bnb = prix_bnb, date_bnb = date_bnb, prix_doge = prix_doge, date_doge = date_doge,prix_dot = prix_dot, date_dot = date_dot,prix_eth = prix_eth, date_eth = date_eth,prix_link = prix_link, date_link = date_link,prix_ltc = prix_ltc, date_ltc = date_ltc,prix_luna = prix_luna, date_luna = date_luna ,prix_klay = prix_klay,date_klay = date_klay,prix_theta = prix_theta,date_theta = date_theta,prix_uni = prix_uni,date_uni = date_uni,prix_usdc = prix_usdc,date_usdc = date_usdc,prix_usdt = prix_usdt,date_usdt = date_usdt,prix_wbtc = prix_wbtc,date_wbtc = date_wbtc,prix_xlm = prix_xlm,date_xlm = date_xlm,prix_xrp = prix_xrp,date_xrp = date_xrp, prix_fil = prix_fil, date_fil = date_fil) 

    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    try:
        seconds = int(input("Set updating time of data chart in seconds: "))
    except ValueError:
        print("The value is not an integer ")
        sys.exit(1)
    scheduler.add_job(id = 'update of data charts', func = chart, trigger = 'interval', seconds = seconds )
    scheduler.start()
    app.run(debug=True, host='localhost')
