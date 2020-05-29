from flask import Flask, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/')
def index(prestations=None, titre=None, desc=None):
    prestations = [
        {
            'icon': 'fa-home',
            'desc': '20 villas',
        },
        {
            'icon': 'fa-cutlery',
            'desc': '4 restaurants gastronomiques',
        },
        {
            'icon': 'fa-plane',
            'desc': 'Tours en hélicoptère',
        }
    ]

    description_hotel = "Vous venez d'ouvrir un hôtel. Comme vous n'êtes pas sûr de la qualité de votre établissement, vous permettez aux personnes de poster des commentaires mais pas de mettre de note. Cependant, vous voulez quand même déterminer si le commentaire est positif ou négatif. Pour cela, vous allez scrapper des commentaires sur booking et leur note associée afin de faire tourner un algorithme de classification pour faire des prédictions sur vos propres commentaires."
    return render_template('livredor2.html', prestations=prestations, titre='Projet NLP', desc=description_hotel)

@app.route('/create_comment')
def create_comment(titre=None, parts=None, objectif=None, variables=None):
    nom = "Anonyme"
    if request.form['nom_user']:
        nom = request.form['nom_user']

    comment = request.form['comment']

    # predict if comment is positive or negative
    result = predict_comment(comment)

    # save results in JSON for future usage
    
    return render_template('presentation.html', titre=titre, parts=parts, objectif=objectif, variables=variables)


def predict_comment(comment):
    X_train, X_test, y_train, y_test = train_test_split(df[["sentence"]], df['sentiment'])

if __name__ == '__main__':
    app.run(debug=True)
