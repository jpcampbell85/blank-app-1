import streamlit as st

st.title("🎈 Happy Happy Joy Joy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.button('Hello There')

col1, col2 = st.columns(2)
col1.write('Column #1')
col2.write('Column #2')
