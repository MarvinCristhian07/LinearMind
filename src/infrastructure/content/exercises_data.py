from src.core.entities.exercise import Exercise

# Fácil
EX_F_1_ID = "ex_f_1"
EX_F_2_ID = "ex_f_2"
EX_F_3_ID = "ex_f_3"
EX_F_4_ID = "ex_f_4"
EX_F_5_ID = "ex_f_5"

# Médio
EX_M_1_ID = "ex_m_1"
EX_M_2_ID = "ex_m_2"
EX_M_3_ID = "ex_m_3"
EX_M_4_ID = "ex_m_4"
EX_M_5_ID = "ex_m_5"

# Difícil
EX_D_1_ID = "ex_d_1"
EX_D_2_ID = "ex_d_2"
EX_D_3_ID = "ex_d_3"
EX_D_4_ID = "ex_d_4"
EX_D_5_ID = "ex_d_5"

EXERCISES_CONTENT = {
    # Nível Fácil
    EX_F_1_ID: Exercise(
        id=EX_F_1_ID,
        level="facil",
        prompt="Dada a função f(x) = 3x - 6, calcule o valor de f(5).\n\nInsira sua resposta para f(5) no campo abaixo:",
        inputs={"f(5)": "float"}, # O input que o aluno deve preencher
        answers={"f(5)": 9.0},     # A resposta correta
        ai_context="O aluno está calculando f(5) para a função f(x) = 3x - 6. A resposta correta é 9. O cálculo é 3 * 5 - 6. O erro provável é na substituição do X ou na operação 15 - 6."
    ),
    
    EX_F_2_ID: Exercise(
        id=EX_F_2_ID,
        level="facil",
        prompt="Dada a função f(x) = -x + 4, encontre o 'zero da função' (o valor de x para o qual f(x) = 0).\n\nInsira o valor de x:",
        inputs={"x": "float"},
        answers={"x": 4.0},
        ai_context="O aluno está encontrando o zero da função f(x) = -x + 4. A resposta correta é x = 4. O cálculo é 0 = -x + 4, logo x = 4. O erro provável é na regra de sinal ao isolar o X."
    ),
    
    # Preencher futuramente
    EX_F_3_ID: Exercise(id=EX_F_3_ID, level="facil", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_F_4_ID: Exercise(id=EX_F_4_ID, level="facil", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_F_5_ID: Exercise(id=EX_F_5_ID, level="facil", prompt="...", inputs={}, answers={}, ai_context="..."),

    
    # Nível Médio
    
    EX_M_1_ID: Exercise(
        id=EX_M_1_ID,
        level="medio",
        prompt="Uma função afim f(x) = ax + b passa pelos pontos A(1, 5) e B(3, 11). Encontre os valores de 'a' e 'b'.",
        inputs={"a": "float", "b": "float"}, # Múltiplos inputs
        answers={"a": 3.0, "b": 2.0},
        ai_context="O aluno está encontrando a lei de formação (a e b) dados dois pontos A(1, 5) e B(3, 11). Resposta: a=3, b=2. O aluno deve montar um sistema: 1) a+b=5; 2) 3a+b=11. O erro provável é no cálculo do sistema de equações."
    ),

    # Preencher futuramente
    EX_M_2_ID: Exercise(id=EX_M_2_ID, level="medio", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_M_3_ID: Exercise(id=EX_M_3_ID, level="medio", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_M_4_ID: Exercise(id=EX_M_4_ID, level="medio", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_M_5_ID: Exercise(id=EX_M_5_ID, level="medio", prompt="...", inputs={}, answers={}, ai_context="..."),

    # Nível Difícil

    # Preencher futuramente
    EX_D_1_ID: Exercise(id=EX_D_2_ID, level="dificil", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_D_2_ID: Exercise(id=EX_D_2_ID, level="dificil", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_D_3_ID: Exercise(id=EX_D_3_ID, level="dificil", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_D_4_ID: Exercise(id=EX_D_4_ID, level="dificil", prompt="...", inputs={}, answers={}, ai_context="..."),
    EX_D_5_ID: Exercise(id=EX_D_5_ID, level="dificil", prompt="...", inputs={}, answers={}, ai_context="..."),
}

EXERCISES_ORDER = {
    "facil": [EX_F_1_ID, EX_F_2_ID, EX_F_3_ID, EX_F_4_ID, EX_F_5_ID],
    "medio": [EX_M_1_ID, EX_M_2_ID, EX_M_3_ID, EX_M_4_ID, EX_M_5_ID],
    "dificil": [EX_D_1_ID, EX_D_2_ID, EX_D_3_ID, EX_D_4_ID, EX_D_5_ID],
}
