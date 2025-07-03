from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
from fastapi.responses import JSONResponse
from datetime import timedelta

app = FastAPI()


# Dados simulados
dados_fake = {
   
    "token": [
        {
            "id_token": 1,
            "token": "abcd1234",
            "data_hora_inicio": datetime.now().isoformat(),
            "data_hora_fim": datetime.now().isoformat(),
            "resposta_cautela": "Aprovado",
            "observacoes": "Nenhuma",
        },
    ],
    "regiao": [
        {
            "id_regiao": 1,
            "nome_regiao": "Região Norte",
            "latitude": -10.12345,
            "longitude": -50.67890,
            "descricao": "Área rural extensa",
            "status": "Ativa",
            "municipios": "Município A, Município B",
            "criado_em": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": datetime.now().isoformat(),
            "atualizado_por": "alberto",
        },
        {
            "id_regiao": 2,
            "nome_regiao": "Região Noroeste",
            "latitude": -10.12345,
            "longitude": -50.67890,
            "descricao": "Área com pequenas propriedades",
            "status": "Ativa",
            "municipios": "Município C, Município D",
            "criado_em": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
        },
    ],
    "guarnicao": [
        {
            "id_guarnicao": 1,
            "responsavel": "Capitão Silva",
            "membro": "Sargento Oliveira, Cabo Pereira"
        },
    ],

    "policial": [
    {
        "id_pm": 1,
        "nome": "João Silva",
        "cpf": 12345678901,
        "cod_pm": 1001,
        "rg_pm": 123456789,
        "posto_grad_abrev": "CB"
    },
    {
        "id_pm": 2,
        "nome": "Maria Oliveira",
        "cpf": 98765432109,
        "cod_pm": 1002,
        "rg_pm": 987654321,
        "posto_grad_abrev": "SGT"
    },
    {
        "id_pm": 3,
        "nome": "Carlos Pereira",
        "cpf": 45678912304,
        "cod_pm": 1003,
        "rg_pm": 456123789,
        "posto_grad_abrev": "TEN"
    },
    {
        "id_pm": 4,
        "nome": "Ana Santos",
        "cpf": 78932165400,
        "cod_pm": 1004,
        "rg_pm": 789321654,
        "posto_grad_abrev": "CAP"
    },
],

    "patrulha": [
        {
            "id_patrulha": 1,
            "id_token": 1,
            "data_inicio": datetime.now().isoformat(),
            "data_final": datetime.now().isoformat(),
            "descricao": "Ronda de patrulhamento da zona rural",
            "id_regiao": 1,
        },
    ],

    "ocorrencia": [
        {
            "id_ocorrencia": 1,
            "guarnicao": "1",
            "numero_ocorrencia": "20230001",
            "descricao": "Furto de equipamentos agrícolas",
            "data_ocorrencia": datetime.now().isoformat(),
        },
        {
            "id_ocorrencia": 2,
            "guarnicao": "2",
            "numero_ocorrencia": "20230002",
            "descricao": "Denúncia de invasão de propriedade",
            "data_ocorrencia": (datetime.now() - timedelta(days=1)).isoformat(),
        },
    ],
    "viatura": [
        {
            "id_viatura": 1,
            "id_patrulha": 1,
            "placa": "PMR-1234",
            "km_inicial": 15000.5,
            "km_final": 15045.3,
            "status": "Disponível",
            "modelo": "Toyota Hilux",
            "capacidade": 5,
            "opm_responsavel": "5º BPM",
            "quilometragem_atual": 15045.3,
            "observacoes": "Veículo em boas condições",
        },
        
    ],

    "proprietario": [
        {
            "id_proprietario": 101,
            "nome": "José Almeida",
            "telefone": "63999998888",
            "cpf": "12345678901",
            "email": "jose.almeida@email.com",
            "endereco": "Rua das Flores, 123",
            "criado_em": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
        },
        {
            "id_proprietario": 102,
            "nome": "Ana Claudia",
            "telefone": "63999997777",
            "cpf": "98765432109",
            "email": "ana.claudia@email.com",
            "endereco": "Av. Principal, 456",
            "criado_em": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
        },
        {
            "id_proprietario": 103,
            "nome": "Carlos Eduardo",
            "telefone": "63999996666",
            "cpf": "45678912304",
            "email": "carlos.eduardo@email.com",
            "endereco": "Rua dos Coqueiros, 789",
            "criado_em": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
        },
    ],
    "propriedade": [
        {
            "id_propriedade": 1,
            "id_regiao": 1,
            "id_proprietario": 101,
            "placa": "ABC-1234",
            "aderiu_programa": True,
            "latitude": -10.23456,
            "longitude": -50.78901,
            "nome_propriedade": "Fazenda Estrela",
            "data_criacao": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
            "area_total": 150.5,
            "imagem": "fazenda_estrela.jpg",
            "residentes": "João, Maria",
        },
        {
            "id_propriedade": 2,
            "id_regiao": 1,
            "id_proprietario": 102,
            "placa": "XYZ-5678",
            "aderiu_programa": False,
            "latitude": -10.34567,
            "longitude": -50.89012,
            "nome_propriedade": "Sítio Paraíso",
            "data_criacao": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
            "area_total": 85.0,
            "imagem": "sitio_paraiso.jpg",
            "residentes": "Carlos, Ana",
        },
        {
            "id_propriedade": 3,
            "id_regiao": 1,
            "id_proprietario": 103,
            "placa": "LMN-9012",
            "aderiu_programa": True,
            "latitude": -10.45678,
            "longitude": -50.90123,
            "nome_propriedade": "Chácara Boa Vista",
            "data_criacao": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
            "area_total": 120.3,
            "imagem": "chacara_boa_vista.jpg",
            "residentes": "Pedro, Julia",
        },
        {
            "id_propriedade": 4,
            "id_regiao": 2,
            "id_proprietario": 101,
            "placa": "DEF-3456",
            "aderiu_programa": True,
            "latitude": -15.441214,
            "longitude": -56.034009,
            "nome_propriedade": "Fazenda Nova Esperança",
            "data_criacao": datetime.now().isoformat(),
            "criado_por": "admin",
            "atualizado_em": None,
            "atualizado_por": None,
            "area_total": 200.0,
            "imagem": "fazenda_esperanca.jpg",
            "residentes": "Marcos, Paula",
        },
    ],

    "contato": [
        {
            "id_contato": 1,
            "id_propriedade": 1,
            "nome": "João (caseiro)",
            "telefone": "63988887777",
            "vinculo": "Funcionário",
            "locacao": "-10.23456, -50.78901",
        },
        {
            "id_contato": 2,
            "id_propriedade": 2,
            "nome": "Carlos (filho)",
            "telefone": "63977776666",
            "vinculo": "Familiar",
            "locacao": "-10.34567, -50.89012",
        },
    ],

    "avaliacaoGU": [
        {
            "id_avaliacao_gu": 1,
            "id_propriedade": 1,
            "percepcao_seguranca": "Alta",
            "capacidade_resposta": "Rápida",
            "probabilidade_suspeita": "Baixa",
            "lista_indicios": "Nenhum",
            "comentario": "Propriedade bem protegida",
            "sugestoes_melhorias": "Instalar mais iluminação no acesso",
            "ultima_alteracao": datetime.now().isoformat(),
        },
        {
            "id_avaliacao_gu": 2,
            "id_propriedade": 2,
            "percepcao_seguranca": "Média",
            "capacidade_resposta": "Moderada",
            "probabilidade_suspeita": "Média",
            "lista_indicios": "Pegadas desconhecidas",
            "comentario": "Necessário reforçar vigilância",
            "sugestoes_melhorias": "Instalar câmeras de segurança",
            "ultima_alteracao": (datetime.now() - timedelta(days=15)).isoformat(),
        },
    ],

    
    "benfeitoria_propriedade": [
        {
            "id_benfeitoria": 1,
            "id_propriedade": 1,
            "outra_benfeitoria": None,
            "descricao": None,
        },
        {
            "id_benfeitoria": 2,
            "id_propriedade": 1,
            "outra_benfeitoria": None,
            "descricao": None,
        },
    ],
    "producao_propriedade": [
        {
            "id_producao": 3,
            "id_propriedade": 1,
            "outro_producao": None,
            "descricao": None,
        },
        {
            "id_producao": 4,
            "id_propriedade": 1,
            "outro_producao": None,
            "descricao": None,
        },
    ],
    "atividade_principal_propriedade": [
        {
            "id_atividade": 2,
            "id_propriedade": 1,
            "outra_atividade": None,
        },
        {
            "id_atividade": 1,
            "id_propriedade": 5,
            "outra_atividade": "Horticultura",
        },
    ],
}
class LoginRequest(BaseModel):
    codigo: str


@app.get("/validar-codigo")
def validar_codigo(codigo: str):  # Recebendo o código como parâmetro de consulta
    if codigo == "12345":
        return dados_fake
    else:
        return JSONResponse(status_code=204)

# Rota de teste
@app.get("/testar")
def testar():
    return {"message": "API funcionando!"}

@app.post("/encerrar")
async def receber_json(request: Request):
    corpo_json = await request.json()
    print(" finalizado:", corpo_json)
    return {"mensagem": " recebido com sucesso!"}
