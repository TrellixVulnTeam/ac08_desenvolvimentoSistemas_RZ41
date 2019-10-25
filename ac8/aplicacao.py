from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    ##return render_template("index.html")
    return '<h1> teste </h1>'



@app.route('/detalhesEletronica.html')
def eletronica():
    return render_template('detalhesEletronica.html')



@app.route('/detalhesInformaticaIndustrial.html')
def informaticaIndustrial():
    return render_template('detalhesInformaticaIndustrial.html')



@app.route('/detalhesMecatronica.html')
def mecatronica():
    return render_template('detalhesMecatronica.html')



@app.route('/detalhesTelecomunicacoes.html')
def telecomunicacoes():
    return render_template('detalhesTelecomunicacoes.html')



@app.route('/matrizCurricular_Eletronica.html')
def matrizEletronica():
    return render_template('matrizCurricular_Eletronica.html')





@app.route('/matrizCurricular_InformaticaIndustrial.html')
def matrizInformaticaIndustrial():
    return render_template('matrizCurricular_InformaticaIndustrial.html')



@app.route('/matrizCurricular_Mecatronica.html')
def matrizMecatronica():
    return render_template('matrizCurricular_Mecatronica.html')



@app.route('/matrizCurricular_Telecomunicacoes.html')
def matrizTelecomunicacoes():
    return render_template('matrizCurricular_Telecominucacoes.html')



@app.route('/listaCurso.html')
def listaCurso():
    return render_template('listaCurso.html')



@app.route('/noticias.html')
def noticias():
    return render_template('noticias.html')
app.run()
