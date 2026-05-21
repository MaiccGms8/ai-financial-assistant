import os, json, requests
import pandas as pd
import streamlit as st

# Configurações Iniciais
st.set_page_config(page_title="Finco", page_icon="📊")
MODELO = "llama3"

# Caminhos e Carga de Dados
base = ".." if os.path.basename(os.getcwd()) == "src" else "."
with open(os.path.join(base, 'data', 'perfil_investidor.json'), 'r', encoding='utf-8') as f1, \
     open(os.path.join(base, 'data', 'produtos_financeiros.json'), 'r', encoding='utf-8') as f2:
    perfil, produtos = json.load(f1), json.load(f2)

transacoes = pd.read_csv(os.path.join(base, 'data', 'transacoes.csv')).tail(5).to_string(index=False)
historico = pd.read_csv(os.path.join(base, 'data', 'historico_atendimento.csv')).tail(3).to_string(index=False)

# 2. Contexto e Prompt da Persona (Finco)
contexto = f"""DADOS: Nome: {perfil.get('nome','')} | Perfil: {perfil.get('perfil_investidor','')} | Patrimônio: R$ {perfil.get('patrimonio_total',0)} | Reserva: R$ {perfil.get('reserva_emergencia_atual',0)}
TRANSAÇÕES RECENTES:\n{transacoes}\nATENDIMENTOS ANTERIORES:\n{historico}\nPRODUTOS:\n{json.dumps(produtos, ensure_ascii=False)}"""

SYSTEM_PROMPT = """Você é o Finco, assistente formal e acessível de inteligência financeira para autônomos. 
REGRAS: 1) Use apenas os dados fornecidos no contexto. Nunca alucine. 2) Se faltar informação, admita e explique o conceito teórico. 3) Não recomende investimentos específicos; explique conceitos (ex: liquidez, CDI). 4) Máximo 3 parágrafos. Termine com uma pergunta consultiva."""

# Integração com Ollama API (/api/chat)
def perguntar_finco(msg):
    payload = {
        "model": MODELO,
        "messages": [
            {"role": "system", "content": f"{SYSTEM_PROMPT}\n\nCONTEXTO:\n{contexto}"},
            {"role": "user", "content": msg}
        ],
        "stream": False
    }
    try:
        r = requests.post("http://localhost:11434/api/chat", json=payload, timeout=45)
        return r.json().get('message', {}).get('content', 'Erro: Resposta vazia.')
    except:
        return "Erro: Certifique-se de que o Ollama está ativo no terminal (ollama run llama3)."

# Interface de Chat 
st.title("Finco — Inteligência Financeira")
st.caption("Análise de fluxo de caixa baseada em dados")

if "chat" not in st.session_state:
    st.session_state.chat = [{"role": "assistant", "content": f"Olá, {perfil.get('nome', 'Cliente')}! Sou o Finco. Como posso ajudar no seu orçamento hoje?"}]

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]): st.write(msg["content"])

if pergunta := st.chat_input("Sua dúvida financeira..."):
    with st.chat_message("user"): st.write(pergunta)
    st.session_state.chat.append({"role": "user", "content": pergunta})
    
    with st.chat_message("assistant"):
        with st.spinner("Analisando..."):
            res = perguntar_finco(pergunta)
            st.write(res)
    st.session_state.chat.append({"role": "assistant", "content": res})