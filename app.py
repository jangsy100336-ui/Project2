import streamlit as st
import random

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="가위바위보", layout="centered")

# -----------------------------
# 스타일
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
    st.session_state.result = None

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if "com_choice" not in st.session_state:
    st.session_state.com_choice = ""

if "winner" not in st.session_state:
    st.session_state.winner = None


# -----------------------------
# 승패 판정
# -----------------------------
def judge(u, c):
    if u == c:
        return "draw"
    if (u == "가위" and c == "보") or (u == "바위" and c == "가위") or (u == "보" and c == "바위"):
        return "win"
    return "lose"


# -----------------------------
# 메인 화면
# -----------------------------
if st.session_state.page == "home":

    st.markdown("<h1 style='text-align:center;'>🎮 가위바위보</h1>", unsafe_allow_html=True)

    if st.button("게임 시작", use_container_width=True):
        st.session_state.page = "game"
        st.session_state.user_score = 0
        st.session_state.com_score = 0
        st.rerun()


# -----------------------------
# 게임 화면
# -----------------------------
else:

    st.markdown(
        f"<h3 style='text-align:center;'>사용자 {st.session_state.user_score} : {st.session_state.com_score} 컴퓨터</h3>",
        unsafe_allow_html=True
    )

    # -------------------------
    # 승리 조건 체크
    # -------------------------
    if st.session_state.user_score >= 5 or st.session_state.com_score >= 5:
        st.session_state.winner = "user" if st.session_state.user_score >= 5 else "com"

        if st.session_state.winner == "user":
            st.success("🏆 사용자 승리!")
        else:
            st.error("🏆 컴퓨터 승리!")

        st.session_state.user_score = 0
        st.session_state.com_score = 0
        st.session_state.page = "home"
        st.rerun()

    # -------------------------
    # 결과 표시
    # -------------------------
    if st.session_state.result is not None:

        st.write(f"당신: {st.session_state.user_choice}")
        st.write(f"컴퓨터: {st.session_state.com_choice}")

        if st.session_state.result == "win":
            st.success("승리!")
        elif st.session_state.result == "lose":
            st.error("패배!")
        else:
            st.info("무승부")

        # 자동 초기화 (sleep 없이)
        st.session_state.result = None
        st.rerun()


    # -------------------------
    # 선택 버튼
    # -------------------------
    col1, col2, col3 = st.columns(3)

    def play(user):
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

    with col1:
        if st.button("가위"):
            play("가위")

    with col2:
        if st.button("바위"):
            play("바위")

    with col3:
        if st.button("보"):
            play("보")

    # -------------------------
    # 종료 버튼
    # -------------------------
    if st.button("종료"):
        st.session_state.page = "home"
        st.session_state.user_score = 0
        st.session_state.com_score = 0
        st.session_state.result = None
        st.rerun()
