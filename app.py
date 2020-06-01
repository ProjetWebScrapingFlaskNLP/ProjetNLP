from flask import Flask, url_for, request, render_template, redirect
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np 
 

app = Flask(__name__)   

def fit_model():
    df = pd.read_csv('static/data/dataset.csv')
    
    # split data
    X_train, X_test, y_train, y_test = train_test_split(df[["sentence"]], df['sentiment'])

    # get points
    pipe = make_pipeline(CountVectorizer(), TfidfTransformer())
    pipe.fit(X_train['sentence'])

    feat_train = pipe.transform(X_train['sentence'])
    feat_test = pipe.transform(X_test['sentence'])

    # train model
    clf = RandomForestClassifier(n_estimators=50, max_depth=40, random_state=42)
    clf = clf.fit(feat_train, y_train)
    score_train = clf.score(feat_train, y_train)
    score_test = clf.score(feat_test, y_test)

    print(score_train, score_test)

    return clf, pipe

def predict_comment(comment, clf, pipe):  
    # predict 
    feat_comment = pipe.transform([comment])
    
    predict = "Négatif" 

    if clf.predict(feat_comment):
        predict = "Positif"

    return predict

def save_comment(new_comment, df):
    df.loc[len(df.index)] = new_comment
    df.to_csv('static/data/comments.csv') 
 
clf, pipe = fit_model() 

@app.route('/')
def index(prestations=None, titre=None, desc=None, comments=None):
    # get prestations of simplon hotel
    prestations = [    
        {
            'icon': 'fa fa-home', 
            'desc': '20 villas',
        },
        {
            'icon': 'fa fa-cutlery',
            'desc': 'Restaurant gastronomique',
        },
        {
            'icon': 'fas fa-umbrella-beach',
            'desc': 'Plage privée',
        },
        {
            'icon': 'fas fa-spa',
            'desc': 'Spa services'
        }
    ]

    # read the database to fetch comments
    df_comments = pd.read_csv('static/data/comments.csv', index_col='Unnamed: 0')

    # we want to fead the latest comments first
    comments = df_comments.values[::-1]  

    #nb_comments in database
    nb_comments = len(df_comments.index)

    description_hotel = "Vous venez d'ouvrir un hôtel. \
    Comme vous n'êtes pas sûr de la qualité de votre établissement, \
    vous permettez aux personnes de poster des commentaires mais pas de mettre de note. \
    Cependant, vous voulez quand même déterminer si le commentaire est positif ou négatif. \
    Pour cela, vous allez scrapper des commentaires sur booking et leur note associée afin de \
    faire tourner un algorithme de classification pour faire des prédictions sur vos propres commentaires."
    titre = 'Projet NLP - Nohossat, Valérie, Williams'

    return render_template('home.html', 
                            prestations=prestations, 
                            titre= titre, 
                            desc=description_hotel, 
                            comments=comments,
                            nb_comments = nb_comments) 


@app.route('/create_comment', methods=['POST'])
def create_comment(titre=None, parts=None, objectif=None, variables=None, clf=clf, pipe=pipe):
    
    nom = "Anonyme"
    if request.form['nom_user']:
        nom = request.form['nom_user']

    comment = request.form['comment']

    # predict if comment is positive or negative
    result = predict_comment(comment, clf, pipe)

    # save to database
    df_comments = pd.read_csv('static/data/comments.csv', index_col='Unnamed: 0')
    save_comment([nom, comment, result], df_comments)

    # refresh homepage and go straight to the comments section
    return redirect(url_for('index') + '#comments') 

if __name__ == '__main__':
    app.run(debug=True)
