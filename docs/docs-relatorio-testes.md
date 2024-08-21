# Relatório de testes de aceitação

## Introdução
Os testes de aceitação têm como propósito principal validar que um sistema ou aplicação atende aos requisitos e expectativas dos usuários finais. Eles garantem que as funcionalidades desenvolvidas estão de acordo com as especificações definidas e que o sistema é capaz de operar de maneira eficiente em um ambiente de produção. Esses testes são fundamentais para verificar a conformidade do software com os critérios de aceitação, ajudando a identificar possíveis problemas ou lacunas antes do lançamento, assegurando, assim, a entrega de um produto de alta qualidade.

## Casos de uso testados

### User Story US16 - Gerar certificado de participação - 100%
| Descrição | O sistema deve ser capaz de gerar um certificado para o membro que participou do evento como, participante e/ou patrocinador do evento. Contendo nome do usuário, CPF do usuário, horas destinadas ao evento, e suas possíveis menções no evento.
|---|---


| **Testes de Aceitação (TA)** | **Descrição** | **Passou**
| ----------- | --------- |--------- |
| TA16.01 | O sistema deve permitir a geração de um certificado de participação para um usuário específico, contendo nome, CPF, horas e menções. | Sim
| TA16.02 | O sistema deve permitir a visualização e o download do certificado gerado em formato PDF.    | Sim
| TA16.03 | O sistema deve garantir que somente eventos aos quais o usuário participou sejam incluídos no certificado. | Sim
