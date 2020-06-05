from flask import Flask, url_for, request, render_template, redirect
import pandas as pd
import numpy as np 
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import FrenchStemmer
from stop_words import get_stop_words
import string
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.pipeline import make_pipeline
 

app = Flask(__name__)   

def remove_stopwords(commentaire):
    # remove stop words from the review
    stop_words = get_stop_words('french')  
    
    # remove stop words, punctuation and words which length is below 2, numbers and none values
    commentaire = [word for word in commentaire if word.lower() not in stop_words and word not in string.punctuation and not word.isnumeric() and word.lower() != 'none' and len(word) > 2]
    
    return ' '.join(commentaire)

def stem_review(review):
    stem = FrenchStemmer()
    review = review.split(' ')
    return [stem.stem(word) for word in review]

def prepare_test_data(test_review):
    # tokenize data
    review_tokens = word_tokenize(test_review)
    
    # remove stop words
    review_tokens = remove_stopwords(review_tokens)
    
    #stem tokens
    review_tokens = stem_review(review_tokens)
    
    #return string
    return ' '.join(review_tokens)

def fit_model():
    df = pd.read_csv('static/data/dataset_model.csv')
    
    # split data
    X_train, X_test, y_train, y_test = train_test_split(df["sentence"], df['polarite'], test_size=0.2, random_state=0)
    print(X_train.isna().sum())
    # get points
    pipe = make_pipeline(CountVectorizer(), TfidfTransformer())
    pipe.fit(X_train)

    feat_train = pipe.transform(X_train)
    feat_test = pipe.transform(X_test)

    # train model
    clf = RandomForestClassifier(n_estimators=100, max_depth=40, random_state=42)
    clf = clf.fit(feat_train, y_train)
    score_train = clf.score(feat_train, y_train)
    score_test = clf.score(feat_test, y_test)

    print(score_train, score_test)

    return clf, pipe

def predict_comment(test_review, clf, pipe):  
    # prepare data
    review = prepare_test_data(test_review)
    print(review)

    # predict 
    transformed_review = pipe.transform([review])
    
    predict = "Négatif" 

    print(clf.predict(transformed_review))

    if clf.predict(transformed_review):
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
