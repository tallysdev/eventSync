# Projeto Arquitetural

## Historico de Revisões
Data | Versão | Descrição | Autores(as) |
-----|--------|-----------|-------------|
29/03/24 | 0.0.1 | Documento Inicial | Tallys |
21/04/24 | 0.0.2 | Atualização do Documento | Italo |
22/04/24 | 0.0.3 | Correção do mecanismo de arquitetura | Italo |

## Descrição
Este documento descreve a arquitetura proposta, descrevendo os padrões arquiteturais usados, decisões arquiteturais e descrição da tecnologias utilizadas.

## Visão Geral
~~~mermaid

graph TD;

style VueJS fill:#81C784,stroke:#33691E,stroke-width:2px;
style Django_REST fill:#64B5F6,stroke:#0D47A1,stroke-width:2px;
style Database fill:#EF5350,stroke:#B71C1C,stroke-width:2px;

subgraph VueJS["Front-End (Vue.js)"]
    style router fill:#C8E6C9
    style components fill:#C8E6C9
    style service fill:#C8E6C9
    style axios fill:#C8E6C9
    router[Vue Router]
    components[Vue Components]
    service[Services]
    axios[Axios]
end

subgraph Django_REST["Back-End (Django REST)"]
    style urlPatterns fill:#BBDEFB
    style views fill:#BBDEFB
    style serializer fill:#BBDEFB
    style models fill:#BBDEFB
    urlPatterns[URL Patterns]
    views[Views]
    serializer[Serializer]
    models[Models]
end

subgraph Database["SGBD"]
    style db fill:#FFCDD2
    db[(PostgreSQL)]
end

router -->|Rotas| components
components --> service
service --> axios
axios -->|Request| urlPatterns
urlPatterns --> views
views -->serializer
views --> models
models --> db
db --> models
urlPatterns -->|Response| axios
axios --> service
components -->|Interface| router
serializer --> models
models --> serializer
serializer --> views    


~~~

## Mecanismo de Arquitetura
### BackEnd 
| Serviço | Descrição |
|---------| --------- |
Postgresql | O PostgreSQL é um poderoso sistema de gerenciamento de banco de dados relacional e não relacional, de código aberto. Reconhecido por sua confiabilidade, escalabilidade e recursos avançados de SQL, oferece suporte a transações ACID, integridade referencial, procedimentos armazenados e gatilhos. Sua arquitetura extensível permite a criação de tipos de dados personalizados, funções e extensões, tornando-o uma escolha popular para aplicativos críticos e complexos. |
Model | A model é a representação dos objetos, permitindo obter informações do banco de dados sem conhecer a complexidade de tal. Essa camada contém tudo sobre os dados: como acessar, validar, comportamentos e relações entre dados  |
View | A view controla o fluxo de informações entre a model e o template. Essa camada utiliza lógica programada para decidir quais informações serão extraídas do banco de dados e quais serão transmitidas para exibição |
Serializer | Os serializers permitem que dados complexos sejam convertidos em tipos de dados nativos do python, que podem ser renderizados facilmente em JSON, XML e outros tipos de conteúdo. No Django Rest, os serializers funcionam de forma semelhante às classes Form e ModelForm do Django. A classe Serializer fornece uma maneira de controlar a saída de suas respostas, bem como uma classe ModelSerializer que fornece um atalho útil para a criação de serializers que lidam com instâncias da model |
URL/Router | O framework REST tem suporte para o roteamento automático de URL para o Django, e fornece uma forma simples, rápida e consistente de conectar sua lógica de visualização a um conjunto de URLs. Tem funcionalidade similar a outras estruturas web como Rails  |

### FrontEnd
| Serviço | Descrição |
|---------| --------- |
Vue Components | Um componente no Vue.js é uma unidade isolada e reutilizável de interface de usuário que encapsula dados, comportamentos e marcação HTML. Ele permite a construção modular de interfaces interativas, simplificando o desenvolvimento e a manutenção de aplicativos Vue.js. |
Services | Os services, ou serviços, são uma maneira de encapsular a lógica de negócios ou a comunicação com o backend em sua aplicação Vue.js. Eles geralmente são usados para fazer solicitações HTTP para o servidor, manipular dados e retornar resultados para os componentes Vue. Isso ajuda a manter seus componentes limpos e focados na interface do usuário, enquanto a lógica de negócios fica isolada em serviços. |
Vue Router | O Vue Router é uma biblioteca oficial de roteamento para Vue.js. Ele permite que você definia rotas em sua aplicação Vue, o que significa que você pode direcionar os usuários para diferentes páginas ou componentes da sua aplicação com base na URL. Isso é fundamental para criar aplicativos de página única (SPA) ou até mesmo para aplicativos multipágina. |
Axios | O Axios é uma biblioteca popular para fazer requisições HTTP no navegador e no Node.js. Ele fornece uma interface simples e poderosa para interagir com APIs, facilitando a comunicação entre o frontend e o backend da aplicação. |

### Referencias
 - https://medium.com/@renatojlelis/entendendo-a-arquitetura-do-django-f4b505773c14
 - https://www.treinaweb.com.br/blog/entendendo-o-mtv-do-django#google_vignette
 - https://fga-eps-mds.github.io/2018.2-Integra-Vendas/docs/doc-arquitetura
 - https://www.django-rest-framework.org/
 - https://docs.google.com/document/d/1i80vPaInPi5lSpI7rk4QExnO86iEmrsHBfmYRy6RDSM/edit
 - https://vuetifyjs.com/en/
 - https://vuejs.org/guide/introduction.html
