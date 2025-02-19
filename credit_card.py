import streamlit as st
import numpy as np
from joblib import load


try:
    model = load("credit_card_model.pkl")
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

st.title("Credit Card Fraud Prediction")


user_input = st.text_area("Enter feature values separated by commas:")

if st.button("Predict"):
    try:
        data_array = np.array([float(x) for x in user_input.split(",")]).reshape(1, -1)


        if data_array.shape[1] != model.n_features_in_:
            st.error(f"Error: The model expects {model.n_features_in_} features, but received {data_array.shape[1]}.")
        else:

            prediction = model.predict(data_array)

            if prediction[0] == 1:
                st.error("⚠️ Warning! The model detected a potential fraud!")
            else:
                st.success("✅ The transaction appears to be safe.")

    except ValueError:
        st.error("Error: Please ensure that all input values are numeric and separated by commas.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
