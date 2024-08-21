# Relatório de testes de aceitação

## Introdução
Os testes de aceitação têm como propósito principal validar que um sistema ou aplicação atende aos requisitos e expectativas dos usuários finais. Eles garantem que as funcionalidades desenvolvidas estão de acordo com as especificações definidas e que o sistema é capaz de operar de maneira eficiente em um ambiente de produção. Esses testes são fundamentais para verificar a conformidade do software com os critérios de aceitação, ajudando a identificar possíveis problemas ou lacunas antes do lançamento, assegurando, assim, a entrega de um produto de alta qualidade.

## Casos de uso testados

### User Story US02 - Formulário de avaliação de evento - 100%
| Descrição | O sistema deve fornecer para o organizador do evento uma seção de criação de formulário de avaliação do evento, está seção será obrigatória. Consiste em um formulário feito pelo organizador para o participante avaliar e retornar seu feedback sobre o evento. |
|---|---

| **Testes de Aceitação (TA)** | **Descrição** | **Passou** |
|------------------------------|---------------|------------|
| TA02.01                       | O sistema deve permitir ao organizador criar um novo formulário de avaliação para um evento. | Sim |
| TA02.02                       | O sistema deve permitir ao organizador adicionar perguntas ao formulário de avaliação. | Sim |
| TA02.03                       | O sistema deve permitir ao organizador alterar as perguntas no formulário de avaliação. | Sim |
| TA02.04                       | O sistema deve permitir ao organizador excluir perguntas do formulário de avaliação. | Sim |
| TA02.05                       | O sistema deve permitir ao organizador visualizar o formulário de avaliação. | Sim |
| TA02.06                       | O sistema deve permitir ao organizador cadastrar perguntas discursivas. | Sim |
| TA02.07                       | O sistema não deve permitir ao organizador cadastrar perguntas discursivas vazias. | Sim |
| TA02.08                       | O sistema deve permitir ao organizador cadastrar perguntas objetivas. | Sim |
| TA02.09                       | O sistema não deve permitir ao organizador cadastrar perguntas objetivas vazias. | Sim |
| TA02.10                       | O sistema não deve permitir ao organizador cadastrar perguntas objetivas sem opções de marcar. | Sim |
| TA02.11                       | O sistema deve permitir ao organizador cadastrar perguntas de múltipla escolha. | Sim |
| TA02.12                       | O sistema não deve permitir ao organizador cadastrar perguntas múltipla escolha vazias. | Sim |
| TA02.13                       | O sistema não deve permitir ao organizador cadastrar perguntas múltipla escolha sem opções de marcar. | Sim |



### User Story US16 - Gerar certificado de participação - 100%
| Descrição | O sistema deve ser capaz de gerar um certificado para o membro que participou do evento como, participante e/ou patrocinador do evento. Contendo nome do usuário, CPF do usuário, horas destinadas ao evento, e suas possíveis menções no evento.
|---|---


| **Testes de Aceitação (TA)** | **Descrição** | **Passou**
| ----------- | --------- |--------- |
| TA16.01 | O sistema deve permitir a geração de um certificado de participação para um usuário específico, contendo nome, CPF, horas e menções. | Sim
| TA16.02 | O sistema deve permitir a visualização e o download do certificado gerado em formato PDF.    | Sim
| TA16.03 | O sistema deve garantir que somente eventos aos quais o usuário participou sejam incluídos no certificado. | Sim
