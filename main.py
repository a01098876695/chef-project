import streamlit as st
import json

# 페이지 설정
st.set_page_config(page_title="AI 주방 로봇 셰프", page_icon="🤖", layout="wide")

# 데이터 불러오기
try:
    with open('recipes.json', 'r', encoding='utf-8') as f:
        recipe_db = json.load(f)
except:
    recipe_db = {}

# 1. 사이드바 메뉴
st.sidebar.title("📖 메뉴 목록")
selected_menu = st.sidebar.radio("오늘의 요리는?", list(recipe_db.keys()))

# 2. 메인 화면
st.title("🤖 AI 주방 로봇 셰프")
search_query = st.text_input("🔍 무엇을 만들어 볼까요?", placeholder="요리 이름을 입력하세요")

# 검색 우선순위 설정
target = search_query if search_query else selected_menu

if target and target in recipe_db:
    data = recipe_db[target]
    st.divider()
    st.header(f"🍳 {target} 조리법")
    
    st.subheader("🛒 필수 재료")
    st.write(", ".join(data['ingredients']))
    
    st.subheader("👨‍🍳 조리 순서")
    for i, step in enumerate(data['steps'], 1):
        st.write(f"{i}. {step}")
        
    st.success(f"{target} 조리를 시작해 보세요!")
elif search_query:
    st.warning(f"'{search_query}' 레시피를 찾을 수 없습니다.")
else:
    st.info("검색창에 입력하거나, 왼쪽 메뉴 목록에서 요리를 선택하세요.")