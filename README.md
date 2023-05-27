# Scrapy_Version

Ce script Python utilise Scrapy, un framework de web scraping, pour extraire des données du site Avito. Les données extraites sont ensuite stockées dans une base de données MongoDB. Le script récupère des informations sur les voitures à vendre dans différentes villes à partir d'Avito et les enregistre dans un format structuré.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les dépendances suivantes :

- Python (version 3.6 ou ultérieure)
- Scrapy (installation : `pip install scrapy`)
- pymongo (installation : `pip install pymongo`)
- MongoDB (Assurez-vous d'avoir une instance MongoDB en cours d'exécution sur `localhost`)

## Utilisation

1. Clonez ce dépôt ou téléchargez le fichier `avitoScrape.py`.

2. Ouvrez un terminal ou une invite de commandes et naviguez jusqu'au répertoire contenant le fichier `avitoScrape.py`.

3. Exécutez le script avec la commande suivante :
```shell
scrapy crawl avitoScrape
```

Cela lancera le processus de scraping. Le script visitera les pages Avito pour différentes villes, extraira les données pertinentes et les stockera dans la base de données MongoDB.

4. Une fois que le script a terminé son exécution, vous pouvez vérifier la base de données MongoDB pour consulter les données extraites.

## Configuration

Le script est actuellement configuré pour se connecter à une instance MongoDB en cours d'exécution sur `localhost` avec les paramètres par défaut. Si vous avez une configuration MongoDB différente, vous pouvez modifier la ligne suivante dans le code pour correspondre à votre configuration :

```python
self.client = MongoClient('mongodb://localhost:27017/mydb?directConnection=true')
```
Remplacez `mongodb://localhost:27017/mydb?directConnection=true` par votre chaîne de connexion MongoDB.
