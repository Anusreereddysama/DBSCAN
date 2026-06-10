import streamlit as st
from src.predict import preprocess_input

st.set_page_config(
    page_title="DBSCAN Clustering"
)

st.title(
    "📊 Customer Segmentation using DBSCAN"
)

income = st.number_input(
    "Annual Income (k$)",
    min_value=0.0,
    max_value=150.0
)

score = st.number_input(
    "Spending Score",
    min_value=0.0,
    max_value=100.0
)

if st.button("Analyze"):

    preprocess_input(
        income,
        score
    )

    st.success(
        "Customer data processed successfully!"
    )

    st.info(
        "DBSCAN identifies clusters based on density and does not directly predict clusters for unseen data."
    )