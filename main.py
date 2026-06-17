import streamlit as st
import json

# JSON 파일 불러오기
try:
    with open('recipes.json', 'r', encoding='utf-8') as f:
        recipe_db = json.load(f)
except:
    recipe_db = {}

st.title("🤖 AI 주방 로봇 셰프")
user_input = st.text_input("메뉴를 입력하세요")

if user_input:
    if user_input in recipe_db:
        data = recipe_db[user_input]
        st.success(f"🤖 '{user_input}' 조리법을 찾았습니다!")
        st.write("**🛒 필수 재료:**", ", ".join(data['ingredients']))
        st.write("**👨‍🍳 조리 순서:**")
        for step in data['steps']:
            st.write(step)
    else:
        st.info("🤖 죄송합니다. 아직 해당 레시피는 책장에 없습니다.")