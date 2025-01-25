from load_sys_path import *
load_sys()

from inference.engine import Model

model = Model(MODEL_PATH, model_type="fairseq")




def translate(text, tgt_language):

    english_language = "eng_Latn"
    translated_text = model.translate_paragraph(text, english_language, tgt_language)
    return translated_text