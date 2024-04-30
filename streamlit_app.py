import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from neo_api_client import NeoAPI
"""
# Welcome to Streamlit!

"""
consumer_key = '3GM5pYdQEQfx_pY9UQTgGcbL3zoa'  
secretKey = 'rtwtfdq0vDdFLpGO_fCOPE7EhNwa' 

mobileNumber = '+918509936057' 
login_password = 'Trina124#'  
def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_close(message):
    print(message)
    
def on_open(message):
    print(message)

client = NeoAPI(consumer_key=consumer_key, consumer_secret=secretKey, environment='prod', on_message=on_message, on_error=on_error, on_close=None, on_open=None)
#client = NeoAPI(consumer_key=consumer_key, consumer_secret=secretKey, environment='uat', access_token=None, neo_fin_key=None)

client.login(mobilenumber=mobileNumber, password=login_password)

client.session_2fa(OTP="112233")

print(client.holdings())
num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
