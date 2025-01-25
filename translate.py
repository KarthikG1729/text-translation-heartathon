from inference.engine import Model

model = Model("/media/sreetej/Extreme SSD2/Sreetej/smolagents/indictrans/en-indic/fairseq_model", model_type="fairseq")




def translate(text, tgt_language):

    english_language = "eng_Latn"
    translated_text = model.translate_paragraph(text, english_language, tgt_language)
    return translated_text