import streamlit as st
from googletrans import Translator

# 제목 설정
st.title("다국어 번역기")
st.write("입력한 텍스트를 여러 언어로 번역합니다.")

# 번역기 초기화
translator = Translator()

# 입력 텍스트
text_to_translate = st.text_area("번역할 텍스트를 입력하세요:", "")

# 언어 선택
languages = {
    "영어": "en",
    "일본어": "ja",
    "중국어": "zh-cn",
    "러시아어": "ru",
    "아랍어": "ar",
    "프랑스어": "fr"
}

selected_languages = st.multiselect(
    "번역할 언어를 선택하세요:",
    options=list(languages.keys()),
    default=["영어"]
)

# 번역 버튼
if st.button("번역하기"):
    if text_to_translate.strip():
        st.subheader("번역 결과")
        for language in selected_languages:
            lang_code = languages[language]
            translated_text = translator.translate(text_to_translate, dest=lang_code).text
            st.write(f"**{language}**: {translated_text}")
    else:
        st.warning("번역할 텍스트를 입력하세요.")
