import streamlit as st
from deep_translator import GoogleTranslator

# 제목 설정
st.title("🌟 ★늘봄★다국어 번역기 🌟")
st.write("🌍 입력한 텍스트를 여러 언어로 번역합니다.")

# 입력 텍스트
st.text_area("📝 번역할 텍스트를 입력하세요:", "", key="text_input")

# 언어 선택
languages = {
    "영어 🇺🇸": "en",
    "일본어 🇯🇵": "ja",
    "중국어 🇨🇳": "zh-cn",
    "러시아어 🇷🇺": "ru",
    "아랍어 🇸🇦": "ar",
    "프랑스어 🇫🇷": "fr",
    "스페인어 🇪🇸": "es",
    "인도네시아어 🇮🇩": "id",
    "베트남어 🇻🇳": "vi"
}

selected_languages = st.multiselect(
    "🌐 번역할 언어를 선택하세요:",
    options=list(languages.keys()),
    default=["영어 🇺🇸"]
)

# 번역 버튼
if st.button("🚀 번역하기"):
    text_to_translate = st.session_state["text_input"]
    if text_to_translate.strip():
        st.subheader("🔍 번역 결과")
        for language in selected_languages:
            lang_code = languages[language]
            try:
                translated_text = GoogleTranslator(source="auto", target=lang_code).translate(text_to_translate)
                st.write(f"**{language}**: {translated_text}")
            except Exception as e:
                st.error(f"⚠️ {language} 번역 중 오류가 발생했습니다: {str(e)}")
    else:
        st.warning("⚠️ 번역할 텍스트를 입력하세요.")

