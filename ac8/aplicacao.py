from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('detalhesEletronica.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('detalhesInformáticaIndustrial.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('detalhesMecatronica.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('detalhesTelecomunicacoes.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('matrizCurricular_Eletronica.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('matrizCurricular_InformaticaIndustrial.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('matrizCurricular_Mecatronica.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('matrizCurricular_Telecominucacoes.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/listaCurso')
def index():
    return render_template('listaCurso.html')
app.run()

from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/noticias')
def index():
    return render_template('noticias.html')
app.run()