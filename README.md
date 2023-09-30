# Validador e Gerenciador de Modelos de Excel

Já teve que lidar com a importação e análise de modelos de Excel? E ainda por cima, verificar se tudo está correto linha por linha? Eu já enfrentei esse 'perrengue' e percebi que era uma tarefa exaustiva. Por isso, desenvolvi o Validador e Gerenciador de Modelos de Excel com a ajuda do nosso querido Python. 😊

## Tecnologias Utilizadas

- PySide2
- xlsx2csv
- xlrd
- pandas
- openpyxl
- pywin32

## Funcionalidades Principais

Então, o que exatamente essa ferramenta faz?

- Definir a quantidade de colunas.
- Nomear os templates.
- Especificar os tipos de dados para cada coluna, incluindo os mais utilizados universalmente, como String, Integer, Date, DateTime, Boolean e Number.
- Configurar a obrigatoriedade de campos.
- Definir o tamanho máximo de campo para evitar estouros.
- Especificar os valores aceitáveis para cada coluna. Por exemplo, você pode definir uma coluna com UF onde os valores aceitos são: 'SP, MG, RJ', etc.
- Gerenciar campos sequenciais. Você pode definir que em uma determinada coluna, os valores devem ser únicos e não podem se repetir.
- Gerar templates com legendas e dicionário de dados para garantir que o preenchimento seja correto.
- Usar Multithreading com a utilização do Pandas para dividir os dados do seu modelo em Dataframes, o que acelera a análise, mesmo em planilhas com 300 ou 400 mil linhas.
- Exportar apenas as linhas que estão corretas.
- Exportar um log de erros detalhado, explicando por que uma célula foi considerada incorreta.

## Deploy

Para fazer o deploy deste projeto e instalar as dependências, siga os passos abaixo:

1. Certifique-se de que você está no ambiente virtual desejado.

2. No terminal, navegue até o diretório raiz do projeto.

3. Execute o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```


executar main
``` Python
python main.py
```

## Contribuindo

Contribuições são sempre bem-vindas!

Caso queria ajudar a adicionar mais funcionalidades será muito bom :)



## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de jhonatan.deni@outlook.com


## Autores

- [@Jhonatan Deni](https://github.com/xjhowxjhow)


## Stack utilizada

**Front-end:** QT Designer

**Back-end:** Python 




## Licença

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

