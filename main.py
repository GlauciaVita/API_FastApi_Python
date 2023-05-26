from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {'item': 'trembolona', 'preco': 300, 'qtd': 5},
    2: {'item': 'hemorrage', 'preco': 180, 'qtd': 2},
    3: {'item': 'decatron', 'preco': 530, 'qtd': 9},
    4: {'item': 'seringuinha', 'preco': 2, 'qtd': 30},
}


@app.get('/')
def home():
    return {'Vendas': len(vendas)}


@app.get('/vendas/{id_venda}')
def mostrar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {'Erro': 'ID Venda inexistente'}


