# Documento Lista de User Stories
Documento construído a partir do Modelo_BSI_-_Doc_001_-_Documento_de_UserStories_SigEvento que pode ser encontrado no
link: <https://docs.google.com/document/d/1EZMq4H7l9eXpIhbgYRLK2Zbm6W0_0091QUN5shtL84U/edit>
## Descrição
Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. O cálculo dos pontos de função podem ser encontrados no link: <https://docs.google.com/document/d/1jk5QUBEMq4GA9Thc2n3ZeyoAplT_dVhXxfaAWZwC7YU/edit?usp=sharing>. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões
| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 13/03/2024 | 0.0.1   | Template e descrição do documento  | Italo e Lucas |
| 13/03/2024 | 0.0.2   | Detalhamento do User Story US01    | Italo e Lucas |
| 31/03/2024 | 0.0.3   | Revisão e correção das numerações  | Italo e Lucas |
| 02/04/2024 | 0.0.4   | Revisão e correção de pontos de função  | Dayanne |
| 10/04/2024 | 0.1.0   | Correção de Users Stories          | Tallys |
| 18/04/2024 | 0.1.1   | Correção de Ortografia             | Tallys |
| 22/04/2024 | 0.1.2   | Aplicando padrão, removendo duplicatas e remodelando user stories | Tallys | 
| 23/04/2024 | 0.1.3   | Correção de Ortografia             | Tallys |
| 20/07/2024 | 0.1.4   | Adição de Testes de aceitação             | Dayanne|



### Tabelas de Users Stories
| Nome | Descrição |
|------|-----------|
| US01 | Manter usuário
| US02 | Formulário de avaliação de evento
| US03 | Manter Evento
| US04 | Manter Sala temática.
| US05 | Manter Presença.
| US06 | Secção do Patrocinador
| US07 | Gerenciar Participantes
| US08 | Calendário de eventos
| US09 | Gerar Relatório de participantes do evento
| US10 | Notificações para Usuários
| US11 | Seção de avaliação
| US12 | Reserva e confirmação
| US13 | Eventos Relacionados
| US14 | Feed de comentários gerais
| US15 | Manter Local de evento
| US16 | Gerar certificado de participação
| US17 | Gerar Crachá

### User Story US01 - Manter Usuário.
| Descrição | O sistema deve ser capaz de cadastrar, listar, excluir, atualizar, vários tipos de usuários com permissões referente ao seu tipo e mantê-los nos sistema. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF001         | Inserir Usuário        |
| RF002         | Buscar Usuário         |
| RF003         | Visualizar Usuário
| RF003.1       | Visualizar Usuário específico
| RF003.2       | Visualizar Usuário(s) específico do evento
| RF004         | Alterar Usuário
| RF004.1       | Alterar qualquer usuário
| RF005         | Excluir conta
| RF005.1       | Excluir conta de usuário

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Essencial                               |
| **Estimativa**              | 8 h                                    |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 7 PF                                   |
| **Analista**                | Ítalo                                  |
| **Desenvolvedor**           | Lucas                                  |
| **Revisor**                 | Dayanne                                |
| **Testador**                | Tallys                                 |

### User Story US02 - Formulário de avaliação de evento.
| Descrição | O sistema deve fornecer para o organizador do evento uma seção de criação de formulário de avaliação do evento, está seção será obrigatória. Consiste em um formulário feito pelo organizador para o participante avaliar e retornar seu feedback sobre o evento. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF006         | Inserir perguntas no formulário
| RF007         | Alterar perguntas no formulário
| RF008         | Excluir perguntas no formulário
| RF009         | Alterar formulário
| RF010         | Visualizar formulários

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Essencial                               |
| **Estimativa**              | 10 h                                    |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 8 PF                                    |
| **Analista**                | Lucas                                  |
| **Desenvolvedor**           | Dayanne                                |
| **Revisor**                 | Tallys                                 |
| **Testador**                | Vinícius                               |                                |

