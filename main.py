from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=['*'],  # Permitir todos os métodos HTTP (GET, POST, etc.)
    allow_headers=['*']   # Permitir todos os cabeçalhos HTTP
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

vendas = {
    1: {'item': 'trembolona', 'preco': 300, 'qtd': 5},
    2: {'item': 'hemorrage', 'preco': 180, 'qtd': 2},
    3: {'item': 'decatron', 'preco': 530, 'qtd': 9},
    4: {'item': 'seringuinha', 'preco': 2, 'qtd': 35},
}


@app.get('/')
def home():
    return {'Vendas': len(vendas)}

@app.get('/vendas')
def get_vendas():
    return vendas

@app.get('/vendas/{id_venda}')
def mostrar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {'Erro': 'ID Venda inexistente'}
        


