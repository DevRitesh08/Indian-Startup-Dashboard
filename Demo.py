import streamlit as st
import pandas as pd
import time

# use streamlit run Demo.py to run the app

st.title("Startup Dashboard")
st.header("Welcome to the Startup Dashboard")
st.subheader("Your one-stop solution for startup insights")
st.write("This dashboard provides insights into various aspects of startups, including funding, growth metrics, and market trends.")

st.markdown("""
### Features :
- **Interactive Visualizations**: Explore data through dynamic charts and graphs.
- **Real-time Data Updates**: Stay informed with the latest information.
- **Customizable Reports**: Generate reports tailored to your needs.
- **User-friendly Interface**: Navigate easily with an intuitive design.
""")
st.code("""
def sq(x) : 
    return x*x
print(sq(5))
""")

st.latex(r''' e^{i\pi} + 1 = 0 ''')
df = pd.DataFrame({
    'Students': ['Ritesh', 'Shantanu', 'Sanjay', 'Ankit'],
    'Column B': [70, 66, 87, 58]
})
st.dataframe(df)

st.metric(label="Total Startups", value="1,234", delta="+5%")
st.metric(label="Total Funding", value="$567M", delta="+10%")
st.metric(label="Active Users", value="8,910", delta="-2%")

st.json({
    'Students': ['Ritesh', 'Shantanu', 'Sanjay', 'Ankit'],
    'Column B': [70, 66, 87, 58]
})

st.image('img.png')

st.video('https://www.youtube.com/watch?v=Z_ikDlimN6A')

st.sidebar.title("Navigation")
st.sidebar.markdown("""
- Home
- Insights
- Reports
- Settings
""")

col1 , col2, col3 = st.columns(3)
with col1:
    st.header("Startups")
    st.write("Explore various startups and their growth metrics.")
    st.button("Explore Startups")
with col2:
    st.header("Funding")
    st.write("Get insights into funding rounds and investors.")
    st.button("View Funding")
with col3:
    st.header("Market Trends")
    st.write("Stay updated with the latest market trends.")
    st.button("See Trends")

st.success("Dashboard Loaded Successfully!")
st.error("Error loading some data.")
st.warning("Data for some startups is outdated.")
st.info("New features coming soon!")

bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    bar.progress(i + 1)

email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type='password')
age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
date = st.date_input("Select a date")
color = st.color_picker("Pick a color")
gender = st.selectbox("Select your Gender", ["MALE", "FEMALE", "OTHER"])
hobbies = st.multiselect("Select your Hobbies", ["Reading", "Traveling", "Gaming", "Cooking", "Sports"])
submit = st.button("Submit")


# login Page
st.title("Login Page")
email = st.text_input("Email")
password = st.text_input("Password", type='password')
btn = st.button("Login")
if btn:
    if email == "riteshswami4567@gmail;.com" and password == "12345":
        st.success("Logged In Successfully")
    else:
        st.error("Invalid Credentials")


file = st.file_uploader("Upload a file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.line_chart(df)
    st.bar_chart(df)