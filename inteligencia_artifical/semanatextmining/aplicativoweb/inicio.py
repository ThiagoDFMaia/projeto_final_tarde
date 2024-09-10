from gtts import gTTS
from flask import Flask, render_template, request
import os

app= Flask(__name__)# cria aplivativo flask]

# / -> pagina principal
# POST -> INSERIR
# GET -> RECUPERAR
@app.route('/',methods=['GET','POST'])
def index():
    audio_path= None
    # Pegar valor do html <textfield>
    if request.method== 'POST':
        texto= request.form['texto']

        # configurar o idioma
        lingua='pt'

        # criação do objeto

        tts= gTTS(text=texto,lang=lingua)
        

        #  Nome do arquivo de audio

        audio_path= 'static/audio_exemplo.mp3'

        # Salvar arquivo
        tts.save(audio_path)
    return render_template('index.html',audio=audio_path)

if __name__=='__main__':
    app.run(debug=True)


    




