from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError
from typing import List, Dict, Optional
import re
from datetime import datetime

class BookManager:
    def __init__(self, connection_string: str = "mongodb://localhost:27017/", database_name: str = "biblioteca"):
        """
        Inicializa o gerenciador de livros com conexão ao MongoDB
        """
        try:
            self.client = MongoClient(connection_string)
            self.db = self.client[database_name]
            self.collection = self.db.livros
            
            # Criar índice único para ISBN
            self.collection.create_index("isbn", unique=True)
            
            print(f"✅ Conectado ao MongoDB - Database: {database_name}")
        except Exception as e:
            print(f"❌ Erro ao conectar ao MongoDB: {e}")
            raise

    def inserir_livro(self, livro_data: Dict) -> bool:
        """
        Insere um novo livro no banco de dados
        """
        try:
            # Validar campos obrigatórios
            campos_obrigatorios = ['titulo', 'autor', 'ano_publicacao', 'genero', 'num_paginas', 'sinopse', 'isbn']
            for campo in campos_obrigatorios:
                if campo not in livro_data or not livro_data[campo]:
                    raise ValueError(f"Campo obrigatório '{campo}' não fornecido")
            
            # Adicionar timestamp de criação
            livro_data['data_criacao'] = datetime.now()
            
            result = self.collection.insert_one(livro_data)
            print(f"✅ Livro inserido com sucesso! ID: {result.inserted_id}")
            return True
            
        except DuplicateKeyError:
            print(f"❌ Erro: Já existe um livro com o ISBN {livro_data.get('isbn')}")
            return False
        except ValueError as e:
            print(f"❌ Erro de validação: {e}")
            return False
        except Exception as e:
            print(f"❌ Erro ao inserir livro: {e}")
            return False

    def listar_livros_por_autor(self, autor: str) -> List[Dict]:
        """
        Lista todos os livros de um determinado autor
        """
        try:
            # Busca case-insensitive usando regex
            regex_autor = re.compile(autor, re.IGNORECASE)
            livros = list(self.collection.find({"autor": regex_autor}))
            
            print(f"📚 Encontrados {len(livros)} livro(s) do autor '{autor}':")
            for livro in livros:
                print(f"  - {livro['titulo']} ({livro['ano_publicacao']})")
            
            return livros
        except Exception as e:
            print(f"❌ Erro ao buscar livros por autor: {e}")
            return []

    def listar_livros_por_genero(self, genero: str) -> List[Dict]:
        """
        Lista todos os livros de um determinado gênero
        """
        try:
            regex_genero = re.compile(genero, re.IGNORECASE)
            livros = list(self.collection.find({"genero": regex_genero}))
            
            print(f"📖 Encontrados {len(livros)} livro(s) do gênero '{genero}':")
            for livro in livros:
                print(f"  - {livro['titulo']} - {livro['autor']}")
            
            return livros
        except Exception as e:
            print(f"❌ Erro ao buscar livros por gênero: {e}")
            return []

    def listar_livros_por_ano(self, ano: int) -> List[Dict]:
        """
        Lista todos os livros publicados em um determinado ano
        """
        try:
            livros = list(self.collection.find({"ano_publicacao": ano}))
            
            print(f"📅 Encontrados {len(livros)} livro(s) publicado(s) em {ano}:")
            for livro in livros:
                print(f"  - {livro['titulo']} - {livro['autor']}")
            
            return livros
        except Exception as e:
            print(f"❌ Erro ao buscar livros por ano: {e}")
            return []

    def listar_livros_mais_paginas(self, limite: int = 10) -> List[Dict]:
        """
        Lista os livros com mais páginas (ordenados decrescente)
        """
        try:
            livros = list(self.collection.find().sort("num_paginas", -1).limit(limite))
            
            print(f"📏 Top {limite} livros com mais páginas:")
            for i, livro in enumerate(livros, 1):
                print(f"  {i}. {livro['titulo']} - {livro['num_paginas']} páginas")
            
            return livros
        except Exception as e:
            print(f"❌ Erro ao buscar livros com mais páginas: {e}")
            return []

    def listar_livros_menos_paginas(self, limite: int = 10) -> List[Dict]:
        """
        Lista os livros com menos páginas (ordenados crescente)
        """
        try:
            livros = list(self.collection.find().sort("num_paginas", 1).limit(limite))
            
            print(f"📖 Top {limite} livros com menos páginas:")
            for i, livro in enumerate(livros, 1):
                print(f"  {i}. {livro['titulo']} - {livro['num_paginas']} páginas")
            
            return livros
        except Exception as e:
            print(f"❌ Erro ao buscar livros com menos páginas: {e}")
            return []

    def buscar_livro_por_isbn(self, isbn: str) -> Optional[Dict]:
        """
        Busca um livro específico pelo ISBN
        """
        try:
            livro = self.collection.find_one({"isbn": isbn})
            
            if livro:
                print(f"📚 Livro encontrado:")
                print(f"  Título: {livro['titulo']}")
                print(f"  Autor: {livro['autor']}")
                print(f"  Ano: {livro['ano_publicacao']}")
                print(f"  Gênero: {livro['genero']}")
                print(f"  Páginas: {livro['num_paginas']}")
                print(f"  ISBN: {livro['isbn']}")
                print(f"  Sinopse: {livro['sinopse'][:100]}...")
            else:
                print(f"❌ Nenhum livro encontrado com ISBN: {isbn}")
            
            return livro
        except Exception as e:
            print(f"❌ Erro ao buscar livro por ISBN: {e}")
            return None

    def atualizar_livro(self, isbn: str, novos_dados: Dict) -> bool:
        """
        Atualiza os dados de um livro existente
        """
        try:
            # Remover campos que não devem ser atualizados
            campos_protegidos = ['_id', 'data_criacao']
            for campo in campos_protegidos:
                novos_dados.pop(campo, None)
            
            # Adicionar timestamp de atualização
            novos_dados['data_atualizacao'] = datetime.now()
            
            result = self.collection.update_one(
                {"isbn": isbn},
                {"$set": novos_dados}
            )
            
            if result.matched_count > 0:
                print(f"✅ Livro com ISBN {isbn} atualizado com sucesso!")
                return True
            else:
                print(f"❌ Nenhum livro encontrado com ISBN: {isbn}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao atualizar livro: {e}")
            return False

    def deletar_livro(self, isbn: str) -> bool:
        """
        Deleta um livro do banco de dados
        """
        try:
            result = self.collection.delete_one({"isbn": isbn})
            
            if result.deleted_count > 0:
                print(f"✅ Livro com ISBN {isbn} deletado com sucesso!")
                return True
            else:
                print(f"❌ Nenhum livro encontrado com ISBN: {isbn}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao deletar livro: {e}")
            return False

    def contar_livros(self) -> int:
        """
        Retorna o número total de livros na coleção
        """
        try:
            count = self.collection.count_documents({})
            print(f"📊 Total de livros na biblioteca: {count}")
            return count
        except Exception as e:
            print(f"❌ Erro ao contar livros: {e}")
            return 0

    def listar_todos_livros(self) -> List[Dict]:
        """
        Lista todos os livros da biblioteca
        """
        try:
            livros = list(self.collection.find())
            print(f"📚 Listando todos os {len(livros)} livros:")
            
            for livro in livros:
                print(f"  - {livro['titulo']} ({livro['autor']}, {livro['ano_publicacao']})")
            
            return livros
        except Exception as e:
            print(f"❌ Erro ao listar todos os livros: {e}")
            return []

    def fechar_conexao(self):
        """
        Fecha a conexão com o MongoDB
        """
        try:
            self.client.close()
            print("✅ Conexão com MongoDB fechada")
        except Exception as e:
            print(f"❌ Erro ao fechar conexão: {e}")
