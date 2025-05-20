from fastapi import FastAPI, HTTPException
from app.database import Database
from model.models import Serie, Ator, Motivo, Avaliacao, Categoria

app = FastAPI()
db = Database()

def executar_comando(sql: str, params: tuple = ()):
    db.conectar()
    result = db.executar_comando(sql, params)
    db.desconectar()
    return result

@app.post("/{table}/")
def criar_item(table: str, item: dict):
    keys = ", ".join(item.keys())
    values = ", ".join(["%s"] * len(item))
    sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
    executar_comando(sql, tuple(item.values()))
    return {"message": f"{table.capitalize()} criado com sucesso"}

@app.get("/{table}/")
def listar_itens(table: str):
    sql = f"SELECT * FROM {table}"
    return executar_comando(sql)

@app.put("/{table}/{id}")
def atualizar_item(table: str, id: int, item: dict):
    updates = ", ".join([f"{key} = %s" for key in item.keys()])
    sql = f"UPDATE {table} SET {updates} WHERE id = %s"
    executar_comando(sql, tuple(item.values()) + (id,))
    return {"message": f"{table.capitalize()} atualizado com sucesso"}

@app.delete("/{table}/{id}")
def deletar_item(table: str, id: int):
    sql = f"DELETE FROM {table} WHERE id = %s"
    executar_comando(sql, (id,))
    return {"message": f"{table.capitalize()} deletado com sucesso"}

#Field: Titulo, descrição na categoria..