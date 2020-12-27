#much love ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import webbrowser
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

#==============================================================================
                                    #FLASK

@app.route('/')
def index():
    return render_template('index.html ')

@app.route('/SomeFunction')
def SomeFunction():
    print('In SomeFunction')
    return "Nothing"



if __name__ == '__main__':
   app.run(debug=True)
   
#==============================================================================

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'30',
  'convert':'EUR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '4aaaa51e-2ac2-48ce-8e75-a49c61efeb33',
}


session = Session()
session.headers.update(headers)
new = 2
try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data) #-> print absolument TOUT donc c'est bien pour voir les tuples mais c'est tout c:
  #print("Sentence describing what you want to tell : ", data['data'])
  donnees = data['data']
  #donnees[n] -> donne l'item classé au rang 'cmc_rank'=n+1
  #donnees[i]['data_you_want_to_print'] -> print la colonne 'data_you_want_to_print' 
  #de l'item i (au rang 0 ce sera la colonne 'blabla' du BTC, et etc)
  

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#os.system('pause')
