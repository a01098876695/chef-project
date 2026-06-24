import streamlit as st
import json

# 페이지 설정
st.set_page_config(page_title="AI 주방 로봇 셰프", page_icon="🤖")

# 1. 레시피 데이터 불러오기
try:
    with open('recipes.json', 'r', encoding='utf-8') as f:
        recipe_db = json.load(f)
except:
    recipe_db = {}

# 2. 메인 화면 구성
st.title("🤖 AI 주방 로봇 셰프")
st.write("요리 이름을 검색하면 조리법을 알려드립니다!")

# 3. 검색창 생성 (사이드바 대신 메인 화면에 배치)
# 사용자가 입력을 마치고 엔터를 누르면 그 값이 search_query에 담깁니다.
search_query = st.text_input("🔍 어떤 요리를 만들어 볼까요?", placeholder="예: 제육볶음")

# 4. 검색 결과 처리
if search_query:
    # 검색어가 레시피 DB에 존재하는지 확인
    if search_query in recipe_db:
        data = recipe_db[search_query]
        
        st.divider()  # 구분선
        st.header(f"🍳 {search_query} 조리법")
        
        # 재료 출력
        st.subheader("🛒 필수 재료")
        st.write(", ".join(data['ingredients']))
        
        # 조리 순서 출력
        st.subheader("👨‍🍳 조리 순서")
        for i, step in enumerate(data['steps'], 1):
            st.write(f"{i}. {step}")
            
        st.success(f"🤖 {search_query} 조리를 시작해 보세요!")
    else:
        # DB에 없는 메뉴일 경우
        st.warning(f"죄송합니다. '{search_query}' 레시피를 찾을 수 없습니다. 메뉴 이름을 다시 확인해 주세요.")
else:
    # 검색 전 홈 화면 메시지
    st.info("위 검색창에 요리 이름을 입력해 주세요.")