import streamlit as st
import random
import time

st.set_page_config(
    page_title="娃娃大转盘",
    page_icon="🎰",
)

# List of dolls
dolls = ["南瓜小熊", "草莓小熊", "浴袍小熊", "玲娜贝儿一", "玲娜贝儿二", "玲娜贝儿三"]
num_dolls = len(dolls)
turns = 3

# List of firework emojis
firework_emojis = ["🔥", "💥", "🎆", "🎇"]
firework_end_emoji = ["✨"]

# text-styling
text_style = "style='font-size: 20px; text-align: center;'"

if 'selected_doll' not in st.session_state:
    st.session_state['selected_doll'] = ''
if 'firework_duplicates' not in st.session_state:
    st.session_state['firework_duplicates'] = 0

# Streamlit app
st.markdown("<h1 style='text-align: center;'>今晚枕边的娃娃是🎰</h1>", unsafe_allow_html=True)

fireplace_holder = st.empty()
placeholder = st.empty()
fireplace_holder_2 = st.empty()

spin_button = st.button("点击转动")

# Spin button
if spin_button:
    # Optional: Simulate spinning effect

    for i in range(num_dolls * turns):
        x1, x2 = random.sample(dolls, 2)
        x = x1 if x1 != st.session_state['selected_doll'] else x2
        st.session_state['selected_doll'] = x

        y = firework_emojis[i % len(firework_emojis)]
        st.session_state['firework_duplicates'] = len(x) + 2
        fireplace_holder.markdown(
            f"<p {text_style}>{y * st.session_state['firework_duplicates']}</p>",
            unsafe_allow_html=True)
        placeholder.markdown(f"<p {text_style}>{y} {x} {y}</p>", unsafe_allow_html=True)
        fireplace_holder_2.markdown(
            f"<p {text_style}>{y * st.session_state['firework_duplicates']}</p>",
            unsafe_allow_html=True)

        time_sleep = max(0.01, (i / (num_dolls * turns)) ** 3)  # Slow down the spinning effect
        time.sleep(time_sleep)

    # Display the final result
    fireplace_holder.markdown(
        f"<p {text_style}>{firework_end_emoji[0] * st.session_state['firework_duplicates']}</p>",
        unsafe_allow_html=True)
    placeholder.markdown(
        f"<p {text_style}>{firework_end_emoji[0]}{st.session_state['selected_doll']}{firework_end_emoji[0]}</p>",
        unsafe_allow_html=True)
    fireplace_holder_2.markdown(
        f"<p {text_style}>{firework_end_emoji[0] * st.session_state['firework_duplicates']}</p>",
        unsafe_allow_html=True)
