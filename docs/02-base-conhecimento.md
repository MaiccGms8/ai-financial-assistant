# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Identificar os limites de orçamento do usuário, metas financeiras e tolerância a risco para simulações |
| `produtos_financeiros.json` | JSON | Consultar as taxas de referência e regras de produtos básicos (como CDB e Poupança) para alimentar o motor de simulação |
| `transacoes.csv` | CSV | Analisar o histórico de entradas e saídas para gerar agrupamentos por categoria e calcular médias de consumo |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados originais do arquivo transacoes.csv foram expandidos com colunas temporais explícitas (mês e ano) e categorias padronizadas de despesas. Essa modificação foi necessária para que o back-end em Python consiga realizar agrupamentos estruturados (.groupby()) e identificar anomalias ou picos de gastos por categoria ao comparar o mês atual com períodos anteriores.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados via Pandas logo no início da execução da aplicação e mantidos na memória da sessão (st.session_state do Streamlit). Isso evita operações repetitivas de leitura de disco (I/O) a cada nova mensagem enviada pelo usuário, otimizando a performance do app.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Regras e Comportamento (System Prompt): O prompt de sistema define rigidamente a persona do Finco, suas limitações e diretrizes de UX.

Injeção Dinâmica de Contexto (User Message): O código Python processa os dados brutos, extrai apenas as métricas de BI necessárias (somas, médias, alertas de desvio padrão) e injeta esse resumo tratado como contexto na mensagem enviada à LLM. A IA nunca lê o CSV bruto; ela recebe o dado previamente lapidado pelo motor estatístico do Python.---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Identificação do Cliente:
- Nome: Maicon Gomes
- Perfil Orçamentário: Renda Flutuante (Autônomo)
- Meta de Gastos Mensal: R$ 2.000,00

Métricas Consolidadas (Mês Atual - Processado via Python):
- Saldo em Conta: R$ 1.050,00
- Total de Entradas: R$ 2.500,00
- Total de Saídas: R$ 1.450,00
- Projeção de Gasto para Fim do Mês: R$ 1.950,00 (Dentro do limite estabelecido)

Anomalias e Insights Identificados pelo Código:
- Alerta de Desvio: A categoria "Assinaturas de Serviços" registrou uma alta de 18% em relação à média do último trimestre.

Últimas Transações Registradas:
- 12/05: Entrada (Recebimento de Projeto) | + R$ 800,00
- 15/05: Saída (Supermercado) | - R$ 220,00
- 18/05: Saída (Assinatura de Software) | - R$ 45,00
...
```
