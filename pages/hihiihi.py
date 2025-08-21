import streamlit as st

st.title('이히히히힣')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 : ')
blood_type = st.selectbox('혈액형을 선택해주세요:', [
    'A형', 'B형', 'O형', 'AB형'
])

# 혈액형 설명 데이터
blood_type_data = {
    'A형': {
        '특징': '세심하고 책임감 있는 완벽주의자. 계획적이고 타인을 배려하는 성향.',
        '직업': '회계사',
        '잘 맞는 혈액형': ['O형']
    },
    'B형': {
        '특징': '자유로운 사고와 창의성. 개성 넘치고 독립적.',
        '직업': '판매',
        '잘 맞는 혈액형': ['AB형']
    },
    'O형': {
        '특징': '리더십과 자신감. 외향적이고 목표 지향적.',
        '직업': '영업 담당자',
        '잘 맞는 혈액형': ['A형']
    },
    'AB형': {
        '특징': '냉철한 분석력과 창의성. 감정과 이성의 균형.',
        '직업': '전문직',
        '잘 맞는 혈액형': ['B형']
    },
}

# 버튼 클릭 시 결과 출력
if st.button('특징 생성'):
    if blood_type in blood_type_data:
        특징 = blood_type_data[blood_type]['특징']
        직업 = blood_type_data[blood_type]['직업']
        잘_맞는_혈액형 = ', '.join(blood_type_data[blood_type]['잘 맞는 혈액형'])

        st.write(f"### {name}님! 당신의 혈액형은 {blood_type}입니다.")
        st.write(f"**특징**: {특징}")
        st.write(f"**어울리는 직업**: {직업}")
        st.write(f"**잘 맞는 혈액형**: {잘_맞는_혈액형}")
    else:
        st.write(f"{name}님! 아직 {blood_type} 유형에 대한 정보가 없습니다.")

