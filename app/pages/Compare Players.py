import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
import math


def clean_label(label):
    label = label.replace('Total ', '').replace(' per 90 min', '').strip()
    return label

def create_radar_chart(player_1_stats, player_2_stats, labels, title):
    player_1_stats = player_1_stats[labels].values.flatten().tolist()
    player_2_stats = player_2_stats[labels].values.flatten().tolist()

    num_vars = len(labels)
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    stats = player_1_stats + player_1_stats[:1]
    ax.plot(angles, stats, linewidth=2, linestyle='solid', label=player_name_1, color='blue')
    ax.fill(angles, stats, 'blue', alpha=0.1)

    stats = player_2_stats + player_2_stats[:1]
    ax.plot(angles, stats, linewidth=2, linestyle='solid', label=player_name_2, color='red')
    ax.fill(angles, stats, 'red', alpha=0.1)

    cleaned_labels = [clean_label(label) for label in labels]
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(cleaned_labels)

    for i, label in enumerate(ax.get_xticklabels()):
        label.set_color('black')

    # Ajouter les cercles alternés
    for i in range(1, 6):
        ax.fill_between(angles, i*0.2, (i+1)*0.2, facecolor='white' if i % 2 == 0 else 'lightgrey', zorder=0, alpha=0.1)

    ax.set_yticklabels([])
    ax.yaxis.grid(True, linestyle='-', color='grey', alpha=0.5)
    ax.xaxis.grid(True, linestyle='-', color='grey', alpha=0.5)

    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    st.pyplot(fig)


df_general = pd.read_csv('data_app/stats_final.csv')
df = pd.read_csv('data_app/stats_ranking.csv')
df_goalkeeper = pd.read_csv('data_app/stats_ranking_gk.csv')

st.set_page_config(page_title="Players Comparison", layout="wide")

options = [''] + list(df_general['player_name'].unique())
player_name_1 = st.selectbox('Select a first player', options)
player_name_2 = st.selectbox('Select a second player', options)

general_player_1 = df_general[df_general['player_name'] == player_name_1]
general_player_2 = df_general[df_general['player_name'] == player_name_2]


