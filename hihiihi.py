import streamlit as st

st.title('이히히히힣')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 : ')
mbti = st.selectbox('MBTI를 선택해주세요:', [
    'A형', 'B형', 'O형', 'AB형', ])

# MBTI 설명 데이터 (더 자세히)
mbti_data = {
    'A형': {
        '특징': '세심하고 책임감 있는 완벽주의자. 계획적이고 타인을 배려하는 성향.',
        '직업': '회계',
        '잘 맞는 혈액형': ['O형']
    },
    'B': {
        '특징': '자유로운 사고와 창의성. 개성 넘치고 독립적.',
        '직업': '판',
        '잘 맞는 혈액형': ['AB형']
    },
    'O형': {
        '특징': '리더십과 자신감. 외향적이고 목표 지향적.',
        '직업': '영업',
        '잘 맞는 혈액형': ['A형']
    },
    'AB형': {
        '특징': '냉철한 분석력과 창의성. 감정과 이성의 균형.',
        '직업': '전문직',
        '잘 맞는 혈액형': ['B형']
    },
   

if st.button('특징 생성'):
    if mbti in mbti_data:
        특징 = mbti_data[mbti]['특징']
        직업 = mbti_data[mbti]['직업']
        잘_맞는_mbti = ', '.join(mbti_data[mbti]['잘 맞는 혈액형'])

        st.write(f"{name}님! 당신의 MBTI 유형은 {mbti}입니다!")
        st.write(f"**특징**: {특징}")
        st.write(f"**어울리는 직업**: {직업}")
        st.write(f"**잘 맞는 MBTI 유형**: {잘_맞는_mbti}")
    else:
        st.write(f"{name}님! 아직 {mbti} 유형에 대한 정보가 없습니다.")
