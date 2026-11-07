import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HR Attrition | Cerlin", layout="wide")
st.title("HR Employee Attrition Analysis")
st.write("By Cerlin Immaculate A | B.E 2026 | Python | MySQL | Power BI")

df = pd.read_csv("HR_Attrition_Cleaned.csv")

# Attrition column ah sari pannu - 1/0, Yes/No ellam handle pannum
df['Attrition'] = df['Attrition'].astype(str).str.strip().str.lower().map({'1':'Yes','1.0':'Yes','yes':'Yes','y':'Yes','true':'Yes','0':'No','0.0':'No','no':'No','n':'No','false':'No'})

if 'OverTime' in df.columns:
    df['OverTime'] = df['OverTime'].astype(str).str.strip().str.lower().map({'1':'Yes','1.0':'Yes','yes':'Yes','y':'Yes','true':'Yes','0':'No','0.0':'No','no':'No','n':'No','false':'No'})
total = len(df)
left = (df['Attrition']=='Yes').sum()
rate = left/total*100

c1,c2,c3 = st.columns(3)
c1.metric("Total Employees", total)
c2.metric("Left", left)
c3.metric("Attrition Rate", f"{rate:.2f}%")

dept = st.sidebar.multiselect("Department", df['Department'].unique(), default=list(df['Department'].unique()))
filtered = df[df['Department'].isin(dept)]

dept_rate = filtered.groupby('Department')['Attrition'].apply(lambda x: (x=='Yes').mean()*100).reset_index()
st.plotly_chart(px.bar(dept_rate, x='Department', y='Attrition', title="Attrition by Department %", color='Department'))

ot_rate = filtered.groupby('OverTime')['Attrition'].apply(lambda x: (x=='Yes').mean()*100).reset_index()
st.plotly_chart(px.bar(ot_rate, x='OverTime', y='Attrition', title="OverTime vs Attrition - 3X Risk", color='OverTime'))

role_rate = filtered.groupby('JobRole')['Attrition'].apply(lambda x: (x=='Yes').mean()*100).sort_values(ascending=False).reset_index()
st.plotly_chart(px.bar(role_rate, x='Attrition', y='JobRole', orientation='h', title="Riskiest Job Roles"))

st.success("Insight: Sales Rep & OverTime employees need urgent follow-up. Reduce OverTime -> Reduce Attrition.")
st.dataframe(filtered.head(20))
