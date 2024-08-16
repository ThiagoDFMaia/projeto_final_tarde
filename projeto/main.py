from flask import Flask, render_template,request


# Importa a função `sessionmaker`, que é usada para criar uma nova sessão para interagir com o banco de dados
from sqlalchemy.orm import sessionmaker

# Importa as funções `create_engine` para estabelecer uma conexão com o banco de dados e `MetaData` para trabalhar com metadados do banco de dados
from sqlalchemy import create_engine, MetaData

# Importa a função `automap_base`, que é usada para refletir um banco de dados existente em classes ORM automaticamente
from sqlalchemy.ext.automap import automap_base


from aluno import Aluno
import pymysql
from conexao import ConexaoSingleton




app = Flask(__name__)

# Criando a configuração do banco de dados
# Configuração do Banco de Dados
# biblioteca para converter e resolver problema do @
import urllib.parse

# Qual o usuário do banco e a senha?
"""
user = 'root'
password = urllib.parse.quote_plus('senai@123')

host = 'localhost'
database = 'schooltracker'
connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'
"""

conexao_instance = ConexaoSingleton()
engine = conexao_instance.get_engine()

# Criar a engine e refletir o banco de dados existente
# engine = create_engine(connection.engine)
metadata = MetaData()
metadata.reflect(engine)


# Mapeamento automático das tabelas para classes Python
Base = automap_base(metadata=metadata)
Base.prepare()

# Acessando a tabela 'aluno' mapeada
Aluno = Base.classes.aluno



# Criar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# session.add()
# session.commit()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route('/novoaluno',methods=['POST'])
def inserir_aluno():
    ra = request.form['ra']
    nome = request.form['nome']
    tempoestudo = request.form['tempoestudo']
    rendafamiliar = request.form['rendafamiliar']

    # sessão ok
   
    
    try:
        existe=session.query(Aluno).filter_by(ra=ra).first()
        if existe:
            mensagem='RA ja cadastrada! Tente novamente..'
            return render_template('index.html',resposta=mensagem) 

  
        aluno = Aluno(ra=ra,nome=nome,tempoestudo=tempoestudo,rendafamiliar=rendafamiliar)
   
        session.add(aluno)
        session.commit()
    except:
        session.rollback()

    finally:
        session.close()
    
    mensagem= "cadastro realizado com sucesso"



    return render_template('index.html',resposta=mensagem)


@app.route('/alunos',methods=['GET'])
def listar_alunos():
    try:
        alunos=session.query(Aluno).all()
    except:
        session.rollback()
        msg= "Erro ao tentar retornar a lista de alunos"
        return render_template ('index.html',msgbanco=msg)
    finally:
        session.close()

    return render_template ('/lista_alunos.html',resposta=alunos)

if __name__ == "__main__":
    app.run(debug=True)
