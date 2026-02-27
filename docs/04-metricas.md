# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste | Resultado                                                                                              |
|---------|--------------|------------------|--------------------------------------------------------------------------------------------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto | Não consegue verificar, porque foi apresentado valores de transações, não o saldo acumulado            |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe | Quando perguntei da previsão do tempo, não falou disso                                                 |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador | Considerou a natureza dos dados fornecidos e me deu estratégias conservadoras para esse tipo de perfil |


---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** 570,00 (baseado no `transacoes.csv`)
- **Resultado:** [ ] Correto  [X] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [ ] Correto  [X] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto Bradesco Bovespa?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Não falou coisa fora do contexto
- Falou de uma determinada categoria
- Analisou os investimentos 
- Admitiu que não há informações sobre o produto que perguntei

**O que pode melhorar:**
- Adicionar calculos.
- Retirar as chaves da resposta, quando o cliente não irá tratar do contexto. Ex.: <unused3921>
- Precisa de contexto quando o cliente pergunta.

---

