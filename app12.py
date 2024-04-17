# -*- coding: utf-8 -*

import pickle
import streamlit as st
from pathlib import Path
import sklearn
print(f"Scikit-learn version: {sklearn.__version__}")
try:
    file_path = Path("svc_model.pkl")
    with file_path.open("rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("File not found: svc_model.pkl")
except pickle.UnpicklingError:
    st.error("Error unpickling the file: svc_model.pkl")
# Function to predict the cluster based on input features
def predict_cluster(Education, Marital_Status, Income, Kids, Expenses,
                    TotalAcceptedCmp, NumTotalPurchases, Customer_Age, Customer_For):
    # Predict the cluster label using the trained model
    prediction = model.predict([[Education, Marital_Status, Income, Kids, Expenses,
                                  TotalAcceptedCmp, NumTotalPurchases, Customer_Age, Customer_For]])
    return prediction

# Main function to create the Streamlit app
def main():
    # Set the title of the app
    st.title('Customer Cluster Prediction')

    # Input fields for user to enter feature values
    Education = st.number_input('Education')
    Marital_Status = st.number_input('Marital Status')
    Income = st.number_input('Income')
    Kids = st.number_input('Kids')
    Expenses = st.number_input('Expenses')
    TotalAcceptedCmp = st.number_input('Total Accepted Campaigns')
    NumTotalPurchases = st.number_input('Total Purchases')
    Customer_Age = st.number_input('Customer Age')
    Customer_For = st.number_input('Customer For')
    
    # Prediction button
    if st.button('Predict'):
        # Call the predict_cluster function with input values
        result = predict_cluster(Education, Marital_Status, Income, Kids, Expenses,
                                 TotalAcceptedCmp, NumTotalPurchases, Customer_Age, Customer_For)
        
        # Display the predicted cluster label
        if result is not None:
            st.success(f'Predicted Cluster: {result[0]}')
        else:
            st.error('Prediction failed.')

# Run the main function
if __name__ == '__main__':
    main()
