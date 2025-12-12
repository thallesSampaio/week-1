Descrição

Este é um programa simples em Python que realiza uma requisição HTTP para a API RestCountries. Ele obtém um JSON contendo o nome e a população de todos os países, ordena os resultados pelas maiores populações e exibe na tela a quantidade desejada de países, por exemplo, um Top 5.

O usuário também pode escolher o formato do nome exibido: common (nome comum) ou official (nome oficial).


Como usar

Execute o programa passando dois argumentos:

Quantidade de países que deseja exibir

Tipo de nome: common ou official

python nome_do_arquivo.py <quantidade> <common|official>

python exercicio1.py 5 common
Isso exibirá os 5 países mais populosos, usando o nome comum de cada um.