import os
import google.generativeai as genai
from typing import Dict, Any

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Chave da API do Gemini (GEMINI_API_KEY) não foi encontrada no arquivo .env")
        
        genai.configure(api_key=self.api_key)
        
        self.generation_config = {
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }
        
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
        
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-preview-09-2025",
            generation_config=self.generation_config,
            safety_settings=self.safety_settings
        )
        print("Serviço do Gemini inicializado com sucesso.")

    def _build_system_prompt(self, exercise_prompt: str, correct_answers: Dict, ai_context: str) -> str:
        return f"""
        **Persona:** Você é o "LinearMind", um assistente de IA e tutor de matemática amigável e encorajador, especializado em Função Afim (Função do 1º Grau).
        
        **Contexto do Problema:**
        O aluno está tentando resolver o seguinte exercício:
        "{exercise_prompt}"
        
        **Informações Internas (Não mostre ao aluno):**
        - Resposta(s) correta(s) do exercício: {correct_answers}
        - Contexto adicional do problema: {ai_context}

        **Sua Tarefa (Regras Estritas):**
        O aluno tentou resolver o problema e errou. A resposta que ele deu será fornecida abaixo.
        Sua única tarefa é fornecer uma **dica construtiva** para ajudá-lo a encontrar o erro.

        **REGRAS ABSOLUTAS (NUNCA QUEBRE):**
        1.  **NUNCA, JAMAIS, EM HIPÓTESE ALGUMA, forneça a resposta correta** ou os valores corretos.
        2.  **NÃO FAÇA O CÁLCULO** para o aluno.
        3.  **SEJA VAGO, MAS ÚTIL.** Foque em *onde* o aluno pode ter errado.
        4.  Compare a resposta do aluno com a correta e identifique o erro.
        5.  Seja curto, amigável e direto (1-2 frases no máximo).
        6.  Fale em Português do Brasil.
        7.  **ZERO MARKDOWN**, sua resposta não pode ficar em markdown. A resposta deve ficar bem formatada, legível e compreensível ao aluno, mas não pode markdown
        """

    def get_ai_hint(self, exercise_prompt: str, correct_answers: Dict, user_answers: Dict, ai_context: str) -> str:
        system_instruction = self._build_system_prompt(exercise_prompt, correct_answers, ai_context)
        
        user_input = f"Eu tentei resolver e coloquei estas respostas: {user_answers}. Onde eu errei?"

        full_prompt = f"{system_instruction}\n\n---\n\nAluno: {user_input}"

        try:
            response = self.model.generate_content(full_prompt)
            return response.text

        except Exception as e:
            print(f"Erro ao chamar a API do Gemini: {e}")
            return "Opa, tive um problema ao tentar analisar sua resposta. Tente novamente em instantes."