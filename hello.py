from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/presentation')
def presentation(titre=None, parts=None, objectif=None, variables=None):

    objectif = {
        'titre' : "Classification de commentaires",
        'desc' : "Vous venez d'ouvrir un hôtel. Comme vous n'êtes pas sûr de la qualité de votre établissement, vous permettez aux personnes de poster des commentaires mais pas de mettre de note. Cependant, vous voulez quand même déterminer si le commentaire est positif ou négatif. Pour cela, vous allez scrapper des commentaires sur booking et leur note associée afin de faire tourner un algorithme de classification pour faire des prédictions sur vos propres commentaires."
    }

    parts = [
        {
            'titre':'Introduction',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : 'intro'
        },
         {
            'titre': 'Scraping',
            'sstitre' : 'Récupération du dataset',
            'desc' : 'Raptim igitur properantes ut motus sui rumores celeritate nimia praevenirent, vigore corporum ac levitate confisi per flexuosas semitas ad summitates collium tardius evadebant. et cum superatis difficultatibus arduis ad supercilia venissent fluvii Melanis alti et verticosi, qui pro muro tuetur accolas circumfusus, augente nocte adulta terrorem quievere paulisper lucem opperientes. arbitrabantur enim nullo inpediente transgressi inopino adcursu adposita quaeque vastare, sed in cassum labores pertulere gravissimos.',
            'site': 'Booking',
            'url' : 'https://www.booking.com/',
            'link' : 'scrap'
        },
         {
            'titre':'Preprocessing',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : 'prepro'
        },
        {
            'titre':'Modèle',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : 'model'
        },
        {
            'titre':'Résulats',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : 'resultat'
        },
         {
            'titre':'Conclusions',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : 'conclusion'
        }, 
        {
            'titre':'Livre d\'or',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '/livredor'
        },
    ]

    variables = [
        {
            'nom': 'nom',
            'type' : 'string',
            'desc' : 'nom de l\'invité'
        },
        {
            'nom': 'pays',
            'type' : 'string',
            'desc' : 'Nationalité de l\'invité'
        },
        {
            'nom': 'favorite',
            'type' : 'integer',
            'desc' : 'indique si l\'hébergement fait parti des favoris de l\'invité'
        },
        {
            'nom': 'date',
            'type' : 'datetime',
            'desc' : 'la date d\'envoi du commentaire'
        },
        {
            'nom': 'titre',
            'type' : 'string',
            'desc' : 'le titre du commentaire'
        },
        {
            'nom': 'bons points',
            'type' : 'string',
            'desc' : 'les points positifs relevés par l\'invité'
        },
        {
            'nom': 'mauvais points',
            'type' : 'string',
            'desc' : 'les points négatifs relevés par l\'invité'
        },
        {
            'nom': 'note',
            'type' : 'string',
            'desc' : 'note attribuée au séjour par l\'invité'
        },
        {
            'nom': 'type établissement',
            'type' : 'string',
            'desc' : 'le type d\'établissement comme par exemple Appartement, Hôtel, etc...'
        },
        {
            'nom': 'lieu',
            'type' : 'string',
            'desc' : 'le lieu du séjour'
        },
        {
            'nom': 'note établissement',
            'type' : 'string',
            'desc' : 'note moyenne attribuée à l\'établissement par l\'ensemble des invités'
        }
    ]

    titre = 'Projet NLP'

    return render_template('presentation.html', titre=titre, parts=parts, objectif=objectif, variables=variables)

@app.route('/livredor')
def livredor():
    return render_template('livredor.html')


if __name__ == '__main__':
    app.run(debug=True)
