import streamlit as st
import pandas as pd

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="CSV Data Cleaning Tool",
    page_icon="🧹",
    layout="centered"
)

# ---------------------------
# Hide Streamlit default UI
# ---------------------------
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------------------
# Title and description
# ---------------------------
st.title("🧹 CSV Data Cleaning Tool")

st.markdown(
    """
Upload one or multiple CSV files to clean, merge, and download them easily.

**Features:**
- Upload multiple CSV files
- Merge files safely
- Remove duplicate rows
- Remove empty rows
- Download cleaned data
"""
)

# ---------------------------
# File uploader
# ---------------------------
uploaded_files = st.file_uploader(
    "Choose CSV files",
    type="csv",
    accept_multiple_files=True
)

# ---------------------------
# Helper Functions
# ---------------------------

def load_csv(file):
    """Load CSV safely into DataFrame."""
    try:
        file.seek(0)
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Error reading file {file.name}: {e}")
        return None


def align_columns(reference_df, df):
    """Align columns with reference dataframe."""
    common_columns = reference_df.columns.intersection(df.columns)
    return df[common_columns]


def clean_dataframe(df, remove_duplicates, remove_empty):
    """Apply cleaning operations."""
    if remove_duplicates:
        df = df.drop_duplicates()

    if remove_empty:
        df = df.dropna(how="all")

    return df


# ---------------------------
# Main Logic
# ---------------------------
if not uploaded_files:
    st.warning("Please upload at least one CSV file.")
    st.stop()

# Load files
dataframes = []

for file in uploaded_files:
    df = load_csv(file)
    if df is not None:
        dataframes.append(df)

# ---------------------------
# Merge Options
# ---------------------------
if len(dataframes) > 1:

    st.subheader("Merge Options")

    merge_files = st.checkbox("Merge uploaded CSV files")

    if merge_files:

        keep_first_header_only = st.selectbox(
            "Use first file as column reference",
            ["Yes", "No"]
        )

        remove_duplicates_option = st.selectbox(
            "Remove duplicate rows",
            ["Yes", "No"]
        )

        remove_empty_option = st.selectbox(
            "Remove empty rows",
            ["Yes", "No"]
        )

        try:

            # Align columns if selected
            if keep_first_header_only == "Yes":
                reference_df = dataframes[0]
                for i in range(1, len(dataframes)):
                    dataframes[i] = align_columns(reference_df, dataframes[i])

            # Merge
            merged_df = pd.concat(
                dataframes,
                ignore_index=True,
                join="outer"
            )

            # Clean merged data
            merged_df = clean_dataframe(
                merged_df,
                remove_duplicates_option == "Yes",
                remove_empty_option == "Yes"
            )

            # Replace list with merged dataframe
            dataframes = [merged_df]

            st.success("Files merged successfully.")

        except Exception as e:
            st.error(f"Error during merging: {e}")
            st.stop()

# ---------------------------
# Show DataFrames
# ---------------------------
st.subheader("Preview")

show_dataframes = st.checkbox("Show DataFrames")

if show_dataframes:

    for i, df in enumerate(dataframes):

        st.write(f"DataFrame {i+1}")
        st.dataframe(df, use_container_width=True)

# ---------------------------
# Download Section
# ---------------------------
st.subheader("Download Cleaned Data")

for i, df in enumerate(dataframes):

    csv = df.to_csv(index=False)

    st.download_button(
        label=f"Download cleaned_data_{i+1}.csv",
        data=csv,
        file_name=f"cleaned_data_{i+1}.csv",
        mime="text/csv"
    )

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")

st.markdown(
    "<p style='text-align:center'>"
    "<a href='https://ghttps://github.com/abioludipe' target='_blank'>GitHub</a> "
    "</p>",
    unsafe_allow_html=True
)
