import streamlit as st
from deep_translator import GoogleTranslator

# 제목 설정
st.title("한국어-영어 번역기")
st.write("텍스트를 한국어에서 영어로, 또는 영어에서 한국어로 번역합니다.")

# 입력 텍스트
text_to_translate = st.text_area("번역할 텍스트를 입력하세요:", "")

# 번역 방향 선택
translation_direction = st.radio(
    "번역 방향을 선택하세요:",
    options=["한국어 → 영어", "영어 → 한국어"],
    index=0
)

# 번역 버튼
if st.button("번역하기"):
    if text_to_translate.strip():
        st.subheader("번역 결과")
        try:
            if translation_direction == "한국어 → 영어":
                translated_text = GoogleTranslator(source="ko", target="en").translate(text_to_translate)
            else:
                translated_text = GoogleTranslator(source="en", target="ko").translate(text_to_translate)
            
            st.write(translated_text)
        except Exception as e:
            st.error(f"번역 중 오류가 발생했습니다: {str(e)}")
    else:
        st.warning("번역할 텍스트를 입력하세요.")

