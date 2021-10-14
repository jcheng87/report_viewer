import streamlit as st
import pandas as pd 

# filter df reports based on col_selected columns. 
def convert_report(df, col_selected):
    return df[col_selected].to_csv(index=False)

# file upload 
file_upload = st.file_uploader('Upload File', type='csv')

# when file is uploaded, output list of columns to filter
if file_upload is not None:
    data = pd.read_csv(file_upload)

    data_columns = data.columns
    
    col_checkbox_clicked = {}

    for col in data_columns:
        col_checkbox_clicked[col] = st.checkbox(col, key=col)

    columns_selected = [col for col,checked_bool in col_checkbox_clicked.items() if checked_bool]

# takes columns selected and runs new report
run_report_button = st.button("Run Report")
if run_report_button: 
    new_report = convert_report(data,columns_selected)

    # button to download new report
    st.download_button("Download", 
                        data=new_report,
                        file_name = 'report.csv'
                        )



