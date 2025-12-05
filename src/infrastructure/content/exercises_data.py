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
        inputs={"Nível": "float"}, 
        answers={"Nível": 6}, 
        ai_context="O aluno deve primeiro deduzir a função pelo gráfico: b=10 (início) e raiz=5 (fim), logo a = -2 (f(x) = -2x + 10). Em seguida, deve calcular f(2): -2 * 2 + 10 = -4 + 10 = 6. A resposta correta é 6.",
        image_path=get_asset_path("exercises/medium/m2.png")
    ),

    EX_M_5_ID: Exercise(
        id=EX_M_5_ID, 
        level="medio", 
        prompt="Considere a função de lucro L(x) = 4x - 24. A partir de qual quantidade vendida (x) o lucro deixa de ser negativo e passa a ser zero (ponto de equilíbrio)?", 
        inputs={"x": "float"}, 
        answers={"x": 6}, 
        ai_context="O exercício pede o ponto onde o lucro deixa de ser negativo, ou seja, a raiz da função (onde zera). O aluno deve resolver 4x - 24 = 0. 4x = 24 -> x = 6. A resposta correta é 6."
    ),

    # Nível Difícil

    # Preencher futuramente
    EX_D_1_ID: Exercise(
        id=EX_D_1_ID,
        level="dificil",
        prompt="Uma máquina produz peças em ritmo constante. Em 2 horas de funcionamento, ela produziu um total de 100 peças. Em 5 horas, o total subiu para 220 peças. Quantas peças essa máquina terá produzido ao completar 8 horas?",
        inputs={"Peças": "float"},
        answers={"Peças": 340},
        ai_context="O aluno deve primeiro descobrir a função f(x) = ax + b usando os pontos (2, 100) e (5, 220). Calculando o 'a' (delta): (220-100)/(5-2) = 40. Calculando o 'b': 100 = 40*2 + b -> b = 20. Função: f(x) = 40x + 20. Por fim, calcular f(8): 40*8 + 20 = 320 + 20 = 340."
    ),
    
    EX_D_2_ID: Exercise(
        id=EX_D_2_ID,
        level="dificil",
        prompt="Observe o gráfico acima, que mostra uma reta passando pelos pontos (2, 3) e (-1, 9). Calcule a raiz (zero da função) desta reta.",
        inputs={"x": "float"},
        answers={"x": 3.5},
        ai_context="O aluno deve: 1) Achar o 'a': (9-3)/(-1-2) = -2. 2) Achar o 'b' substituindo um ponto: 3 = -2(2) + b -> b = 7. A função é f(x) = -2x + 7. 3) Calcular a raiz: -2x + 7 = 0 -> 2x = 7 -> x = 3.5.",
        image_path=get_asset_path("exercises/hard/h1.png")
    ),
    
    EX_D_3_ID: Exercise(
        id=EX_D_3_ID,
        level="dificil",
        prompt="Sabendo que a função f(x) = ax + 10 possui sua raiz igual a 5, calcule o valor de f(-2).",
        inputs={"Resultado": "float"},
        answers={"Resultado": 14},
        ai_context="Este é um problema de lógica reversa. Se a raiz é 5, então f(5) = 0. O aluno substitui: a*5 + 10 = 0 -> 5a = -10 -> a = -2. Com a função completa (f(x) = -2x + 10), ele calcula f(-2): -2*(-2) + 10 = 4 + 10 = 14."
    ),
    
    EX_D_4_ID: Exercise(
        id=EX_D_4_ID,
        level="dificil",
        prompt="Uma empresa começa o dia com um saldo negativo de R$ -1.200,00 (custos fixos). Após vender 100 unidades de seu produto, o saldo sobe para R$ -400,00. Quantas unidades a empresa precisa vender no total para atingir o ponto de equilíbrio (saldo zero)?",
        inputs={"Unidades": "float"},
        answers={"Unidades": 150},
        ai_context="O aluno identifica b = -1200. Usa o ponto (100, -400) para achar o 'a': f(100) = a*100 - 1200 = -400 -> 100a = 800 -> a = 8. A função é f(x) = 8x - 1200. Para achar o equilíbrio (raiz): 8x - 1200 = 0 -> 8x = 1200 -> x = 150."
    ),
    
    EX_D_5_ID: Exercise(
        id=EX_D_5_ID,
        level="dificil",
        prompt="Analise o gráfico acima, que contém os pontos (-1, -1) e (2, 5). Determine o valor numérico onde essa reta cortará o eixo vertical Y (Coeficiente Linear).",
        inputs={"b": "float"},
        answers={"b": 1},
        ai_context="O aluno precisa achar o valor de 'b'. Primeiro acha o 'a': (5 - (-1))/(2 - (-1)) = 6/3 = 2. Depois substitui um ponto para achar o 'b': 5 = 2(2) + b -> 5 = 4 + b -> b = 1. A reta corta o eixo Y no 1.",
        image_path=get_asset_path("exercises/hard/h2.png")
    ),
}

EXERCISES_ORDER = {
    "facil": [EX_F_1_ID, EX_F_2_ID, EX_F_3_ID, EX_F_4_ID, EX_F_5_ID],
    "medio": [EX_M_1_ID, EX_M_2_ID, EX_M_3_ID, EX_M_4_ID, EX_M_5_ID],
    "dificil": [EX_D_1_ID, EX_D_2_ID, EX_D_3_ID, EX_D_4_ID, EX_D_5_ID],
}
