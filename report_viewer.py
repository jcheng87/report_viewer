import streamlit as st
import pandas as pd 

def convert_report(df):
    return df[columns_selected].to_csv(index=False)

file_upload = st.file_uploader('Upload File', type='csv')


if file_upload is not None:
    data = pd.read_csv(file_upload)

    data_columns = data.columns

    columns_selected = st.multiselect("Column Names:",
                                        data_columns,
                                        )

run_report_button = st.button("Run Report")

if run_report_button: 
    new_report = convert_report(data)



    st.download_button("Download", 
                        data=new_report,
                        file_name = 'report.csv'
)



