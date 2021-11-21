import streamlit as st
import pandas as pd 
import os

# filter df reports based on col_selected columns. 
def convert_report(df, col_selected,query_code_input):
    if query_code_input != '':
        df = df.query(query_code_input)
    return df[col_selected]


# file upload 
file_upload = st.file_uploader('Upload File', type=['csv', 'xlsx'])

# when file is uploaded, output list of columns to filter
if file_upload is not None:
    if file_upload.type == 'text/csv':
        base_data = pd.read_csv(file_upload, keep_default_na= False)
    else:
        base_data = pd.read_excel(file_upload, keep_default_na= False)

    report_data = base_data.copy()

    # display shape of dataframe
    st.caption(f"Rows: {report_data.shape[0]}, Columns:{report_data.shape[1]}")

    # text box for query
    query_code_input = st.text_area("Query Code")

    # split app into 3 columns for checkboxes
    app_col1, app_col2, app_col3 = st.columns(3)
    app_cols = [app_col1, app_col2, app_col3]

    # reads column header from report
    column_headers = report_data.columns
    col_checkbox_clicked = {}

    for i, col in enumerate(column_headers): # display checkbox in each of the 3 columns
        col_checkbox_clicked[col] = app_cols[i%3].checkbox(col, key=col)



    # stores in list: checked_cols with True values
    columns_selected = [col for col,checked_bool in col_checkbox_clicked.items() if checked_bool]

    # takes columns selected and runs new report
run_report_button = st.button("Run Report")



if run_report_button: 
    report_data = convert_report(report_data,columns_selected,query_code_input)
    st.caption(f"Rows: {report_data.shape[0]}, Columns:{report_data.shape[1]}")

    # button to download new report
    st.download_button("Download", 
                        data=report_data.to_csv(index=False),
                        file_name = 'report.csv'
                        )



