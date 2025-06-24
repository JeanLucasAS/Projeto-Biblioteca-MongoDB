
from pymongo import MongoClient

# Substitua pela sua URI real
uri = "mongodb+srv://jeanlucas:o8AjoadIRyvbxDc3@cluster0.f7tzj2o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Conexão com MongoDB Atlas
client = MongoClient(uri)

# Acessa o banco e a coleção
db = client['biblioteca']
colecao = db['livros']

# Documento de exemplo
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "genero": "Romance",
    "num_paginas": 256,
    "sinopse": "Um romance psicológico que explora a mente de Bentinho e sua visão sobre Capitu.",
    "isbn": "978-85-01-02437-9"
}

# Inserindo o livro
colecao.insert_one(livro)

# Mostrando todos os livros
print("\nLivros na coleção:")
for l in colecao.find():
    print(f"{l['titulo']} ({l['autor']}) - ISBN: {l['isbn']}")
