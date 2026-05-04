import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 EDA Dashboard")
st.markdown(
    "Upload a CSV file to instantly explore your data with statistics, plots, and summaries.")
st.divider()

file = "IPL.csv"

if file is None:
    st.write("File not valid")
    st.stop()

df = pd.read_csv(file)

st.success(
    f"✅ File loaded: **{file}** — {df.shape[0]:,} rows × {df.shape[1]} columns")
st.divider()

tab1, tab2, tab3 = st.tabs(["📋 Overview",
                            "📈 Distributions",
                           "🔗 Correlations"])

with tab1:
    st.subheader("Data Overview")

    numerical_col = df.select_dtypes(include=np.number).columns.tolist()
    categorical_col = df.select_dtypes(exclude=np.number).columns.tolist()
    total_miss = df.isna().sum().sum()
    miss_pct = round((total_miss * 100) / df.size, 2)
    duplicate_rows = df.duplicated().sum()

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Numerical Columns", len(numerical_col))
    col4.metric("Categorical Columns", len(categorical_col))
    col5.metric("Missing Value", f"{miss_pct}%")
    col6.metric("Duplicate Row", duplicate_rows)

    st.divider()

    col_info = pd.DataFrame({
        "Columns": df.columns,
        "Data Type": df.dtypes.values,
        "Not Null": df.notnull().sum().values,
        "Missing": df.isna().sum().values,
        "Missing(%)": ((df.isna().sum().sum() * 100)/df.shape[1]).round(2),
        "Unique": df.nunique().values,
        "Sample 1": df[df.columns].iloc[0],
        "Sample 2": df[df.columns].iloc[1]
    })

    st.dataframe(col_info, use_container_width=True, hide_index=False)


with tab2:
    st.subheader("Data Distribution")

    all_cols = df.columns.tolist()

    selected_col = st.selectbox("Select columns", all_cols)

    col1, col2 = st.columns(2)

    if selected_col in numerical_col:
        with col1:
            # Histogram
            st.markdown("**Histogram**")
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.hist(df[selected_col].dropna(), bins=30,
                    edgecolor="white", color="#185fa5", alpha=0.85)
            ax.set_title(f"Distribution of {selected_col}")
            ax.set_xlabel(selected_col)
            ax.set_ylabel("Frequency")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        pass

    else:
        pass
