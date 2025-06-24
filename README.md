# 📚 Sistema de Gerenciamento de Biblioteca com MongoDB

Um sistema completo para gerenciar uma biblioteca de livros usando Python e MongoDB Atlas. O projeto oferece funcionalidades completas de CRUD (Create, Read, Update, Delete) e consultas avançadas para gerenciamento de acervo bibliográfico.

## 🎯 Funcionalidades

### 📖 Gerenciamento de Livros
- ✅ **Inserir** novos livros com validação completa
- ✅ **Buscar** livros por ISBN, autor, gênero ou ano
- ✅ **Atualizar** informações de livros existentes
- ✅ **Deletar** livros do acervo
- ✅ **Listar** todos os livros da biblioteca

### 🔍 Consultas Especializadas
- 👤 Listar todos os livros de um autor específico
- 🏷️ Listar todos os livros de um gênero específico
- 📅 Listar todos os livros publicados em um ano específico
- 📏 Top 10 livros com mais páginas
- 📖 Top 10 livros com menos páginas
- 🔎 Busca exata por ISBN

### 📊 Estatísticas e Relatórios
- 📈 Distribuição de livros por gênero
- 📏 Média de páginas por livro
- 📚 Total de páginas na biblioteca
- 📊 Contagem total de livros

## 🏗️ Estrutura do Projeto

```
projeto-biblioteca/
├── book_manager.py          # Classe principal de gerenciamento
├── exemplo_uso.py           # Demonstração completa do sistema
├── menu_interativo.py       # Interface de linha de comando
├── connection_test.py       # Teste de conexão com MongoDB
├── test_mongo.py           # Teste básico de inserção
├── limpar_duplicados.py    # Script para limpeza de dados
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## 🚀 Instalação e Configuração

### 1. Pré-requisitos
- Python 3.7 ou superior
- Conta no MongoDB Atlas (gratuita)
- Git (opcional)

### 2. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd projeto-biblioteca
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configuração do MongoDB Atlas

#### Opção A: Usar a Configuração Existente
O projeto já está configurado para usar o MongoDB Atlas. Os arquivos já contêm a string de conexão configurada.

#### Opção B: Configurar Sua Própria Instância
1. Acesse [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Crie uma conta gratuita
3. Crie um novo cluster
4. Configure as credenciais de acesso
5. Obtenha a string de conexão
6. Substitua a URI nos arquivos:
   - `book_manager.py`
   - `exemplo_uso.py`
   - `menu_interativo.py`

### 5. Teste a Conexão
```bash
python connection_test.py
```

Se a conexão for bem-sucedida, você verá:
```
✅ Conectado ao MongoDB Atlas!
```

## 📋 Como Usar

### 🎮 Menu Interativo (Recomendado)
Execute o menu interativo para usar todas as funcionalidades:

```bash
python menu_interativo.py
```

O menu oferece 11 opções principais:
1. 📖 Inserir novo livro
2. 🔍 Buscar livro por ISBN
3. 👤 Listar livros por autor
4. 🏷️ Listar livros por gênero
5. 📅 Listar livros por ano
6. 📏 Top 10 livros com mais páginas
7. 📖 Top 10 livros com menos páginas
8. ✏️ Atualizar livro
9. 🗑️ Deletar livro
10. 📊 Estatísticas da biblioteca
11. 📋 Listar todos os livros

### 🧪 Demonstração Completa
Execute o exemplo completo com dados de teste:

```bash
python exemplo_uso.py
```

Este script irá:
- Inserir 8 livros de exemplo
- Demonstrar todas as consultas
- Mostrar operações CRUD
- Exibir estatísticas da biblioteca

### 💻 Uso Programático
```python
from book_manager import BookManager

# Inicializar o gerenciador
manager = BookManager()

# Inserir um novo livro
livro = {
    "titulo": "O Alquimista",
    "autor": "Paulo Coelho",
    "ano_publicacao": 1988,
    "genero": "Ficção",
    "num_paginas": 163,
    "sinopse": "A jornada de Santiago em busca de seu tesouro pessoal.",
    "isbn": "978-85-325-1158-9"
}

manager.inserir_livro(livro)

# Buscar livros por autor
livros = manager.listar_livros_por_autor("Paulo Coelho")

