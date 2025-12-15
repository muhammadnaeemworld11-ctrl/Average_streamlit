import streamlit as st 
st.title("SIMPLE AVERAGE CALCULATOR ")

num1 = st.number_input("Enter first number to get average: ")
num2 = st.number_input("Enter second number to get average: ")
st.success((num1 + num2)/2)