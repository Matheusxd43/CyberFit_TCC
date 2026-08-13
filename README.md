<div align="center">

# ⚡ CyberFit TCC

### *Treino Inteligente. Evolução com Segurança.*

  <p align="center">
    Plataforma web interativa desenvolvida em Django para auxiliar alunos de academia no uso correto de equipamentos por meio de instruções dinâmicas, vídeos explicativos e integração com QR Codes.
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10+-00d4ff?style=for-the-badge&logo=python&logoColor=black" alt="Python">
    <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
    <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
    <img src="https://img.shields.io/badge/UI/UX-Dark%20Mode-1e293b?style=for-the-badge" alt="Dark Mode">
  </p>

</div>

---

## 🎯 Sobre o Projeto

O **CyberFit** é uma solução criada para transformar a experiência do treino em academias. Através de tags físicas fixadas em cada equipamento contendo **QR Codes**, o aluno pode escanear o código direto pelo smartphone e ser direcionado para a página do aparelho, onde encontra:

* 🏋️ **Guia de Execução:** Instruções detalhadas de postural e repetições.
* 🎥 **Conteúdo em Vídeo:** Demonstração visual do exercício.
* ⭐ **Avaliações de Usuários:** Espaço de feedback sobre a usabilidade do aparelho.

Além disso, o sistema conta com uma **módulo administrativo moderno** para cadastrar, atualizar e excluir equipamentos e mídias de forma prática.

---

## 🚀 Funcionalidades Principais

### 🏋️‍♂️ Para o Aluno (Visão Pública)
- [x] **Catálogo Dinâmico:** Visualização em *Cards* modernos estilo esportivo.
- [x] **Player de Vídeo Embutido:** Acesso direto a tutoriais do YouTube sem sair da plataforma.
- [x] **Acesso Rápido via QR Code:** Cada aparelho possui um link único (ID/PK).
- [x] **Design Responsivo:** Adaptado para celulares, tablets e computadores.

### 🛡️ Para o Administrador (Painel Restrito)
- [x] **Autenticação Segura:** Separação automática da interface via controle de permissão do Django.
- [x] **Gestão Completa (CRUD):** Cadastro, edição e exclusão de equipamentos e vídeos.
- [x] **Atalhos no Header:** Botões diretos para cadastro rápido quando logado.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python** | Linguagem principal do ecossistema |
| **Django** | Framework Web (Arquitetura MVT) |
| **SQLite3** | Banco de Dados relacional leve e integrado |
| **HTML5 & CSS3** | Estilização customizada em *Dark Mode* Esportivo |
| **Git / GitHub** | Controle de versão do código |

---

## 📁 Estrutura do Projeto

```text
CyberFit/
│
├── core/                         # Aplicação Principal
│   ├── migrations/               # Histórico do Banco de Dados
│   ├── static/core/css/          # Arquivos de Estilo (style.css)
│   ├── templates/                # Arquivos HTML
│   │   ├── admin/                # Customizações do Painel Admin
│   │   └── core/                 # base.html, home.html, detalhe_equipamento.html
│   ├── admin.py                  # Configuração do Django Admin
│   ├── models.py                 # Tabelas (Equipamento, ConteudoDigital, etc)
│   ├── urls.py                   # Rotas da aplicação
│   └── views.py                  # Lógica de renderização
│
├── cyberfit_project/             # Configurações Globais do Django
│   ├── settings.py               # Definições do Projeto e Banco
│   └── urls.py                   # Rota Principal
│

💻 Como Rodar o Projeto Localmente
Pré-requisitos
Python 3.10+ instalado.
Git instalado.
asso a Passo

Clone o repositório:
git clone [https://github.com/Matheusxd43/CyberFit_TCC.git](https://github.com/Matheusxd43/CyberFit_TCC.git)
cd CyberFit_TCC

Crie e ative o ambiente virtual:
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

Execute as migrações do Banco de Dados:
python manage.py migrate

Crie o usuário Administrador (Superuser):
python manage.py createsuperuser

Inicie o servidor de desenvolvimento:
python manage.py runserver.

Acesse no seu navegador:

Página dos Alunos: http://127.0.0.1:8000/

Painel Administrativo: http://127.0.0.1:8000/admin/

👥 Autores & Contribuidores
Matheus - Desenvolvedor & Idealizador do Projeto - @Matheusxd43

Gabriel Dias - Contribuição Front-end & UI Design - @Dev-Diias

├── db.sqlite3                    # Banco de dados local
├── manage.py                     # Script do Django
└── README.md                     # Documentação do Projeto
