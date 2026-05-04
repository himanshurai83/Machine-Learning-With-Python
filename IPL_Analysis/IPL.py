import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)
st.title("📊 EDA Dashboard")
st.title("IPL 2022")


st.markdown(
    "Upload a CSV file to instantly explore your data with statistics, plots, and summaries.")
st.divider()

# file = st.file_uploader("Upload your CSV file", type=["csv"])
file = "IPL.csv"

if file is None:
    st.info("👆 Upload a csv file")
    st.stop()


@st.cache_data
def load_data(file):
    return pd.read_csv(file)


df = load_data(file)

st.success(
    f"✅ File loaded: **{file}** — {df.shape[0]:,} rows × {df.shape[1]} columns")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview",
                                 "📈 Distributions",
                                  "🔗 Correlations", "ℹ️Top Insights"])  # Show summary

numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(exclude=np.number).columns.tolist()
missing_values = df.isna().sum().sum()
duplicate_value = df.duplicated().sum()
missing_pct = (missing_values * 100) / df.shape[0]

cols_info = pd.DataFrame({
    "Columns": df.columns,
    "Data Types": df.dtypes.values,
    "Missing": df.isna().sum().values,
    "Not Null": df.notnull().sum().values,
    "Unique": df.nunique().values
})
with tab1:
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Numerical columns", len(numerical_cols))
    col4.metric("Categorical columns", len(categorical_cols))
    col5.metric("Missing Values", missing_values)
    col6.metric("Missing Values", f"{missing_values}%")

    st.subheader("**All Dataset Information**")
    st.dataframe(cols_info)

    st.write("**Dataset Preview**")
    st.dataframe(df.head(10))

    if st.checkbox("Show Duplicate Row"):
        st.dataframe(df[df.duplicated(keep=False)])

    # Updated DataFrame like adding wickets and run columns
    # temp_df = df.copy()
    # temp_df[['wicket', 'run']] = df['best_bowling_figure'].str.split(
    #     "--", expand=True)
    # st.header("Updated Data Frame")
    # temp_df['wicket'] = temp_df['wicket'].astype(int)
    # temp_df['run'] = temp_df['run'].astype(int)
    # if st.checkbox("Updated Dataframe"):
    #     st.dataframe(temp_df.head())


def bar_plot(x, y, xlabel, ylabel):
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y, palette='rainbow', ax=ax)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45)
    st.pyplot(fig)


if "date" in categorical_cols:
    categorical_cols.remove("date")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        # Selecting numerical columns
        num_column = st.selectbox("Numerical Columns", numerical_cols)
        if num_column in numerical_cols:
            # Showing the distribution of specific columns (Histogram)
            fig = px.histogram(df, x=num_column, nbins=10,
                               title=f"Distribution of {num_column}")
            # Setting EdgeColor
            fig.update_traces(
                marker=dict(
                    color='skyblue',          # bar color
                    line=dict(color='white', width=1.5)  # border
                )
            )
            st.plotly_chart(fig)

            # Detecting outliers and plotting box plot
            fig = px.box(x=df[num_column],
                         title=f"Detecting Outliers and Five number Summary of {num_column}")
            st.plotly_chart(fig)

            # Showing relationship between two specific columns

            multiple_columns = st.multiselect(
                "Select Multiple cols", numerical_cols, max_selections=2, default=[numerical_cols[0], numerical_cols[1]])
            if len(multiple_columns) == 2:
                fig = px.scatter(df,
                                 x=multiple_columns[0], y=multiple_columns[1], title=f"{multiple_columns[0]} v/s {multiple_columns[1]}")
                st.plotly_chart(fig)
            else:
                st.info("Select atleast Two Columns")

        else:
            st.info("Select any Numerical columns")

    with col2:
        cat_column = st.selectbox("Categorical Columns", categorical_cols)
        if cat_column in categorical_cols:
            # Showing the distribution of Categorical Columns
            value_counts = df[cat_column].value_counts().reset_index()
            value_counts.columns = [cat_column, "Count"]
            top_n = st.slider("Select Top Categories", 5, 20, 10)
            value_counts = value_counts.head(top_n)
            # st.write(value_counts)
            # st.write(cat_column)

            # Bar Chart
            fig = px.bar(value_counts, x=cat_column, y='Count',
                         title=f"Distribution of {cat_column}")
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

            # Pie Chart
            fig = px.pie(value_counts, names=cat_column,
                         values="Count",
                         title=f"Distribution of {cat_column}")
            st.plotly_chart(fig)

            # One Numerical and One Categorical Columns
            st.subheader(
                "Now showing the relation between numerical and categorical columns")
            numerical = st.selectbox(
                "Select Numerical columns", numerical_cols)
            categorical = st.selectbox(
                "Select Categorical columns", categorical_cols)
            agg_type = st.selectbox("Select Aggregation", [
                'mean', 'median', 'sum'])

            grouped_data = df.groupby(categorical)[numerical].agg(
                agg_type).reset_index()

            fig = px.bar(grouped_data, x=categorical, y=numerical,
                         title=f"{agg_type} of {numerical} by {categorical}")
            st.plotly_chart(fig)

        else:
            st.info("Select any Categorical Columns")
