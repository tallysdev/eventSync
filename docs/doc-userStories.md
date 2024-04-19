# Documento Lista de User Stories
Documento construído a partir do **Modelo_BSI_-_Doc_001_-_Documento_de_UserStories_SigEvento** que pode ser encontrado no
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
| 18/04/2024 | 0.1.1   | Correção de Ortografia | Tallys |


### Tabelas de Users Stories
| Nome | Descrição |
|------|-----------|
| US01 | Manter usuário
| US02 | Formulário de avaliação de evento
| US03 | Manter Evento 
| US04 | Secção do Patrocinador
| US05 | Gerenciar Participantes
| US06 | Calendário de eventos
| US07 | Gerar Relatório de participantes do evento
| US08 | Notificações para Usuários
| US09 | Seção de avaliação
| US10 | Reserva e confirmação
| US11 | Calendários De eventos
| US12 | Eventos Relacionados
| US13 | Feed de comentários gerais
| US14 | Manter Local de evento
| US15 | Gerar certificado de participação
| US16 | Gerar Crachá

### User Story US01 - Manter Usuário
| **Descrição** | O sistema deve ser capaz de cadastrar, listar, excluir, atualizar, vários tipos de usuários com permissões referente ao seu tipo e mantê-los nos sistema. |
| ------------- | :----------------------------------------------------------------------------- |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Manter Usuário                                                  |
| RF01.1        | Inserir Usuário                                                 |
| RF01.2        | Alterar Usuário                                                 |
| RF01.3        | Consultar Usuários                                              |
| RF01.4        | Excluir Usuário                                                 |
| RF01.5        | visualizar detalhes do Usuário                                  |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 55 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Lucas Mateus                        |
| **Revisor**               | Vinicius Maia                       |
| **Testador**              | Dayanne Xavier                      |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 55 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Lucas Mateus                        |
| **Revisor**               | Vinicius Maia                       |
| **Testador**              | Dayanne Xavier                      |

### User Story US02 - Formulário de avaliação de evento
**Descrição** | O sistema deve fornecer para o organizador do evento uma seção de criação de formulário de avaliação do evento, está seção será obrigatória. Consiste em um formulario feito pelo organizador para o participante avaliar e retornar seu feedback sobre o evento. |
|---|---

### User Story US03 - Manter Evento
| **Descrição** | O sistema deve ser capaz de cadastrar e manter qualquer tipo de evento, podendo também alterar, excluir e visualizar os dados do evento.   |
| ------------- | :------------------------------------------------------------- |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF02          | Manter Eventos |
| RF02.1        | Inserir Evento                                                  |
| RF02.2        | Alterar Evento                                                  |
| RF02.3        | Consultar Evento                                                |
| RF02.4        | Excluir Evento                                                  |
| RF02.5        | visualizar detalhes do Evento                                   |
| RF09          | Sistema de Reservas                                             |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 67 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Mauricio                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 67 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Mauricio                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |

### User Story US04 Seção do Patrocinador
| **Descrição** | O sistema deve conter uma área na tela para os patrocinadores e apoiadores(órgãos gerais que são cadastrados pelo administrador) do sistema, na seção particular de eventos deve conter uma mesma área para os patrocinadores e organizadores da plataforma. |
|-----|----|
### User Story US05 - Gerenciar Participantes
|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve ser capaz de permitir que os usuários, gerencie a lista de participantes inscritos em um evento específico, possibilitando adicionar, autorizar, remover e visualizar participantes, garantindo uma gestão eficiente das inscrições |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF03          | Gerenciar Participantes |
| RF03.1        | Inserir participante   |
| RF03.2 &&       | Excluir participante   |
| RF03.2 &&       | Excluir participante   |
| RF03.3        | Visualizar participante   |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 33 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Dayanne Xavier                      |
| **Revisor**               | Italo Maurício                      |
| **Testador**              | Lucas Mateus                        |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 33 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Dayanne Xavier                      |
| **Revisor**               | Italo Maurício                      |
| **Testador**              | Lucas Mateus                        |

### User Story US06 - Calendário de Eventos
| **Descrição**| O sistema deve permitir o gerenciamento de uma agenda, possibilitando visualizar datas disponíveis e realizar agendamentos para eventos, com base em datas e locais. |
|--------------|------------------------------------------------------------------|

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF04          | Controlar Agenda             |
| RF04          | Visualizar datas disponíveis |
| RF04          | Agendar evento               |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 22 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Maurício                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 22 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Maurício                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |

