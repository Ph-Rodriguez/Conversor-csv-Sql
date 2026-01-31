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
    parser = argparse.ArgumentParser(description="CSV para SQL - Ferramenta de Automação")
    parser.add_argument("-f", "--file", required=True, help="Caminho do arquivo CSV")
    parser.add_argument("-t", "--table", required=True, help="Nome da tabela destino")
    parser.add_argument("-i", "--insert", action="store_true", help="Inserir direto no banco de dados")
    parser.add_argument("-o", "--output", help="Salvar script em um arquivo .sql")

    args = parser.parse_args()

    dados_para_inserir = []
    cabecalho = []

    try:
        with open(args.file, newline='', encoding='utf-8') as csvfile:
            leitor = csv.reader(csvfile)
            cabecalho = next(leitor)
            for linha in leitor:
                # Mantemos os dados brutos para o banco tratar a tipagem
                dados_para_inserir.append(tuple(linha))
    except FileNotFoundError:
        print(f"❌ Arquivo '{args.file}' não encontrado.")
        return

    # Ação 1: Salvar em arquivo (Mantendo sua lógica de gerar o script texto)
    if args.output:
        with open(args.output, "w", encoding='utf-8') as f:
            for linha in dados_para_inserir:
                valores_str = [f"'{str(v).replace("'", "''")}'" for v in linha]
                sql = f"INSERT INTO {args.table} ({', '.join(cabecalho)}) VALUES ({', '.join(valores_str)});\n"
                f.write(sql)
        print(f"✅ Arquivo SQL gerado: {args.output}")

    # Ação 2: Inserir no Banco (Uso de executemany para performance e segurança)
    if args.insert:
        con = conectar_banco()
        if con:
            try:
                cursor = con.cursor()
                # Placeholder dinâmico: %s, %s, %s...
                placeholders = ", ".join(["%s"] * len(cabecalho))
                colunas = ", ".join(cabecalho)
                query = f"INSERT INTO {args.table} ({colunas}) VALUES ({placeholders})"
                
                print(f"🚀 Inserindo {len(dados_para_inserir)} linhas...")
                cursor.executemany(query, dados_para_inserir)
                con.commit()
                print("✨ Sucesso! Dados inseridos com segurança.")
            except mysql.connector.Error as err:
                print(f"❌ Erro na inserção: {err}")
            finally:
                con.close()

if __name__ == "__main__":
    main()