### User Story US03 - Manter Evento.
| Descrição | O sistema deve ser capaz de cadastrar e manter qualquer tipo de evento, podendo também alterar, excluir e visualizar os dados do evento.|
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF011         | Inserir evento
| RF012         | Alterar Evento
| RF013         | Excluir eventos
| RF016         | Visualizar Evento

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Essencial                               |
| **Estimativa**              | 8 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 7 PF                                    |
| **Analista**                | Tallys                                  |
| **Desenvolvedor**           | Vinícius                                |
| **Revisor**                 | Ítalo                                   |
| **Testador**                | Lucas                                   |

### User Story US04 - Manter Sala tematica.
| Descrição | Dentro do evento pode ser criando salas temáticas dentro de um evento. As salas se assemelham a um evento normal só que sem avaliação obrigatória do organizador, o participante pode se inscrever nas salas dos eventos contato que as salas estejam em horários separados.
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF017         | Inserir sala temática no evento
| RF018         | Alterar Sala temática
| RF019         | Excluir sala temática

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Essencial                               |
| **Estimativa**              | 6 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 5 PF                                    |
| **Analista**                | Lucas                                   |
| **Desenvolvedor**           | Dayanne                                 |
| **Revisor**                 | Tallys                                  |
| **Testador**                | Vinícius                                |

| **Testes de Aceitação (TA)** | **Descrição** |
| ----------- | --------- |
| TA04.01 | O sistema deve permitir a criação de uma nova sala temática dentro de um evento existente.            |
| TA04.02 | O sistema deve permitir a alteração dos dados de uma sala temática existente.                         |
| TA04.03 | O sistema deve permitir a exclusão de uma sala temática existente.                                    |
| TA04.04 | O sistema deve garantir que as salas temáticas sejam criadas com horários distintos e não se sobreponham. |
| TA04.05 | O sistema deve listar todas as salas temáticas de um evento de forma clara e organizada.              |

### User Story US05 - Manter Presença.
| Descrição | Dentro do evento e/ou sala temática o criador do evento pode adicionar uma lista de presença que marca a participação do participante no evento e/ou sala. O organizador também pode validar a presença do o usuário no evento principal se ele tiver uma quantidade X de presença em salas temáticas.
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF022         | Marcar presença
| RF023         | Marcar presença automática
| RF024         | Contestar presença

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 7 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 6 PF                                    |
| **Analista**                | Dayanne                                 |
| **Desenvolvedor**           | Tallys                                  |
| **Revisor**                 | Vinícius                                |
| **Testador**                | Ítalo                                   |

| **Testes de Aceitação (TA)** | **Descrição** |
| ----------- | --------- |
| TA05.01 | O sistema deve permitir que o criador do evento adicione uma lista de presença para o evento e/ou sala temática. |
| TA05.02 | O sistema deve permitir que o criador do evento marque a presença de um participante manualmente. |
| TA05.03 | O sistema deve permitir que a presença seja marcada automaticamente para os participantes que se inscreveram nas salas temáticas. |
| TA05.04 | O sistema deve permitir que o participante conteste a presença registrada em um evento ou sala temática. |
| TA05.05 | O sistema deve permitir que o organizador valide a presença de um usuário no evento principal com base na quantidade de presenças em salas temáticas. |
| TA05.06 | O sistema deve gerar relatórios de presença para análise e verificação. |

### User Story US06 - Seção do Patrocinador.
| Descrição | O sistema deve conter uma área na tela para os patrocinadores e apoiadores(órgãos gerais que são cadastrados pelo administrador) do sistema, na seção particular de eventos deve conter uma mesma área para os patrocinadores e organizadores da plataforma. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF025         | Inserir Patrocinador
| RF026         | Alterar Patrocinador
| RF027         | Excluir patrocinador
| RF028         | Listagem de patrocinadores no evento

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 6 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 5 PF                                    |
| **Analista**                | Tallys                                  |
| **Desenvolvedor**           | Vinícius                                |
| **Revisor**                 | Ítalo                                   |
| **Testador**                | Lucas                                   |

