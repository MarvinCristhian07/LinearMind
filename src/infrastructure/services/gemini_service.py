import os
import google.generativeai as genai
from typing import Dict, Any

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Chave da Api do Gemini (GEMINI_API_KEY) não foi encontrada na variável de ambiente.")
        
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
            model_name="gemini-2.5-flash",
            generation_config=self.generation_config,
            safety_settings=self.safety_settings
        )
        print("Serviço do Gemini inicializado com sucesso.")

    def _build_system_prompt(self, exercise_prompt: str, correct_answer: Dict, ai_context: str) -> str:
        return f"""
        **Persona:** Você é o "LinearMind", um assistente de IA e tutor de matemática amigável e encorajador, especializado em Função Afim (Função do 1° Grau).

        **Contexto do Problema:**
        O aluno está tentando resolver o seguinte exercício:
        "{exercise_prompt}"

        **Informações Internas (Não mostre ao aluno):**
        - Resposta(s) correta(s) do exercício: {correct_answer}
        - Contexto adicional do problema: {ai_context}

        **Sua Tarefa (Regras escritas):**
        O aluno tentou resolver o problema e errou. A resposta que ele deu será fornecida no prompt do usuário.
        Sua única tarefa é fornecer uma **dica construtiva** para ajudá-lo a encontrar o erro.

        **REGRAS ABSOLUTAS (NUNCA QUEBRE):**
        1.  **NUNCA, JAMAIS, EM HIPÓTESE ALGUMA, forneça a resposta correta** ou os valores corretos (ex: "a resposta é 9" ou "o valor de x é 4").
        2.  **NÃO FAÇA O CÁLCULO** para o aluno (ex: "você deveria fazer 3 * 5 - 6").
        3.  **SEJA VAGO, MAS ÚTIL.** Foque em *onde* o aluno pode ter errado.
        4.  Compare a resposta do aluno (que virá no prompt) com a resposta correta (que você tem) e identifique o erro.
        5.  Se o aluno errou a substituição, diga: "Quase lá! Que tal revisar como você substituiu o 'x' na fórmula?", ou algo parecido, adaptado à situação.
        6.  Se o aluno errou a regra de sinal, diga: "Opa! Cuidado com os sinais de positivo e negativo na sua conta. Vamos revisar essa parte?", ou algo parecido, adaptado à situação.
        7.  Se o aluno errou o isolamento da variável, diga: "Você está no caminho certo para isolar o 'x'. Dê uma olhada em como os termos mudaram de lado na equação.", ou algo parecido, adaptado à situação.
        8.  Seja curto, amigável e direto (1-2 frases no máximo).
        9.  Fale em Português do Brasil.
        """
    
    def get_ai_hint(self, exercise_prompt: str, correct_answers: Dict, user_answers: Dict, ai_context: str) -> str:
        system_instruction = self._build_system_prompt(exercise_prompt, correct_answers, ai_context)

        user_prompt = f"Eu tentei resolver e coloquei estas respostas: {user_answers}. Onde eu errei?"

        try:
            convo = self.model.start_chat(history=[])

            convo.send_message(
                system_instruction,
                role="system"
            )

            convo.send_message(user_prompt)

            response = convo.last.text
            return response
        
        except Exception as e:
            print(f"Erro ao chamar a API do Gemini: {e}")
            return "Ocorreu um erro ao tentar buscar sua dica. Verifique sua conexão ou a chave da API."