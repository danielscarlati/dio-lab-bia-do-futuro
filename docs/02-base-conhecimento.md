# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no CIA |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, para conhecer melhor o cliente e dar continuidade ao atendimento |
| `perfil_investidor.json` | JSON | Personalizar explicações sobre as dúvidas e necessidades do cliente |
| `produtos_financeiros.json` | JSON | Servem para dar exemplos nas explicações sobre investimentos com o cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usa-las de forma didatica|
| `personal_finance_customer_data.csv` | CSV | Analisar o arqueótipo do cliente em relação à vida financeira |
| `credit_risk.csv` | CSV | Analisar as dívidas e inadimplencias do cliente | 

Obs: As três últimas tabelas vão servir também de inspiração para procurar ideias e soluções para resolver os problemas do cliente sem falar aonde investir.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.<br>
O produto Fundo Imobiliario (FII) substituiu o Fundo Multimercado, pois preciso validar as respostas do CIA de forma consultiva.
---

## Estratégia de Integração

### Como os dados são carregados?
Programação em Python com a biblioteca Pandas ou injetar os dados no prompt.


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
Injetamos os dados no prompt para que o agente tenha o melhor contexto para ajudar o cliente. Essas informações devem ser carregadas dinamicamente para ganhar flexibilidade.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Resumo de Gastos:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55

Dívidas:
- Cartão de credito: R$ 556
- Conta de luz: R$ 4096
- Eletricidade: R$ 2514
- Impostos: R$ 5781

Explicações sobre:
- Tesouro Relic
- CDB Liquidez diaria
- LCI/LCA
- Fundo Imobiliario
- Fundo de ações

Soluções:
- Mapear dívidas e organizar bem o seu dinheiro
- Negociação de dívidas
- Fazer rendas extras


```
