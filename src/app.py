import json
import pandas as pd
import requests
from streamlit import chat_input, title, chat_message, spinner

# CONFIGURAÇÃO
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma3"


# FUNÇÃO SEGURA PARA CARREGAR ARQUIVOS
def carregar_json(caminho):
    try:
        return json.load(open(caminho, encoding="utf-8"))
    except Exception:
        return {}


def carregar_csv(caminho):
    try:
        return pd.read_csv(caminho)
    except Exception:
        return pd.DataFrame()


# BASE DE CONHECIMENTO
perfil = carregar_json('./data/perfil_investidor.json')
transacoes = carregar_csv('./data/transacoes.csv')
atendimento = carregar_csv('./data/historico_atendimento.csv')
produtos = carregar_json('./data/produtos_financeiros.json')
pesFinancas = carregar_csv('./data/personal_finance_customer_data.csv')  # pode estar vazio
dividas = carregar_csv('./data/credit_risk.csv')

# MONTAR CONTEXTO
contexto = f"""
CLIENTE: {perfil.get('nome', 'N/A')}, {perfil.get('idade', 'N/A')} anos, perfil {perfil.get('perfil_investidor', 'N/A')}
OBJETIVO: {perfil.get('objetivo_principal', 'N/A')}
PATRIMONIO: R${perfil.get('patrimonio_total', 'N/A')}  
RESERVA: R${perfil.get('reserva_emergencia_atual', 'N/A')}

TRANSAÇÕES:
{transacoes.to_string(index=False) if not transacoes.empty else "Sem dados disponíveis"}

ATENDIMENTOS:
{atendimento.to_string(index=False) if not atendimento.empty else "Sem dados disponíveis"}

PRODUTOS:
{json.dumps(produtos, indent=2, ensure_ascii=False) if produtos else "Sem dados disponíveis"}

FINANÇAS PESSOAIS:
{pesFinancas.to_string(index=False) if not pesFinancas.empty else "Arquivo muito grande, não carregado"}

DIVIDAS:
{dividas.to_string(index=False) if not dividas.empty else "Sem dados disponíveis"}
"""

# SYSTEM PROMPT
SYSTEM_PROMPT = """
Você é CIA, uma inteligência artificial financeira que é educativa e consultiva. 
Seu tom de comunicação deve ser formal, técnico, acessível e empreendedor.

OBJETIVOS:
- Ensinar clientes sobre juros, impostos e investimentos com exemplos práticos usando os dados fornecidos.
- Analisar o status do cliente, mapeando entradas e saídas, mostrando seus últimos gastos e quanto de dinheiro ele possui.
- Providenciar soluções para resolver os problemas do cliente.

REGRAS:
- Sempre responde com os dados fornecidos.
- Responde com simplicidade, como se explicasse para um amigo.
- Sempre responde em Português.
- JAMAIS responda perguntas fora do contexto de finanças.
- Procura e idealiza soluções sem recomendar onde investir.
- Não faz recomendações de investimento sem o perfil do cliente.
- Não acessa dados sensíveis (senhas, CPFs, etc.).
- Deve falar com o cliente dessa maneira:
  - Saudação: "Olá, meu nome é CIA, seu assistente virtual. Como posso te ajudar?"
  - Confirmação: "Deixa eu encontrar uma solução ou explicação para o problema. Por favor, aguarde."
  - Erro/Limitação: "Infelizmente, não posso recomendar onde investir, mas posso ajudar com várias soluções para investimentos."
- Sempre pergunte se o cliente entendeu.
"""


# FUNÇÃO DE PERGUNTA
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}        
"""
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    resposta = r.json().get('response', '')
    return resposta


# INTERFACE
title("CIA, SEU AGENTE DE FINANÇAS")

if pergunta := chat_input("Seu problema sobre finanças..."):
    chat_message("user").write(pergunta)
    with spinner("..."):
        chat_message("assistant").write(perguntar(pergunta))
