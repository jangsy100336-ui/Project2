import streamlit as st
import random
import time

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="가위바위보 게임", layout="centered")

# -----------------------------
# 스타일 (간단 UI)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1b3a;
    color: white;
}

h1, h2, h3, p, div {
    color: white !important;
}

div.stButton > button {
    background-color: white;
    color: black;
    border-radius: 10px;
    padding: 0.6em 1.5em;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #d9e6ff;
    color: black;
}

/* 오른쪽 아래 종료 버튼 */
div[data-testid="column"] {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 상태 초기화
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "com_score" not in st.session_state:
    st.session_state.com_score = 0

if "result" not in st.session_state:
    st.session_state.result = ""

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if "com_choice" not in st.session_state:
    st.session_state.com_choice = ""

if "show_winner" not in st.session_state:
    st.session_state.show_winner = False

# -----------------------------
# 함수: 승패 판정
# -----------------------------
def judge(user, com):
    if user == com:
        return "draw"
    elif (
        (user == "가위" and com == "보") or
        (user == "바위" and com == "가위") or
        (user == "보" and com == "바위")
    ):
        return "win"
    else:
        return "lose"

# -----------------------------
# 메인 화면
# -----------------------------
if st.session_state.page == "home":

    st.markdown("<h1 style='text-align:center;'>🎮 가위바위보 게임</h1>", unsafe_allow_html=True)

    if st.button("게임 시작", use_container_width=True):
        st.session_state.page = "game"
        st.rerun()

# -----------------------------
# 게임 화면
# -----------------------------
else:

    # 점수판
    st.markdown(
        f"<h3 style='text-align:center;'>사용자 {st.session_state.user_score} : {st.session_state.com_score} 컴퓨터</h3>",
        unsafe_allow_html=True
    )

    st.write("---")

    # 우승 체크
    if st.session_state.user_score >= 5 or st.session_state.com_score >= 5:
        st.session_state.show_winner = True

    # 우승 화면
    if st.session_state.show_winner:
        if st.session_state.user_score >= 5:
            st.markdown("<h1 style='text-align:center;'>🏆 사용자 승리!</h1>", unsafe_allow_html=True)
        else:
            st.markdown("<h1 style='text-align:center;'>🏆 컴퓨터 승리!</h1>", unsafe_allow_html=True)

        time.sleep(3)

        # 초기화 후 메인으로
        st.session_state.user_score = 0
        st.session_state.com_score = 0
        st.session_state.page = "home"
        st.session_state.show_winner = False
        st.rerun()

    # 결과 표시
    if st.session_state.result:
        st.markdown(f"### 당신: {st.session_state.user_choice}")
        st.markdown(f"### 컴퓨터: {st.session_state.com_choice}")

        if st.session_state.result == "win":
            st.success("당신이 이겼습니다!")
        elif st.session_state.result == "lose":
            st.error("컴퓨터가 이겼습니다!")
        else:
            st.info("무승부!")

        time.sleep(2)

        st.session_state.result = ""
        st.rerun()

    # 선택 버튼
    col1, col2, col3 = st.columns(3)

    if col1.button("가위"):
        user = "가위"
        com = random.choice(["가위", "바위", "보"])

        st.session_state.user_choice = user
        st.session_state.com_choice = com

        result = judge(user, com)
        st.session_state.result = result

        if result == "win":
            st.session_state.user_score += 1
        elif result == "lose":
            st.session_state.com_score += 1

        st.rerun()

    if col2.button("바위"):
        user = "바위"
        com = random.choice(["가위", "바위", "보"])

        st.session_state.user_choice = user
        st.session_state.com_choice = com

        result = judge(user, com)
        st.session_state.result = result

        if result == "win":
            st.session_state.user_score += 1
        elif result == "lose":
            st.session_state.com_score += 1

        st.rerun()

    if col3.button("보"):
        user = "보"
        com = random.choice(["가위", "바위", "보"])

        st.session_state.user_choice = user
        st.session_state.com_choice = com

        result = judge(user, com)
        st.session_state.result = result

        if result == "win":
            st.session_state.user_score += 1
        elif result == "lose":
            st.session_state.com_score += 1

        st.rerun()

    st.write("---")

    # 종료 버튼 (오른쪽 아래)
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        if st.button("종료"):
            st.session_state.user_score = 0
            st.session_state.com_score = 0
            st.session_state.page = "home"
            st.session_state.result = ""
            st.rerun()
