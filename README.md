# CSV to SQL Automator 🚀

Ferramenta de automação desenvolvida em **Python** para facilitar a migração de dados de arquivos **CSV** para bancos de dados **MySQL / MariaDB**.

O projeto permite tanto a **geração de scripts `.sql`** quanto a **inserção direta e automatizada no banco**, eliminando trabalho manual e reduzindo erros comuns de sintaxe.

---

## 💡 Ideia do Projeto

O **CSV to SQL Automator** foi criado para resolver um problema recorrente: popular bancos de dados a partir de arquivos CSV de forma rápida, segura e automatizada.

O script:
- Lê arquivos CSV estruturados
- Utiliza a **primeira linha como mapeamento automático de colunas**
- Trata **aspas simples** para evitar erros de SQL
- Usa **argumentos de linha de comando (CLI)** para definir o modo de execução
- Protege credenciais sensíveis usando **variáveis de ambiente**

---

## ⚙️ Principais Funcionalidades

- 📌 **Mapeamento Automático**  
  A primeira linha do CSV é utilizada como nome das colunas na query SQL.

- 🔁 **Modo Flexível de Execução**  
  - Gerar apenas o arquivo `.sql`
  - Inserir diretamente no banco
  - Ou fazer ambos simultaneamente

- 🔐 **Segurança**  
  Credenciais de acesso protegidas via arquivo `.env`.

- 💻 **Interface CLI**  
  Totalmente controlado via terminal usando `argparse`.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x 
- **Banco de Dados:** MySQL / MariaDB 
- **Bibliotecas:**
  - `mysql-connector-python`
  - `python-dotenv`
  - `argparse` (nativo)

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python **3.x**
- MySQL ou MariaDB
- Ambiente virtual Python (recomendado)

---

## 📦 Instalação

### 1️⃣ Preparar o Ambiente

Navegue até a pasta do projeto e ative o ambiente virtual:

bash
cd ~/Projetos/Python/Conversor-csv-Sql
source venv/bin/activate

As dependências já estão listadas no arquivo requirements.txt:

pip install -r requirements.txt

Crie um arquivo .env na raiz do projeto (use o .env.example como referência):

DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME= Sua_database

O script principal é executado via terminal utilizando flags para definir o comportamento.

📌 Flags Disponíveis
Flag	Descrição	Exemplo
-f	Caminho do arquivo CSV	-f dados.csv
-t	Nome da tabela no banco	-t minha_tabela
-o	Gera arquivo SQL de saída	-o insert.sql
-i	Insere diretamente no banco	-i

🧪 Exemplos de Uso

🔹 Gerar apenas o script SQL
python3 main.py -f dados.csv -t minha_tabela -o script.sql

🔹 Inserir diretamente no banco
python3 main.py -f dados.csv -t minha_tabela -i

🔹 Execução completa (gera script + insere no banco)
python3 main.py -f dados.csv -t minha_tabela -i -o script.sql


📊 Estrutura do CSV

O arquivo CSV deve possuir cabeçalhos que correspondam exatamente aos campos da tabela no banco de dados:

id,nome,idade,email
1,Pedro,28,pedro@email.com

📁 Estrutura do Projeto (exemplo)
Conversor-csv-Sql/
├── main.py
├── requirements.txt
├── .env.example
├── README.md
└── venv/

✅ Status do Projeto

✔️ Projeto finalizado e funcional
📌 Pronto para uso, estudo ou expansão futura.

👨‍💻 Autor

Desenvolvido por Ph_Rodriguez
Projeto focado em automação de processos e manipulação de dados em banco de dados.


