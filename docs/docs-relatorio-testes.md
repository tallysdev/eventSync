# Relatório de testes de aceitação

## Introdução
Os testes de aceitação têm como propósito principal validar que um sistema ou aplicação atende aos requisitos e expectativas dos usuários finais. Eles garantem que as funcionalidades desenvolvidas estão de acordo com as especificações definidas e que o sistema é capaz de operar de maneira eficiente em um ambiente de produção. Esses testes são fundamentais para verificar a conformidade do software com os critérios de aceitação, ajudando a identificar possíveis problemas ou lacunas antes do lançamento, assegurando, assim, a entrega de um produto de alta qualidade.

## Casos de uso testados

### User Story US01 - Manter Usuário - 40%
| Descrição | O sistema deve ser capaz de cadastrar, listar, excluir, atualizar, vários tipos de usuários com permissões referente ao seu tipo e mantê-los nos sistema. |
|---|---

| **Testes de Aceitação (TA)** | **Descrição** | **Passou** |
| ---------------------------- | ------------- | ---------- |
| TA01.01                       | O sistema deve permitir o cadastro de um novo usuário com todos os campos obrigatórios preenchidos. | Sim |
| TA01.02                       | O sistema deve permitir a busca de um usuário pelo seu ID. | Não |
| TA01.03                       | O sistema deve permitir a atualização dos dados de um usuário existente. | Não |
| TA01.04                       | O sistema deve permitir a exclusão de um usuário específico. | Não |
| TA01.05                       | O sistema não deve permitir o cadastro de um novo usuário sem todos os campos obrigatórios preenchidos. | Sim |

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

### User Story US03 - Manter Evento - 67%
| Descrição | O sistema deve ser capaz de cadastrar e manter qualquer tipo de evento, podendo também alterar, excluir e visualizar os dados do evento.|
|---|---

| **Testes de Aceitação (TA)** | **Descrição** | **Passou** |
| ---------------------------- | ------------- | ---------- |
| TA03.01                       | O sistema deve permitir o cadastro de um novo evento com todos os campos obrigatórios preenchidos. | Sim |
| TA03.02                       | O sistema não deve permitir o cadastro de um novo evento sem todos os campos obrigatórios preenchidos. | Sim |
| TA03.03                       | O sistema deve permitir a visualização dos detalhes de um evento específico cadastrado. | Sim |
| TA03.04                       | O sistema deve permitir a alteração dos dados de um evento existente. | Não |
| TA03.05                       | O sistema deve permitir a exclusão de um evento específico. | Não |
| TA03.06                       | O sistema deve listar todos os eventos cadastrados de forma organizada. | Sim |

### User Story US06 - Seção do Patrocinador - 50%
| Descrição | O sistema deve conter uma área na tela para os patrocinadores e apoiadores(órgãos gerais que são cadastrados pelo administrador) do sistema, na seção particular de eventos deve conter uma mesma área para os patrocinadores e organizadores da plataforma. |
|---|---

| **Testes de Aceitação (TA)** | **Descrição** | **Passou** |
| ---------------------------- | ------------- | ---------- |
| TA06.01                       | O sistema deve permitir ao administrador inserir um novo patrocinador na plataforma. | Sim |
| TA06.02                       | O sistema deve permitir ao administrador alterar os dados de um patrocinador existente. | Não |
| TA06.03                       | O sistema deve permitir ao administrador excluir um patrocinador existente. | Não |
| TA06.04                       | O sistema deve listar todos os patrocinadores cadastrados de forma organizada. |Sim |
| TA06.05                       | O sistema não deve permitir a inserção de um patrocinador sem todas as informações obrigatórias preenchidas. | Sim |
| TA06.08                       | O sistema deve permitir ao administrador filtrar patrocinadores por eventos associados. | Não |

### User Story US12 - Reserva e confirmação - 100%
| Descrição | O sistema deve possuir uma seção onde o usuário posso fazer uma reserva para algum evento futuro. |
|---|---

| **Testes de Aceitação (TA)** | **Descrição** | **Passou** |
| ---------------------------- | ------------- | ---------- |
| TA12.01                       | O sistema deve permitir ao usuário fazer uma reserva para um evento futuro. | Sim |
| TA12.03                       | O sistema deve enviar uma confirmação de reserva ou presença para o usuário. | Sim |
| TA12.04                       | O sistema deve permitir que o usuário visualize suas reservas e confirmações de eventos. | Sim |
| TA12.05                       | O sistema deve permitir ao usuário cancelar uma reserva ou confirmação de presença. | Sim |


### User Story US15 - Manter Local de evento 83%
| Descrição |O sistema deve ser capaz de cadastrar, listar, excluir e atualizar, locais onde acontecerá o evento.
|---|---

