import streamlit as st

# 웹 페이지 제목 설정
st.title("🌌 만유인력 계산기")
st.markdown("두 물체의 질량과 거리를 입력하여 서로 당기는 중력을 계산하고, 태양-지구 / 달-지구 중력과 비교해 보세요.")

st.divider()

# 레이아웃을 두 열로 나누어 입력창 배치
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 입력 값 설정")
    a = st.number_input('물체 a의 질량 (kg)', min_value=0.0, value=1.0e24, step=1.0e22, format="%e")
    b = st.number_input('물체 b의 질량 (kg)', min_value=0.0, value=1.0e24, step=1.0e22, format="%e")
    r = st.number_input('물체 a와 물체 b의 거리 (m)', min_value=1e-10, value=1.0e8, step=1.0e6, format="%e")

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
        
        # 1. 태양-지구 중력과 비교 (요청하신 기능 추가)
        st.write(f"☀️ **태양-지구 사이 중력의** `{(g/sun_earth):.6e}` 배")
        if g > sun_earth:
            st.info("💡 계산된 중력이 **태양-지구 사이의 중력보다 큽니다!**")
        elif g < sun_earth:
            st.warning("📉 계산된 중력이 **태양-지구 사이의 중력보다 작습니다.**")
        else:
            st.success("⚖️ 계산된 중력이 **태양-지구 사이의 중력과 같습니다.**")
            
        st.divider()
        
        # 2. 달-지구 중력과 비교 (보너스로 달-지구 비교도 동일하게 적용!)
        st.write(f"🌕 **달-지구 사이 중력의** `{(g/moon_earth):.6e}` 배")
        if g > moon_earth:
            st.info("💡 계산된 중력이 **달-지구 사이의 중력보다 큽니다!**")
        elif g < moon_earth:
            st.warning("📉 계산된 중력이 **달-지구 사이의 중력보다 작습니다.**")
        else:
            st.success("⚖️ 계산된 중력이 **달-지구 사이의 중력과 같습니다.**")
            
    else:
        st.error("거리는 0보다 커야 합니다.")

st.divider()
st.caption("공식: $F = G \\frac{m_1 m_2}{r^2}$ | 중력상수 $G = 6.67430 \\times 10^{-11} \\text{ m}^3 \\text{kg}^{-1} \\text{s}^{-2}$")