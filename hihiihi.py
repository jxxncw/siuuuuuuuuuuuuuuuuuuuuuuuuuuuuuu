# st.write(): 가장 기본적인 텍스트 출력 함수입니다
st.write("이것은 기본 텍스트 출력입니다.")
# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")
# 페이지 구조용 제목 출력
st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입니다")
# 수평선 (구분선) 출력
st.markdown("---")  # 또는
st.divider()        # Streamlit >= 1.22 이상에서 가능
# LaTeX 수식 출력
st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}")
# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")
