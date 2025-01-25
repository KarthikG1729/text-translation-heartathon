import streamlit as st

from translate import translate

# ===== UI ===========
st.title("AI Translator App")
st.divider()
st.markdown("## Translate text to any language.")


language_to_translate = st.selectbox(
    label="Language to translate to:",
    options=["Telugu","Hindi"]
)

text_to_translate = st.text_area("Paste text here:")

translate_btn = st.button("Translate")


lang_map = {"Telugu": "tel_Telu", "Hindi": "hin_Deva"}
language_to_translate = lang_map[language_to_translate]





if translate_btn and text_to_translate.strip() != "":
    placeholder = st.empty()
    full_translation = translate(text_to_translate, language_to_translate)
    placeholder.text(full_translation)
    print("translation completed")

    st.balloons()

elif translate_btn:
    st.error("Please provide the text to translate.")