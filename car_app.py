import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Automobile Exploratory Analysis App", layout="centered")

st.title("Automobile Exploratory Analysis App")
st.write(
    "Bu uygulama, otomobil veri seti üzerinden markaları, yakıt tiplerini ve gövde tiplerini interaktif grafiklerle görselleştirir."
)

@st.cache_data
def load_data():
    return pd.read_csv("cars_ds_final.csv")

try:
    df = load_data()
    st.subheader("Veri Seti On Izleme")
    st.dataframe(df.head())

    st.subheader("Gorsellestirme Paneli")
    chart_type = st.selectbox(
        "Grafik Turunu Seciniz",
        ["En Populer 10 Araba Markasi", "Yakit Tipi Dagilimi", "Govde Tipi Dagilimi"]
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    if chart_type == "En Populer 10 Araba Markasi":
        top_makes = df["Make"].value_counts().head(10)
        sns.barplot(x=top_makes.values, y=top_makes.index, palette="magma", hue=top_makes.index, legend=False, ax=ax)
        ax.set_title("Top 10 Car Brands by Model Count", fontsize=14, fontweight="bold")
        ax.set_xlabel("Number of Models / Variants", fontsize=12)
        ax.set_ylabel("Car Brand", fontsize=12)
    elif chart_type == "Yakit Tipi Dagilimi":
        if "Fuel_Type" in df.columns:
            sns.countplot(x="Fuel_Type", data=df, palette="Set2", order=df["Fuel_Type"].value_counts().index, ax=ax)
            ax.set_title("Distribution of Cars by Fuel Type", fontsize=14, fontweight="bold")
            ax.set_xlabel("Fuel Type", fontsize=12)
            ax.set_ylabel("Count", fontsize=12)
            plt.xticks(rotation=45)
    elif chart_type == "Govde Tipi Dagilimi":
        if "Body_Type" in df.columns:
            top_bodies = df["Body_Type"].value_counts().head(8)
            sns.barplot(x=top_bodies.index, y=top_bodies.values, palette="coolwarm", hue=top_bodies.index, legend=False, ax=ax)
            ax.set_title("Top Car Body Types Distribution", fontsize=14, fontweight="bold")
            ax.set_xlabel("Body Type", fontsize=12)
            ax.set_ylabel("Count", fontsize=12)
            plt.xticks(rotation=45)

    st.pyplot(fig)
except Exception as e:
    st.error(f"Veri yuklenirken veya gorsellestirilirken bir hata olustu: {e}")