### User Story US07 - Gerar Relatórios de participantes do evento
| **Descrição** | O sistema deve ser capaz de gerar relatórios informativos sobre eventos realizados, participantes com filtros sobre: Instituição, região, raça, sexo, idade e genero. |
| ------------- | :------------------------------------------------------------- |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF05          | Geração de Relatórios       |
| RF05.1        | Relatório de eventos feitos |
| RF05.2        | Relatório de participantes  |
| RF05.3        | Relatório de despesas |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 34 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Vinicius Maia                       |
| **Revisor**               | Dayanne Xavier                      |
| **Testador**              | Tallys Aureliano                    |

### User Story US08 - Notificações para Usuários
| **Descrição** | O sistema deve ser capaz de possibilitar o envio de mensagens, notificações aos usuários do sistema sobre novos eventos e/ou eventos marcados como favoritos, atualizações e informações relevantes. Via email e/ou telefone |

| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 34 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Vinicius Maia                       |
| **Revisor**               | Dayanne Xavier                      |
| **Testador**              | Tallys Aureliano                    |

### User Story US08 - Notificações para Usuários
| **Descrição** | O sistema deve ser capaz de possibilitar o envio de mensagens, notificações aos usuários do sistema sobre novos eventos e/ou eventos marcados como favoritos, atualizações e informações relevantes. Via email e/ou telefone |
| ------------- | :------------------------------------------------------------- |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF06          | Comunicação com Participantes |
| RF06.1        | Cadastrar mensagens           |
| RF06.2        | Notificar participantes       |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 22 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Maurício                      |
| **Revisor**               | Vinicius Maia                       |
| **Testador**              | Lucas Mateus                        |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 22 PF                               |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Maurício                      |
| **Revisor**               | Vinicius Maia                       |
| **Testador**              | Lucas Mateus                        |

### User Story US09 - Seção de avaliação
| **Descrição** | O sistema deve possuir uma seção onde o usuário possa ver os eventos que já participou, na sessão do evento em si deve ter uma opção para feedbacks sobre o evento. Em que o usuário possa comentar ou preencher um formulário de avaliação do evento, desde que ainda esteja dentro do prazo de avaliação. |
| ------------- | :------------------------------------------------------------- |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF011         | Calendário de Eventos |
| RF08          | Avaliação dos Eventos  |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 11 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Vinicius Maia                       |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Dayanne Xavier                      |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 11 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Vinicius Maia                       |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Dayanne Xavier                      |

### User Story US10 - Reserva e confirmação
|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve possuir uma seção onde o usuário posso fazer uma reserva para algum evento futuro, ou confirmar presença em algum evento privado no qual tenha sido convidado |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF09          | Sistema de reservas    |
| RF09.1        | Sistema de confirmação |
| RF011         | Calendário de Eventos  |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 22 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Mauricio                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 22 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Mauricio                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |

### User Story US11 - Calendários De eventos
|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve ser capaz de verificar os eventos cadastrados e exibi-los para o usuário em forma de agenda, sendo eles públicos e privados caso o usuário esteja convidado para aquele evento |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF011          | Calendário de Eventos |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 11 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Maurício                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |  
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 11 PF                                |
| **Analista**              | Taciano                             |
| **Desenvolvedor**         | Italo Maurício                      |
| **Revisor**               | Tallys Aureliano                    |
| **Testador**              | Lucas Mateus                        |  

### User Story US012 - Eventos Relacionados
|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve possuir uma seção que a partir do histórico de eventos do usuário logado, ele possa fornecer indicações outros eventos próximos que estejam nas mesma categorias dos eventos anteriores |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF012          | Recomendações personalizadas |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 15 h                                |
| **Tempo Gasto (real):**   |                                     |
| **Tamanho Funcional**     | 12 PF                                |
| **Analista**              | Taciano                             |
| **Testador**              | Dayanne Xavier                      |
| **Desenvolvedor**         | Italo Maurício                      |
| **Revisor**               | Vinicius Maia                       |

### User Story US13 Manter Feed de comentários gerais
| **Descrição** | **Deve ter uma seção no sistema para interações de conversar de texto de todos os usuários, algo como um fórum. O usuário adiciona seu comentário e aparecerá sua foto do perfil, nome e comentário para todos.**
|---|---

### User Story US14 Manter Local de evento
|**Descrição**|O sistema deve ser capaz de cadastrar, listar, excluir e atualizar, locais onde acontecerá o evento.
|---|---

### User Story US15 Gerar certificado de participação
|Descrição| O sistema deve ser capaz de gerar um certificado para o membro que participou do evento como, participante e/ou patrocinador do evento. Contendo nome do usuário, CPF do usuário, horas destinadas ao evento, e suas possíveis menções no evento.
|---|---

### User Story US16 Gerar Crachá
| Descrição | O sistema deve ser capaz de gerar uma figura de crachá para o usuário cadastrado em um evento ativo com suas informações pessoais públicas e sua atuação no evento.
|---|---


