from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/presentation')
def presentation(parts=None):
    parts = [
        {
            'titre':'Introduction',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#intro'
        },
         {
            'titre': 'Recuperation des donnees',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#scrap'
        },
         {
            'titre':'Preprocessing',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#prepro'
        },
        {
            'titre':'Modelisation',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#model'
        },
        {
            'titre':'Resultats',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#resultat'
        },
         {
            'titre':'Application',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#appli'
        },
        {
            'titre':'Conclusion',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#conclusion'
        },
        {
            'titre':'Difficultes rencontrees',
            'desc' : 'Verum ad istam omnem orationem brevis est defensio. Nam quoad aetas M. Caeli dare potuit isti suspicioni locum',
            'link' : '#difficulte'
        },
    ]
    return render_template('presentation.html', parts=parts)

@app.route('/livredor')
def livredor():
    return render_template('livredor.html')


if __name__ == '__main__':
    app.run(debug=True)
