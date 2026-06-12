import streamlit as st

# 웹 페이지 제목 설정
st.title("🌌 만유인력 계산기")
st.markdown("두 물체의 질량과 거리를 입력하여 서로 당기는 중력을 계산하고, 태양-지구 / 달-지구 중력과 비교해 보세요.")

st.divider()

# 레이아웃을 두 열로 나누어 입력창 배치
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 입력 값 설정")
    # 물체의 질량 및 거리 입력 (st.number_input 활용, 기본값 및 최소값 설정)
    a = st.number_input('물체 a의 질량 (kg)', min_value=0.0, value=1.0, step=1.0, format="%f")
    b = st.number_input('물체 b의 질량 (kg)', min_value=0.0, value=1.0, step=1.0, format="%f")
    r = st.number_input('물체 a와 물체 b의 거리 (m)', min_value=1e-10, value=1.0, step=0.1, format="%f")

with col2:
    st.subheader("📊 계산 결과")
    
    # 중력 상수 및 만유인력 계산
    G = 6.67430e-11
    
    if r > 0:
        g = (a * b * G) / (r**2)
        
        # 결과 출력
        st.success(f"**물체 a와 물체 b 사이의 중력:**")
        st.code(f"{g:.6e} N (뉴턴)", language="text")
        
        # 기준 중력 값 정의
        sun_earth = 3.52e22
        moon_earth = 1.98e20
        
        st.divider()
        
        # 비교 결과 출력 (소수점 아래가 너무 길어질 수 있으므로 과학적 표기법 활용)
        st.write(f"☀️ **태양-지구 사이 중력의** `{(g/sun_earth):.6e}` 배")
        st.write(f"🌕 **달-지구 사이 중력의** `{(g/moon_earth):.6e}` 배")
    else:
        st.error("거리는 0보다 커야 합니다.")

st.divider()
st.caption("공식: $F = G \\frac{m_1 m_2}{r^2}$ | 중력상수 $G = 6.67430 \\times 10^{-11} \\text{ m}^3 \\text{kg}^{-1} \\text{s}^{-2}$")