import streamlit as st
import json
import os

st.set_page_config(page_title="AI 주방 로봇 셰프", layout="wide")

# 데이터 파일 읽기
file_path = 'recipes.json'
recipe_db = {}

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            recipe_db = json.load(f)
        except:
            st.error("JSON 파일 형식이 올바르지 않습니다.")
else:
    st.error(f"{file_path} 파일을 찾을 수 없습니다.")

# 사이드바
st.sidebar.title("📖 메뉴 목록")
if recipe_db:
    selected_menu = st.sidebar.radio("오늘의 요리는?", list(recipe_db.keys()))
else:
    selected_menu = None
    st.sidebar.write("불러올 레시피가 없습니다.")

# 메인 화면
st.title("🤖 AI 주방 로봇 셰프")
search_query = st.text_input("🔍 무엇을 만들어 볼까요?")

target = search_query if search_query else selected_menu

if target and target in recipe_db:
    data = recipe_db[target]
    st.header(f"🍳 {target} 조리법")
    st.subheader("🛒 필수 재료")
    st.write(", ".join(data['ingredients']))
    st.subheader("👨‍🍳 조리 순서")
    for i, step in enumerate(data['steps'], 1):
        st.write(f"{i}. {step}")
elif target:
    st.warning(f"'{target}' 레시피를 찾을 수 없습니다.")