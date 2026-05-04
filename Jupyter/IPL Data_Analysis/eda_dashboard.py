import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <style>
        .block-container { padding-top: 1.5rem; }
        .stMetric { background: #f8f9fa; border-radius: 10px; padding: 0.5rem; }
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.title("📊 EDA Dashboard")
st.markdown("Upload a CSV file to instantly explore your data with statistics, plots, and summaries.")
st.divider()

# ─────────────────────────────────────────────
# File Upload
# ─────────────────────────────────────────────
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is None:
    st.info("👆 Upload a CSV file above to get started.")
    st.stop()

# ─────────────────────────────────────────────
# Load Data
# ─────────────────────────────────────────────
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

df = load_data(uploaded_file)

st.success(f"✅ File loaded: **{uploaded_file.name}** — {df.shape[0]:,} rows × {df.shape[1]} columns")
st.divider()

# ─────────────────────────────────────────────
# Tabs
# ─────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📋 Overview",
    "📈 Distributions",
    "🔗 Correlations",
    "📐 Statistics",
    "❓ Missing Values",
    "🔍 Data Preview"
])

# ══════════════════════════════════════════════
# TAB 1 — OVERVIEW
# ══════════════════════════════════════════════
with tab1:
    st.subheader("Dataset Overview")

    num_cols   = df.select_dtypes(include=np.number).columns.tolist()
    cat_cols   = df.select_dtypes(exclude=np.number).columns.tolist()
    total_miss = df.isnull().sum().sum()
    miss_pct   = round(total_miss / df.size * 100, 2)
    dup_rows   = df.duplicated().sum()

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Rows",             f"{df.shape[0]:,}")
    c2.metric("Columns",          df.shape[1])
    c3.metric("Numeric Cols",     len(num_cols))
    c4.metric("Categorical Cols", len(cat_cols))
    c5.metric("Missing Values",   f"{miss_pct}%")
    c6.metric("Duplicate Rows",   dup_rows)

    st.divider()
    st.subheader("Column Information")

    col_info = pd.DataFrame({
        "Column":    df.columns,
        "Dtype":     df.dtypes.values,
        "Non-Null":  df.notnull().sum().values,
        "Missing":   df.isnull().sum().values,
        "Miss %":    (df.isnull().mean() * 100).round(2).values,
        "Unique":    df.nunique().values,
        "Sample 1":  [df[c].dropna().iloc[0]  if df[c].dropna().shape[0] > 0 else "" for c in df.columns],
        "Sample 2":  [df[c].dropna().iloc[1]  if df[c].dropna().shape[0] > 1 else "" for c in df.columns],
    })
    st.dataframe(col_info, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════
# TAB 2 — DISTRIBUTIONS
# ══════════════════════════════════════════════
with tab2:
    st.subheader("Column Distributions")

    all_cols = df.columns.tolist()
    selected_col = st.selectbox("Select a column", all_cols)

    col_a, col_b = st.columns(2)

    if selected_col in num_cols:
        # Histogram
        with col_a:
            st.markdown(f"**Histogram — {selected_col}**")
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.hist(df[selected_col].dropna(), bins=30, color="#185fa5", edgecolor="white", alpha=0.85)
            ax.set_xlabel(selected_col)
            ax.set_ylabel("Frequency")
            ax.set_title(f"Distribution of {selected_col}")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        # Boxplot
        with col_b:
            st.markdown(f"**Boxplot — {selected_col}**")
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.boxplot(df[selected_col].dropna(), vert=True, patch_artist=True,
                       boxprops=dict(facecolor="#dbeafe", color="#185fa5"),
                       medianprops=dict(color="#c0392b", linewidth=2))
            ax.set_ylabel(selected_col)
            ax.set_title(f"Boxplot of {selected_col}")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        # Stats
        st.markdown("**Descriptive Stats**")
        stats = df[selected_col].describe().to_frame().T
        stats["skewness"] = df[selected_col].skew()
        stats["kurtosis"] = df[selected_col].kurt()
        st.dataframe(stats.round(4), use_container_width=True)

    else:
        # Bar chart for categorical
        with col_a:
            st.markdown(f"**Value Counts — {selected_col}**")
            vc = df[selected_col].value_counts().head(20)
            fig, ax = plt.subplots(figsize=(6, 5))
            vc.plot(kind="barh", ax=ax, color="#185fa5", edgecolor="white")
            ax.set_xlabel("Count")
            ax.set_title(f"Top values in {selected_col}")
            ax.invert_yaxis()
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        # Pie chart
        with col_b:
            st.markdown(f"**Pie Chart — {selected_col}**")
            vc_top = df[selected_col].value_counts().head(8)
            fig, ax = plt.subplots(figsize=(6, 5))
            ax.pie(vc_top, labels=vc_top.index, autopct="%1.1f%%",
                   startangle=140, colors=sns.color_palette("Blues_r", len(vc_top)))
            ax.set_title(f"Distribution of {selected_col}")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        st.markdown("**Value Counts Table**")
        vc_df = df[selected_col].value_counts().reset_index()
        vc_df.columns = [selected_col, "Count"]
        vc_df["Percentage"] = (vc_df["Count"] / len(df) * 100).round(2)
        st.dataframe(vc_df, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════
# TAB 3 — CORRELATIONS
# ══════════════════════════════════════════════
with tab3:
    st.subheader("Correlation Analysis")

    if len(num_cols) < 2:
        st.warning("Need at least 2 numeric columns for correlation analysis.")
    else:
        corr_method = st.selectbox("Correlation method", ["pearson", "spearman", "kendall"])
        corr_matrix = df[num_cols].corr(method=corr_method)

        col_a, col_b = st.columns([2, 1])

        with col_a:
            st.markdown("**Correlation Heatmap**")
            fig, ax = plt.subplots(figsize=(max(6, len(num_cols)), max(5, len(num_cols) - 1)))
            mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
            sns.heatmap(
                corr_matrix, mask=mask, annot=True, fmt=".2f",
                cmap="coolwarm", center=0, linewidths=0.5,
                ax=ax, cbar_kws={"shrink": 0.8},
                annot_kws={"size": 9}
            )
            ax.set_title(f"{corr_method.capitalize()} Correlation Matrix")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        with col_b:
            st.markdown("**Top Correlated Pairs**")
            pairs = (
                corr_matrix.where(~mask)
                .stack()
                .reset_index()
            )
            pairs.columns = ["Col A", "Col B", "Correlation"]
            pairs["Abs"] = pairs["Correlation"].abs()
            pairs = pairs.sort_values("Abs", ascending=False).drop(columns="Abs")
            pairs["Correlation"] = pairs["Correlation"].round(4)
            st.dataframe(pairs.head(20), use_container_width=True, hide_index=True)

        # Scatter plot for selected pair
        st.divider()
        st.markdown("**Scatter Plot — select two columns**")
        sc1, sc2 = st.columns(2)
        x_col = sc1.selectbox("X axis", num_cols, index=0)
        y_col = sc2.selectbox("Y axis", num_cols, index=min(1, len(num_cols) - 1))

        hue_col = st.selectbox("Color by (optional)", ["None"] + cat_cols)

        fig, ax = plt.subplots(figsize=(7, 4))
        if hue_col != "None" and hue_col in df.columns:
            groups = df[hue_col].unique()[:10]
            palette = sns.color_palette("tab10", len(groups))
            for grp, color in zip(groups, palette):
                subset = df[df[hue_col] == grp]
                ax.scatter(subset[x_col], subset[y_col], label=str(grp),
                           color=color, alpha=0.6, s=20)
            ax.legend(title=hue_col, bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=9)
        else:
            ax.scatter(df[x_col], df[y_col], color="#185fa5", alpha=0.5, s=20)

        # Regression line
        clean = df[[x_col, y_col]].dropna()
        if len(clean) > 1:
            m, b = np.polyfit(clean[x_col], clean[y_col], 1)
            ax.plot(clean[x_col], m * clean[x_col] + b, color="#c0392b", linewidth=1.5, label="Trend")

        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{x_col} vs {y_col}")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ══════════════════════════════════════════════
# TAB 4 — STATISTICS
# ══════════════════════════════════════════════
with tab4:
    st.subheader("Descriptive Statistics")

    if not num_cols:
        st.warning("No numeric columns found.")
    else:
        desc = df[num_cols].describe().T
        desc["skewness"] = df[num_cols].skew()
        desc["kurtosis"] = df[num_cols].kurt()
        desc["median"]   = df[num_cols].median()
        desc["variance"] = df[num_cols].var()

        col_order = ["count", "mean", "median", "std", "variance",
                     "min", "25%", "50%", "75%", "max", "skewness", "kurtosis"]
        col_order = [c for c in col_order if c in desc.columns]
        st.dataframe(desc[col_order].round(4), use_container_width=True)

    if cat_cols:
        st.divider()
        st.subheader("Categorical Column Summary")
        cat_summary = pd.DataFrame({
            "Column":  cat_cols,
            "Unique":  [df[c].nunique() for c in cat_cols],
            "Top Value":     [df[c].mode()[0] if not df[c].mode().empty else "" for c in cat_cols],
            "Top Freq":      [df[c].value_counts().iloc[0] if df[c].value_counts().shape[0] > 0 else 0 for c in cat_cols],
            "Top Freq %":    [(df[c].value_counts().iloc[0] / len(df) * 100).round(2)
                              if df[c].value_counts().shape[0] > 0 else 0 for c in cat_cols],
        })
        st.dataframe(cat_summary, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════
# TAB 5 — MISSING VALUES
# ══════════════════════════════════════════════
with tab5:
    st.subheader("Missing Value Analysis")

    miss = df.isnull().sum()
    miss = miss[miss > 0].sort_values(ascending=False)

    if miss.empty:
        st.success("🎉 No missing values found in the dataset!")
    else:
        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("**Missing Values per Column**")
            miss_df = pd.DataFrame({
                "Column":  miss.index,
                "Missing": miss.values,
                "Pct (%)": (miss / len(df) * 100).round(2).values
            })
            st.dataframe(miss_df, use_container_width=True, hide_index=True)

        with col_b:
            st.markdown("**Missing Values Bar Chart**")
            fig, ax = plt.subplots(figsize=(6, max(3, len(miss) * 0.4)))
            miss.plot(kind="barh", ax=ax, color="#e74c3c", edgecolor="white")
            ax.set_xlabel("Missing Count")
            ax.set_title("Missing Values by Column")
            ax.invert_yaxis()
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        # Heatmap of missing
        st.markdown("**Missing Values Heatmap (first 200 rows)**")
        fig, ax = plt.subplots(figsize=(min(16, len(df.columns)), 4))
        sns.heatmap(
            df[miss.index].head(200).isnull(),
            cbar=False, ax=ax,
            cmap=["#f0f0f0", "#e74c3c"],
            yticklabels=False
        )
        ax.set_title("Red = Missing")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ══════════════════════════════════════════════
# TAB 6 — DATA PREVIEW
# ══════════════════════════════════════════════
with tab6:
    st.subheader("Data Preview")

    n_rows = st.slider("Rows to display", min_value=5, max_value=min(500, len(df)), value=10, step=5)
    view   = st.radio("Show", ["First N rows", "Last N rows", "Random sample"], horizontal=True)

    if view == "First N rows":
        st.dataframe(df.head(n_rows), use_container_width=True)
    elif view == "Last N rows":
        st.dataframe(df.tail(n_rows), use_container_width=True)
    else:
        st.dataframe(df.sample(n=n_rows, random_state=42), use_container_width=True)

    st.divider()
    # Download filtered/full data
    st.download_button(
        label="⬇️ Download full CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="data_export.csv",
        mime="text/csv"
    )
