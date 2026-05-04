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
# st.title("IPL 2022")


st.markdown(
    "Upload a CSV file to instantly explore your data with statistics, plots, and summaries.")
st.divider()

file = st.file_uploader("Upload your CSV file", type=["csv"])
# file = "IPL.csv"

if file is None:
    st.info("👆 Upload a csv file")
    st.stop()


@st.cache_data
def load_data(file):
    return pd.read_csv(file)


st.title(f"{file.name} Analysis")

df = load_data(file)

st.success(
    f"✅ File loaded: **{file.name}** — {df.shape[0]:,} rows × {df.shape[1]} columns")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview",
                                 "📈 Distributions",
                                  "🔗 Correlations", "ℹ️Top Insights"])  # Show summary

numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(exclude=np.number).columns.tolist()
missing_values = df.isna().sum().sum()
duplicate_value = df.duplicated().sum()
missing_pct = (missing_values * 100) / (df.shape[0] * df.shape[1])

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
    if st.checkbox("Show Missing Rows"):
        st.dataframe(df[df.isna().any(axis=1)])

    st.download_button(
        "Download Dataset",
        df.to_csv(index=False),
        file_name="processed_data.csv"
    )


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
    corr = df[numerical_cols].corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    st.plotly_chart(fig)


# Contains all information(Top runs scorer,Top Wicket taker,Avg scores etc)
with tab4:
    if st.button("Generate Insights"):
        st.subheader("🔍 Key Insights")

        # Correlation
        corr = df[numerical_cols].corr()
        for i in range(len(corr.columns)):
            for j in range(i):
                if abs(corr.iloc[i, j]) > 0.7:
                    st.success(
                        f"Strong correlation found between {corr.columns[i]} and {corr.columns[j]}")

        # Top performer
        grouped = df.groupby(categorical_cols)[numerical_cols].mean(
        ).sort_values(by=numerical_cols, ascending=False)
        st.write(f"Top {categorical_cols}: {grouped.index[0]}")

        # Most frequent
        counts = df[categorical_cols].value_counts()
        st.write(f"Most frequent {categorical_cols}: {counts.index[0]}")

        # Top Category Performance
        cat_col = st.selectbox("Categorical for Insight", categorical_cols)
        num_col = st.selectbox("Numerical for Insight", numerical_cols)

        grouped = df.groupby(cat_col)[num_col].mean(
        ).sort_values(ascending=False)

        top = grouped.index[0]
        bottom = grouped.index[-1]

        st.write(
            f"🔝 {top} has highest average {num_col} = {round(grouped.iloc[0], 2)}")
        st.write(
            f"🔻 {bottom} has lowest average {num_col} = {round(grouped.iloc[-1], 2)}")

        # Detecting Outliers
        Q1 = df[num_col].quantile(0.25)
        Q3 = df[num_col].quantile(0.75)
        IQR = Q3 - Q1

        outliers = df[(df[num_col] < Q1 - 1.5*IQR) |
                      (df[num_col] > Q3 + 1.5*IQR)]

        st.write(f"Outliers in {num_col}: {len(outliers)} rows")

# with st.sidebar:
#     st.header("Filters")

#     for col in categorical_cols[:3]:  # limit for UI
#         selected = st.multiselect(f"{col}", df[col].unique())
#         if selected:
#             df = df[df[col].isin(selected)]
