# beanalytics-desafio
## [Link Planilha Google Sheets](https://docs.google.com/spreadsheets/d/1BiI9OwoOecftso-GiGM-x4e7xjfyTsfBzSxHRDleUyA/edit?pli=1#gid=1697636033)
## [Link do Notebook de Extração](https://colab.research.google.com/drive/1OLBQ9S9_lg4W3_hMEjtXtb_4Bm3dI9W5)

## Descrição
Este projeto tem como objetivo realizar a extração, processamento e carregamento de dados do SteamDB para o Google BigQuery. Os dados extraídos incluem informações de classificações de jogos, top sellers, picos históricos de jogadores e histórico de preços. 

Além disso, os dados estão conectados ao Google Sheets por meio de uma extensão chamada OWOX BI BigQuery Reports, que permite extrair os dados do BigQuery utilizando SQL. Isso facilita a visualização e análise dos dados diretamente em planilhas do Google Sheets.

# Imagem tabelas do Google Big Query
## ![Tabelas Google Big Query](https://github.com/HenriqueHideaki/beanalytics-desafio/blob/main/img/big_query.png)

# Extra - Dashboard feito com Streamlit
## ![img dash](https://github.com/HenriqueHideaki/beanalytics-desafio/blob/main/img/dash_steamdb.png)

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal para automação de tarefas de extração, limpeza e processamento de dados.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **BeautifulSoup**: Biblioteca para analisar e extrair dados de HTML.
- **Google Cloud BigQuery**: Plataforma de armazenamento e análise de grandes volumes de dados.
- **Google Cloud Credentials**: Biblioteca para autenticação e autorização de acesso ao Google BigQuery.
- **OWOX BI BigQuery Reports**: Extensão para conectar BigQuery ao Google Sheets e executar consultas SQL.

## Como Utilizar
1. **Configurar Credenciais**:
    - Coloque o arquivo de credenciais JSON do Google Cloud no diretório `big_query/credentials.json`.

2. **Executar o Notebook**:
    - Siga as células do notebook para executar cada etapa do processo de extração, processamento e carregamento de dados.

3. **Verificar os Dados no BigQuery**:
    - Após o carregamento, os dados estarão disponíveis nas tabelas do BigQuery para análise.

4. **Conectar ao Google Sheets**:
    - Utilize a extensão OWOX BI BigQuery Reports para conectar o BigQuery ao Google Sheets.
    - Configure consultas SQL para extrair os dados necessários para visualização nas planilhas.
