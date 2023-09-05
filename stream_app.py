# Day 10
import streamlit as st
import pandas as pd
import numpy as np

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green')
)

st.write('Your favorite color is ', option)
