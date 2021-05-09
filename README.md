# :moneybag: cryptocurrency_analysis

## :chart: Analyse graphique des cryptomonnaies

## :gear: Mise en route

Ces instructions vous permettront de mettre en place une copie du projet sur votre machine locale à des fins de développement et de test.

### :book: Prérequis

Les éléments dont vous avez besoin pour installer l'application sur l'environnement Windows


#### Télécharger [Python3](https://www.python.org/downloads/)
---

#### Cloner le projet en local
Pour récupérer le projet, il faut effectuer la commande suivante:
```
 git clone https://github.com/Projetmaths/cryptocurrency_analysis.git
```

#### Création d'un compte sur [procoinmarketcap](https://pro.coinmarketcap.com/signup/)

Puis définissez API_KEY dans la variable système et redémarrez le PC
```
setx API_KEY "votre jeton d'api"
```
Installation des dépendances python via le fichier <strong>"requirements.txt"</strong>
```
py -m pip install -r requirements.txt
```


## :pray: Exécuter le programme

```
python ./Projet.py
```
Il faut se rendre sur l'url suivante : http://localhost:5000
![Chart](https://github.com/Projetmaths/cryptocurrency_analysis/blob/master/img/chart.png "Chart Bitcoin")


## :muscle: Construit avec

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Framework python intégrant un serveur web.
* [APScheduler](https://apscheduler.readthedocs.io/en/stable/) - Plannification du code python périodiquement.
* [Chart.js](https://www.chartjs.org/) - Créations des graphiques pour les cryptomonnaies.


## :memo: Versionnage

Nous utilisons [Git](https://git-scm.com/) pour le versionnage Pour les versions disponibles, voir les [commit sur ce dépôt](https://github.com/Projetmaths/cryptocurrency_analysis/releases/tag/v1.0). 

## :beers: Auteurs

**Enrich** **Florian** **Thibault**

[cryptocurrency_analysis](https://github.com/Projetmaths/cryptocurrency_analysis)


## :clap: Remerciements

* Professeur de mathématiques Mr CANTELAUBE Luc pour nous avoir guidé sur la gestion de notre projet et à avoir fait force de proposition concerant les outils à utiliser.


