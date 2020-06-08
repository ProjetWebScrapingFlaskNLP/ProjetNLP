# Groupe 1 - Projet NLP

## Introduction

Vous venez d'ouvrir un hôtel. Comme vous n'êtes pas sûr de la qualité de votre établissement, vous permettez aux personnes de poster des commentaires mais pas de mettre de note. Cependant, vous voulez quand même déterminer si le commentaire est positif ou négatif.  

Pour cela, vous allez scrapper des commentaires sur booking et leur note associée afin de faire tourner un algorithme de classification pour faire des prédictions sur vos propres commentaires.

Ce projet vous permet de :
- scrapper les commentaires du site Booking.com
- analyser les commentaires récupérés
- tester plusieurs modèles de classification de texte sur le jeu de données nettoyés
- lancer une application Flask inclut le meilleur modèle de prédiction

## Installation

### Récupération du projet

```
git clone https://github.com/ProjetWebScrapingFlaskNLP/ProjetNLP.git
```

### Création d'un environnement virtuel

Pour éviter tout conflit avec des librairies déjà installées sur votre système, créez un environnement virtuel.

```python
cd ProjetNLP
python3 -m venv venv
source venv/bin/activate
```

### Installation des dépendances

```python
cd ProjetNLP
python3 -m venv venv
pip3 install -r requirements.txt
```

### Première étape : Scraping

Lancer le fichier scraping.ipynb avec le module Jupyter.

Par défaut, le script tourne avec 3 processus, 1 processus correspondant à une recherche sur Booking. Les processus sauvegardent régulièrement les commentaires scrappés dans un fichier CSV associé.Ils s'arrêtent lorsque toutes les pages de résultats ont été scrappé. 

Les recherches par défaut sont :

```python
cities = ['Paris', 'Nice', 'Toulouse']

with multiprocessing.Pool() as pool:
    pool.map(connect_to_booking, cities)
```

Vous pouvez augmenter/modifier le nombre de ville selon vos besoins.

Pour fusionner l'ensemble des fichiers CSV générés, lancer la fonction :

```python
merge_datasets()
```



