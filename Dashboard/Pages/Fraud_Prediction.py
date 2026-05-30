import streamlit as st

st.title("🚨 Fraud Prediction")

amount = st.number_input(
    "Transaction Amount",
    0.0
)

previous = st.selectbox(
    "Previous Fraud Activity",
    [0,1]
)

if st.button("Predict"):

    if amount > 5000 or previous == 1:

        st.error(
            "High Fraud Risk"
        )

    else:

        st.success(
            "Low Fraud Risk"
        )
