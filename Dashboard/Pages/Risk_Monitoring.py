import streamlit as st
import pandas as pd

st.title("📈 Risk Monitoring")

df = pd.read_csv("../synthetic_fraud_dataset1.csv")

fraud_df = df[
    df["Fraud_Label"]==1
]

st.dataframe(
    fraud_df.head(100)
)
