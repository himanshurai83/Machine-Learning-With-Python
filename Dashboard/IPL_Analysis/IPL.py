import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


@st.cache_data
def load_data():
    return pd.read_csv("IPL.csv")


df = load_data()

st.title("IPL Data Analysis EDA Dashboard")
# Show summary
col1, col2, col3 = st.columns(3)
col1.metric("Total Matches", df.shape[0])
col2.metric("Teams", df['team1'].nunique())
col3.metric("Venues", df['venue'].nunique())


def bar_plot(x, y, xlabel, ylabel):
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y, palette='rainbow', ax=ax)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)


# print(df.head())
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Making two columns
col1, col2 = st.columns(2)

# show distribution of specific column
with col1:
    column = st.selectbox("Select column", df.columns)
    if df[column].dtype == 'object':
        counts = df[column].value_counts().head(10)
        fig, ax = plt.subplots()
        sns.barplot(x=counts.index, y=counts.values, ax=ax)
        ax.tick_params(axis='x', rotation=45)  # 👈 rotate here
        st.pyplot(fig)
    else:
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        ax.tick_params(axis='x', rotation=45)  # 👈 rotate here
        st.pyplot(fig)

# show correlation between all columns
with col2:
    st.subheader("Relation Between All columns")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Match winner and toss winner
col1, col2 = st.columns(2)

# Match winner
with col2:
    st.markdown("Total Match win by Each Team")
    match_winner = df['match_winner'].value_counts()
    bar_plot(match_winner.values, match_winner.index, "Matches", "Team")

# Toss winner
with col1:
    st.markdown("Total Toss win by Each Team")
    toss = df['toss_winner'].value_counts()
    bar_plot(toss.values, toss.index, "Toss", "Team")

# Insight for toss
toss_win_and_match_win = df[df['toss_winner'] == df['match_winner']].count()
actual_win = toss_win_and_match_win['match_winner']
wining_percentage = (actual_win * 100) / df.shape[0]
st.write(
    f"There is a {wining_percentage}% chance team won the toss and Also Won the match.")


# Toss Decision
toss_decision = df['toss_decision'].value_counts()
toss_percentage_field = (toss_decision['Field'] * 100) / df.shape[0]
toss_percentage_bat = (toss_decision['Bat'] * 100) / df.shape[0]
st.markdown(
    f"**After winning a toss, There are {toss_percentage_field}% chance to choose Field and {toss_percentage_bat}% chance to choose Bat.**")

# Toss Distribution
fig = px.pie(values=toss_decision.values, names=toss_decision.index)
st.plotly_chart(fig)


col1, col2 = st.columns(2)
with col1:
    # Avg 1st inning score
    st.subheader("Average First Inning Scores")
    fig, ax = plt.subplots()
    venue_by = df.groupby(
        "venue")['first_ings_score'].mean().sort_values(ascending=False)
    bar_plot(venue_by.values, venue_by.index, "Score", "Stadium Name")


# Avg second inning score
with col2:
    st.subheader("Average Second Inning score")
    venue_by_second = df.groupby(
        "venue")['second_ings_score'].mean().sort_values()
    bar_plot(venue_by_second.values, venue_by_second.index, "Score", "Venue")
st.write("As you see 'Eden Gardens, Kolkata' has more chance to score high Runs.")

# Top scorer in IPL 2022
st.title("Top 5 Runs getter in TATA IPL 2022")
top_scorer = df.groupby('top_scorer')[
    'highscore'].sum().sort_values(ascending=False).head()
bar_plot(top_scorer.index, top_scorer.values, "Name", "Score")

# Plyer of the match
st.title("Top 5 Player of the Match")
player_of_the_match = df['player_of_the_match'].value_counts(
).sort_values(ascending=False).head()
bar_plot(player_of_the_match.index, player_of_the_match.values, "Time", "Name")

# Top Chases in TATA IPL 2022

st.header("Top 10 Chases by Teams")
chase = df[df['won_by'] == 'Wickets']
top_chases = chase.sort_values(by='first_ings_score', ascending=False).head(10)
top_chases['loser_team'] = np.where(
    top_chases['match_winner'] == top_chases['team1'], top_chases['team2'], top_chases['team1'])
if st.checkbox("Want to saw Top 10 Run chases"):
    st.dataframe(top_chases)


# Most wicket Takers
temp_df = df.copy()
temp_df[['wicket', 'run']] = df['best_bowling_figure'].str.split(
    "--", expand=True)
st.header("Updated Data Frame")
temp_df['wicket'] = temp_df['wicket'].astype(int)
temp_df['run'] = temp_df['run'].astype(int)
st.dataframe(temp_df.head())
highest_wicket_taker = temp_df.groupby('best_bowling')['wicket'].sum()

# Top five wicket taker
st.subheader("Highest Wicket Taker")
top_wicket_taker = highest_wicket_taker.sort_values(ascending=False).head()
bar_plot(top_wicket_taker.values, top_wicket_taker.index, "Wickets", "Player")
