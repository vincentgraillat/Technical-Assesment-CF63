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

def display_stats(stats_list, header, data):
    st.header(header)
    stats_markdown = """
    <div style='border: 1px solid #ddd; padding: 10px; border-radius: 5px; display: inline-block; background-color: #f9f9f9;'>
    """
    for stat in stats_list:
        value = data[stat].values[0]  
        try:
            float_value = float(value)
            if float_value.is_integer():
                rounded_value = int(float_value)
            else:
                rounded_value = np.round(float_value, 2)
        except ValueError:
            rounded_value = value
        stats_markdown += f"<p><strong>{stat}:</strong> <span style='color: #FC34B6; font-weight: bold;'>{rounded_value}</span></p>"
    stats_markdown += "</div>"
    st.markdown(stats_markdown, unsafe_allow_html=True)

df = pd.read_csv('data_app/stats_final.csv')

df_graph_all = pd.read_csv('data_app/stats_ranking.csv')


st.set_page_config(page_title="Players Stats", layout="wide")


options = [''] + list(df['player_name'].unique())
player_name = st.selectbox('Select a player', options)


if player_name:
    player_data_graph = df_graph_all[df_graph_all['player_name'] == player_name]
    player_data = df[df['player_name'] == player_name]  
    with st.sidebar:
        st.header("Player Informations")


        if not player_data.empty:
            st.write(f"**Name:** {player_name}")
            st.write(f"**Country:** {player_data['country.name'].iloc[0]}")
            st.write(f"**Team:** {player_data['team_name'].iloc[0]}")
            st.write(f"**Jersey number:** {player_data['jersey_number'].iloc[0]}")
            st.write(f"**Position:** {player_data['position'].iloc[0]}")
            st.write(f"**Game as Starter:** {player_data['starting'].iloc[0]}")
            st.write(f"**Game as Substitute:** {player_data['subbing'].iloc[0]}")
            st.write(f"**Minutes per Game:** {min(math.ceil(player_data['time'].iloc[0]/(player_data['starting'].iloc[0] + player_data['subbing'].iloc[0])),90)}")
            results_markdown = f"""
            **Results :** 
            <span style='color: green;'>{player_data['win'].iloc[0]}W </span>
            <span style='color: black;'>{player_data['draw'].iloc[0]}D </span> 
            <span style='color: red;'>{player_data['lose'].iloc[0]}L </span>
            """
            st.markdown(results_markdown, unsafe_allow_html=True)

        else:
            st.write("Aucune donnée disponible pour le joueur sélectionné.")

    if player_data['position'].iloc[0] in ['Left Center Back', 'Right Center Back']:
        stats_graph_90 = ['Clearances per 90 min', 'Blocks per 90 min', 'Interceptions per 90 min', 'Ball Recoveries per 90 min', 'Dribbled Past per 90 min', 'Duels Won per 90 min', 'Duel Won Rate', 'Long Passes per 90 min']
        stats_graph_total = ['Total Clearances', 'Total Blocks', 'Total Interceptions', 'Total Ball Recoveries', 'Total Dribbled Past', 'Total Duels Won', 'Duel Won Rate', 'Total Long Passes']
        df_graph = pd.read_csv('data_app/stats_ranking_cb.csv')

    if player_data['position'].iloc[0] in ['Left Back', 'Right Back']:
        stats_graph_90 = ['Clearances per 90 min', 'Blocks per 90 min', 'Interceptions per 90 min', 'Ball Recoveries per 90 min', 'Dribbled Past per 90 min', 'Duels Won per 90 min', 'Duel Won Rate', 'Crosses per 90 min']
        stats_graph_total = ['Total Clearances', 'Total Blocks', 'Total Interceptions', 'Total Ball Recoveries', 'Total Dribbled Past', 'Total Duels Won', 'Duel Won Rate', 'Total Crosses']
        df_graph = pd.read_csv('data_app/stats_ranking_lb_rb.csv')

    if player_data['position'].iloc[0] in ['Left Defensive Midfield', 'Right Defensive Midfield','Center Defensive Midfield']:
        stats_graph_90 = ['Completed Passes per 90 min', 'Pass Success Rate', 'Carries per 90 min', 'Lost Balls per 90 min', 'Duel Won Rate', 'Duels Won per 90 min', 'Ball Recoveries per 90 min', 'Clearances per 90 min']
        stats_graph_total = ['Total Completed Passes', 'Pass Success Rate', 'Total Carries', 'Total Lost Balls', 'Duel Won Rate', 'Total Duels Won', 'Total Ball Recoveries', 'Total Clearances']
        df_graph = pd.read_csv('data_app/stats_ranking_dm.csv')

    if player_data['position'].iloc[0] in ['Left Center Midfield','Center Attacking Midfield', 'Left Midfield','Right Center Midfield', 'Right Midfield']:
        stats_graph_90 = ['Completed Passes per 90 min', 'Pass Success Rate', 'Total Goal Assists', 'Shot Assists per 90 min', 'Dribble Success Rate', 'Completed Dribbles per 90 min', 'Carries per 90 min', 'Lost Balls per 90 min']
        stats_graph_total = ['Total Completed Passes', 'Pass Success Rate', 'Total Goal Assists', 'Total Shot Assists', 'Dribble Success Rate', 'Total Completed Dribbles', 'Total Carries', 'Total Lost Balls']
        df_graph = pd.read_csv('data_app/stats_ranking_cm.csv')

    if player_data['position'].iloc[0] in ['Right Center Forward', 'Right Wing', 'Left Center Forward','Center Forward','Left Wing']:
        stats_graph_90 = ['Goals per 90 min', 'Shots per 90 min', 'Goal Conversion Rate', 'Shots On Target Rate', 'Total Goal Assists', 'Dribble Success Rate', 'Completed Dribbles per 90 min', 'Carries per 90 min']
        stats_graph_total = ['Total Goals', 'Total Shots', 'Goal Conversion Rate', 'Shots On Target Rate', 'Total Goal Assists', 'Dribble Success Rate', 'Total Completed Dribbles', 'Total Carries']
        if player_data_graph['position'].iloc[0] in ['Right Center Forward', 'Left Center Forward', 'Center Forward']:
            df_graph = pd.read_csv('data_app/stats_ranking_f.csv')
        else:
            df_graph = pd.read_csv('data_app/stats_ranking_w.csv')

    if player_data['position'].iloc[0] == 'Goalkeeper':
        stats_graph_total = ['Total Saves', 'Total Goals Conceded', 'Total Penalties Saved','Total Penalties Scored Against', 'Total Punches','Total Keeper Sweeper', 
                                 'Total Smothers', 'Total Collected', 'Goals Conceded Rate', 'Penalties Saved Rate']
        stats_graph_90 = ['Saves per 90 min', 'Goals Conceded per 90 min', 'Goals Conceded Rate', 'Penalties Saved Rate', 'Punch per 90 min', 
                                 'Keeper Sweeper per 90 min','Smothers per 90 min', 'Collected per 90 min']
        df_graph = pd.read_csv('data_app/stats_ranking_gk.csv')
        player_data_pos = df_graph[df_graph['player_name'] == player_name]

        values = player_data_pos[stats_graph_total].iloc[0]

        graph_df_pos_total = pd.DataFrame({
            'Stat': [stat.replace('Total ', '') for stat in stats_graph_total],
            'Value': values
        })

        values = player_data_pos[stats_graph_90].iloc[0]

        graph_df_pos_90 = pd.DataFrame({
            'Stat': [stat.replace(' per 90 min', '') for stat in stats_graph_90],
            'Value': values
        })



        plot_bars_altair(graph_df_pos_total, f"{player_name}'s stats compared to other goalkeepers La Liga 2015-2016")

        plot_bars_altair(graph_df_pos_90, f"{player_name}'s stats compared to players other goalkeepers in La Liga 2015-2016 (per 90 min)")



        col1, col2, col3 = st.columns(3)


        with col1:
            goalkeeping_stats = ['Total Saves', 'Total Goals Conceded', 'Total Penalties Saved','Total Penalties Scored Against', 'Total Punches','Total Keeper Sweeper', 
                                 'Total Smothers', 'Total Collected','Saves per 90 min', 'Goals Conceded per 90 min', 'Goals Conceded Rate', 'Penalties Saved Rate', 'Punch per 90 min', 
                                 'Keeper Sweeper per 90 min','Smothers per 90 min', 'Collected per 90 min']
            display_stats(goalkeeping_stats, "Goalkeeping Stats", player_data)


    else:

        player_data_pos = df_graph[df_graph['player_name'] == player_name]
        
        values = player_data_graph[stats_graph_total].iloc[0]

        graph_df_total = pd.DataFrame({
            'Stat': [stat.replace('Total ', '') for stat in stats_graph_total],
            'Value': values
        })

        values = player_data_graph[stats_graph_90].iloc[0]

        graph_df_90 = pd.DataFrame({
            'Stat': [stat.replace(' per 90 min', '') for stat in stats_graph_90],
            'Value': values
        })

        values = player_data_pos[stats_graph_total].iloc[0]

        graph_df_pos_total = pd.DataFrame({
            'Stat': [stat.replace('Total ', '') for stat in stats_graph_total],
            'Value': values
        })

        values = player_data_pos[stats_graph_90].iloc[0]

        graph_df_pos_90 = pd.DataFrame({
            'Stat': [stat.replace(' per 90 min', '') for stat in stats_graph_90],
            'Value': values
        })


        # Afficher les graphiques dans Streamlit
        plot_bars_altair(graph_df_total, f"{player_name}'s stats compared to all players in La Liga 2015-2016")

        plot_bars_altair(graph_df_90, f"{player_name}'s stats compared to all players in La Liga 2015-2016 (per 90 min)")

        plot_bars_altair(graph_df_pos_total, f"{player_name}'s stats compared to players in his position in La Liga 2015-2016")

        plot_bars_altair(graph_df_pos_90, f"{player_name}'s stats compared to players in his position in La Liga 2015-2016 (per 90 min)")



        col1, col2, col3 = st.columns(3)


        with col1:
            pass_stats = ['Total Passes','Total Completed Passes', 'Pass Success Rate', 'Total Short Passes', 'Total Medium Passes', 'Total Long Passes', 'Total Crosses', 'Total Goal Assists', 'Total Shot Assists' , 
                    'Completed Passes per 90 min', 'Short Passes per 90 min', 'Medium Passes per 90 min', 'Long Passes per 90 min', 'Crosses per 90 min', 'Shot Assists per 90 min']
            display_stats(pass_stats, "Passing Stats", player_data)


            duel_stats = ['Total Duels', 'Total Duels Won', 'Duel Won Rate', 'Total Aerial Duels Won', 'Duels Won per 90 min', 'Aerial Duels Won per 90 min']
            display_stats(duel_stats, "Duel Stats", player_data)

        with col2:
            shooting_stats = ['Total Goals', 'Total Shots', 'Total Shots On Target', 'Shots On Target Rate', 'Goal Conversion Rate', 'Total Shots On the Post', 'Total Shots Saved', 
                            'Total Shots Blocked', 'Goals per 90 min', 'Shots per 90 min', 'Shots on Target per 90 min']
            display_stats(shooting_stats, "Shooting Stats", player_data)

            clearance_stats = ['Total Clearances', 'Total Left Foot Clearances', 'Total Right Foot Clearances', 'Total Head Clearances', 'Clearances per 90 min']
            display_stats(clearance_stats, "Clearance Stats", player_data)

            carries_stats = ['Total Ball Receipts', 'Total Carries', 'Carries per 90 min', 'Mean Distance Carries',  'Total Lost Balls', 'Lost Balls per 90 min']
            display_stats(carries_stats, "Carries Stats", player_data)

        with col3:
            dribble_stats = ['Total Completed Dribbles', 'Completed Dribbles per 90 min', 'Dribble Success Rate']
            display_stats(dribble_stats, "Dribble Stats", player_data)

            foul_stats = ['Total Fouls Won', 'Total Fouls Committed', 'Total Yellow Cards', 'Total Red Cards', 'Total Penalties Won', 'Total Penalties Conceded']
            display_stats(foul_stats, "Foul Stats", player_data)

            defensive_stats = ['Total Interceptions', 'Interceptions per 90 min', 'Total Blocks', 'Blocks per 90 min', 'Total Ball Recoveries', 'Ball Recoveries per 90 min', 'Total Dribbled Past', 'Dribbled Past per 90 min']
            display_stats(defensive_stats, "Defensive Stats", player_data)