# Fechar conexão
manager.fechar_conexao()
```

## 📊 Estrutura dos Dados

Cada livro é armazenado como um documento MongoDB com a seguinte estrutura:

```json
{
  "_id": ObjectId("..."),
  "titulo": "1984",
  "autor": "George Orwell",
  "ano_publicacao": 1949,
  "genero": "Ficção Científica",
  "num_paginas": 328,
  "sinopse": "Um romance distópico que retrata...",
  "isbn": "978-0-452-28423-4",
  "data_criacao": ISODate("2024-01-15T10:30:00Z"),
  "data_atualizacao": ISODate("2024-01-16T14:20:00Z")
}
```

### Campos Obrigatórios
- `titulo`: Título do livro
- `autor`: Nome do autor
- `ano_publicacao`: Ano de publicação (inteiro)
- `genero`: Gênero literário
- `num_paginas`: Número de páginas (inteiro)
- `sinopse`: Resumo do livro
- `isbn`: ISBN único do livro

### Campos Automáticos
- `_id`: ID único gerado pelo MongoDB
- `data_criacao`: Timestamp de criação
- `data_atualizacao`: Timestamp da última atualização

## 🛠️ Scripts Utilitários

### Teste de Conexão
```bash
python connection_test.py
```
Verifica se a conexão com MongoDB Atlas está funcionando.

### Teste Básico
```bash
python test_mongo.py
```
Insere um livro de teste e lista todos os livros.

### Limpeza de Duplicados
```bash
python limpar_duplicados.py
```
Remove livros duplicados baseado no ISBN, mantendo apenas uma cópia de cada.

## 🔧 Recursos Técnicos

### Validações Implementadas
- ✅ Campos obrigatórios
- ✅ Tipos de dados corretos
- ✅ ISBN único (índice único)
- ✅ Tratamento de erros completo

### Funcionalidades Avançadas
- 🔍 Busca case-insensitive usando regex
- 📊 Agregações MongoDB para estatísticas
- 🔒 Índices únicos para evitar duplicatas
- ⏰ Timestamps automáticos
- 🛡️ Proteção contra campos sensíveis

### Performance
- 📈 Índices otimizados para consultas frequentes
- 🚀 Consultas eficientes usando agregação
- 💾 Conexão reutilizável
- 🔄 Pool de conexões automático

## 🐛 Solução de Problemas

### Erro de Conexão
```
❌ Erro ao conectar ao MongoDB: ...
```
**Solução**: Verifique sua conexão com a internet e as credenciais do MongoDB Atlas.

### Erro de ISBN Duplicado
```
❌ Erro: Já existe um livro com o ISBN ...
```
**Solução**: Cada ISBN deve ser único. Use um ISBN diferente ou atualize o livro existente.

### Erro de Validação
```
❌ Erro de validação: Campo obrigatório 'titulo' não fornecido
```
**Solução**: Certifique-se de que todos os campos obrigatórios estão preenchidos.

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas principais:

```
pymongo==4.13.2          # Driver MongoDB para Python
python-dotenv==1.1.0      # Gerenciamento de variáveis de ambiente
requests==2.32.4          # Requisições HTTP
```

## 🚀 Próximos Passos

### Melhorias Planejadas
- 🌐 Interface web com Flask
- 📱 API REST completa
- 🔐 Sistema de autenticação
- 📊 Dashboard com gráficos
- 📤 Exportação de dados (CSV, JSON)
- 🔍 Busca full-text avançada

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:
- 🐛 Reportar bugs
- 💡 Sugerir melhorias
- 🔧 Enviar pull requests
- 📖 Melhorar a documentação


## 👨‍💻 Autor

Jean Lucas Álvaro da Silva

---

**🎉 Divirta-se explorando o sistema de gerenciamento de biblioteca!**
```

Este README.md fornece instruções completas e detalhadas para executar seu projeto, incluindo:

1. **Instalação passo a passo** com todas as dependências
2. **Configuração do MongoDB Atlas** (usando sua configuração atual)
3. **Múltiplas formas de uso** (menu interativo, exemplo completo, programático)
4. **Documentação completa** da estrutura de dados
5. **Scripts utilitários** que você criou
6. **Solução de problemas** comuns
7. **Recursos técnicos** implementados

O README está formatado de forma profissional e inclui emojis para melhor visualização, seguindo as melhores práticas de documentação de projetos Python.

