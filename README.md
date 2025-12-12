<h1>Descrição</h1>

Este é um programa simples em Python que realiza uma requisição HTTP para a API RestCountries. Ele obtém um JSON contendo o nome e a população de todos os países, ordena os resultados pelas maiores populações e exibe na tela a quantidade desejada de países, por exemplo, um Top 5.

O usuário também pode escolher o formato do nome exibido: common (nome comum) ou official (nome oficial).

<h1>Como usar</h1>
Execute o programa passando <strong>dois argumentos</strong>:
 <ol>
  <li><strong>Quantidade de países que deseja exibir</strong></li>
  <li><strong>Tipo de nome: common ou official</strong></li>
</ol> 

<h1>Exemplo</h1>
<p><code>python nome_do_arquivo.py <quantidade> <common|official></code></p>
<p><code>python exercicio1.py 5 common</code></p>
<p>Isso exibirá os 5 países mais populosos, usando o nome comum de cada um.</p>

<h1>Bônus</h1>
<p>Funciona basicamente da mesma maneira, porém ao invés de exibir os dados no terminal, vai criar um arquivo CSV e exportar os dados para esse arquivo CSV.</p>
<p><code>python exercicio_bonus.py 5 common</code></p>

<h1>Aprendizado</h1>
<p>No meu caso, como já programva antes, ja tenho experiencia formal de trabalho, foi mais relembrar alguns conceitos e aprender a consumir APIS com python, como manipular e printar os dados.</p>
<p>Já no segundo exercício, o aprendizado foi mais voltado para compreender como funciona a API da 42. Também revisei o processo de autenticação e como implementá-lo utilizando OAuth2. O principal desafio foi entender os endpoints disponíveis, interpretar os JSONs retornados e identificar o propósito de cada campo.</p>