### User Story US07 - Gerenciar Participantes.
| Descrição | O sistema deve ser capaz de permitir que os usuários, gerencie a lista de participantes inscritos em um evento específico, possibilitando adicionar, autorizar, remover e visualizar participantes, marcar presença, garantindo uma gestão eficiente das inscrições |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF015         | Convidar participante
| RF016         | Visualizar Evento
| RF020         | Realizar Inscrição
| RF020.1         | Inscrição Adicionada
| RF021         | Cancelar Inscrição
| RF030         | Listagem geral de participantes no evento
| RF031         | Mensagem para participantes

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Essencial                               |
| **Estimativa**              | 8 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 7 PF                                    |
| **Analista**                | Vinícius                                |
| **Desenvolvedor**           | Ítalo                                   |
| **Revisor**                 | Lucas                                   |
| **Testador**                | Dayanne                                 |

| **Testes de Aceitação (TA)** | **Descrição** |
| ----------- | --------- |
| TA07.01 | O sistema deve permitir que um usuário convide participantes para um evento específico.      |
| TA07.02 | O sistema deve permitir visualizar a lista de participantes inscritos em um evento.          |
| TA07.03 | O sistema deve permitir que um usuário realize a inscrição de novos participantes no evento. |
| TA07.04 | O sistema deve permitir que um usuário cancele a inscrição de um participante no evento.     |
| TA07.05 | O sistema deve listar todos os participantes inscritos em um evento de forma clara e organizada. |
| TA07.06 | O sistema deve permitir o envio de mensagens para os participantes do evento.                |

### User Story US08 - Calendário de Eventos.
| Descrição| O sistema deve permitir o gerenciamento de uma agenda, possibilitando visualizar datas disponíveis e realizar agendamentos para eventos, com base em datas e locais. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF029         | Listar eventos por datas e locais

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Média                                   |
| **Estimativa**              | 5 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 4 PF                                    |
| **Analista**                | Lucas                                   |
| **Desenvolvedor**           | Dayanne                                 |
| **Revisor**                 | Tallys                                  |
| **Testador**                | Vinícius                                |

### User Story US09 - Gerar Relatórios de participantes do evento.
| Descrição | O sistema deve ser capaz de gerar relatórios informativos sobre eventos realizados, participantes com filtros sobre: Instituição, região, raça, sexo, idade e gênero. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF009         | Relatórios de participantes
| RF030         | Listagem geral de participantes no evento

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 7 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 6 PF                                    |
| **Analista**                | Dayanne                                 |
| **Desenvolvedor**           | Tallys                                  |
| **Revisor**                 | Vinícius                                |
| **Testador**                | Ítalo                                   |

| **Testes de Aceitação (TA)** | **Descrição** |
| ----------- | --------- |
| TA09.01 | O sistema deve permitir gerar relatórios detalhados sobre os participantes de um evento.     |
| TA09.02 | O sistema deve permitir filtrar os participantes do evento por instituição, região, raça, sexo, idade e gênero. |
| TA09.03 | O sistema deve exibir os relatórios gerados de forma clara e organizada para fácil interpretação. |

### User Story US10 - Notificações para Usuários.
| Descrição | O sistema deve ser capaz de possibilitar o envio de mensagens, notificações aos usuários do sistema sobre novos eventos e/ou eventos marcados como favoritos, atualizações e informações relevantes. Via email e/ou telefone |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF031         | Mensagem para participantes

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 6 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 5 PF                                    |
| **Analista**                | Tallys                                  |
| **Desenvolvedor**           | Vinícius                                |
| **Revisor**                 | Ítalo                                   |
| **Testador**                | Lucas                                   |

### User Story US11 - Seção de avaliação.
| Descrição | O sistema deve possuir uma seção onde o usuário possa ver os eventos que já participou, na seção do evento em si deve ter uma opção para feedback sobre o evento. Em que o usuário possa preencher um formulário de avaliação do evento, desde que ainda esteja dentro do prazo de avaliação. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF006         | Inserir perguntas no formulário
| RF010         | Visualizar formulários

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Média                                   |
| **Estimativa**              | 4 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 3 PF                                    |
| **Analista**                | Vinícius                                |
| **Desenvolvedor**           | Ítalo                                   |
| **Revisor**                 | Lucas                                   |
| **Testador**                | Dayanne                                 |

