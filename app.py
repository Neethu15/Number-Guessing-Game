import random
import streamlit as st

# Title
st.title("🎯 Number Guessing Game")

# Initialize game state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.won = False

max_attempts = 5

# User input
guess = st.number_input("Enter your guess (1–10):", min_value=1, max_value=10, step=1)

# Button to submit guess
if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess == st.session_state.secret_number:
        st.success("🎉 Correct! You guessed the number!")
        st.image("Happy.jpg", width=150)  # congratulatory smiley
        st.session_state.game_over = True
        st.session_state.won = True
    elif guess < st.session_state.secret_number:
        st.info("Too low! 📉 Try again.")
    else:
        st.info("Too high! 📈 Try again.")

    # Check if game over after 5 attempts
    if st.session_state.attempts >= max_attempts and not st.session_state.won:
        st.error(f"❌ Game Over! The number was {st.session_state.secret_number}.")
        st.image("Angry.jpg", width=150)  # angry smiley
        st.session_state.game_over = True

# Reset game button
if st.button("Restart Game"):
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.won = False
    st.experimental_rerun()
