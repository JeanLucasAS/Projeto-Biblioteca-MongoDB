from book_manager import BookManager

def popular_dados_exemplo(manager: BookManager):
    """
    Popula o banco com alguns livros de exemplo
    """
    livros_exemplo = [
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "ano_publicacao": 1949,
            "genero": "Ficção Científica",
            "num_paginas": 328,
            "sinopse": "Um romance distópico que retrata uma sociedade totalitária onde o governo controla todos os aspectos da vida dos cidadãos.",
            "isbn": "978-0-452-28423-4"
        },
        {
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis",
            "ano_publicacao": 1899,
            "genero": "Romance",
            "num_paginas": 256,
            "sinopse": "A história de Bentinho e sua obsessão por Capitu, questionando se ela o traiu ou não.",
            "isbn": "978-85-359-0277-5"
        },
        {
            "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
            "autor": "J.R.R. Tolkien",
            "ano_publicacao": 1954,
            "genero": "Fantasia",
            "num_paginas": 423,
            "sinopse": "A jornada épica de Frodo Baggins para destruir o Um Anel e salvar a Terra-média.",
            "isbn": "978-0-547-92822-7"
        },
        {
            "titulo": "Cem Anos de Solidão",
            "autor": "Gabriel García Márquez",
            "ano_publicacao": 1967,
            "genero": "Realismo Mágico",
            "num_paginas": 417,
            "sinopse": "A saga da família Buendía na cidade fictícia de Macondo, misturando realidade e fantasia.",
            "isbn": "978-0-06-088328-7"
        },
        {
            "titulo": "O Pequeno Príncipe",
            "autor": "Antoine de Saint-Exupéry",
            "ano_publicacao": 1943,
            "genero": "Fábula",
            "num_paginas": 96,
            "sinopse": "A história de um pequeno príncipe que viaja de planeta em planeta, aprendendo sobre a vida e o amor.",
            "isbn": "978-0-15-601219-5"
        },
        {
            "titulo": "Neuromancer",
            "autor": "William Gibson",
            "ano_publicacao": 1984,
            "genero": "Ficção Científica",
            "num_paginas": 271,
            "sinopse": "Um hacker é contratado para realizar o hack definitivo em um mundo cyberpunk.",
            "isbn": "978-0-441-56956-9"
        },
        {
            "titulo": "Pride and Prejudice",
            "autor": "Jane Austen",
            "ano_publicacao": 1813,
            "genero": "Romance",
            "num_paginas": 432,
            "sinopse": "A história de Elizabeth Bennet e sua relação complicada com o orgulhoso Sr. Darcy.",
            "isbn": "978-0-14-143951-8"
        },
        {
            "titulo": "Dune",
            "autor": "Frank Herbert",
            "ano_publicacao": 1965,
            "genero": "Ficção Científica",
            "num_paginas": 688,
            "sinopse": "Paul Atreides navega pela política intergaláctica no planeta desértico Arrakis.",
            "isbn": "978-0-441-17271-9"
        }
    ]
    
    print("🔄 Populando banco de dados com livros de exemplo...")
    for livro in livros_exemplo:
        manager.inserir_livro(livro)
    print("✅ Dados de exemplo inseridos!\n")

def demonstrar_consultas(manager: BookManager):
    """
    Demonstra todas as funcionalidades do sistema
    """
    print("=" * 60)
    print("📚 SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("=" * 60)
    
    # Contar livros
    manager.contar_livros()
    print()
    
    # Consultas por autor
    print("🔍 CONSULTA POR AUTOR:")
    manager.listar_livros_por_autor("George Orwell")
    print()
    
    # Consultas por gênero
    print("🔍 CONSULTA POR GÊNERO:")
    manager.listar_livros_por_genero("Ficção Científica")
    print()
    
    # Consultas por ano
    print("🔍 CONSULTA POR ANO:")
    manager.listar_livros_por_ano(1984)
    print()
    
    # Livros com mais páginas
    print("🔍 LIVROS COM MAIS PÁGINAS:")
    manager.listar_livros_mais_paginas(5)
    print()
    
    # Livros com menos páginas
    print("🔍 LIVROS COM MENOS PÁGINAS:")
    manager.listar_livros_menos_paginas(5)
    print()
    
    # Busca por ISBN
    print("🔍 BUSCA POR ISBN:")
    manager.buscar_livro_por_isbn("978-0-452-28423-4")
    print()

def demonstrar_crud(manager: BookManager):
    """
    Demonstra operações CRUD
    """
    print("=" * 60)
    print("🔧 DEMONSTRAÇÃO DE OPERAÇÕES CRUD")
    print("=" * 60)
    
    # Inserir novo livro
    print("➕ INSERINDO NOVO LIVRO:")
    novo_livro = {
        "titulo": "O Hobbit",
        "autor": "J.R.R. Tolkien",
        "ano_publicacao": 1937,
        "genero": "Fantasia",
        "num_paginas": 310,
        "sinopse": "A aventura de Bilbo Baggins com treze anões para recuperar o tesouro guardado pelo dragão Smaug.",
        "isbn": "978-0-547-92822-1"
    }
    manager.inserir_livro(novo_livro)
    print()
    
    # Atualizar livro
    print("✏️ ATUALIZANDO LIVRO:")
    manager.atualizar_livro("978-0-547-92822-1", {
        "num_paginas": 320,
        "sinopse": "A jornada inesperada de Bilbo Baggins, um hobbit que se junta a treze anões em uma quest épica."
    })
    print()
    
    # Verificar atualização
    print("🔍 VERIFICANDO ATUALIZAÇÃO:")
    manager.buscar_livro_por_isbn("978-0-547-92822-1")
    print()
    
    # Deletar livro
    print("🗑️ DELETANDO LIVRO:")
    manager.deletar_livro("978-0-547-92822-1")
    print()

def main():
    """
    Função principal que executa o exemplo completo
    """
    try:
        # Inicializar o gerenciador
        # NOTA: Para usar com MongoDB real, altere a connection_string
        # Exemplo: "mongodb://username:password@localhost:27017/"
        manager = BookManager("mongodb+srv://jeanlucas:o8AjoadIRyvbxDc3@cluster0.f7tzj2o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

        
        # Popular com dados de exemplo
        popular_dados_exemplo(manager)
        
        # Demonstrar consultas
        demonstrar_consultas(manager)
        
        # Demonstrar CRUD
        demonstrar_crud(manager)
        
        # Listar todos os livros no final
        print("=" * 60)
        print("📋 TODOS OS LIVROS NA BIBLIOTECA:")
        print("=" * 60)
        manager.listar_todos_livros()
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
    
    finally:
        # Fechar conexão
        if 'manager' in locals():
            manager.fechar_conexao()

if __name__ == "__main__":
    main()
