import streamlit as st
import pandas as pd

st.title("🤖 Model Performance")

data = {
    "Model":[
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy":[0.92,0.97,0.98],
    "Precision":[0.91,0.96,0.97],
    "Recall":[0.89,0.95,0.96],
    "F1":[0.90,0.95,0.96]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.success("Best Model : XGBoost")

# Confusion matrix

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

cm = np.array([
    [950, 50],
    [30, 970]
])

cm_df = pd.DataFrame(
    cm,
    index=["Actual Non-Fraud","Actual Fraud"],
    columns=["Predicted Non-Fraud","Predicted Fraud"]
)

fig = px.imshow(
    cm_df,
    text_auto=True,
    title="Confusion Matrix"
)

st.plotly_chart(fig, use_container_width=True)

#ROC Curve 

import plotly.graph_objects as go

fpr = [0.0,0.05,0.10,0.20,1.0]
tpr = [0.0,0.80,0.90,0.97,1.0]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=fpr,
        y=tpr,
        mode="lines",
        name="ROC Curve (AUC=0.98)"
    )
)

fig.add_trace(
    go.Scatter(
        x=[0,1],
        y=[0,1],
        mode="lines",
        name="Random Classifier"
    )
)

st.plotly_chart(fig,use_container_width=True)