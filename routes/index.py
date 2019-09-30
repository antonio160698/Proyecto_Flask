from flask import Flask, render_template
from random import randint
from routes.curso.basic_example import Example
import pandas as pd
app = Flask(__name__)
ex = Example()
@app.route('/curso/')
def homecurso():
    return ex.helloworld3()

@app.route('/curso/authors')
def authorscurso():
    return ex.authors()

@app.route('/curso/author/<authors_last_name>')
def authorcurso(authors_last_name):
    return ex.author(authors_last_name)

@app.errorhandler(404)
def not_found(error):
    return render_template('curso/404.html'), 404

@app.errorhandler(400)
def not_found_400(error):
    return {"message":"perfecto"}, 400

@app.route('/curso/author/<string:authors_last_name>/edit')
def author_admin(authors_last_name):
    return ex.abort_401()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/CurriculumVitae')
def CurriculumVitae():
    # return render_template('CV.html', name="Antonio")
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
"'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
"'To understand recursion you must first understand recursion..' -- Unknown",
"'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
"'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
"'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]

    return render_template('CV.html',**locals())

@app.route('/Pandas')
def pandas():
    algo = pd.read_csv('AlumnoModificado.csv')
    datos = pd.read_csv('saved.csv', encoding="ISO-8859-1")
    materia = datos.iloc[:,[0,3,4,6,7,9]]
    before=materia.drop_duplicates().reset_index(drop=True)
    length = before.shape[0]
    return render_template('pandas.html',**locals())

@app.route('/Vertice')
def vertice():
    return render_template('Vertice.html')
