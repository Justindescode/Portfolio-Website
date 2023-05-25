import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_8796.jpg")
with col2:
    st.title("Justin Darryl")
    content = """
    A self-motivated Full Stack Developer with experience in hands-on experience with designing, 
    developing, and implementing applications and solutions using a range of technologies and programming languages. 
    I'm eager to learn new technologies, and computer systems and seeking to Pursue a highly rewarding career in a 
    healthy work environment utilizing my skills and knowledge.
    """
    st.info(content)

