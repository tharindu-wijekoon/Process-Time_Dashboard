import streamlit as st
import pandas as pd
from selections import seSB, heSB, productMS, processtimeMS
from utils import filter

def main():
    st.set_page_config(layout="wide")
    # loadcss("styles.css")

    col1, col2 = st.columns([3,2])
    with col1:
        st.title("Process Time Dashboard")
    with col2:
        file = st.file_uploader("Upload a Process-time CSV file", type=["csv"])

    if file is not None:
        df = pd.read_csv(file)        
        out_df = dashboard(df)
        st.subheader("Table of Process Time Values")
        st.dataframe(out_df, use_container_width=True)
        st.subheader("Bar Chart of Process Time Values")
        barChart(out_df)
    else:
        df = pd.read_csv("../Process-time.csv")
        out_df = dashboard(df)
        st.subheader("Table of Process Time Values")
        st.dataframe(out_df, use_container_width=True)
        st.subheader("Bar Chart of Process Time Values")
        barChart(out_df)


def dashboard(df):
    df = dataProcessor(df)

    if "home" not in st.session_state:
        st.session_state["home"] = 'AIESEC INTERNATIONAL'
    if "host" not in st.session_state:
        st.session_state["host"] = 'AIESEC INTERNATIONAL'
    if "product" not in st.session_state:
        st.session_state["product"] = []
    if "processtime" not in st.session_state:
        st.session_state["processtime"] = []
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        seSB(df)
    with col2:
        heSB(df)
    with col3:
        productMS()
    with col4:
        processtimeMS()

    out_df = filter(df, st.session_state)

    return out_df

def barChart(df):
    try:
        odf_flattened = df.stack(level=["Host", "Process Time", "Product"]).reset_index()
        odf_flattened.columns = ['Home', 'Host', 'Process Time', 'Product', 'Value']

        # st.dataframe(odf_flattened, use_container_width=True)

        chart_data = odf_flattened.groupby(['Home', 'Host', 'Process Time', 'Product']).mean().reset_index()
        

        # Example: Grouping by 'Home' and 'Host' for the bar chart
        chart_data = chart_data.groupby(['Home', 'Host']).agg({'Value': 'mean'}).reset_index()
        chart_data['Concat'] = chart_data['Home'] + ' to ' + chart_data['Host']
        chart_data.drop(['Home', 'Host'], axis=1, inplace=True)
        chart_data = chart_data[['Concat', 'Value']]
        chart_data.set_index('Concat', inplace=True)

        # # Plot the bar chart using Streamlit's built-in bar chart
        return st.bar_chart(chart_data['Value'], use_container_width=True)
    except ValueError as e:
        # Catch specific ValueError (e.g., invalid levels passed to stack)
        return st.warning("Select Product and Process Time")


def dataProcessor(df):
    columns_to_convert = df.columns[10:16]  # Slicing to get columns 10 to 15
    df[columns_to_convert] = df[columns_to_convert].apply(pd.to_datetime, format='%Y-%m-%d %H:%M', errors='coerce')
    columns_to_drop = ['Person ID', 'OP ID', 'Company ID', 'Company Name']
    df.drop(columns_to_drop, axis=1, inplace=True)
    return df

def loadcss(filepath):
    with open(filepath) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()