# importando as bibliotecas e modulos
from fastapi import FastAPI, HTTPException, status, Depends
# biblioteca de token de segurança
from fastapi.security import OAuth2PasswordBearer
import csv


app= FastAPI()

auth2_scheme=OAuth2PasswordBearer(tokenUrl='token')

def verifica_token(token: str):
    if token != 'supersecreto':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return {'usuario': 'thiago'}

@app.post('/token')
async def login():
    return {'access_token': 'supersecreto','token_type': 'bearer'}

@app.get('/')
async def index(token:str= Depends(auth2_scheme)):
    usuario=verifica_token(token)


    return {'mensagem':f'Olá {usuario}'}

@app.get('/items/{item_id}')
async def ler_item(item_id: int, pesquisa: str):
    return  {'ID do item': item_id, 'caisa de pesquisa': pesquisa}

@app.get('/creditos/{idade}')
async def filtrar_por_idade(indade: int):
    lista=[]
    with open('dataset/credit_risk_dataset.csv') as arquivo:
        for linha in arquivo:
            if linha[0]==indade:
                lista.append({'loan_intent': linha[4]})
    return lista    

