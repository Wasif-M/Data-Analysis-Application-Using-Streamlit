import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import graph_objs as go

st.title('Data Analysis Application')

dataset_options=['iris','titanic','diamonds','tips']
select_dataset=st.selectbox("Select Dataset",dataset_options)

if select_dataset=='iris':
    df=sns.load_dataset('iris')
elif select_dataset=='diamonds':
    df=sns.load_dataset('diamonds')
elif select_dataset=='titanic':
    df=sns.load_dataset('titanic')
else:
    df=sns.load_dataset('tips')

file_upload=st.file_uploader("Upload a file",type=['csv','xlsx'])
if file_upload is not None:
    df=pd.read_csv(file_upload)

st.write(df)

st.write("Number of Rows",df.shape[0])
st.write("Number of Columns",df.shape[1])
st.write('Columns Names and their Datatypes',df.dtypes)

if df.isnull().sum().sum() >  0:
    st.write('Missing Values',df.isnull().sum().sort_values(ascending=False))
else:
    st.write('No Missing Values')

st.write('Descriptive Statistics',df.describe())

st.subheader("Pairplot")
hue_Select=st.selectbox("Select a column used for Hue",df.columns)
st.pyplot(sns.pairplot(df,hue=hue_Select))

st.subheader("Correlation Heatmap")
numeric_columns=df.select_dtypes(include=np.number).columns
corr_matrix=df[numeric_columns].corr()
numeric_columns=df.select_dtypes(include=np.number).columns
corr_matrix=df[numeric_columns].corr()
heatmap_fig=go.Figure(data=go.Heatmap(z=corr_matrix.values,x=corr_matrix.columns,y=corr_matrix.columns,colorscale='Viridis'))
st.plotly_chart(heatmap_fig)