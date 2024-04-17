# Projeto Arquitetural

## Historico de Revisões
Data | Versão | Descrição | Autores(as) |
-----|--------|-----------|-------------|
29/03/24 | 0.0.1 | Documento Inicial | Tallys |

## Descrição
Este documento descreve a arquitetura proposta, descrevendo os padrões arquiteturais usados, decisões arquiteturais e descrição da tecnologias utilizadas.

## Visão Geral
~~~mermaid

graph TD;

subgraph VueJS["Front-End (Vue.js)"]
    http[Vue Js]
    vueComponent[Vue Component]
    vuex[Vuex Store]
    axios[Axios HTTP client]
    style http fill:darkGreen
    style vueComponent fill:darkGreen
    style vuex fill:darkGreen
    style axios fill:darkGreen
end

subgraph Django_REST["Back-End (Django REST)"]
    urls[URLs/Router]
    views[Views]
    serializer[Serializer]
    models[Models]
    style urls fill:Blue
    style views fill:Blue
    style serializer fill:Blue
    style models fill:Blue
end

subgraph Database["SGBD"]
    db[(PostgreSQL)]
    style db fill:darkRed
end

http -->|Requisições HTTP| urls
urls -->|Define rotas e mapeia para views| views
views -->|Manipula dados utilizando serializers| serializer
serializer -->|Serializa/deserializa dados| models
models -->|Interage com o banco de dados| db
views -->|Se conecta com o Serializer| serializer
serializer -->|Se conecta com a View| views

vueComponent -->|Renderiza a interface| vuex
vuex -->|Acessa e gerencia o estado global| axios
axios -->|Envia requisições para o back-end| http
http -->|Retorna dados| axios
axios -->|Manipula dados| vuex
vuex -->|Atualiza estado| vueComponent
vueComponent -->|Envia dados para o model| models
models -->|Se conecta com a Vue component| vueComponent



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
Componentes | Um componente no Vue.js é uma unidade isolada e reutilizável de interface de usuário que encapsula dados, comportamentos e marcação HTML. Ele permite a construção modular de interfaces interativas, simplificando o desenvolvimento e a manutenção de aplicativos Vue.js. |
Pages | As "pages" no Vue.js referem-se a componentes que representam páginas específicas em um aplicativo de página única. Cada página geralmente contém uma combinação de componentes menores e é roteada usando um roteador Vue, mas agora também de forma dinamica. Isso facilita a organização e a navegação em aplicativos Vue.js, permitindo a separação clara de funcionalidades e a criação de uma experiência de usuário consistente. |
Layout | "layout" é um componente que define a estrutura visual básica de uma página ou de um conjunto de páginas em um aplicativo. Ele geralmente inclui elementos comuns, como cabeçalho, navegação, rodapé e áreas de conteúdo variável. Os layouts ajudam na manutenção do design consistente em todo o aplicativo, simplificando a implementação de alterações de estilo ou de layout. Além disso, permitem uma melhor organização do código, separando preocupações de layout de lógica de negócios. |
Telas | A "tela" em si é usada no desenho apenas para direcionar o usuário sobre o que ele esta vendo na tela, podendo ser diferentes telas em N momentos, mas sempre seguindo essa mesma arquitetura de componentes gráficos. |
Store | No Vue.js, o "store" refere-se ao Vuex, que é uma biblioteca de gerenciamento de estado. O Vuex permite compartilhar dados entre componentes de forma centralizada, facilitando a comunicação e o gerenciamento do estado de um aplicativo Vue.js. O store contém o estado global da aplicação, bem como métodos para atualizá-lo de forma previsível e reativa. Isso ajuda a manter a consistência dos dados em toda a aplicação e simplifica a depuração e o desenvolvimento de funcionalidades complexas. |

### Referencias
 - https://medium.com/@renatojlelis/entendendo-a-arquitetura-do-django-f4b505773c14
 - https://www.treinaweb.com.br/blog/entendendo-o-mtv-do-django#google_vignette
 - https://fga-eps-mds.github.io/2018.2-Integra-Vendas/docs/doc-arquitetura
 - https://www.django-rest-framework.org/
 - https://docs.google.com/document/d/1i80vPaInPi5lSpI7rk4QExnO86iEmrsHBfmYRy6RDSM/edit
 - https://vuetifyjs.com/en/
 - https://vuejs.org/guide/introduction.html