if player_name_1 and player_name_2:
    with st.sidebar:
        st.header("Player 1 Informations")

        st.write(f"**Name:** {player_name_1}")
        st.write(f"**Country:** {general_player_1['country.name'].iloc[0]}")
        st.write(f"**Team:** {general_player_1['team_name'].iloc[0]}")
        st.write(f"**Jersey number:** {general_player_1['jersey_number'].iloc[0]}")
        st.write(f"**Position:** {general_player_1['position'].iloc[0]}")
        st.write(f"**Game as Starter:** {general_player_1['starting'].iloc[0]}")
        st.write(f"**Game as Substitute:** {general_player_1['subbing'].iloc[0]}")
        st.write(f"**Minutes per Game:** {min(math.ceil(general_player_1['time'].iloc[0] / (general_player_1['starting'].iloc[0] + general_player_1['subbing'].iloc[0])), 90)}")
        results_markdown = f"""
        **Results :** 
        <span style='color: green;'>{general_player_1['win'].iloc[0]}W </span>
        <span style='color: black;'>{general_player_1['draw'].iloc[0]}D </span> 
        <span style='color: red;'>{general_player_1['lose'].iloc[0]}L </span>
        """
        st.markdown(results_markdown, unsafe_allow_html=True)

        st.header("Player 2 Informations")

        st.write(f"**Name:** {player_name_2}")
        st.write(f"**Country:** {general_player_2['country.name'].iloc[0]}")
        st.write(f"**Team:** {general_player_2['team_name'].iloc[0]}")
        st.write(f"**Jersey number:** {general_player_2['jersey_number'].iloc[0]}")
        st.write(f"**Position:** {general_player_2['position'].iloc[0]}")
        st.write(f"**Game as Starter:** {general_player_2['starting'].iloc[0]}")
        st.write(f"**Game as Substitute:** {general_player_2['subbing'].iloc[0]}")
        st.write(f"**Minutes per Game:** {min(math.ceil(general_player_2['time'].iloc[0] / (general_player_2['starting'].iloc[0] + general_player_2['subbing'].iloc[0])), 90)}")
        results_markdown = f"""
        **Results :** 
        <span style='color: green;'>{general_player_2['win'].iloc[0]}W </span>
        <span style='color: black;'>{general_player_2['draw'].iloc[0]}D </span> 
        <span style='color: red;'>{general_player_2['lose'].iloc[0]}L </span>
        """
        st.markdown(results_markdown, unsafe_allow_html=True)

    if (general_player_1['position'].iloc[0] != 'Goalkeeper') & (general_player_2['position'].iloc[0] != 'Goalkeeper'):
        player_1 = df[df['player_name'] == player_name_1]
        player_2 = df[df['player_name'] == player_name_2]

        st.write("  ")
        st.write("# Comparison Total Stats")
        st.write("  ")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("### Passing Stats")
            pass_stats = ['Total Passes','Total Completed Passes', 'Pass Success Rate', 'Total Short Passes', 'Total Medium Passes', 'Total Long Passes', 'Total Crosses', 'Total Goal Assists', 'Total Shot Assists']
            create_radar_chart(player_1, player_2, pass_stats,"Passing Stats")

            st.write("### Duel Stats")
            duel_stats = ['Total Duels', 'Total Duels Won', 'Duel Won Rate', 'Total Aerial Duels Won']
            create_radar_chart(player_1, player_2, duel_stats, "Duel Stats")

            st.write("### Carries and Dribbles Stats")
            carries_stats = ['Total Ball Receipts', 'Total Carries', 'Mean Distance Carries', 'Total Lost Balls', 'Total Completed Dribbles', 'Dribble Success Rate']
            create_radar_chart(player_1, player_2, carries_stats, "Carries and Dribbles Stats")

        with col2:
            st.write("### Shooting Stats")
            shooting_stats = ['Total Goals', 'Total Shots', 'Total Shots On Target', 'Shots On Target Rate', 'Goal Conversion Rate', 'Total Shots On the Post', 'Total Shots Saved', 'Total Shots Blocked']
            create_radar_chart(player_1, player_2, shooting_stats, "Shooting Stats")

            st.write("### Clearance Stats")
            clearance_stats = ['Total Clearances', 'Total Left Foot Clearances', 'Total Right Foot Clearances', 'Total Head Clearances']
            create_radar_chart(player_1, player_2, clearance_stats, "Clearance Stats")



        with col3:
            st.write("### Foul Stats")
            foul_stats = ['Total Fouls Won', 'Total Fouls Committed', 'Total Yellow Cards', 'Total Red Cards', 'Total Penalties Won', 'Total Penalties Conceded']
            create_radar_chart(player_1, player_2, foul_stats, "Foul Stats")

            st.write("### Defensive Stats")
            defensive_stats = ['Total Interceptions', 'Total Blocks', 'Total Ball Recoveries', 'Total Dribbled Past']
            create_radar_chart(player_1, player_2, defensive_stats, "Defensive Stats")

        st.write("  ")
        st.write('# Comparison Stats per 90 minutes')
        st.write("  ")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("### Passing Stats Comparison")
            st.write("  ")
            pass_stats = ['Pass Success Rate', 'Completed Passes per 90 min', 'Short Passes per 90 min', 'Medium Passes per 90 min', 'Long Passes per 90 min', 'Crosses per 90 min', 'Shot Assists per 90 min']
            create_radar_chart(player_1, player_2, pass_stats, "Passing Stats Comparison")

            st.write("### Duel Stats")
            duel_stats = ['Duel Won Rate', 'Duels Won per 90 min', 'Aerial Duels Won per 90 min']
            create_radar_chart(player_1, player_2, duel_stats, "Duel Stats")

        with col2:
            st.write("### Shooting Stats")
            shooting_stats = ['Shots On Target Rate', 'Goal Conversion Rate', 'Goals per 90 min', 'Shots per 90 min', 'Shots on Target per 90 min']
            create_radar_chart(player_1, player_2, shooting_stats, "Shooting Stats")

            st.write("### Carries and Dribbles Stats")
            carries_stats = ['Carries per 90 min', 'Mean Distance Carries', 'Lost Balls per 90 min', 'Completed Dribbles per 90 min', 'Dribble Success Rate']
            create_radar_chart(player_1, player_2, carries_stats, "Carries and Dribbles Stats")

        with col3:
            st.write("### Defensive Stats")
            defensive_stats = ['Interceptions per 90 min', 'Blocks per 90 min', 'Ball Recoveries per 90 min', 'Dribbled Past per 90 min']
            create_radar_chart(player_1, player_2, defensive_stats, "Defensive Stats")

    elif (general_player_1['position'].iloc[0] == 'Goalkeeper') & (general_player_2['position'].iloc[0] == 'Goalkeeper'):
        player_1 = df_goalkeeper[df_goalkeeper['player_name'] == player_name_1]
        player_2 = df_goalkeeper[df_goalkeeper['player_name'] == player_name_2]

            
        st.write("  ")
        st.write('# Comparison Total Stats')
        st.write("  ")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            goalkeeping_stats = ['Total Saves', 'Total Goals Conceded', 'Total Penalties Saved', 'Total Penalties Scored Against', 'Total Punches',
            'Total Keeper Sweeper', 'Total Smothers', 'Total Collected','Goals Conceded Rate','Penalties Saved Rate']
            create_radar_chart(player_1, player_2, goalkeeping_stats, "Goalkeeping Stats Comparison")

        st.write("  ")
        st.write('# Comparison Stats per 90 minutes')
        st.write("  ")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            goalkeeping_stats = ['Saves per 90 min', 'Goals Conceded per 90 min', 'Goals Conceded Rate',
            'Penalties Saved Rate', 'Punch per 90 min', 'Keeper Sweeper per 90 min', 'Smothers per 90 min', 'Collected per 90 min']
            create_radar_chart(player_1, player_2, goalkeeping_stats, "Goalkeeping Stats Comparison")

               
    else:
        st.write(" ")

        st.write("You cannot compare a goalkeeper and a field player.")

        st.write("Please select two players to compare.")




