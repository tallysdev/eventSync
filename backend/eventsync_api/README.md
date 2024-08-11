# eventsync-api

<h2>Instalação</h2>

<p>Para rodar o projeto, siga as etapas abaixo:</p>

<ol>

<li>Crie um ambiente virtual para isolar as dependências do projeto:</li>
    <pre>python -m venv venv</pre>

<li>Ative o ambiente virtual:</li>
<ul>
    <li>No Windows:</li>
    <pre>venv\Scripts\activate</pre>
    <li>No Linux/MacOS:</li>
    <pre>source venv/bin/activate</pre>
</ul>

<li>Instale as dependências do projeto:</li>
<pre>pip install -r requirements.txt</pre>

<li>Gere sua SECRET_KEY a partir do seguinte comando no terminal:</li>
<pre>python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
</pre>

<li>Crie um arquivo .env na raiz do diretório do projeto, copie o conteudo de .env.example e adicione sua SECRET_KEY:</li>
<pre>SECRET_KEY='your-secret-key-here'</pre>

<li>Faça as migrações do banco de dados:</li>
<pre>python manage.py migrate</pre>

<li>OPCIONAL SE FOR USAR A INTERFACE DO DRF: execute o comando de coleta de arquivos estaticos:</li>
<pre>python manage.py collectstatic --no-input</pre>

<li>Inicie o servidor de desenvolvimento:</li>
<pre>python manage.py runserver</pre>

<li>Abra o navegador e acesse o endereço http://localhost:8000 para acessar a aplicação.</li>
</ol>

<h2>TESTES</h2>

<p>Para rodar os testes do projeto use o seguinte comando:</p>
<pre>python manage.py test</pre>

<p>Para rodar os testes verificando a localmente a cobertura use:</p>
<pre>coverage run manage.py test
coverage report</pre>

<h2>Popular Banco</h2>
Para popular o banco de dados com dados iniciais, você pode usar os seguintes comandos de gerenciamento localizados em `core/management/commands`:

<ol>
<li>Para criar um usuário administrador:
    <pre>python manage.py initadmin</pre>
</li>

<li>Para adicionar eventos iniciais:
    <pre>python manage.py initevents</pre>
</li>

<li>Para adicionar patrocínios iniciais:
    <pre>python manage.py initsponsorships</pre>
</li>

<li>Para adicionar patrocinadores iniciais:
    <pre>python manage.py initsponsors</pre>
</li>

<li>Para adicionar usuários iniciais a partir de um arquivo CSV:
    <pre>python manage.py initusers --path=&lt;path/to/your/csvfile&gt;</pre>
</li>
</ol>

Certifique-se de substituir `<path/to/your/csvfile>` pelo caminho real do seu arquivo CSV contendo os dados dos usuários.
