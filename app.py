# =========================================================
# 🦋 Butterfly Catching Garden
# Interactive Nature Mini Game
# Built with Python & Streamlit
# =========================================================

# ---------------- IMPORT LIBRARIES ----------------
import streamlit as st
import random
import time

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Butterfly Catching Garden 🦋",
    page_icon="🦋",
    layout="wide"
)

# =========================================================
# CUSTOM CSS STYLING
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to bottom right, #d8f3dc, #e0c3fc, #cfe8ff);
    color: #2d3748;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #bbf7d0, #ddd6fe);
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #7c3aed;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #4b5563;
    margin-bottom: 30px;
}

/* Glass Card */
.card {
    background: rgba(255,255,255,0.45);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Butterfly */
.butterfly {
    text-align: center;
    font-size: 120px;
    animation: float 3s ease-in-out infinite;
}

/* Floating Animation */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-15px);}
    100% {transform: translateY(0px);}
}

/* Buttons */
.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(to right, #ec4899, #8b5cf6);
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
}

/* Score Box */
.score-box {
    background: rgba(255,255,255,0.55);
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align: center;
    color: #6b7280;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "score" not in st.session_state:
    st.session_state.score = 0

if "high_score" not in st.session_state:
    st.session_state.high_score = 0

if "combo" not in st.session_state:
    st.session_state.combo = 0

if "butterfly" not in st.session_state:
    st.session_state.butterfly = "🦋"

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🦋 Butterfly Garden")

    st.markdown("---")

    mode = st.radio(
        "🌸 Navigation",
        [
            "🏠 Home",
            "🎮 Play Game",
            "🏆 Scores",
            "📖 About"
        ]
    )

    st.markdown("---")

    difficulty = st.selectbox(
        "🎯 Difficulty",
        [
            "Easy 🌼",
            "Medium 🌿",
            "Hard 🌪️"
        ]
    )

    st.markdown("---")

    dark_mode = st.toggle("🌙 Dark Mode")

# =========================================================
# DARK MODE
# =========================================================

if dark_mode:

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(to right, #111827, #1f2937);
        color: white;
    }

    .card {
        background: rgba(255,255,255,0.08);
        color: white;
    }

    .subtitle {
        color: #d1d5db;
    }

    </style>
    """, unsafe_allow_html=True)

# =========================================================
# HOME PAGE
# =========================================================

if mode == "🏠 Home":

    st.markdown(
        '<div class="main-title">🦋 Butterfly Catching Garden</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Relax, explore nature, and catch magical butterflies 🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h2>🌿 Welcome to the Garden</h2>

        <p>
        Catch beautiful butterflies flying through the magical garden.
        Earn points, build combos, and enjoy a relaxing nature experience.
        </p>

        <p>
        Golden butterflies 🌟 give bonus points!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Floating Butterflies
    butterflies = ["🦋", "💜🦋", "🌸🦋", "✨🦋"]

    cols = st.columns(4)

    for i, col in enumerate(cols):

        with col:

            st.markdown(
                f'<div class="butterfly">{random.choice(butterflies)}</div>',
                unsafe_allow_html=True
            )

    st.success("🌼 Enjoy the peaceful garden atmosphere")

# =========================================================
# GAME PAGE
# =========================================================

elif mode == "🎮 Play Game":

    st.markdown(
        '<div class="main-title">🎮 Catch Butterflies</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
    Click the butterflies to catch them and increase your score!
    </div>
    """, unsafe_allow_html=True)

    # Difficulty Settings
    if difficulty == "Easy 🌼":
        timer = 30

    elif difficulty == "Medium 🌿":
        timer = 20

    else:
        timer = 15

    # Score Display
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏆 Score", st.session_state.score)

    with col2:
        st.metric("🔥 Combo", st.session_state.combo)

    with col3:
        st.metric("🌟 High Score", st.session_state.high_score)

    st.markdown("---")

    # Random Butterfly
    butterfly_options = [
        "🦋",
        "💜🦋",
        "🌸🦋",
        "✨🦋",
        "🌟🦋"
    ]

    butterfly = random.choice(butterfly_options)

    st.markdown(
        f'<div class="butterfly">{butterfly}</div>',
        unsafe_allow_html=True
    )

    # Catch Button
    if st.button("🫴 Catch Butterfly"):

        # Golden Butterfly Bonus
        if butterfly == "🌟🦋":

            st.session_state.score += 10

            st.success("🌟 Golden Butterfly! Bonus +10 Points!")

            st.balloons()

        else:

            st.session_state.score += 5

            st.success("✨ Butterfly Caught Successfully!")

        # Combo Increase
        st.session_state.combo += 1

        # High Score Update
        if st.session_state.score > st.session_state.high_score:
            st.session_state.high_score = st.session_state.score

    # Progress Bar
    st.markdown("### 🌸 Garden Energy")
    st.progress(min(st.session_state.score, 100))

    # Nature Quotes
    quotes = [

        "🌿 Nature always brings peace to the soul.",
        "🦋 Butterflies are nature’s flying flowers.",
        "☀️ Happiness blooms in gardens.",
        "🌸 Relax and enjoy the beauty around you."
    ]

    st.info(random.choice(quotes))

    # Reset Button
    if st.button("🔄 Reset Game"):

        st.session_state.score = 0
        st.session_state.combo = 0

        st.success("🌱 Garden has been refreshed!")

# =========================================================
# SCORE PAGE
# =========================================================

elif mode == "🏆 Scores":

    st.markdown(
        '<div class="main-title">🏆 Garden Scores</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="score-box">
        🦋 Current Score: {st.session_state.score}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="score-box">
        🌟 Highest Score: {st.session_state.high_score}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="score-box">
        🔥 Current Combo: {st.session_state.combo}
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.high_score >= 50:

        st.balloons()

        st.success("🎉 Amazing! You are a Butterfly Master!")

# =========================================================
# ABOUT PAGE
# =========================================================

elif mode == "📖 About":

    st.markdown(
        '<div class="main-title">📖 About This Game</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h2>🦋 Butterfly Catching Garden</h2>

    <p>
    This relaxing mini-game was developed using:
    </p>

    <ul>
        <li>Python 🐍</li>
        <li>Streamlit ⚡</li>
        <li>Custom CSS 🎨</li>
    </ul>

    <p>
    The goal is to create a calming and visually beautiful
    digital garden experience.
    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
🌸 Made with Python & Streamlit | Relaxing Nature Mini Game
</div>
""", unsafe_allow_html=True)
