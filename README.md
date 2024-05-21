# data-engineer-test

Teste técnico para vaga de engenharia de dados júnior

## Objetivo

Objetivo do teste é consumir dados da API Fake Store, tratá-los e persisti-los de alguma forma.

Documentação da API: https://fakestoreapi.com/docs

## Requisitos

Gerar um arquivo com um dos seguintes formatos: Parquet, CSV, AVRO ou JSON que deve contar as seguintes informações:  
1. identificador de usuário
2. data mais recente em que o usuário adicionou produtos ao carrinho
3. categoria em que o usuário tem mais produtos adicionados ao carrinho

## Linguagem de programação
Para realizar esse teste usei python e as biblioteca pandas e requests.

## Processo
Ao analisar a documentação da API, decidi usar os endpoints carts e products.  

- Products  
Esse endpoint disponibiliza as informações do produto, como preço, título, categoria, descrição e imagem.
A única transformação realizada foi excluir colunas que não considerei necessárias, mantendo apenas o id do produto, categoria e preço unitário

- Carts  
No endpoint carts temos as informações de id do usuário, data e os produtos e suas quantidades adicionados ao carrinho.  
Como um carrinho pode ter mais de um produto, ele retorna uma lista com dicionários, e para tratar isso usei a função explode para que cada produto ficasse em uma linha e depois criei duas novas colunas para separar produto e quantidade.  

Gerei um dataframe com a junção de carts e products com base no id do produto e adicionei uma nova coluna de valor total do produto multiplicando o valor unitário e a quantidade pois ao meu ver é uma informação importante de se ter.  

No fim, agrupei o dataframe pelo id do carrinho, id do usuário, data e os valores de quantidade de produtos, valor total do carrinho e a categoria com mais produtos adicionados.

## Observações
Fique com dúvida na questão de trazer a data mais recente em que o usuário adicionou produtos ao carrinho pois vi que existe registros de um usuário ter mais de um carrinho, então decidi trazer todos os carrinhos mesmo que repetisse o usuário.
