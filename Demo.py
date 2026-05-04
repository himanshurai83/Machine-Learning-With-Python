import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page config
st.set_page_config(page_title="IPL EDA Dashboard", layout="wide")

# Title
st.title("🏏 IPL Data Analysis Dashboard")

# Load Data
df = pd.read_csv("IPL.csv")

# Sidebar
st.sidebar.header("Filter Options")

# Show dataset
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Basic Info
st.subheader("Dataset Overview")
col1, col2 = st.columns(2)

with col1:
    st.write("Shape of dataset:", df.shape)

with col2:
    st.write("Columns:", df.columns.tolist())

# Missing values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Select Column for Analysis
column = st.selectbox("Select Column for Analysis", df.columns)

# Value Counts
st.subheader(f"Value Counts of {column}")
st.write(df[column].value_counts())

# Plot 1: Bar Chart
st.subheader("Bar Chart")
fig1 = px.bar(df[column].value_counts().head(10),
              x=df[column].value_counts().head(10).index,
              y=df[column].value_counts().head(10).values)

st.plotly_chart(fig1, use_container_width=True)

# Plot 2: Pie Chart
st.subheader("Pie Chart")
fig2 = px.pie(names=df[column].value_counts().head(5).index,
              values=df[column].value_counts().head(5).values)

st.plotly_chart(fig2, use_container_width=True)

# Numerical Analysis
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

if len(num_cols) > 0:
    st.subheader("Numerical Column Analysis")
    num_col = st.selectbox("Select Numerical Column", num_cols)

    # Histogram
    fig3, ax = plt.subplots()
    sns.histplot(df[num_col], kde=True, ax=ax)
    st.pyplot(fig3)

    # Boxplot
    fig4, ax = plt.subplots()
    sns.boxplot(x=df[num_col], ax=ax)
    st.pyplot(fig4)

# Correlation Heatmap
if len(num_cols) > 1:
    st.subheader("Correlation Heatmap")
    fig5, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig5)

# Match Insights (IPL Specific)
if 'match_winner' in df.columns:
    st.subheader("🏆 Match Winners Analysis")
    fig6 = px.bar(df['match_winner'].value_counts().head(10),
                  x=df['match_winner'].value_counts().head(10).index,
                  y=df['match_winner'].value_counts().head(10).values)

    st.plotly_chart(fig6, use_container_width=True)

if 'venue' in df.columns:
    st.subheader("📍 Matches by Venue")
    fig7 = px.bar(df['venue'].value_counts().head(10),
                  x=df['venue'].value_counts().head(10).index,
                  y=df['venue'].value_counts().head(10).values)

    st.plotly_chart(fig7, use_container_width=True)
