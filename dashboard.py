import streamlit as st
from app_model.incidents import get_all_cyber_incidents
from app_model.db import get_db_connection


conn = get_db_connection()

st.header("Home Page")
st.write("Welcome to the Home Page of the Application")

st.set_page_config(
    page_title = "Home page" ,
    page_icon = "🏠" ,
    layout = "wide"
)
 

data = get_all_cyber_incidents(conn)

with st.sidebar:
   st.header("Cyber Severity Overview")
   severity_ = st.selectbox("Severity", data["severity"].unique())

filtered_data = data[data["severity"] == severity_] 

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(filtered_data["category"].value_counts())
    st.dataframe(filtered_data)

with col2:
   st.subheader("Filtered Cyber Incidents Data")
   st.line_chart(filtered_data, x= 'timestamp', y='incident_id')
st.dataframe(filtered_data)
   

 
st.set_page_config(layout='wide')
st.title( 'Dashboard' )
 
with st.sidebar:
    year = st.selectbox('Year', [2025, 2019, 20201])
 
col1,col2 = st.columns(2)
 
with col1:
    st.subheader('1st Chart')
    st.bar_chart(data, x ='status', y='incident_id')
 
with col2:
    st.subheader('2nd Chart')
    st.line_chart(data, x='timestamp', y='category')
