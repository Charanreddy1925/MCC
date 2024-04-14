import streamlit as st
import pandas as pd
from pickle import load

def create_page():
    st.title('Customer segmentation')
    st.write('Cluster')
    Education = st.sidebar.slider('Education',min_value=0,max_value=2)
    Age = st.sidebar.slider('Choose your age', min_value=10, max_value=80)
    Children = st.sidebar.slider('Children', min_value=0, max_value=3)
    MaritalStatus = st.sidebar.radio('Marital Status', [0, 1], key='Marital_Status')
    Income = st.slider('Income', min_value=1730, max_value=113734)
    Recency = st.sidebar.slider('Recency', min_value=0, max_value=5)
    Wines = st.sidebar.slider('Wines', min_value=0.0, max_value=8.0, step=0.1)
    Fruits = st.sidebar.slider('Fruits', min_value=0.0, max_value=5.0, step=0.1)
    Meatproducts = st.sidebar.slider('Meat Products', min_value=0.0, max_value=7.0, step=0.1)
    Fishproducts = st.sidebar.slider('Fish Products', min_value=0.0, max_value=6.0, step=0.1)
    Sweetproducts = st.sidebar.slider('Sweet Products', min_value=0.0, max_value=6.0, step=0.1)
    MntGoldProds = st.sidebar.slider('MntGoldProds', min_value=0, max_value=6,step=1)
    NumDealsPurchases = st.sidebar.slider('NumDealsPurchases', min_value=0.0, max_value=3.0, step=0.1)
    NumWebPurchases = st.sidebar.slider('NumWebPurchases', min_value=0.0, max_value=4.0, step=0.1)
    NumCatalogPurchases = st.sidebar.slider('NumCatalogPurchases', min_value=0.0, max_value=4.0, step=0.1)
    NumStorePurchases = st.sidebar.slider('NumStorePurchases', min_value=0.0, max_value=4.0, step=0.1)
    NumWebVisitsMonth = st.sidebar.slider('NumWebVisitsMonth', min_value=0.0, max_value=4.0, step=0.1)
    AcceptedCmp1 = st.sidebar.radio('AcceptedCmp1', [0, 1])
    AcceptedCmp2 = st.sidebar.radio('AcceptedCmp2', [0, 1])
    AcceptedCmp3 = st.sidebar.radio('AcceptedCmp3', [0, 1])
    AcceptedCmp4 = st.sidebar.radio('AcceptedCmp4', [0, 1])
    AcceptedCmp5 = st.sidebar.radio('AcceptedCmp5', [0, 1])
    Complain = st.sidebar.slider('Complain', min_value=0.0, max_value=3.0, step=0.1)
    Response = st.sidebar.radio('Response', [0,1], key='Response')

    data1 = {'Education': Education, 'Marital_Status': MaritalStatus, 'Income': Income,
             'Recency': Recency, 'MntWines': Wines, 'MntFruits': Fruits, 'MntMeatProducts': Meatproducts,
             'MntFishProducts': Fishproducts, 'MntSweetProducts': Sweetproducts,'MntGoldProds':MntGoldProds,'NumDealsPurchases': NumDealsPurchases,
             'NumWebPurchases': NumWebPurchases, 'NumCatalogPurchases': NumCatalogPurchases,
             'NumStorePurchases': NumStorePurchases, 'NumWebVisitsMonth': NumWebVisitsMonth,
             'AcceptedCmp3': AcceptedCmp3, 'AcceptedCmp4': AcceptedCmp4, 'AcceptedCmp5': AcceptedCmp5,
             'AcceptedCmp1': AcceptedCmp1,'AcceptedCmp2': AcceptedCmp2, 'Complain': Complain,'Response':Response,'age': Age,'Children': Children}

    df = pd.DataFrame(data1, index=[0])
    return df
features = create_page()

if st.sidebar.button('Submit'):
    st.write(features)

    loaded_model = load(open('clusf.pkl', 'rb'))
    cluster_label = loaded_model.predict(features)

    st.write(f'Belongs to cluster {cluster_label[0]}')

    st.write(cluster_label)

