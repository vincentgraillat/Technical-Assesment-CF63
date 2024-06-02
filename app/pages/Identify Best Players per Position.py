import streamlit as st
import pandas as pd
import math 
import numpy as np
import altair as alt

def plot_bars_altair(df, title):
    chart = alt.Chart(df).mark_bar(size=60).encode(  
        x=alt.X('Stat', sort=None, title=None, axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('Value', title=None, scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(
            values=[30, 50, 70, 90],
            labelExpr='datum.value == 90 ? "ELITE" : datum.value == 70 ? "GREAT" : datum.value == 50 ? "MEDIUM" : datum.value == 30 ? "WEAK" : datum.value'
        )),  
        color=alt.Color('Stat', legend=None)
    ).properties(
        title=title,
        width=500,
        height=500
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16,
        anchor='middle'
    )
    
    st.altair_chart(chart, use_container_width=True)

st.set_page_config(page_title="Position Analysis", layout="wide")

positions = ['Goalkeeper', 'Left/Right Back', 'Center Back', 'Defensive Midfielder', 'Central/Attacking Midfielder', 'Left/Right Winger', 'Striker']

df_stats_general = pd.read_csv('data_app/stats_final.csv')
options = [''] + positions	
position_name = st.selectbox('Select a position', options)

if position_name:
    if position_name == 'Goalkeeper':
        df_stats = pd.read_csv('data_app/stats_ranking_gk.csv')
        stats_graph_total = ['Total Saves', 'Total Goals Conceded', 'Total Penalties Saved','Total Penalties Scored Against', 'Total Punches','Total Keeper Sweeper', 
                                 'Total Smothers', 'Total Collected', 'Goals Conceded Rate', 'Penalties Saved Rate']
        stats_graph_90 = ['Saves per 90 min', 'Goals Conceded per 90 min', 'Goals Conceded Rate', 'Penalties Saved Rate', 'Punch per 90 min', 
                                 'Keeper Sweeper per 90 min','Smothers per 90 min', 'Collected per 90 min']
        weights = { 
        'Total Saves': 2, 'Total Goals Conceded': 3, 'Total Penalties Saved': 2, 'Total Penalties Scored Against': 2, 'Total Punches': 1, 'Total Keeper Sweeper': 1,
        'Total Smothers': 1, 'Total Collected': 1, 'Saves per 90 min': 2, 'Goals Conceded per 90 min': 3, 'Goals Conceded Rate': 2, 'Penalties Saved Rate': 2,
        'Punch per 90 min': 1, 'Keeper Sweeper per 90 min': 1, 'Smothers per 90 min': 1, 'Collected per 90 min': 1}
    elif position_name == 'Left/Right Back':
        df_stats = pd.read_csv('data_app/stats_ranking_lb_rb.csv')
        stats_graph_90 = ['Clearances per 90 min', 'Blocks per 90 min', 'Interceptions per 90 min', 'Ball Recoveries per 90 min', 'Dribbled Past per 90 min', 'Duels Won per 90 min', 'Duel Won Rate', 'Crosses per 90 min']
        stats_graph_total = ['Total Clearances', 'Total Blocks', 'Total Interceptions', 'Total Ball Recoveries', 'Total Dribbled Past', 'Total Duels Won', 'Duel Won Rate', 'Total Crosses']
        weights = {
        'Total Completed Passes': 1, 'Total Long Passes': 1, 'Total Medium Passes': 1,
        'Total Short Passes': 1, 'Total Goal Assists': 1.5, 'Total Passes': 1,
        'Total Shot Assists': 1.5, 'Total Crosses': 2, 'Completed Passes per 90 min': 1,
        'Long Passes per 90 min': 1, 'Medium Passes per 90 min': 1, 'Goal Assists per 90 min': 1.5,
        'Short Passes per 90 min': 1, 'Shot Assists per 90 min': 1.5, 'Crosses per 90 min': 2,
        'Pass Success Rate': 1, 'Total Ball Receipts': 1, 'Total Lost Balls': 1,
        'Ball Receipts per 90 min': 1, 'Lost Balls per 90 min': 1, 'Total Own Goals': 1,
        'Total Clearances': 1.5, 'Total Left Foot Clearances': 0.5, 'Total Right Foot Clearances': 0.5,
        'Total Head Clearances': 0.5, 'Total Other Clearances': 0.5, 'Total Aerial Duels Won': 1.5,
        'Clearances per 90 min': 1.5, 'Aerial Duels Won per 90 min': 1.5, 'Total Interceptions': 1.5,
        'Interceptions per 90 min': 1.5, 'Total Fouls Won': 1, 'Total Penalties Won': 1,
        'Fouls Won per 90 min': 1, 'Total Fouls Committed': 1, 'Total Yellow Cards': 1,
        'Total Red Cards': 2, 'Total Penalties Conceded': 2, 'Fouls Committed per 90 min': 1,
        'Total Ball Recoveries': 1.5, 'Ball Recoveries per 90 min': 1.5, 'Total Blocks': 1.5,
        'Blocks per 90 min': 1.5, 'Total Completed Dribbles': 0.5, 'Dribble Success Rate': 0.5,
        'Completed Dribbles per 90 min': 0.5, 'Total Dribbled Past': 2, 'Dribbled Past per 90 min': 2,
        'Total Carries': 1.5, 'Mean Distance Carries': 1.5, 'Carries per 90 min': 1.5,
        'Total Duels': 1.5, 'Total Duels Won': 1.5, 'Duel Won Rate': 1.5, 'Duels Won per 90 min': 1.5,
        'Total Shots': 0.5, 'Total Goals': 0.5, 'Total Shots Saved': 0.5, 'Total Shots Blocked': 0.5,
        'Total Shots On the Post': 0.5, 'Total Shots Off Target': 0.5, 'Total Shots On Target': 0.5,
        'Goals per 90 min': 0.5, 'Shots per 90 min': 0.5, 'Shots on Target per 90 min': 0.5,
        'Shots On Target Rate': 0.5, 'Goal Conversion Rate': 0.5} 
    elif position_name == 'Center Back':
        df_stats = pd.read_csv('data_app/stats_ranking_cb.csv')
        stats_graph_90 = ['Clearances per 90 min', 'Blocks per 90 min', 'Interceptions per 90 min', 'Ball Recoveries per 90 min', 'Dribbled Past per 90 min', 'Duels Won per 90 min', 'Duel Won Rate', 'Long Passes per 90 min']
        stats_graph_total = ['Total Clearances', 'Total Blocks', 'Total Interceptions', 'Total Ball Recoveries', 'Total Dribbled Past', 'Total Duels Won', 'Duel Won Rate', 'Total Long Passes']
        weights = {
        'Total Completed Passes': 1, 'Total Long Passes': 2, 'Total Medium Passes': 1,
        'Total Short Passes': 1, 'Total Goal Assists': 0.5, 'Total Passes': 1,
        'Total Shot Assists': 0.5, 'Total Crosses':0.5, 'Completed Passes per 90 min': 1,
        'Long Passes per 90 min': 2, 'Medium Passes per 90 min': 1, 'Goal Assists per 90 min': 0.5,
        'Short Passes per 90 min': 1, 'Shot Assists per 90 min': 0.5, 'Crosses per 90 min': 0.5,
        'Pass Success Rate': 1, 'Total Ball Receipts': 1, 'Total Lost Balls': 1,
        'Ball Receipts per 90 min': 1, 'Lost Balls per 90 min': 1, 'Total Own Goals': 1,
        'Total Clearances': 2, 'Total Left Foot Clearances': 0.5, 'Total Right Foot Clearances': 0.5,
        'Total Head Clearances': 0.5, 'Total Other Clearances': 0.5, 'Total Aerial Duels Won': 2,
        'Clearances per 90 min': 2, 'Aerial Duels Won per 90 min': 2, 'Total Interceptions': 2,
        'Interceptions per 90 min': 2, 'Total Fouls Won': 1, 'Total Penalties Won': 1,
        'Fouls Won per 90 min': 1, 'Total Fouls Committed': 1, 'Total Yellow Cards': 1,
        'Total Red Cards': 2, 'Total Penalties Conceded': 2, 'Fouls Committed per 90 min': 1,
        'Total Ball Recoveries': 2, 'Ball Recoveries per 90 min': 2, 'Total Blocks': 2,
        'Blocks per 90 min': 2, 'Total Completed Dribbles': 0.5, 'Dribble Success Rate': 0.5,
        'Completed Dribbles per 90 min': 0.5, 'Total Dribbled Past': 2, 'Dribbled Past per 90 min': 2,
        'Total Carries': 1, 'Mean Distance Carries': 1, 'Carries per 90 min': 1,
        'Total Duels': 2, 'Total Duels Won': 2, 'Duel Won Rate': 2, 'Duels Won per 90 min': 2,
        'Total Shots': 0.5, 'Total Goals': 0.5, 'Total Shots Saved': 0.5, 'Total Shots Blocked': 0.5,
        'Total Shots On the Post': 0.5, 'Total Shots Off Target': 0.5, 'Total Shots On Target': 0.5,
        'Goals per 90 min': 0.5, 'Shots per 90 min': 0.5, 'Shots on Target per 90 min': 0.5,
        'Shots On Target Rate': 0.5, 'Goal Conversion Rate': 0.5}
    elif position_name == 'Defensive Midfielder':
        df_stats = pd.read_csv('data_app/stats_ranking_dm.csv')
        stats_graph_90 = ['Completed Passes per 90 min', 'Pass Success Rate', 'Carries per 90 min', 'Lost Balls per 90 min', 'Duel Won Rate', 'Duels Won per 90 min', 'Ball Recoveries per 90 min', 'Clearances per 90 min']
        stats_graph_total = ['Total Completed Passes', 'Pass Success Rate', 'Total Carries', 'Total Lost Balls', 'Duel Won Rate', 'Total Duels Won', 'Total Ball Recoveries', 'Total Clearances']
        weights = {
        'Total Completed Passes': 2, 'Total Long Passes': 2, 'Total Medium Passes': 2,
        'Total Short Passes': 1, 'Total Goal Assists': 1.5, 'Total Passes': 2,
        'Total Shot Assists': 1.5, 'Total Crosses':0.5, 'Completed Passes per 90 min': 2,
        'Long Passes per 90 min': 2, 'Medium Passes per 90 min': 2, 'Goal Assists per 90 min': 1.5,
        'Short Passes per 90 min': 1, 'Shot Assists per 90 min': 1.5, 'Crosses per 90 min': 0.5,
        'Pass Success Rate': 1, 'Total Ball Receipts': 1, 'Total Lost Balls': 1,
        'Ball Receipts per 90 min': 1, 'Lost Balls per 90 min': 1, 'Total Own Goals': 1,
        'Total Clearances': 2, 'Total Left Foot Clearances': 0.5, 'Total Right Foot Clearances': 0.5,
        'Total Head Clearances': 0.5, 'Total Other Clearances': 0.5, 'Total Aerial Duels Won': 1,
        'Clearances per 90 min': 2, 'Aerial Duels Won per 90 min': 1, 'Total Interceptions': 2,
        'Interceptions per 90 min': 2, 'Total Fouls Won': 1, 'Total Penalties Won': 1,
        'Fouls Won per 90 min': 1, 'Total Fouls Committed': 1, 'Total Yellow Cards': 1,
        'Total Red Cards': 2, 'Total Penalties Conceded': 2, 'Fouls Committed per 90 min': 1,
        'Total Ball Recoveries': 2, 'Ball Recoveries per 90 min': 2, 'Total Blocks': 2,
        'Blocks per 90 min': 2, 'Total Completed Dribbles': 1, 'Dribble Success Rate': 1,
        'Completed Dribbles per 90 min': 1, 'Total Dribbled Past': 2, 'Dribbled Past per 90 min': 2,
        'Total Carries': 1, 'Mean Distance Carries': 1, 'Carries per 90 min': 1,
        'Total Duels': 2, 'Total Duels Won': 2, 'Duel Won Rate': 2, 'Duels Won per 90 min': 2,
        'Total Shots': 1, 'Total Goals': 1, 'Total Shots Saved': 1, 'Total Shots Blocked': 1,
        'Total Shots On the Post': 1, 'Total Shots Off Target': 1, 'Total Shots On Target': 1,
        'Goals per 90 min': 1, 'Shots per 90 min': 1, 'Shots on Target per 90 min': 1,
        'Shots On Target Rate': 1, 'Goal Conversion Rate': 1}
    elif position_name == 'Central/Attacking Midfielder':
        df_stats = pd.read_csv('data_app/stats_ranking_cm.csv')
        stats_graph_90 = ['Completed Passes per 90 min', 'Pass Success Rate', 'Total Goal Assists', 'Shot Assists per 90 min', 'Dribble Success Rate', 'Completed Dribbles per 90 min', 'Carries per 90 min', 'Lost Balls per 90 min']
        stats_graph_total = ['Total Completed Passes', 'Pass Success Rate', 'Total Goal Assists', 'Total Shot Assists', 'Dribble Success Rate', 'Total Completed Dribbles', 'Total Carries', 'Total Lost Balls']
        weights = {
        'Total Completed Passes': 2, 'Total Long Passes': 2, 'Total Medium Passes': 2,
        'Total Short Passes': 2, 'Total Goal Assists': 2, 'Total Passes': 2,
        'Total Shot Assists': 2, 'Total Crosses':1, 'Completed Passes per 90 min': 2,
        'Long Passes per 90 min': 2, 'Medium Passes per 90 min': 2, 'Goal Assists per 90 min': 2,
        'Short Passes per 90 min': 2, 'Shot Assists per 90 min': 2, 'Crosses per 90 min': 1,
        'Pass Success Rate': 2, 'Total Ball Receipts': 1, 'Total Lost Balls': 1,
        'Ball Receipts per 90 min': 1, 'Lost Balls per 90 min': 1, 'Total Own Goals': 1,
        'Total Clearances': 1, 'Total Left Foot Clearances': 0.5, 'Total Right Foot Clearances': 0.5,
        'Total Head Clearances': 0.5, 'Total Other Clearances': 0.5, 'Total Aerial Duels Won': 1,
        'Clearances per 90 min': 1, 'Aerial Duels Won per 90 min': 1, 'Total Interceptions': 1,
        'Interceptions per 90 min': 1, 'Total Fouls Won': 1, 'Total Penalties Won': 1,
        'Fouls Won per 90 min': 1, 'Total Fouls Committed': 1, 'Total Yellow Cards': 1,
        'Total Red Cards': 1, 'Total Penalties Conceded': 1, 'Fouls Committed per 90 min': 1,
        'Total Ball Recoveries': 1, 'Ball Recoveries per 90 min': 1, 'Total Blocks': 1,
        'Blocks per 90 min': 1, 'Total Completed Dribbles': 1.5, 'Dribble Success Rate': 1.5,
        'Completed Dribbles per 90 min': 1.5, 'Total Dribbled Past': 1, 'Dribbled Past per 90 min': 1,
        'Total Carries': 1.5, 'Mean Distance Carries': 1.5, 'Carries per 90 min': 1.5,
        'Total Duels': 1, 'Total Duels Won': 1, 'Duel Won Rate': 1, 'Duels Won per 90 min': 1,
        'Total Shots': 1, 'Total Goals': 1, 'Total Shots Saved': 1, 'Total Shots Blocked': 1,
        'Total Shots On the Post': 1, 'Total Shots Off Target': 1, 'Total Shots On Target': 1,
        'Goals per 90 min': 1, 'Shots per 90 min': 1, 'Shots on Target per 90 min': 1,
        'Shots On Target Rate': 1, 'Goal Conversion Rate': 1}
    elif position_name == 'Left/Right Winger':
        df_stats = pd.read_csv('data_app/stats_ranking_w.csv')
        stats_graph_90 = ['Goals per 90 min', 'Shots per 90 min', 'Goal Conversion Rate', 'Shots On Target Rate', 'Total Goal Assists', 'Dribble Success Rate', 'Completed Dribbles per 90 min', 'Carries per 90 min']
        stats_graph_total = ['Total Goals', 'Total Shots', 'Goal Conversion Rate', 'Shots On Target Rate', 'Total Goal Assists', 'Dribble Success Rate', 'Total Completed Dribbles', 'Total Carries']
        weights = {
        'Total Completed Passes': 0.5, 'Total Long Passes': 0.5, 'Total Medium Passes': 0.5,
        'Total Short Passes': 0.5, 'Total Goal Assists': 10, 'Total Passes': 0.5,
        'Total Shot Assists': 2, 'Total Crosses':2, 'Completed Passes per 90 min': 0.5,
        'Long Passes per 90 min': 0.5, 'Medium Passes per 90 min': 0.5, 'Goal Assists per 90 min': 10,
        'Short Passes per 90 min': 0.5, 'Shot Assists per 90 min': 2, 'Crosses per 90 min': 2,
        'Pass Success Rate': 0.5, 'Total Ball Receipts': 0.5, 'Total Lost Balls': 0.5,
        'Ball Receipts per 90 min': 0.5, 'Lost Balls per 90 min': 0.5, 'Total Own Goals': 1,
        'Total Clearances': 0.5, 'Total Left Foot Clearances': 0.5, 'Total Right Foot Clearances': 0.5,
        'Total Head Clearances': 0.5, 'Total Other Clearances': 0.5, 'Total Aerial Duels Won': 0.5,
        'Clearances per 90 min': 0.5, 'Aerial Duels Won per 90 min': 0.5, 'Total Interceptions': 0.5,
        'Interceptions per 90 min': 0.5, 'Total Fouls Won': 0.5, 'Total Penalties Won': 2,
        'Fouls Won per 90 min': 1.5, 'Total Fouls Committed': 0.5, 'Total Yellow Cards': 0.5,
        'Total Red Cards': 0.5, 'Total Penalties Conceded': 0.5, 'Fouls Committed per 90 min': 0.5,
        'Total Ball Recoveries': 0.5, 'Ball Recoveries per 90 min': 0.5, 'Total Blocks': 0.5,
        'Blocks per 90 min': 0.5, 'Total Completed Dribbles': 1, 'Dribble Success Rate': 1,
        'Completed Dribbles per 90 min': 1, 'Total Dribbled Past': 0.5, 'Dribbled Past per 90 min': 0.5,
        'Total Carries': 1, 'Mean Distance Carries': 1, 'Carries per 90 min': 1,
        'Total Duels': 0.5, 'Total Duels Won': 0.5, 'Duel Won Rate': 1, 'Duels Won per 90 min': 0.5,
        'Total Shots': 5, 'Total Goals': 10, 'Total Shots Saved': 2, 'Total Shots Blocked': 2,
        'Total Shots On the Post': 2, 'Total Shots Off Target': 2, 'Total Shots On Target': 2,
        'Goals per 90 min': 10, 'Shots per 90 min': 5, 'Shots on Target per 90 min': 2,
        'Shots On Target Rate': 1, 'Goal Conversion Rate': 1}
    elif position_name == 'Striker':
        df_stats = pd.read_csv('data_app/stats_ranking_f.csv')
        stats_graph_90 = ['Goals per 90 min', 'Shots per 90 min', 'Goal Conversion Rate', 'Shots On Target Rate', 'Total Goal Assists', 'Dribble Success Rate', 'Completed Dribbles per 90 min', 'Carries per 90 min']
        stats_graph_total = ['Total Goals', 'Total Shots', 'Goal Conversion Rate', 'Shots On Target Rate', 'Total Goal Assists', 'Dribble Success Rate', 'Total Completed Dribbles', 'Total Carries']
        weights = {
        'Total Completed Passes': 0.5, 'Total Long Passes': 0.5, 'Total Medium Passes': 0.5,
        'Total Short Passes': 0.5, 'Total Goal Assists': 5, 'Total Passes': 0.5,
        'Total Shot Assists': 2, 'Total Crosses':0.5, 'Completed Passes per 90 min': 0.5,
        'Long Passes per 90 min': 0.5, 'Medium Passes per 90 min': 0.5, 'Goal Assists per 90 min': 5,
        'Short Passes per 90 min': 0.5, 'Shot Assists per 90 min': 2, 'Crosses per 90 min': 0.5,
        'Pass Success Rate': 0.5, 'Total Ball Receipts': 0.5, 'Total Lost Balls': 0.5,
        'Ball Receipts per 90 min': 0.5, 'Lost Balls per 90 min': 0.5, 'Total Own Goals': 1,
        'Total Clearances': 0.5, 'Total Left Foot Clearances': 0.5, 'Total Right Foot Clearances': 0.5,
        'Total Head Clearances': 0.5, 'Total Other Clearances': 0.5, 'Total Aerial Duels Won': 0.5,
        'Clearances per 90 min': 0.5, 'Aerial Duels Won per 90 min': 0.5, 'Total Interceptions': 0.5,
        'Interceptions per 90 min': 0.5, 'Total Fouls Won': 0.5, 'Total Penalties Won': 2,
        'Fouls Won per 90 min': 1.5, 'Total Fouls Committed': 0.5, 'Total Yellow Cards': 0.5,
        'Total Red Cards': 0.5, 'Total Penalties Conceded': 0.5, 'Fouls Committed per 90 min': 0.5,
        'Total Ball Recoveries': 0.5, 'Ball Recoveries per 90 min': 0.5, 'Total Blocks': 0.5,
        'Blocks per 90 min': 0.5, 'Total Completed Dribbles': 1, 'Dribble Success Rate': 1,
        'Completed Dribbles per 90 min': 1, 'Total Dribbled Past': 0.5, 'Dribbled Past per 90 min': 0.5,
        'Total Carries': 1, 'Mean Distance Carries': 1, 'Carries per 90 min': 1,
        'Total Duels': 0.5, 'Total Duels Won': 0.5, 'Duel Won Rate': 1, 'Duels Won per 90 min': 0.5,
        'Total Shots': 5, 'Total Goals': 10, 'Total Shots Saved': 2, 'Total Shots Blocked': 2,
        'Total Shots On the Post': 2, 'Total Shots Off Target': 2, 'Total Shots On Target': 2,
        'Goals per 90 min': 10, 'Shots per 90 min': 5, 'Shots on Target per 90 min': 2,
        'Shots On Target Rate': 1, 'Goal Conversion Rate': 1}

    name_col = df_stats['player_name']
    filtered_df = df_stats[[col for col in weights.keys() if col in df_stats.columns]]
    for col in filtered_df.columns:
        filtered_df[col] *= weights[col]        
    df_stats['mean'] = filtered_df.mean(axis=1)
    df_stats['player_name'] = name_col

    sorted_df = df_stats.sort_values(by='mean', ascending=False)
    top_5_df = sorted_df.head(5)

    st.write(f"## 5 Best {position_name}s in La Liga 2015-2016")
    j=1
    for i, row in top_5_df.iterrows():
        
        df_stats_general_indiv = df_stats_general[df_stats_general['player_name'] == row['player_name']]
        st.write(f"## {j} - {row['player_name']}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"**Name:** {row['player_name']}")
            st.write(f"**Country:** {df_stats_general_indiv['country.name'].iloc[0]}")
            st.write(f"**Team:** {df_stats_general_indiv['team_name'].iloc[0]}")
        with col2:
            st.write(f"**Jersey number:** {df_stats_general_indiv['jersey_number'].iloc[0]}")
            st.write(f"**Position:** {df_stats_general_indiv['position'].iloc[0]}")
            st.write(f"**Game as Starter:** {df_stats_general_indiv['starting'].iloc[0]}")
        with col3:
            st.write(f"**Game as Substitute:** {df_stats_general_indiv['subbing'].iloc[0]}")
            st.write(f"**Minutes per Game:** {min(math.ceil(df_stats_general_indiv['time'].iloc[0]/(df_stats_general_indiv['starting'].iloc[0] + df_stats_general_indiv['subbing'].iloc[0])),90)}")
            results_markdown = f"""
            **Results :** 
            <span style='color: green;'>{df_stats_general_indiv['win'].iloc[0]}W </span>
            <span style='color: black;'>{df_stats_general_indiv['draw'].iloc[0]}D </span> 
            <span style='color: red;'>{df_stats_general_indiv['lose'].iloc[0]}L </span>
            """
            st.markdown(results_markdown, unsafe_allow_html=True)

        player_data = df_stats[df_stats['player_name'] == row['player_name']]

        values = player_data[stats_graph_total].iloc[0]

        df_stats_total = pd.DataFrame({
            'Stat': [stat.replace('Total ', '') for stat in stats_graph_total],
            'Value': values
        })

        values = player_data[stats_graph_90].iloc[0]

        df_stats_90 = pd.DataFrame({
            'Stat': [stat.replace(' per 90 min', '') for stat in stats_graph_90],
            'Value': values
        })

        st.write(" ")
        plot_bars_altair(df_stats_total, f"{row['player_name']}'s stats compared to players in his position in La Liga 2015-2016")
        st.write(" ")
        plot_bars_altair(df_stats_90, f"{row['player_name']}'s stats compared to players in his position in La Liga 2015-2016 (per 90 min)")
        st.write(" ")

        j+=1





