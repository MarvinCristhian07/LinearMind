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
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/1.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/2.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/3.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/4.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/5.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/6.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/7.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/8.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/9.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/10.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/11.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/12.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_02/13.png")}),
        ]
    ),

    LESSON_3_ID: Lesson(
        id=LESSON_3_ID, 
        title="3. Zero da Função", 
        slides=[
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/1.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/2.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/3.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/4.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/5.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/6.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/7.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/8.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/9.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/10.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/11.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/12.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/13.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_03/14.png")}),
        ]
    ),
    LESSON_4_ID: Lesson(
        id=LESSON_4_ID, 
        title="4. Construção e Leitura de Gráficos", 
        slides=[
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/1.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/2.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/3.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/4.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/5.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/6.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/7.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/8.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/9.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/10.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/11.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/12.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/13.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/14.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/15.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_04/16.png")}),
        ]
    ),
    LESSON_5_ID: Lesson(
        id=LESSON_5_ID, 
        title="5. Estudo do Sinal", 
        slides=[
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/1.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/2.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/3.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/4.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/5.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/6.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/7.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/8.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/9.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/10.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/11.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/12.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/13.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/14.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_05/15.png")}),
        ]
    ),
    LESSON_6_ID: Lesson(
        id=LESSON_6_ID, 
        title="6. Obtenção da Lei de Formação", 
        slides=[
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/1.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/2.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/3.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/4.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/5.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/6.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/7.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/8.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/9.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/10.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/11.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/12.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/13.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/14.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/15.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_06/16.png")}),
        ]
    ),
    LESSON_7_ID: Lesson(
        id=LESSON_7_ID, 
        title="7. Casos Particulares", 
        slides=[
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/1.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/2.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/3.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/4.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/5.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/6.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/7.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/8.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/9.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/10.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/11.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/12.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/13.png")}),
            Slide(type="image", content={"image_path": get_asset_path("slides/aula_07/14.png")}),
        ]
    ),
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