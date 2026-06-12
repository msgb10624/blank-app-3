import streamlit as st

# 웹 페이지 제목 설정
st.title("🌌 반복문과 리스트를 활용한 만유인력 계산기")
st.markdown("입력한 질량을 바탕으로 다양한 거리에서의 중력을 **리스트**와 **반복문**을 통해 계산합니다.")

st.divider()

# 입력창 배치
st.subheader("📥 물체 질량 설정")
col1, col2 = st.columns(2)
with col1:
    a = st.number_input('물체 a의 질량 (kg)', min_value=0.0, value=5.972e24, step=1.0e22, format="%e") # 기본값: 지구 질량 수준
with col2:
    b = st.number_input('물체 b의 질량 (kg)', min_value=0.0, value=7.347e22, step=1.0e22, format="%e") # 기본값: 달 질량 수준

# 사용자 정의 거리 입력
user_r = st.number_input('비교해볼 사용자 정의 거리 (m)', min_value=1e-10, value=3.844e8, step=1.0e6, format="%e") # 기본값: 지구-달 거리

st.divider()
st.subheader("📊 거리별 중력 계산 결과 (반복문 활용)")

# 중력 상수 및 기준 중력 값 정의
G = 6.67430e-11
sun_earth = 3.52e22

# 1. 💡 [리스트(List) 활용] 비교하고 싶은 거리 정보와 이름을 딕셔너리 리스트로 저장
distances = [
    {"name": "인공위성 고도 수준 (약 42,000 km)", "value": 4.2e7},
    {"name": "지구-달 거리 수준 (약 384,400 km)", "value": 3.844e8},
    {"name": "태양-지구 거리 수준 (약 1억 5천만 km)", "value": 1.5e11},
    {"name": "사용자가 입력한 거리", "value": user_r}
]

# 2. 🔁 [반복문(For문) 활용] 리스트를 순회하며 중력 계산 및 태양-지구 중력과 비교
for dist in distances:
    name = dist["name"]
    r = dist["value"]
    
    # 만유인력 공식 계산
    g = (a * b * G) / (r**2)
    
    # 웹 화면에 각 거리별 결과 출력
    st.write(f"### 📍 {name}")
    st.write(f"- **거리:** `{r:,.2e} m` | **계산된 중력:** `{g:.6e} N`")
    st.write(f"- ☀️ 태양-지구 사이 중력의 `{(g/sun_earth):.6e}` 배")
    
    # 태양-지구 중력과 대소 비교 (조건문)
    if g > sun_earth:
        st.info("💡 이 거리에서의 중력은 **태양-지구 사이의 중력보다 큽니다!**")
    elif g < sun_earth:
        st.warning("📉 이 거리에서의 중력은 **태양-지구 사이의 중력보다 작습니다.**")
    else:
        st.success("⚖️ 이 거리에서의 중력은 **태양-지구 사이의 중력과 같습니다.**")
        
    st.markdown("---") #