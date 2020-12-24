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
   app.run()
   
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


Html_file = open("file.html", "w", encoding="utf-8")

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
  
  url = "D:/Git-repositories/cryptocurrency_analysis_for_dummies/file.html"
  
  IndexHeader = """
      <h1><center><strong>The best tool you need to perform in crypto trading</strong></center></h1>
      <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"> </script>
      <script type=text/javascript> $(function() { $("#button").click(function (event) { $.getJSON('/SomeFunction', { }, function(data) { }); return false; }); }); </script>
      <center><button name="button">Refresh page</button></center><br>
  """
  Html_file.write(IndexHeader)
  
  for i in range(0,30):
      
      
      #print("Crypto currency n°",i+1,"from CMC analysis :", donnees[i]['name'])
      #print("Currency's price :", donnees[i]['quote']['EUR']['price'], 'euros.') 
      #print('Percent change last 24hours :', str(donnees[i]['quote']['EUR']['percent_change_24h'])+'%.')
      #print('Percent change last hour :', str(donnees[i]['quote']['EUR']['percent_change_1h'])+'%.')
      #print('\n')
      
      importhtml = []
      
      importhtml.append(str("Crypto currency n° "+str(i+1)+" from CMC analysis : "+donnees[i]['name'])+'<br>')
      importhtml.append(str("Currency's price : "+str(donnees[i]['quote']['EUR']['price'])+'euros.')+'<br>') 
      importhtml.append(str('Percent change last 24hours : '+str(donnees[i]['quote']['EUR']['percent_change_24h'])+'%.')+'<br>')
      importhtml.append(str('Percent change last hour : '+str(donnees[i]['quote']['EUR']['percent_change_1h'])+'%.')+'<br>')
      importhtml.append(str('<br>'))
      
      HTML = """<!DOCTYPE html>
 
            <html>
 
                <head>
 
                    <meta charset="utf-8" />
 
                    <title>Python Project Crypto-Currencies</title>
 
                </head>
 
                <body>
                    {a}{b}{c}{d}{e}
                </body>
 
            </html>""".format(a=importhtml[0],b=importhtml[1],c=importhtml[2],d=importhtml[3],e=importhtml[4])
 
      Html_file.write(HTML)
  webbrowser.open(url,new=new)
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
Html_file.close()
#os.system('pause')
