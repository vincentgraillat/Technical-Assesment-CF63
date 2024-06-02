import streamlit as st
import pandas as pd
import math 
import numpy as np
import altair as alt

st.set_page_config(
    page_title="Scouting Assistant - La Liga 2015-2016",
    page_icon="⚽",
)

st.write("# Welcome to your Scouting Assistant!")

st.sidebar.success("Select an option above.")

st.markdown(
    """
    This app's purpose is to help you assess the performances of all players that played more than 500 minutes in the **2015-2016 La Liga's season**.
    ### What can you visualize on this app?
    - **Player's stats**: Check the stats of each player in the season and how they have performed relatively to the rest of the players.
    - **Player's comparison**: Compare the performance's quantiles of two players.
    - **Bests players per position**: Check the best players per position.
    
    This app has been created for a technical assessment for a Data Scientist Internship position.
    
    All data comes from StatsBomb open access data: https://github.com/statsbomb/open-data.
"""
)




