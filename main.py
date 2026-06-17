import streamlit as st
import json

# 페이지 설정 (브라우저 탭 제목과 아이콘)
st.set_page_config(page_title="AI 주방 로봇 셰프", page_icon="🤖")

# 1. 레시피 데이터 불러오기
try:
    with open('recipes.json', 'r', encoding='utf-8') as f:
        recipe_db = json.load(f)
except:
    recipe_db = {}

# 2. 왼쪽 사이드바 설정
st.sidebar.title("📖 메뉴 목록")
st.sidebar.write("원하는 메뉴를 선택하세요!")

# 레시피 이름들만 가져와서 리스트로 만들기
menu_list = list(recipe_db.keys())

# 사이드바에 라디오 버튼(클릭형 목록) 생성
# 만약 메뉴가 너무 많다면 st.sidebar.selectbox를 써도 좋습니다.
selected_menu = st.sidebar.radio("오늘의 요리는?", menu_list)

# 3. 오른쪽 메인 화면 설정
st.title("🤖 AI 주방 로봇 셰프")

if selected_menu:
    # 선택된 메뉴의 데이터 가져오기
    data = recipe_db[selected_menu]
    
    st.divider() # 구분선
    st.header(f"🍳 {selected_menu} 조리법")
    
    # 재료 출력
    st.subheader("🛒 필수 재료")
    st.write(", ".join(data['ingredients']))
    
    # 조리 순서 출력
    st.subheader("👨‍🍳 조리 순서")
    for i, step in enumerate(data['steps'], 1):
        st.write(f"{i}. {step}")
        
    st.success(f"🤖 {selected_menu} 조리를 시작해 보세요!")
else:
    st.info("왼쪽 메뉴에서 요리를 선택해 주세요.")
    import streamlit as st

# 사이드바에서 메뉴를 선택했다고 가정
selected_menu = "갈치" 

# 조리 시작 버튼 구현
if st.button("🚀 조리 시작"):
    st.success(f"로봇 셰프가 {selected_menu} 조리를 지원합니다! 재료 준비 되셨나요?")
    
    # 조리 순서에 체크박스 추가
    st.write("---")
    step1 = st.checkbox("1. 갈치를 토막 낸다.")
    step2 = st.checkbox("2. 노릇하게 굽는다.")
    
    if step1 and step2:
        st.balloons() # 축하 폭죽 효과!
        st.write("🎉 완벽합니다! 맛있는 요리가 완성되었습니다.")