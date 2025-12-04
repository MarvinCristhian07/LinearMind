import os
from src.core.entities.exercise import Exercise

def get_asset_path(subpath):
    # Retornar o caminho absoluto para um arquivo dentro da pasta assets na raiz.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    return os.path.join(project_root, "assets", subpath)

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
        prompt="Dada a função f(x) = 3x - 4, calcule o valor de f(5).\n\nInsira sua resposta para f(5) no campo abaixo:",
        inputs={"f(5)": "float"}, # O input que o aluno deve preencher
        answers={"f(5)": 11},     # A resposta correta
        ai_context="O aluno está calculando f(5) para a função f(x) = 3x - 4. A resposta correta é 11. O cálculo esperado é 3 * 5 - 4 = 15 - 4 = 11."
    ),
    
    EX_F_2_ID: Exercise(
        id=EX_F_2_ID,
        level="facil",
        prompt="Observe a função f(x) = 2x + 15. Qual é o valor numérico do coeficiente linear (o termo independente b)?\n\nInsira o valor de b:",
        inputs={"b": "float"},
        answers={"b": 15},
        ai_context="O aluno está encontrando o coeficiente linear (b) para a função f(x) = 2x + 15. A resposta correta é 15 (O aluno deve identificar o número que está sozinho)."
    ),
    
    EX_F_3_ID: Exercise(
        id=EX_F_3_ID,
        level="facil",
        prompt="Determine a raiz da função f(x) = 2x - 10.\n\nInsira o valor da raiz (x) no campo abaixo:",
        inputs={"x": "float"},
        answers={"x": 5},
        ai_context="O aluno está calculando a raiz da função f(x) = 2x - 10. A resposta correta é 5. O cálculo esperado é igualar a zero: 2x - 10 = 0 -> 2x = 10 -> x = 5."
    ),

    EX_F_4_ID: Exercise(
        id=EX_F_4_ID,
        level="facil",
        prompt="Um motorista cobra uma taxa fixa de R$ 5,00 mais R$ 2,00 por quilômetro rodado. Se a corrida tiver exatamente 10 km, qual será o valor final a pagar?\n\nInsira o valor final:",
        inputs={"valor": "float"},
        answers={"valor": 25},
        ai_context="O aluno está aplicando a função em um contexto real. O cálculo é 5 (fixo) + 2 * 10 (km) = 5 + 20 = 25. A resposta correta é 25."
    ),

    EX_F_5_ID: Exercise(
        id=EX_F_5_ID,
        level="facil",
        prompt="Na função f(x) = 12 - 4x, qual é o valor do coeficiente angular (a)?\n\nInsira o valor de a:",
        inputs={"a": "float"},
        answers={"a": -4},
        ai_context="O aluno deve identificar o coeficiente angular (a) na função f(x) = 12 - 4x. A resposta correta é -4. O aluno deve notar que a ordem está invertida e o 'a' é o termo que multiplica o x."
    ),

    
    # Nível Médio
    
    EX_M_1_ID: Exercise(
        id=EX_M_1_ID,
        level="medio",
        prompt="Dada a função f(x) = 5x - 20, qual deve ser o valor de x para que o resultado da função (y) seja igual a 15?",
        inputs={"x": "float"},
        answers={"x": 7},
        ai_context="O aluno precisa encontrar o valor de x que resulta em y = 15. Ele deve igualar a função a 15, montando a equação: 5x - 20 = 15. Isolando o x: 5x = 35 -> x = 7. A resposta correta é 7."
    ),

    EX_M_2_ID: Exercise(
        id=EX_M_2_ID, 
        level="medio", 
        prompt="Observe o gráfico acima. Ele corta o eixo Y em 4 e o eixo X em -2. Calcule o valor do coeficiente angular (a) dessa função.", 
        inputs={"a": "float"}, 
        answers={"a": 2}, 
        ai_context="O aluno deve interpretar o gráfico para achar a lei de formação. O corte em Y indica que b = 4. O corte em X indica que a raiz é -2. Substituindo na equação (0 = a*(-2) + 4), temos 2a = 4, logo a = 2. A resposta correta é 2.",
        image_path=get_asset_path("exercises/medium/m1.png")
    ),
    
    EX_M_3_ID: Exercise(
        id=EX_M_3_ID, 
        level="medio", 
        prompt="Uma função afim passa pelos pontos A(2, 5) e B(4, 13). Qual é o valor da taxa de variação (coeficiente angular a) dessa função?", 
        inputs={"a": "float"}, 
        answers={"a": 4}, 
        ai_context="O aluno deve calcular o coeficiente angular (a) usando a fórmula da variação (Delta y / Delta x) entre os pontos (2, 5) e (4, 13). O cálculo é (13 - 5) / (4 - 2) = 8 / 2 = 4. A resposta correta é 4."
    ),

    EX_M_4_ID: Exercise(
        id=EX_M_4_ID, 
        level="medio", 
        prompt="O gráfico mostra o nível de água de um tanque. Ele começa no 10 e chega a zero no tempo 5. Baseado nesse gráfico, qual seria o nível da água no tempo x = 2?", 
        inputs={}, 
        answers={}, 
        ai_context="O aluno deve primeiro deduzir a função pelo gráfico: b=10 (início) e raiz=5 (fim), logo a = -2 (f(x) = -2x + 10). Em seguida, deve calcular f(2): -2 * 2 + 10 = -4 + 10 = 6. A resposta correta é 6.",
        image_path=get_asset_path("exercises/medium/m2.png")
    ),

    EX_M_5_ID: Exercise(
        id=EX_M_5_ID, 
        level="medio", 
        prompt="...", 
        inputs={}, 
        answers={}, 
        ai_context="O exercício pede o ponto onde o lucro deixa de ser negativo, ou seja, a raiz da função (onde zera). O aluno deve resolver 4x - 24 = 0. 4x = 24 -> x = 6. A resposta correta é 6."
    ),

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
