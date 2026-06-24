import streamlit as st

# 1. 메뉴 목록을 출력하는 함수 정의
def show_menu():
    st.title("👨‍🍳 AI 주방 로봇 셰프")
    st.subheader("오늘의 메뉴를 선택하세요")
    
    # 메뉴 리스트 예시
    menu = ["김치찌개", "제육볶음", "계란말이", "비빔밥"]
    
    # 메뉴를 화면에 뿌려줌
    for item in menu:
        st.write(f"- {item}")

# 2. 실행 시 바로 메뉴를 보여주는 코드
if __name__ == "__main__":
    show_menu()