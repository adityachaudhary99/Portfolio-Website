import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.markdown(f"<h1 style='text-align: center;'> Home </h1>", unsafe_allow_html=True)

st.markdown("***")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpeg")

with col2:
    st.markdown(f"<h1 style='text-align: center;'> Aditya Chaudhary </h1>", unsafe_allow_html=True)

    st.text("")

    content = """
    Highly motivated and enthusiastic beginner aspiring Data Scientist with \
    a strong passion for leveraging data to drive insights. 
    <br>
    Limited experience but eager to learn and develop skills in data analysis, machine learning, \
    and programming. Committed to continuous self-improvement and staying updated with industry advancements.
    <br>
    Looking to connect with experienced professionals and mentors to learn from their expertise and \
    contribute to impactful data-driven projects. Let's connect and embark on the journey of becoming successful Data Scientists together.
    """
    st.write(f"<p style='text-align: center;'> {content} </p>", unsafe_allow_html=True)

    st.text("")

    col3, col4, col5, col6, col7, col8, col9 = st.columns(7)
    with col6:
        connect = st.button(label="Connect")
        if connect:
            st.markdown(
                """<a style='display: block; text-align: center;' href="https://www.linkedin.com/in/adityachaudhary99/">
                LinkedIn</a>""", unsafe_allow_html=True)

            st.text("")

            st.markdown(
                """<a style='display: block; text-align: center;' href="https://github.com/adityaacodes">GitHub
                </a>""", unsafe_allow_html=True)

            st.markdown(
                """<a style='display: block; text-align: center; font: 20;' href="https://twitter.com/adityaacodes">Twitter
                </a>""", unsafe_allow_html=True)


st.markdown("***")
content2 = """
           Below you can find some of the apps I have built in Python. Feel free to contact me!
           """
st.markdown(f"<h2 style='text-align: center;'> {content2} </h2>", unsafe_allow_html=True)
st.markdown("***")

col10, empty_col, col11 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')

with col10:
    for index, row in df[:6].iterrows():
        st.markdown(f"<h1 style='text-align: center;'> {row['title']} </h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'> {row['description']}</p>", unsafe_allow_html=True)
        st.image('images/' + row['image'])
        st.markdown(
            f"""<a style='display: block; text-align: center;' href="{row['url']}">Source Code
                </a>""", unsafe_allow_html=True)
        st.markdown("***")

with col11:
    for index, row in df[6:12].iterrows():
        st.markdown(f"<h1 style='text-align: center;'> {row['title']} </h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'> {row['description']}</p>", unsafe_allow_html=True)
        st.image('images/' + row['image'])
        st.markdown(
            f"""<a style='display: block; text-align: center;' href="{row['url']}">Source Code
                </a>""", unsafe_allow_html=True)
        st.markdown("***")


st.markdown("***")
for index, row in df[12:].iterrows():
    st.markdown(f"<h1 style='text-align: center;'> {row['title']} </h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'> {row['description']}</p>", unsafe_allow_html=True)
    st.image('images/' + row['image'])
    st.markdown(
        f"""<a style='display: block; text-align: center;' href="{row['url']}">Source Code
        </a>""", unsafe_allow_html=True)
    st.markdown("***")

