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

#### Activation de XGBoost

L'activation de XGBoost dépend du système d'exploitation. 


##### Installation Linux

Sur Ubuntu, il faut lancer les commandes suivantes 

```
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost
mkdir build
cd build
cmake ..
make -j$(nproc)
```

##### Installation OSX

Sur les systèmes OSX, il faut installer la librairie OpenMP pour activer le multi-threading. 

```
brew install libomp
```

##### Installation Windows

- Télécharger [Cmake](https://cmake.org/download/)
- Lancer les commandes suivantes: 

```
git clone --recursive https://github.com/dmlc/xgboost
git submodule init
git submodule update

mkdir build
cd build
cmake .. -G"Visual Studio 14 2015 Win64"
# for VS15: cmake .. -G"Visual Studio 15 2017" -A x64
# for VS16: cmake .. -G"Visual Studio 16 2019" -A x64
cmake --build . --config Release
python setup.py install
```

### Installation des dépendances

```python
cd ProjetNLP
python3 -m venv venv
pip3 install -r requirements.txt
```

### Première étape : Scraping

Lancer le fichier scraping.ipynb avec le module Jupyter.

Par défaut, le script tourne avec 3 processus, 1 processus correspondant à une recherche sur Booking. Les processus sauvegardent régulièrement les commentaires scrappés dans un fichier CSV associé. Ils s'arrêtent lorsque toutes les pages de résultats ont été scrappé. 

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

### Analyse des données 

Lancer le fichier analyse_donnees.ipynb depuis Jupyter Notebook.

Exécuter toutes les cellules pour observer les statistiques et récupérer le dataset nettoyé et normalisé (tokenisation, retrait des stop words et stemming).

### Machine Learning

Lancer le fichier machine_learning.ipynb depuis Jupyter Notebook.

Exécuter toutes les cellules pour avoir une analyse comparative de plusieurs modèles de classification. 

### Application Flask

#### Lancement de l'application

```python
export FLASK_APP=app.py
flask run
```