# Contains relationship among all columns
with tab3:

    st.subheader("**Statistical Information**")
    st.dataframe(df.describe())
    # show correlation between all columns
    st.subheader("🤝Relation Between All columns")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True),
                annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)


# Contains all information(Top runs scorer,Top Wicket taker,Avg scores etc)
with tab4:
    # Toss Decision
    st.subheader("Toss Decisions")
    toss_decision = df['toss_decision'].value_counts()
    toss_percentage_field = (toss_decision['Field'] * 100) / df.shape[0]
    toss_percentage_bat = (toss_decision['Bat'] * 100) / df.shape[0]

    # Toss Distribution
    fig = px.pie(values=toss_decision.values, names=toss_decision.index)
    st.plotly_chart(fig)
    st.markdown(
        f"**After winning a toss, There are {round(toss_percentage_field, 2)}% chance to choose Field and {round(toss_percentage_bat, 2)}% chance to choose Bat.**")

    st.subheader("Toss vs Match")
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
    toss_win_and_match_win = df[df['toss_winner']
                                == df['match_winner']].count()
    actual_win = toss_win_and_match_win['match_winner']
    wining_percentage = (actual_win * 100) / df.shape[0]
    st.markdown(
        f"**There is a {round(wining_percentage, 2)}% chance team won the toss and Also Won the match.**")

    # Score Insights

    st.title("First Inning Score vs Second Inning Score")

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
        bar_plot(venue_by_second.values,
                 venue_by_second.index, "Score", "Venue")
    st.write("As you see 'Eden Gardens, Kolkata' has more chance to score Runs high.")

    # Top scorer in IPL 2022
    col1, col2 = st.columns(2)
    # Top 5 run scorer
    with col1:
        st.subheader("Top 5 Runs getter in TATA IPL 2022")
        top_scorer = df.groupby('top_scorer')[
            'highscore'].sum().sort_values(ascending=False).head()
        bar_plot(top_scorer.index, top_scorer.values, "Name", "Score")

    with col2:
        # Most wicket Takers
        temp_df = df.copy()
        temp_df[['wicket', 'run']] = df['best_bowling_figure'].str.split(
            "--", expand=True)
        temp_df['wicket'] = temp_df['wicket'].astype(int)
        temp_df['run'] = temp_df['run'].astype(int)
        highest_wicket_taker = temp_df.groupby('best_bowling')['wicket'].sum()
        st.subheader("Top 5 Highest Wicket Taker")

        # Top 5 wicket taker
        top_wicket_taker = highest_wicket_taker.sort_values(
            ascending=False).head()
        bar_plot(top_wicket_taker.index,
                 top_wicket_taker.values, "Players", "Wickets")

    # Plyer of the match
    st.title("Top 5 Player of the Match")
    player_of_the_match = df['player_of_the_match'].value_counts(
    ).sort_values(ascending=False).head()
    bar_plot(player_of_the_match.index,
             player_of_the_match.values, "Player", "Time")

    # Top Chases in TATA IPL 2022

    st.header("Top 10 Run Chases by Teams")
    chase = df[df['won_by'] == 'Wickets']
    top_chases = chase.sort_values(
        by='first_ings_score', ascending=False).head(10)
    top_chases['loser_team'] = np.where(
        top_chases['match_winner'] == top_chases['team1'], top_chases['team2'], top_chases['team1'])
    if st.checkbox("Top 10 Run chases"):
        st.dataframe(top_chases)
