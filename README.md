# 📚 Cadastro de Alunos

Pequeno sistema em **Django** para cadastrar, listar e excluir alunos.  
Interface feita com **Bootstrap 5** e ícones do **Font Awesome**.

---

## 🚀 Funcionalidades

- ➕ Cadastro de novos alunos  
- 🗑 Exclusão com confirmação  
- 📋 Listagem em tabela responsiva  

---

## 🛠 Tecnologias

- [Django 5](https://www.djangoproject.com/)  
- [Bootstrap 5](https://getbootstrap.com/)  
- [Font Awesome](https://fontawesome.com/)  

---

## ▶ Como rodar

```bash
# Clone o repositório
git clone https://github.com/Predox/Escola.git
cd Escola

# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# ou
.venv\Scripts\activate      # Windows

# Instale dependências
pip install -r requirements.txt

# Rode migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
