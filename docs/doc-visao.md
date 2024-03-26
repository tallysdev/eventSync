# Documento de Visão

Documento construído a partido do **Modelo_BSI_-_Doc_001_-_Documento_de_Visao_SigEvento** que pode ser encontrado no
link: <https://docs.google.com/document/d/1EZMq4H7l9eXpIhbgYRLK2Zbm6W0_0091QUN5shtL84U/edit>

## Equipe e Definição de Papéis

Membro              |     Papel     |   E-mail                         |
------------------  | ------------- | ----------                       |
Tallys Aureliano    | Analista, Gerente | <tallys.santos.017@ufrn.edu.br>
Italo Maurício      | Analista      | <italo.santos.059@ufrn.edu.br>
Lucas Mateus        | Analista      | <lucas.mateus.130@ufrn.edu.br>
Vinicius Maia       | Analista      | <vinicius.maia.706@ufrn.edu.br>
Dayanne Xavier      | Analista      | <dayanne.xavier.119@ufrn.edu.br>
Taciano Silva       | Cliente       | <taciano@bsi.ufrn.br>

### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
Italo Maurício      | Desenvolvedor Java
Lucas Mateus        | Desenvolvedor Python
Vinicius Maia       | Desenvolvedor TypeScript
Tallys Aureliano    | Desenvolvedor Dart
Dayanne Xavier      | Desenvolvedor C

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador                          | Responsável pelo gerenciamento geral da plataforma. Possui acesso completo a todas as funcionalidades, incluindo cadastro de eventos, gestão de equipes, geração de relatórios e controle financeiro.
Organizador de Eventos | Usuário responsável pela criação e organização de eventos na plataforma. Pode cadastrar novos eventos, gerenciar participantes, definir agendas e enviar comunicações aos clientes.
Perfil Cliente | Usuário que contrata os serviços de organização de eventos através da plataforma. Pode visualizar eventos disponíveis, realizar inscrições, efetuar pagamentos e interagir com os organizadores.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Manter Eventos | Permitir o cadastro e manutenção de eventos na plataforma, incluindo informações como nome, data, local, descrição e tipo de evento | Organizador de Eventos
RF002 - Gerenciar Participantes | Possibilitar o controle de participantes inscritos em cada evento, incluindo informações como nome, contato e status de pagamento | Organizador de Eventos
RF003 - Controlar Agenda | Permitir o gerenciamento de agenda, com visualização de datas disponíveis e agendadas para eventos | Organizador de Eventos
RF004 - Geração de Relatórios | Gerar relatórios informativos sobre eventos realizados, participantes, receitas e despesas | Administrador
RF005 - Comunicação com Clientes | Possibilitar o envio de mensagens e notificações aos clientes sobre novos eventos, atualizações e informações relevantes | Organizador de Eventos
RF006 - Controle Financeiro | Permitir o registro e controle de pagamentos, incluindo faturamento, recibos, e status de pagamento dos participantes |Administrador
RF007 - Avaliação dos eventos | Permitir que os participantes avaliem e forneçam feedbacks sobre os eventos após a conclusão do mesmo | Cliente
RF008 - Sistema de reservas | Permitir que o cliente reserve e confirme sua participação no evento | Cliente  
RF009 - Gerenciamento de patrocinadores | Possibilitar o cadastro e gerenciamento de patrocinadores para eventos, incluindo informações sobre eles | Organizador de eventos  
RF010 - Calendário de eventos | Disponibilizar um calendário público de eventos, permitindo que os participantes visualizem e acompanhem os eventos futuros, e os participantes convidados podem visualizar no calendário os eventos privados | Cliente
RF011 - Recomendações personalizadas | Uma vez cadastrado na plataforma, os usuários podem marcar quais tipos de eventos eles tem interesse, com base nisso e no histórico de eventos já participados, o sistema pode sugerir eventos para ele participar | Cliente

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF01 - Segurança e Autenticação | Implementar mecanismos robustos de segurança e autenticação para proteger os dados dos usuários e informações sensíveis dos eventos.
RNF02 - Escalabilidade | Garantir que a plataforma seja escalável, capaz de lidar com um grande número de eventos e usuários simultaneamente.
RNF03 - Usabilidade | Desenvolver uma interface intuitiva e de fácil uso, proporcionando uma experiência agradável aos usuários.
RNF04 - Conformidade Legal | Assegurar que a plataforma esteja em conformidade com todas as leis e regulamentos aplicáveis, especialmente no que diz respeito à proteção de dados e direitos do consumidor.

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
07/03/2024 | Possibilidade de não compreensão total das funcionalidades da plataforma | Alta | Gerente | Vigente | Realizar treinamentos e oferecer suporte contínuo aos usuários
07/03/2024 | Risco de Falha no Sistema de Pagamentos | Média | Gerente | Vigente | Realizar testes extensivos do sistema de pagamentos, implementar soluções de backup e suporte técnico adequado
07/03/2024 | Risco de Sobrecarga do Servidor |Alta | Gerente | Vigente | Monitoramento constante da carga do servidor, implementação de escalabilidade e redundância


## Modelos

### Modelo de entidade relacionamento

Para criar modelos ER é possível usar o BrModelo e gerar uma imagem. Contudo, atualmente é possível criar modelos ER usando a ferramenta **Mermaid**, escrevendo o modelo diretamente em markdown. Acesse a documentação para escrever modelos [ER Diagram Mermaid](https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram).

```mermaid
erDiagram
    USUARIO {
        string id pk
        string cpf
        string rg
        string permissoes
        date data_nascimento
    }
    
    ADM

    ORGANIZADOR 
    
    PARTICIPANTE {
        string[] interesse
    }
    
    TIPO {
        string id pk
        string descricao
    }

    EVENTO {
        string id pk
        date data
        string titulo
        string local
        string descricao
        boolean ativo
        boolean autorizado
    }

    PATROCINADOR{
        string cnpj
    }
    
    CRIACAO {
        string evento_id pk
        string organizador_id pk
    }
    
    %% PARTICIPA {
    %%     string evento_id pk
    %%     string participante_id pk
    %% }

    USUARIO ||--|| ORGANIZADOR : "é um"
    USUARIO ||--|| PARTICIPANTE : "é um"
    USUARIO ||--|| ADM : "é um"
    %% Na duvida se isso se mantém PARTICIPANTE ||--|{ PARTICIPA : participa
    PARTICIPANTE }|--o{ EVENTO : "participa"
    ORGANIZADOR ||--|{ CRIACAO : cria
    EVENTO ||--|| CRIACAO : "é criado por"
    EVENTO }|--||TIPO : "é de tipo"
    EVENTO }|--|{ PATROCINADOR : "patrocina"
```