| **Testes de Aceitação (TA)** | **Descrição** | **Passou** |
| ---------------------------- | ------------- | ---------- |
| TA15.01                       | O sistema deve permitir o cadastro de um novo local para eventos com todas as informações obrigatórias. | Sim |
| TA15.02                       | O sistema não deve permitir o cadastro de um novo local para eventos com alguma informação obrigatória faltando. | Sim |
| TA15.03                       | O sistema deve permitir a atualização das informações de um local já cadastrado. | Sim |
| TA15.04                       | O sistema não deve permitir a atualização das informações de um local já cadastrado faltando campos obrigatórios. | Sim |
| TA15.05                       | O sistema deve permitir a exclusão de um local cadastrado, caso não esteja associado a eventos futuros. | Não |
| TA15.06                       | O sistema deve listar todos os locais cadastrados com suas informações detalhadas. | Sim |

### User Story US16 - Gerar certificado de participação - 100%
| Descrição | O sistema deve ser capaz de gerar um certificado para o membro que participou do evento como, participante e/ou patrocinador do evento. Contendo nome do usuário, CPF do usuário, horas destinadas ao evento, e suas possíveis menções no evento.
|---|---

| **Testes de Aceitação (TA)** | **Descrição** | **Passou**
| ----------- | --------- |--------- |
| TA16.01 | O sistema deve permitir a geração de um certificado de participação para um usuário específico, contendo nome, CPF, horas e menções. | Sim
| TA16.02 | O sistema deve permitir a visualização e o download do certificado gerado em formato PDF.    | Sim
| TA16.03 | O sistema deve garantir que somente eventos aos quais o usuário participou sejam incluídos no certificado. | Sim

## Casos de uso não testados

### User Story US08 - Calendário de Eventos.
| Descrição| O sistema deve permitir o gerenciamento de uma agenda, possibilitando visualizar datas disponíveis e realizar agendamentos para eventos, com base em datas e locais. |
|---|---

- O US08 não foi implementado pois o tempo estava bem corrido, foi focado nos principais USs do sistema, mas com alguns USs existentes no sistema (US03 e US15) já se torna possível a sua implementação no futuro. O que falta para esse US ser concluído seria criar a parte da agenda, por exemplo para facilitar a visualização das datas disponíveis no sistema de forma que não bata com outros eventos no mesmo local, no momento o sistema não trata sobre eventos no mesmo dia e local.

### User Story US10 - Notificações para Usuários.
| Descrição | O sistema deve ser capaz de possibilitar o envio de mensagens, notificações aos usuários do sistema sobre novos eventos e/ou eventos marcados como favoritos, atualizações e informações relevantes. Via email e/ou telefone |
|---|---

- O US10 não foi implementado, mas a existência de alguns USs (US01, US03 e US12 por exemplo) já torna possível a possibilidade da sua existência futuramente, já que temos a existência de usuários com diferentes tipos de permissão (participante e organizador por exemplo), o que falta para ele ser concluído seria de fato cadastrar as mensagens para que o organizador com apenas um clique possa notificar os participantes do evento em que ele criou.

### User Story US11 - Seção de avaliação.
| Descrição | O sistema deve possuir uma seção onde o usuário possa ver os eventos que já participou, na seção do evento em si deve ter uma opção para feedback sobre o evento. Em que o usuário possa preencher um formulário de avaliação do evento, desde que ainda esteja dentro do prazo de avaliação. |
|---|---

- O US11 não foi implementado, mas a existência de alguns USs (US01, US02, US03 e US12 por exemplo) já torna possível a possibilidade da sua existência futuramente, já que temos a existência de usuários, eventos e o organizador de evento pode criar um formulário, o que falta a ser feito é colocar um botão que possibilite ao participante ter acesso ao formulário, assim como armazenar as suas respostas.

### User Story US13 - Eventos Relacionados.
| Descrição | O sistema deve possuir uma seção que a partir do histórico de eventos do usuário logado, ele possa fornecer indicações outros eventos próximos que estejam nas mesma categorias dos eventos anteriores. |
|---|---

- O US13 não foi implementado, mas a existência de alguns USs (US01, US03 e US12 por exemplo) já torna possível a possibilidade da sua existência futuramente, já que podemos fazer cruzamento de informações fornecidas desses usuários com base em eventos que participou, e assim o sistema poder recomendar eventos, isso ainda não foi implementado.

### User Story US14 - Manter Feed de comentários gerais.
| Descrição | Deve ter uma seção no sistema para interações de conversar de texto de todos os usuários, algo como um fórum. O usuário adiciona seu comentário e aparecerá sua foto do perfil, nome e comentário para todos.
|---|---

- O US14 não foi implementado, mas a existência de alguns USs (US01 por exemplo) já torna possível a possibilidade da sua existência futuramente, pois usuários já podem se cadastrar no nosso sistema, o que falta é existir um local apropiado para se colocar esses comentários, assim como falta implementar o seu armazenamento no banco de dados.

### User Story US17 - Gerar Crachá
| Descrição | O sistema deve ser capaz de gerar uma figura de crachá para o usuário cadastrado em um evento ativo com suas informações pessoais públicas e sua atuação no evento e qr code para registrar a presença no evento e/ou sala temática.
|---|---

- O US17 não foi implementado, mas a existência de alguns USs (US01, US02 por exemplo) já torna possível a possibilidade da sua existência futuramente, o que falta é o sistema ser capaz de pegar essas informações e gerar de fato o crachá.