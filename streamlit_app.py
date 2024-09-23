import streamlit as st

st.title("🎈 Whatever Goes Here")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.button('Testing 1-2-3')

col1, col2, col3 = st.columns(3)
col1.write(':cancer:')
col2.write(':scorpio')
col3.write(':pisces:')
