import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Fraud Analytics")

df = pd.read_csv("../synthetic_fraud_dataset1.csv")

col1,col2,col3 = st.columns(3)

col1.metric("Transactions",len(df))
col2.metric("Fraud Cases",df["Fraud_Label"].sum())
col3.metric("Fraud Rate",
            round(df["Fraud_Label"].mean()*100,2))

fig = px.histogram(
    df,
    x="Fraud_Label",
    title="Fraud Distribution"
)

st.plotly_chart(fig,use_container_width=True)

if "Transaction_Type" in df.columns:
    fig2 = px.histogram(
        df,
        x="Transaction_Type",
        color="Fraud_Label"
    )

    st.plotly_chart(fig2,use_container_width=True)
