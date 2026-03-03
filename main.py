from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 🔹 Classe modelo
class Cidade(BaseModel):
    id: int
    nome: str
    uf: str

# 🔹 Classe para criação (sem id)
class NovaCidade(BaseModel):
    nome: str
    uf: str

# 🔹 Lista simulando banco
cidades = [
    Cidade(id=1, nome='Teresina', uf='PI'),
    Cidade(id=2, nome='Altos', uf='PI'),
    Cidade(id=3, nome='Coelho Neto', uf='MA'),
    Cidade(id=4, nome='Pedro II', uf='PI'),
]

# 🔹 Controle de ID automático
proximo_id = 5

# =========================
# ROTAS
# =========================

@app.get('/cidades')
def listar_cidades():
    return cidades

@app.get('/cidades/{id}')
def cidades_detail(id: int):
    for cidade in cidades:
        if cidade.id == id:
            return cidade
    raise HTTPException(status_code=404, detail="Cidade não encontrada")

@app.post('/cidades', status_code=201)
def cidades_create(nova_cidade: NovaCidade):
    global proximo_id
    
    cidade = Cidade(
        id=proximo_id,
        nome=nova_cidade.nome,
        uf=nova_cidade.uf
    )
    
    proximo_id += 1
    cidades.append(cidade)
    
    return cidade