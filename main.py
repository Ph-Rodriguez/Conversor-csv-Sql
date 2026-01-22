import csv
import mysql.connector
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    except mysql.connector.Error as err:
        print(f"❌ Erro ao conectar: {err}")
        return None

def main():
    # Configuração das Flags
    parser = argparse.ArgumentParser(description="CSV para SQL - Ferramenta de Automação")
    parser.add_argument("-f", "--file", required=True, help="Caminho do arquivo CSV")
    parser.add_argument("-t", "--table", required=True, help="Nome da tabela destino")
    parser.add_argument("-i", "--insert", action="store_true", help="Inserir direto no banco de dados")
    parser.add_argument("-o", "--output", help="Salvar script em um arquivo .sql")

    args = parser.parse_args()

    linhas_sql = []

    # Processamento do CSV
    try:
        with open(args.file, newline='', encoding='utf-8') as csvfile:
            leitor = csv.reader(csvfile)
            cabecalho = next(leitor)
            
            for linha in leitor:
                # Tratamento de dados (Aspas e Números)
                valores = [f"'{v.replace("'", "''")}'" if not v.isdigit() else v for v in linha]
                sql = f"INSERT INTO {args.table} ({', '.join(cabecalho)}) VALUES ({', '.join(valores)});"
                linhas_sql.append(sql)
    except FileNotFoundError:
        print(f"❌ Arquivo '{args.file}' não encontrado.")
        return

    # Ação 1: Salvar em arquivo
    if args.output:
        with open(args.output, "w", encoding='utf-8') as f:
            f.write("\n".join(linhas_sql))
        print(f"✅ Arquivo gerado: {args.output}")

    # Ação 2: Inserir no Banco
    if args.insert:
        con = conectar_banco()
        if con:
            cursor = con.cursor()
            print(f"🚀 Inserindo {len(linhas_sql)} linhas na tabela '{args.table}'...")
            for sql in linhas_sql:
                cursor.execute(sql)
            con.commit()
            print("✨ Sucesso! Dados inseridos.")
            con.close()

if __name__ == "__main__":
    main()