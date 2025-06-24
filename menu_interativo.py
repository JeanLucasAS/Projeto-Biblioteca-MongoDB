from book_manager import BookManager

class MenuInterativo:
    def __init__(self):
        self.manager = BookManager("mongodb+srv://jeanlucas:o8AjoadIRyvbxDc3@cluster0.f7tzj2o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    
    def exibir_menu(self):
        """
        Exibe o menu principal
        """
        print("\n" + "=" * 50)
        print("📚 SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
        print("=" * 50)
        print("1. 📖 Inserir novo livro")
        print("2. 🔍 Buscar livro por ISBN")
        print("3. 👤 Listar livros por autor")
        print("4. 🏷️  Listar livros por gênero")
        print("5. 📅 Listar livros por ano")
        print("6. 📏 Top 10 livros com mais páginas")
        print("7. 📖 Top 10 livros com menos páginas")
        print("8. ✏️  Atualizar livro")
        print("9. 🗑️  Deletar livro")
        print("10. 📊 Estatísticas da biblioteca")
        print("11. 📋 Listar todos os livros")
        print("0. 🚪 Sair")
        print("-" * 50)
    
    def inserir_livro_interativo(self):
        """
        Interface para inserir um novo livro
        """
        print("\n📖 INSERIR NOVO LIVRO")
        print("-" * 30)
        
        try:
            livro = {
                "titulo": input("Título: ").strip(),
                "autor": input("Autor: ").strip(),
                "ano_publicacao": int(input("Ano de publicação: ")),
                "genero": input("Gênero: ").strip(),
                "num_paginas": int(input("Número de páginas: ")),
                "sinopse": input("Sinopse: ").strip(),
                "isbn": input("ISBN: ").strip()
            }
            
            self.manager.inserir_livro(livro)
            
        except ValueError:
            print("❌ Erro: Ano e número de páginas devem ser números inteiros!")
        except Exception as e:
            print(f"❌ Erro ao inserir livro: {e}")
    
    def buscar_por_isbn_interativo(self):
        """
        Interface para buscar livro por ISBN
        """
        print("\n🔍 BUSCAR LIVRO POR ISBN")
        print("-" * 30)
        
        isbn = input("Digite o ISBN: ").strip()
        if isbn:
            self.manager.buscar_livro_por_isbn(isbn)
        else:
            print("❌ ISBN não pode estar vazio!")
    
    def listar_por_autor_interativo(self):
        """
        Interface para listar livros por autor
        """
        print("\n👤 LISTAR LIVROS POR AUTOR")
        print("-" * 30)
        
        autor = input("Digite o nome do autor: ").strip()
        if autor:
            self.manager.listar_livros_por_autor(autor)
        else:
            print("❌ Nome do autor não pode estar vazio!")
    
    def listar_por_genero_interativo(self):
        """
        Interface para listar livros por gênero
        """
        print("\n🏷️ LISTAR LIVROS POR GÊNERO")
        print("-" * 30)
        
        genero = input("Digite o gênero: ").strip()
        if genero:
            self.manager.listar_livros_por_genero(genero)
        else:
            print("❌ Gênero não pode estar vazio!")
    
    def listar_por_ano_interativo(self):
        """
        Interface para listar livros por ano
        """
        print("\n📅 LISTAR LIVROS POR ANO")
        print("-" * 30)
        
        try:
            ano = int(input("Digite o ano: "))
            self.manager.listar_livros_por_ano(ano)
        except ValueError:
            print("❌ Erro: Ano deve ser um número inteiro!")
    
    def atualizar_livro_interativo(self):
        """
        Interface para atualizar um livro
        """
        print("\n✏️ ATUALIZAR LIVRO")
        print("-" * 30)
        
        isbn = input("Digite o ISBN do livro a ser atualizado: ").strip()
        if not isbn:
            print("❌ ISBN não pode estar vazio!")
            return
        
        # Primeiro, mostrar o livro atual
        livro_atual = self.manager.buscar_livro_por_isbn(isbn)
        if not livro_atual:
            return
        
        print("\nDigite os novos valores (deixe em branco para manter o valor atual):")
        
        novos_dados = {}
        
        # Campos que podem ser atualizados
        campos = {
            "titulo": "Título",
            "autor": "Autor", 
            "ano_publicacao": "Ano de publicação",
            "genero": "Gênero",
            "num_paginas": "Número de páginas",
            "sinopse": "Sinopse"
        }
        
        for campo, label in campos.items():
            valor_atual = livro_atual.get(campo, "")
            novo_valor = input(f"{label} (atual: {valor_atual}): ").strip()
            
            if novo_valor:
                if campo in ["ano_publicacao", "num_paginas"]:
                    try:
                        novos_dados[campo] = int(novo_valor)
                    except ValueError:
                        print(f"❌ Erro: {label} deve ser um número inteiro!")
                        return
                else:
                    novos_dados[campo] = novo_valor
        
        if novos_dados:
            self.manager.atualizar_livro(isbn, novos_dados)
        else:
            print("ℹ️ Nenhum campo foi alterado.")
    
    def deletar_livro_interativo(self):
        """
        Interface para deletar um livro
        """
        print("\n🗑️ DELETAR LIVRO")
        print("-" * 30)
        
        isbn = input("Digite o ISBN do livro a ser deletado: ").strip()
        if not isbn:
            print("❌ ISBN não pode estar vazio!")
            return
        
        # Mostrar o livro antes de deletar
        livro = self.manager.buscar_livro_por_isbn(isbn)
        if not livro:
            return
        
        confirmacao = input("\n⚠️ Tem certeza que deseja deletar este livro? (s/N): ").strip().lower()
        if confirmacao == 's':
            self.manager.deletar_livro(isbn)
        else:
            print("ℹ️ Operação cancelada.")
    
    def mostrar_estatisticas(self):
        """
        Mostra estatísticas da biblioteca
        """
        print("\n📊 ESTATÍSTICAS DA BIBLIOTECA")
        print("-" * 30)
        
        total = self.manager.contar_livros()
        
        if total > 0:
            # Estatísticas adicionais
            try:
                pipeline = [
                    {"$group": {
                        "_id": "$genero",
                        "count": {"$sum": 1}
                    }},
                    {"$sort": {"count": -1}}
                ]
                
                generos = list(self.manager.collection.aggregate(pipeline))
                
                print(f"\n📈 Distribuição por gênero:")
                for genero in generos:
                    print(f"  - {genero['_id']}: {genero['count']} livro(s)")
                
                # Média de páginas
                pipeline_media = [
                    {"$group": {
                        "_id": None,
                        "media_paginas": {"$avg": "$num_paginas"},
                        "total_paginas": {"$sum": "$num_paginas"}
                    }}
                ]
                
                resultado = list(self.manager.collection.aggregate(pipeline_media))
                if resultado:
                    media = resultado[0]['media_paginas']
                    total_pag = resultado[0]['total_paginas']
                    print(f"\n📏 Média de páginas por livro: {media:.1f}")
                    print(f"📚 Total de páginas na biblioteca: {total_pag:,}")
                
            except Exception as e:
                print(f"❌ Erro ao calcular estatísticas: {e}")
    
    def executar(self):
        """
        Loop principal do menu interativo
        """
        print("🎉 Bem-vindo ao Sistema de Gerenciamento de Biblioteca!")
        
        while True:
            try:
                self.exibir_menu()
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == "0":
                    print("\n👋 Obrigado por usar o sistema! Até logo!")
                    break
                elif opcao == "1":
                    self.inserir_livro_interativo()
                elif opcao == "2":
                    self.buscar_por_isbn_interativo()
                elif opcao == "3":
                    self.listar_por_autor_interativo()
                elif opcao == "4":
                    self.listar_por_genero_interativo()
                elif opcao == "5":
                    self.listar_por_ano_interativo()
                elif opcao == "6":
                    self.manager.listar_livros_mais_paginas(10)
                elif opcao == "7":
                    self.manager.listar_livros_menos_paginas(10)
                elif opcao == "8":
                    self.atualizar_livro_interativo()
                elif opcao == "9":
                    self.deletar_livro_interativo()
                elif opcao == "10":
                    self.mostrar_estatisticas()
                elif opcao == "11":
                    self.manager.listar_todos_livros()
                else:
                    print("❌ Opção inválida! Tente novamente.")
                
                input("\n⏸️ Pressione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Sistema encerrado pelo usuário. Até logo!")
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")
                input("\n⏸️ Pressione Enter para continuar...")
        
        # Fechar conexão
        self.manager.fechar_conexao()

def main():
    """
    Função principal para executar o menu interativo
    """
    menu = MenuInterativo()
    menu.executar()

if __name__ == "__main__":
    main()
