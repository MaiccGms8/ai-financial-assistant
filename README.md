# 📊 Finco — Agente Financeiro Inteligente com IA Generativa

## 📝 Contexto do Desafio
Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para agentes inteligentes e proativos. Neste projeto, desenvolvido a partir do desafio da DIO, foi prototipado o **Finco**: um agente financeiro focado em orientação orçamentária para profissionais autônomos e microempreendedores que utiliza IA Generativa local para:
* **Antecipar necessidades:** Traduzir dados brutos de fluxo de caixa em insights práticos.
* **Personalizar sugestões:** Adaptar respostas com base no perfil estratégico do cliente de forma consultiva.
* **Garantir segurança (Anti-Alucinação):** Blindagem do prompt para evitar invenções de dados ou recomendações de ativos diretas.

---

## 🎯 Entregas do Projeto (Passo a Passo Concluído)

### 1. Documentação do Agente
Definição detalhada do caso de uso, persona, tom de voz e o pipeline de dados seguro.
* 📄 **Documento:** [docs/01-documentacao-agente.md](docs/01-documentacao-agente.md)

### 2. Base de Conhecimento
Utilização estratégica dos dados mockados locais. Em vez de enviar arquivos massivos, o ecossistema usa **Pandas** para fatiar dinamicamente os registros (`.tail()`), otimizando o envio do contexto à LLM.
* 📁 **Pasta de Dados:** `data/` (`transacoes.csv`, `historico_atendimento.csv`, `perfil_investidor.json`, `produtos_financeiros.json`)
* 📄 **Documento:** [docs/02-base-conhecimento.md](docs/02-base-conhecimento.md)

### 3. Prompts do Agente
Engenharia de prompts contendo as travas rígidas do *System Prompt* do Finco: atuação pedagógica (explicar conceitos teóricos como liquidez e CDI) e **proibição estrita de recomendar ativos diretamente**.
* 📄 **Documento:** [docs/03-prompts.md](docs/03-prompts.md)

### 4. Aplicação Funcional
Desenvolvimento de um protótipo com interface interativa de chat alimentada por um modelo de linguagem rodando **100% local e privado** (sem custos com chaves de API externas).
* 📁 **Código Fonte:** [src/app.py](src/app.py)

### 5. Avaliação e Métricas
Validação da aplicação com base em 4 cenários críticos de testes estruturados: Assertividade de gastos, Recomendação restrita/ética, Filtro de escopo e Tratamento de informações ausentes.
* 📄 **Documento:** [docs/04-metricas.md](docs/04-metricas.md)

---

## 🛠️ Stack Tecnológica Utilizada

* **LLM Local:** [Ollama](https://ollama.com/) com o modelo open-source **Llama 3 (8B)**.
* **Interface do Usuário (UI):** [Streamlit](https://streamlit.io/) para criação do chat e gerenciamento de estado (`st.session_state`).
* **Engenharia de Dados:** [Pandas](https://pandas.pydata.org/) para manipulação rápida dos arquivos CSV.
* **Comunicação de API:** Biblioteca `requests` do Python integrada ao endpoint oficial do Ollama (`/api/chat`).

---

## 📁 Estrutura Atual do Repositório

```text
ai-financial-assistant/
│
├── 📄 README.md                      # Instruções e visão geral do projeto
│
├── 📁 data/                          # Base de conhecimento e dados mockados
│   ├── historico_atendimento.csv     # Histórico de atendimentos anteriores
│   ├── perfil_investidor.json        # Informações e perfil do cliente
│   ├── produtos_financeiros.json     # Catálogo de produtos disponíveis
│   └── transacoes.csv                # Histórico do fluxo de caixa
│
├── 📁 docs/                          # Documentação das etapas do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados e engenharia
│   ├── 03-prompts.md                 # Engenharia de prompts do Finco
│   └── 04-metricas.md                # Relatório de avaliação e testes
│
├── 📁 src/                           # Código-fonte da aplicação
│   └── app.py                        # Script principal do app Streamlit

