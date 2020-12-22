#much love ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import webbrowser

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


Html_file = open("file.html", "wb")

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
  
  #Html_file.write('<html>')
  #Html_file.write('<body>')
  for i in range(0,30):
      print("Crypto currency n°",i+1,"from CMC analysis :", donnees[i]['name'])
      print("Currency's price :", donnees[i]['quote']['EUR']['price'], 'euros.') 
      print('Percent change last 24hours :', str(donnees[i]['quote']['EUR']['percent_change_24h'])+'%.')
      print('Percent change last hour :', str(donnees[i]['quote']['EUR']['percent_change_1h'])+'%.')
      print('\n')
      
     # message = """
      
     # """
      
      """Html_file.write('<p>')
      Html_file.write("Crypto currency n°")
      Html_file.write(str(i+1))
      Html_file.write("from CMC analysis :")
      Html_file.write(str(donnees[i]['name']))
      
      Html_file.write("Currency's price :")
      Html_file.write(str(donnees[i]['quote']['EUR']['price']))
      Html_file.write('euros.')
      
      Html_file.write('Percent change last 24hours :')
      Html_file.write(str(donnees[i]['quote']['EUR']['percent_change_24h'])+'%.')
      
      Html_file.write('Percent change last hour :')
      Html_file.write(str(donnees[i]['quote']['EUR']['percent_change_1h'])+'%.')
      
      Html_file.write('\n')
      Html_file.write('</p>')"""
      
      
  #Html_file.write('</body>')
  #Html_file.write('</html>')
  #webbrowser.open(url,new=new)
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  

os.system('pause')
Html_file.close()