from fastapi import FastAPI, Depends, HTTPException
from app.database import Database
from model.models import Serie, Ator, Motivo, Avaliacao, Categoria

app = FastAPI()
db = Database()

# Rotas para séries
@app.post("/series/")
def cadastrar_serie(serie: Serie):
    db.conectar()
    sql = "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s, %s, %s)"
    db.executar_comando(sql, (serie.titulo, serie.descricao, serie.ano_lancamento, serie.id_categoria))
    db.desconectar()
    return {"message": "Série cadastrada com sucesso"}

@app.post("/atores/")
def cadastrar_ator(ator: Ator):
    db.conectar()
    sql = "INSERT INTO ator (nome) VALUES (%s)"
    db.executar_comando(sql, (ator.nome,))
    db.desconectar()
    return {"message": "Ator cadastrado com sucesso"}

@app.post("/categorias/")
def adicionar_categoria(categoria: Categoria):
    db.conectar()
    sql = "INSERT INTO categoria (nome) VALUES (%s)"
    db.executar_comando(sql, (categoria.nome,))
    db.desconectar()
    return {"message": "Categoria adicionada com sucesso"}

@app.post("/atores/{id_ator}/series/{id_serie}")
def associar_ator_serie(id_ator: int, id_serie: int, personagem: str):
    db.conectar()
    sql = "INSERT INTO ator_serie (id_ator, id_serie, personagem) VALUES (%s, %s, %s)"
    db.executar_comando(sql, (id_ator, id_serie, personagem))
    db.desconectar()
    return {"message": "Ator associado à série com sucesso"}

@app.post("/motivos/")
def incluir_motivo(motivo: Motivo):
    db.conectar()
    sql = "INSERT INTO motivo_assistir (id_serie, motivo) VALUES (%s, %s)"
    db.executar_comando(sql, (motivo.id_serie, motivo.motivo))
    db.desconectar()
    return {"message": "Motivo incluído com sucesso"}

@app.post("/avaliacoes/")
def avaliar_serie(avaliacao: Avaliacao):
    db.conectar()
    sql = "INSERT INTO avaliacao_serie (id_serie, nota, comentario) VALUES (%s, %s, %s)"
    db.executar_comando(sql, (avaliacao.id_serie, avaliacao.nota, avaliacao.comentario))
    db.desconectar()
    return {"message": "Avaliação registrada com sucesso"}

@app.get("/series/")
def listar_series():
    db.conectar()
    sql = "SELECT * FROM serie"
    series = db.executar_comando(sql)
    db.desconectar()
    return series

@app.get("/atores/")
def listar_autores():
    db.conectar()
    sql = "SELECT * FROM ator"
    autores = db.executar_comando(sql)
    db.desconectar()
    return autores

# Rotas para categorias
@app.get("/categorias/")
def listar_categorias():
    db.conectar()
    sql = "SELECT * FROM categoria"
    categorias = db.executar_comando(sql)
    db.desconectar()
    return categorias

@app.get("/avaliacoes/")
def listar_avaliacoes():
    db.conectar()
    sql = "SELECT * FROM avaliacao_serie"
    avaliacoes = db.executar_comando(sql)
    db.desconectar()
    return avaliacoes

@app.put("/series/{id_serie}")
def atualizar_serie(id_serie: int, serie: Serie):
    db.conectar()
    sql = "UPDATE serie SET titulo = %s, descricao = %s, ano_lancamento = %s, id_categoria = %s WHERE id = %s"
    db.executar_comando(sql, (serie.titulo, serie.descricao, serie.ano_lancamento, serie.id_categoria, id_serie))
    db.desconectar()
    return {"message": "Série atualizada com sucesso"}

@app.put("/atores/{id_ator}")
def atualizar_ator(id_ator: int, ator: Ator):
    db.conectar()
    sql = "UPDATE ator SET nome = %s WHERE id = %s"
    db.executar_comando(sql, (ator.nome, id_ator))
    db.desconectar()
    return {"message": "Ator atualizado com sucesso"}

@app.put("/categorias/{id_categoria}")
def atualizar_categoria(id_categoria: int, categoria: Categoria):
    db.conectar()
    sql = "UPDATE categoria SET nome = %s WHERE id = %s"
    db.executar_comando(sql, (categoria.nome, id_categoria))
    db.desconectar()
    return {"message": "Categoria atualizada com sucesso"}

@app.put("/avaliacoes/{id_avaliacao}")
def atualizar_avaliacao(id_avaliacao: int, avaliacao: Avaliacao):
    db.conectar()
    sql = "UPDATE avaliacao_serie SET nota = %s, comentario = %s WHERE id = %s"
    db.executar_comando(sql, (avaliacao.nota, avaliacao.comentario, id_avaliacao))
    db.desconectar()
    return {"message": "Avaliação atualizada com sucesso"}

@app.delete("/series/{id_serie}")
def deletar_serie(id_serie: int):
    db.conectar()
    sql = "DELETE FROM serie WHERE id = %s"
    db.executar_comando(sql, (id_serie,))
    db.desconectar()
    return {"message": "Série deletada com sucesso"}

@app.delete("/atores/{id_ator}")
def deletar_ator(id_ator: int):
    db.conectar()
    sql = "DELETE FROM ator WHERE id = %s"
    db.executar_comando(sql, (id_ator,))
    db.desconectar()
    return {"message": "Ator deletado com sucesso"}

@app.delete("/categorias/{id_categoria}")
def deletar_categoria(id_categoria: int):
    db.conectar()
    sql = "DELETE FROM categoria WHERE id = %s"
    db.executar_comando(sql, (id_categoria,))
    db.desconectar()
    return {"message": "Categoria deletada com sucesso"}

@app.delete("/avaliacoes/{id_avaliacao}")
def deletar_avaliacao(id_avaliacao: int):
    db.conectar()
    sql = "DELETE FROM avaliacao_serie WHERE id = %s"
    db.executar_comando(sql, (id_avaliacao,))
    db.desconectar()
    return {"message": "Avaliação deletada com sucesso"}