# database_utils.py

import cx_Oracle


class DatabaseUtils:
    def __init__(self, host, port, service_name, schema, username, password):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.schema = schema
        self.username = username
        self.password = password

    def connect(self):
        try:
            dsn_tns = cx_Oracle.makedsn(
                self.host, self.port, service_name=self.service_name)
            conn = cx_Oracle.connect(
                user=self.username, password=self.password, dsn=dsn_tns)
            return conn
        except cx_Oracle.Error as error:
            print(f"Erro ao conectar ao banco de dados: {error}")
            return None

    def check_table_existence(self, conn, table_name):
        try:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT COUNT(*) FROM all_tables WHERE table_name = '{table_name}' AND owner = '{self.schema}'")
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0 if result else False
        except cx_Oracle.Error as error:
            print(f"Erro ao verificar a existência da tabela: {error}")
            return False

    def get_total_records(self, conn, table_name):
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            total_records = cursor.fetchone()[0]
            cursor.close()
            return total_records
        except cx_Oracle.Error as error:
            print(f"Erro ao obter o total de registros da tabela: {error}")
            return 0

    def clear_table(self, conn, table_name):
        try:
            total_records = self.get_total_records(conn, table_name)

            confirm = input(
                f"Tem certeza que deseja excluir todos os {total_records} registros da tabela? (s/n): ").lower()
            if confirm == "s":
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM {table_name}")
                conn.commit()
                cursor.close()
                print("Tabela limpa com sucesso.")
            else:
                print("Operação cancelada.")

        except cx_Oracle.Error as error:
            print(f"Erro ao limpar a tabela: {error}")
