<div align="center">

# 🧠 LinearMind
### Objeto Educacional para estudo da Função Afim (1° Grau)

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-F7931E?style=for-the-badge&logo=materialdesign&logoColor=white)
![Google Generative AI](https://img.shields.io/badge/Google%20Generative%20AI-FF0000?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

</div>

## 📖 Sobre o Projeto

O **LinearMind** é um software educacional desenvolvido como parte da avaliação acadêmica da disciplina de Matemática do Curso de Inteligência Artificial da **Fatec Rio Claro**.

O projeto visa solucionar a lacuna no aprendizado de matemática no Ensino Médio, especificamente no tópico de **Função Afim (Função do 1º Grau)**. Utilizando uma abordagem gamificada e interativa, o software transforma o aprendizado passivo em uma experiência ativa, onde o aluno progride através de trilhas de conhecimento e desafios práticos.

O diferencial tecnológico do LinearMind reside na integração de um **Tutor Inteligente** baseado em IA Generativa, capaz de identificar erros de raciocínio lógico-matemático e fornecer feedbacks construtivos em tempo real, sem entregar a resposta final (Método Socrático).

---

## 🚀 Funcionalidades Principais

### 1. Trilha de Aprendizado Sequencial 📚
Sistema de aulas estruturado onde o progresso é controlado. O aluno deve concluir os módulos teóricos para desbloquear novos conteúdos:
* Lei de Formação
* Classificação pelo Coef. Angular
* Zero da Função
* Construção e Leitura de Gráficos
* Estudo do Sinal
* Obtenção da Lei de Formação
* Casos Particulares

### 2. Prática Gamificada 🎮
Exercícios divididos por níveis de dificuldade (**Fácil, Médio e Difícil**). O sistema de progressão exige domínio dos conceitos básicos antes de liberar problemas complexos que envolvem interpretação de gráficos e sistemas lineares.

### 3. Tutor Inteligente (IA) 🤖
Integração com a API **Google Gemini 2.5 Flash**.
* **Análise Contextual:** A IA recebe o enunciado, a resposta correta e a resposta errada do aluno.
* **Feedback Pedagógico:** O sistema é instruído a não fornecer a resposta. Em vez disso, ele analisa *onde* o aluno errou (ex: regra de sinal, isolamento de variável) e oferece uma dica para que o próprio aluno corrija seu raciocínio.

### 4. Interface Moderna e Responsiva 💻
Desenvolvido com **CustomTkinter**, oferecendo uma experiência de usuário (UX) fluida, com modo tela cheia, tema escuro (Dark Mode) e suporte a renderização de gráficos e imagens.

---

## 🛠️ Arquitetura e Tecnologias

O projeto foi construído seguindo rigorosamente os princípios da **Clean Architecture** (Arquitetura Limpa), garantindo desacoplamento entre a interface, a lógica de negócios e os serviços externos.

* **Linguagem:** Python 3.15.5
* **Interface Gráfica:** CustomTkinter (CTk)
* **Inteligência Artificial:** Google Generative AI (Gemini)
* **Processamento de Imagem:** Pillow (PIL)
* **Padrões de Projeto:** Singleton, Repository Pattern, Dependency Injection.

### Estrutura de Diretórios
```bash
linearmind/
├── assets/                  # Recursos estáticos (Imagens/Slides)
├── src/
│   ├── core/                # Regras de Negócio e Entidades (Puras)
│   ├── infrastructure/      # Implementação de DB, API e Conteúdo
│   └── presentation/        # Interface Gráfica (Views e ViewModels)
├── main.py                  # Ponto de entrada
└── requirements.txt         # Dependências
```

---

## ⚙️ Instalação e Execução

Siga os passos abaixo para executar o projeto em seu ambiente local.

### Pré-requisitos

* Python 3.10 ou superior instalado.
* Uma chave de API do Google AI Studio (Gemini).

## Passo a Passo
1. **Clone o repositório:**
```bash
git clone [https://github.com/MarvinCristhian07/LinearMind.git](https://github.com/MarvinCristhian07/LinearMind.git)
cd linearmind
```

2. **Crie um ambiente virtual (Recomendado):**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configuração de Ambiente:**
* Renomeie o arquivo ```.env.example``` para ```.env```.
* Abra o arquivo ```.env``` e insira sua chave de API:
```bash
GEMINI_API_KEY="SUA_CHAVE_AQUI"
```

5. **Execute a aplicação:**
```bash
python main.py
```

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

A escolha da licença MIT reflete o compromisso acadêmico e educacional do projeto. Ela permite que qualquer pessoa — estudantes, professores ou instituições — use, copie, modifique e distribua este software livremente, incentivando a colaboração e o avanço do ensino de matemática através da tecnologia.

---

## 🎓 Créditos e Institucional

**Fatec Rio Claro**
* **Curso:** Inteligência Artificial
* **Disciplina:** Matemática
* **Semestre:** 2º Semestre / 2025

Desenvolvido com foco em inovação educacional e aplicação prática de conceitos de IA.
