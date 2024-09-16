from gtts import gTTS
from flask import Flask, render_template, request
import os

app= Flask(__name__)# cria aplivativo flask]

# / -> pagina principal
# POST -> INSERIR
# GET -> RECUPERAR
@app.route('/senia',methods=['GET','POST'])
def abrir_assistente():
    audio_path= None
    # Pegar valor do html <textfield>
    if request.method== 'POST':
        texto= request.form['texto']

        # configurar o idioma
        lingua='pt-br'

        # criação do objeto

        tts= gTTS(text=texto,lang=lingua)
        

        #  Nome do arquivo de audio

        audio_path= 'static/audio_exemplo.mp3'

        # Salvar arquivo
        tts.save(audio_path)
    return render_template('senia.html',audio=audio_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def logar():
    return render_template('login.html')

@app.route('/autenticar',methods=['GET','POST'])
def autentificar():
    # mock
    if request.method == 'POST':
        if request.form['senha']=='123' and request.form['usuario']=='joao':
            return render_template('senia.html')
        else:
            msg='Erro de autentificação'
            return render_template('login.html',msg=msg)

if __name__=='__main__':
    app.run(debug=True)


    




