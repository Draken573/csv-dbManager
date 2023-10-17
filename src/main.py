# main.py

import os
from dotenv import load_dotenv
import webbrowser
from colorama import Fore, Style
from tqdm import tqdm
from database_utils import DatabaseUtils
from file_utils import FileUtils
from menu import Menu

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Credentials for database access
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_SERVICE_NAME = os.getenv("DB_SERVICE_NAME")
DB_SCHEMA = os.getenv("DB_SCHEMA")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    menu = Menu()
    db_utils = DatabaseUtils(
        DB_HOST, DB_PORT, DB_SERVICE_NAME, DB_SCHEMA, DB_USERNAME, DB_PASSWORD)
    file_utils = FileUtils()

    while True:
        clear_screen()
        menu.display_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            table_name = input("Digite o nome da tabela: ").upper()
            conn = db_utils.connect()
            if conn:
                if db_utils.check_table_existence(conn, table_name):
                    db_utils.clear_table(conn, table_name)
                conn.close()
        elif choice == "2":
            table_name = input("Digite o nome da tabela: ").upper()
            file_path = input("Digite o caminho do arquivo .csv: ")
            conn = db_utils.connect()
            if conn:
                if db_utils.check_table_existence(conn, table_name):
                    df = file_utils.read_csv(file_path)
                    if df is not None:
                        db_utils.insert_new_data(conn, table_name, df)
                conn.close()
        elif choice == "3":
            table_name = input("Digite o nome da tabela: ").upper()
            file_path = input("Digite o caminho do arquivo .csv: ")
            conn = db_utils.connect()
            if conn:
                if db_utils.check_table_existence(conn, table_name):
                    db_utils.clear_table(conn, table_name)
                    df = file_utils.read_csv(file_path)
                    if df is not None:
                        db_utils.insert_new_data(conn, table_name, df)
                conn.close()
        elif choice == "4":
            break
        else:
            print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")


if __name__ == "__main__":
    # Check if Python is installed
    try:
        os.system("python --version")
    except OSError:
        print(f"{Fore.RED}Python não está instalado. Por favor, instale Python em: https://www.python.org/downloads/")
        webbrowser.open("https://www.python.org/downloads/")
    else:
        # Check and install dependencies
        print("Verificando e instalando dependências...")
        os.system("python -m ensurepip --default-pip")
        os.system("python -m pip install -r requirements.txt")
        main()
