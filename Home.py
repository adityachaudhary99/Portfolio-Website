import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Home")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Aditya Chaudhary")
    content = """
    Highly motivated and enthusiastic beginner aspiring Data Scientist with a strong passion for leveraging data to drive insights. 

    Limited experience but eager to learn and develop skills in data analysis, machine learning, and programming. Committed to continuous self-improvement and staying updated with industry advancements.

    Looking to connect with experienced professionals and mentors to learn from their expertise and contribute to impactful data-driven projects. Let's connect and embark on the journey of becoming successful Data Scientists together.
    """
    st.info(content)

content2 = """
           Below you can find some of the apps I have built in Python. Feel free to contact me!
           """

st.info(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")