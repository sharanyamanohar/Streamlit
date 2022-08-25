import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to my dashboard")
st.header("This is header")
st.subheader("This is subheader")
st.markdown("This is a markdown")
st.text("This is text")

code_snippet=''' hello streamlit this is my first program'''
st.code(code_snippet)

button_click=st.button('Show code for the current page')
print(button_click)# on terminal all the bolean value will execute
st.text(button_click)#on local host it will execute

if button_click == True:
    st.code(code_snippet)


#import dataset
st.title('Iris Dashboard')
df=pd.read_csv('data/iris.csv')
st.dataframe(df)

df_geoloc=pd.DataFrame(
    np.random.randn(50,2) / [50,50] + [37.76,-122.4],
    columns=['lat','lon'])

st.map(df_geoloc)
