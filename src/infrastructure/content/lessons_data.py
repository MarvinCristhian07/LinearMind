import os
from src.core.entities.lesson import Lesson, Slide

def get_asset_path(subpath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    return os.path.join(project_root, "assets", subpath)

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
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/1.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/2.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/3.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/4.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/5.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/6.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/7.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/8.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/9.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/10.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/11.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/12.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/13.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_01/14.png")}),
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