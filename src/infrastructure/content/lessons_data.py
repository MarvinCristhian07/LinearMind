from src.core.entities.lesson import Lesson, Slide

LESSON_1_ID = "aula_1_formacao"
LESSON_2_ID = "aula_2_classificacao"
LESSON_3_ID = "aula_3_zero"
LESSON_4_ID = "aula_4_graficos"
LESSON_5_ID = "aula_5_sinal"
LESSON_6_ID = "aula_6_obtencao"
LESSON_7_ID = "aula_7_casos"

# Conteúdo de todas as aulas
LESSONS_CONTENT = {
    LESSON_1_ID: Lesson(
        id=LESSON_1_ID,
        title="1. Lei de Formação",
        slides=[
            Slide(type="text", content={"text": "Bem-vindo(a) à Aula 1: Lei de Formação!\n\nUma função afim, também conhecida como função do 1° grau, é toda função f: R → R que pode ser escrita na forma:\n\nf(x) = ax + b"}),
            Slide(type="text", content={"text": "Nesta fórmula:\n\n'a' é o Coeficiente Angular (define a inclinação da reta).\n'b' é o Coeficiente Linear (define onde a reta corta o eixo Y).\n\nAmbos 'a' e 'b' são números reais, e 'a' deve ser diferente de zero (a ≠ 0)."}),
            Slide(type="text", content={"text": "Exemplo:\n\nSe f(x) = 2x + 3:\n\nO coeficiente angular 'a' é 2.\nO coeficiente linear 'b' é 3.\n\nSe f(x) = -x + 10:\n\nO coeficiente angular 'a' é -1.\nO coeficiente linear 'b' é 10."}),
            Slide(type="text", content={"text": "Parabéns! Você concluiu a Aula 1.\n\nClique em 'Concluir' para desbloquear a próxima aula."})
        ]
    ),

    LESSON_2_ID: Lesson(
        id=LESSON_2_ID,
        title="2. Classificação pelo Coef. Angular",
        slides=[
            Slide(type="text", content={"text": "Aula 2: Classificação\n\nO coeficiente angular 'a' define se a função é Crescente, Decrescente ou Constante."}),
            Slide(type="text", content={"text": "Se a > 0 (positivo), a função é CRESCENTE.\nEx: f(x) = 3x + 1"}),
            Slide(type="text", content={"text": "Se a < 0 (negativo), a função é DECRESCENTE.\nEx: f(x) = -2x + 5"})
        ]
    ),

    LESSON_3_ID: Lesson(id=LESSON_3_ID, title="3. Zero da Função", slides=[Slide(type="text", content={"text": "Conteúdo da Aula 3..."})]),
    LESSON_4_ID: Lesson(id=LESSON_4_ID, title="4. Construção e Leitura de Gráficos", slides=[Slide(type="text", content={"text": "Conteúdo da Aula 4..."})]),
    LESSON_5_ID: Lesson(id=LESSON_5_ID, title="5. Estudo do Sinal", slides=[Slide(type="text", content={"text": "Conteúdo da Aula 5..."})]),
    LESSON_6_ID: Lesson(id=LESSON_6_ID, title="6. Obtenção da Lei de Formação", slides=[Slide(type="text", content={"text": "Conteúdo da Aula 6..."})]),
    LESSON_7_ID: Lesson(id=LESSON_7_ID, title="7. Casos Particulares", slides=[Slide(type="text", content={"text": "Conteúdo da Aula 7..."})]),
}

LESSONS_ORDER = [
    LESSON_1_ID,
    LESSON_2_ID,
    LESSON_3_ID,
    LESSON_4_ID,
    LESSON_5_ID,
    LESSON_6_ID,
    LESSON_7_ID,
]