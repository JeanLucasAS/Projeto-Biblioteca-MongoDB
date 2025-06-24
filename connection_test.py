from pymongo import MongoClient

uri = "mongodb+srv://jeanlucas:o8AjoadIRyvbxDc3@cluster0.f7tzj2o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri)
    client.admin.command("ping")
    print("✅ Conectado ao MongoDB Atlas!")
except Exception as e:
    print("❌ Erro ao conectar ao MongoDB:", e)
