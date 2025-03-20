import streamlit as st
import random

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
    }
    .stButton>button {
        width: 100%;
        font-size: 20px;
        padding: 10px;
        border: 2px solid #fa3285;
        background-color: f4f4f4;
        color: blue;
        cursor: pointer;
        border-radius: 10px;
        transition: 0.3s ease-in-out;
        margin-top: 5px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #fa3285 !important;
        border-color: #fa3285 !important;
        color: blue !important;
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        transform: translateY(-5px);      
    }
    .score-card {
        background-color: #fa3285;
        border: 2px solid #fa3285;
        padding: 10px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: normal;
        font-family: 'Arial', sans-serif;
        color: white;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: 0.3s ease-in-out;
    }
    .score-card:hover {
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        transform: translateY(-5px);
        background-color: #fa3285 !important;
        border-color: #fa3285 !important;
        color: white !important;
            
    }
    </style>
""", unsafe_allow_html=True)

# Game Title
st.markdown("<h1 style='text-align: center; color: #fa3285; font-size: 40px; font-weight: bold; transform: scale(1.2); margin-top: 5px; margin-bottom: 10px; font-family: Arial, sans-serif;'>🪨📜✂️ Rock, Paper, Scissors</h1>", unsafe_allow_html=True)
st.write("### 🤖 Play against the Computer!")

# Initialize or reset scores
if 'user_score' not in st.session_state:
    st.session_state['user_score'] = 0
if 'computer_score' not in st.session_state:
    st.session_state['computer_score'] = 0

# Game Choices
choices = ["Rock ✊", "Paper 📜", "Scissors ✂️"]
user_choice = st.selectbox("👉 Select your move:", choices)

# Play Button
if st.button("🔥 Play Now!"):
    computer_choice = random.choice(choices)

    # Display Choices
    st.markdown(f"<h3>🧑‍💻 You chose: {user_choice}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3>🤖 Computer chose: {computer_choice}</h3>", unsafe_allow_html=True)

    # Determine Winner
    user_choice_clean = user_choice.split(" ")[0]  # Extract text without emoji
    computer_choice_clean = computer_choice.split(" ")[0]

    if user_choice_clean == computer_choice_clean:
        result = "😮 It's a tie!"
    elif (
        (user_choice_clean == "Rock" and computer_choice_clean == "Scissors") or
        (user_choice_clean == "Paper" and computer_choice_clean == "Rock") or
        (user_choice_clean == "Scissors" and computer_choice_clean == "Paper")
    ):
        result = "🎉 You win!"
        st.session_state['user_score'] += 1
    else:
        result = "😢 Computer wins!"
        st.session_state['computer_score'] += 1

    # Display Result
    st.markdown(f"<h2 style='text-align: center; color: #fa3285; font-size: 24px; font-weight: bold; transform: scale(1.2); margin-top: 20px; margin-bottom: 20px;'>{result}</h2>", unsafe_allow_html=True)

    # Display Score
    st.markdown(f"""
        <div class='score-card'>
        <h3>📊 Score</h3>
        <p>🧑‍💻 You: {st.session_state['user_score']}</p>
        <p>🤖 Computer: {st.session_state['computer_score']}</p>
        </div>
    """, unsafe_allow_html=True)

# Reset Button (Clears game state)
if st.button("🔄 Reset Game"):
    st.session_state['user_score'] = 0
    st.session_state['computer_score'] = 0
    st.rerun()  # ✅ Correct method to restart Streamlit app

# Footer
st.markdown("<h4 style='text-align: center; color: #fa3285; margin-top: 20px; margin-bottom: 20px; font-size: 20px; font-weight: bold; transform: scale(1.2);'>Made with ❤️ by Rahat Bano</h4>", unsafe_allow_html=True)
