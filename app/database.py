from typing import Any, List, Optional
import mysql.connector as mc #Biblioteca do conector do MySQL
from mysql.connector import Error, MySQLConnection #Importando a classe Error para tratar as mensagens de erro do código
from dotenv import load_dotenv #Importando a função load_dotenv
from typing import Union
from os import getenv #Importando a função getenv
 
class Database:
    def __init__(self) -> None:
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PSWD')
        self.database = getenv('DB_NAME')
        self.connection = Optional[MySQLConnection] = None #Inicialização da conexão
        self.cursor = Union[List[dict], None] = None #Inicialização do cursor
 
    def conectar(self) -> None:
        """Estabelece uma conexão com o banco de dados."""
        try:
            self.connection = mc.connect(
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Conexão ao banco de dados realizada com sucesso,")
        except Error as e:
            print(f"Erro de conexão: {e}")
            self.connection = None
            self.cursor = None
 
    def desconectar(self) -> None:
        """Encerra a conexão com o banco de dados e o cursor, se eles existirem."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão com o banco de dados encerrada com sucesso;")
   
    def executar(self, sql: str, params: Optional[tuple[Any, ...]] = None) -> Optional[List[dict]]:
        """Executa uma instrução no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida?')
            return None
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f'Erro de execução: {e}')
            return None
    
    def consultar(self, sql: str, params:Optional[tuple[Any, ...]] = None) -> Optional[List[dict]]:
        """Executa uma instrução no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida?')
            return None
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f'Erro de execução: {e}')
            return None
 
 
 
 
 