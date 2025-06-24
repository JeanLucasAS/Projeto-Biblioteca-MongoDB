from pymongo import MongoClient

# Conexão com o MongoDB
uri = "mongodb+srv://jeanlucas:o8AjoadIRyvbxDc3@cluster0.f7tzj2o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['biblioteca']
colecao = db['livros']

# Agrupa todos os livros por ISBN e filtra os que têm mais de uma ocorrência
duplicados = colecao.aggregate([
    {"$group": {
        "_id": "$isbn",
        "ids": {"$addToSet": "$_id"},
        "count": {"$sum": 1}
    }},
    {"$match": {
        "count": {"$gt": 1}
    }}
])

# Para cada grupo duplicado, mantém um e remove os demais
total_removidos = 0
for doc in duplicados:
    ids = doc['ids']
    # Mantém o primeiro e remove o resto
    ids_para_remover = ids[1:]
    result = colecao.delete_many({"_id": {"$in": ids_para_remover}})
    total_removidos += result.deleted_count

print(f"✅ Limpeza concluída. {total_removidos} duplicatas removidas.")
