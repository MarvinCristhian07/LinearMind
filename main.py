import os
from dotenv import load_dotenv
from src.presentation.app import App

def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERRO: A variável de ambiente GEMINI_API_KEY não foi definida.")
        print("Verifique se o arquivo .env foi criado corretamente.")
        return
    
    print("Ambiente carregado. Iniciando LinearMind...")

    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")

if __name__ == "__main__":
    main()