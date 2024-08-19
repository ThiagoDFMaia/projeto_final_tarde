# Projeto de Análise de Dados e Desenvolvimento Web

Bem-vindo ao repositório! Este projeto é dividido em três partes principais, cada uma contendo diferentes abordagens e técnicas de análise de dados, desenvolvimento web e manipulação de dados. Abaixo, você encontrará uma descrição detalhada de cada pasta e seus respectivos conteúdos.

## Estrutura do Repositório

O repositório está organizado nas seguintes pastas:

### 1. `analise`

Nesta pasta, você encontrará o projeto relacionado ao MySQL Workbench:

- **Projetos Conceitual e Lógico**: Arquivos e documentos relacionados ao desenvolvimento de modelos conceituais e lógicos usando o MySQL Workbench.
- **`analise.ipynb`**: Notebook Jupyter com comandos do Pandas para manipulação de dados. Este arquivo inclui:
  - Geração de arquivos XLS e CSV da tabela `avaliação` criada no MySQL.
  - Comandos para calcular médias, medianas e quartis.

### 2. `projeto`

Esta pasta contém o projeto desenvolvido utilizando Flask e Pandas:

- **Diário de Bordo**: Implementação de um diário de bordo em Flask para gerenciar e registrar informações.
- **Páginas HTML e CSS**: Arquivos HTML estilizados com CSS para a interface do usuário.
- **Conexão com MySQL**: Implementação de uma classe de conexão com o banco de dados MySQL utilizando a biblioteca ABC.

### 3. `semana_EDA`

Aqui você encontrará o início da análise exploratória de dados:

- **DataSet de Movies**: Dataset baixado do site MovieLens.
- **Análise Exploratória**: Códigos e explicações sobre características do Python, orientação a objetos e uso de funções lambda.

## Como Usar

### Requisitos

Antes de começar, certifique-se de ter os seguintes pacotes instalados:

- Python (preferencialmente Python 3.x)
- Flask
- Pandas
- MySQL Connector
- Jupyter Notebook

Você pode instalar as dependências necessárias usando `pip`:

```bash
pip install flask pandas mysql-connector-python jupyter
