import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

st.set_page_config(layout='wide', page_title='Startup Funding Analysis', page_icon='💰')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')
    with col3:
        st.metric('Avg', str(avg_funding) + ' Cr')

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type', ['Total Money invested', 'Number of Deals'])
    temp_df = None
    if selected_option == 'Total Money invested':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    elif selected_option == 'Number of Deals':
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    # Create a datetime object for each row to use as x-axis (for better label management)
    temp_df['x_axis'] = pd.to_datetime(temp_df[['year', 'month']].assign(day=1))

    fig3, ax3 = plt.subplots(figsize=(10, 5))
    if selected_option == 'Total':
        ax3.plot(temp_df['x_axis'], temp_df['amount'])
    else:
        ax3.bar(temp_df['x_axis'], temp_df['amount'], width=20)

    # Format x-axis for better visibility
    ax3.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig3.autofmt_xdate(rotation=45)
    ax3.set_xlabel("Month-Year")

    st.pyplot(fig3)

    # sector pie => count + amount
    # top startups year wise and overall
    # top investors year wise and overall
    # funding heatmap


def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        verical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series, labels=verical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        stage_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Stage of Investments')
        fig2, ax2 = plt.subplots()
        ax2.pie(stage_series, labels=stage_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)
    with col4:
        city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader('City of Investments')
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series, labels=city_series.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    # similar investors


    print(df.info())
    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index, year_series.values)
    st.pyplot(fig2)


st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select StartUp', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)