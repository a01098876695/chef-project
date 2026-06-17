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