### User Story US12 - Reserva e confirmação.
| Descrição | O sistema deve possuir uma seção onde o usuário posso fazer uma reserva para algum evento futuro. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF020         | Realizar Inscrição
| RF020.1       | Inscrição Adicionada
| RF012         | Alterar Evento

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 5 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 4 PF                                    |
| **Analista**                | Ítalo                                   |
| **Desenvolvedor**           | Dayanne                                 |
| **Revisor**                 | Tallys                                  |
| **Testador**                | Vinícius                                |

### User Story US13 - Eventos Relacionados.
| Descrição | O sistema deve possuir uma seção que a partir do histórico de eventos do usuário logado, ele possa fornecer indicações outros eventos próximos que estejam nas mesma categorias dos eventos anteriores. |
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF011         | Inserir evento
| RF016         | Visualizar Evento
| RF017         | Inserir sala temática no evento

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Média                                   |
| **Estimativa**              | 6 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 5 PF                                    |
| **Analista**                | Tallys                                  |
| **Desenvolvedor**           | Lucas                                   |
| **Revisor**                 | Vinícius                                |
| **Testador**                | Ítalo                                   |

### User Story US14 - Manter Feed de comentários gerais.
| Descrição | Deve ter uma seção no sistema para interações de conversar de texto de todos os usuários, algo como um fórum. O usuário adiciona seu comentário e aparecerá sua foto do perfil, nome e comentário para todos.
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF032         | Inserir comentário no forum da plataforma
| RF033         | Alterar comentário
| RF034         | Apagar comentário
| RF034.1         | Apagar comentário de usuário
| RF035         | Denunciar comentário
| RF035.1         | Confirmar denuncia

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 7 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 6 PF                                    |
| **Analista**                | Lucas                                   |
| **Desenvolvedor**           | Vinícius                                |
| **Revisor**                 | Dayanne                                 |
| **Testador**                | Tallys                                  |

### User Story US15 - Manter Local de evento.
| Descrição |O sistema deve ser capaz de cadastrar, listar, excluir e atualizar, locais onde acontecerá o evento.
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF036         | Inserir Local
| RF037         | Alterar Local

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Média                                   |
| **Estimativa**              | 4 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 3 PF                                    |
| **Analista**                | Dayanne                                 |
| **Desenvolvedor**           | Tallys                                  |
| **Revisor**                 | Vinícius                                |
| **Testador**                | Lucas                                   |

### User Story US16 - Gerar certificado de participação.
| Descrição | O sistema deve ser capaz de gerar um certificado para o membro que participou do evento como, participante e/ou patrocinador do evento. Contendo nome do usuário, CPF do usuário, horas destinadas ao evento, e suas possíveis menções no evento.
|---|---

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF038         | Gerar certificado

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 5 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 4 PF                                    |
| **Analista**                | Tallys                                  |
| **Desenvolvedor**           | Ítalo                                   |
| **Revisor**                 | Lucas                                   |
| **Testador**                | Vinícius                                |

### User Story US17 - Gerar Crachá
| Descrição | O sistema deve ser capaz de gerar uma figura de crachá para o usuário cadastrado em um evento ativo com suas informações pessoais públicas e sua atuação no evento e qr code para registrar a presença no evento e/ou sala temática.
|---|---


| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF039         | Gerar crachá
| RF039.1       | Alterar crachá

| Informação                   | Detalhes                                |
|------------------------------|----------------------------------------|
| **Prioridade**              | Alta                                    |
| **Estimativa**              | 6 h                                     |
| **Tempo Gasto (real):**     |                                        |
| **Tamanho Funcional**       | 5 PF                                    |
| **Analista**                | Vinícius                                |
| **Desenvolvedor**           | Dayanne                                 |
| **Revisor**                 | Tallys                                  |
| **Testador**                | Lucas                                   |