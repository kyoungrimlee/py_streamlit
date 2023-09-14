import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='데이터프레임 둘러보기',
    page_icon='🎹',
    layout='centered',
)

st.subheader('📅 General dataframe with editable')

df = pd.DataFrame(
    [
       {"tourist attraction": "설악산", "ranking": 1},
       {"tourist attraction": "한라산", "ranking": 2},
       {"tourist attraction": "뒷동산", "ranking": 3},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic", hide_index=False)

favorite_command = edited_df.loc[edited_df["ranking"].idxmin()]["tourist attraction"]
st.markdown(f"Your favorite tourist attraction is **{favorite_command}** 🎈")
st.markdown("""---""")

st.subheader('📅 Add a CheckboxColumn')

data_df = pd.DataFrame(
    {
        "nations": ["France", "USA", "China", "UK"],
        "favorite": [True, True, False, True],
    }
)

st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** nations",
            default=False,
        )
    },
    disabled=["nations"],
    hide_index=False,
)

st.markdown("""---""")

st.subheader('📅 Display a Dataframe as ImageColumn')

data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=False,
)

st.markdown("""---""")

st.subheader('📅 Display External File (예: Excel, CSV)')

filename = st.file_uploader("Upload an Excel file", type=['xlsx', 'csv'])

if filename is not None:
    df_file = pd.read_excel(filename, sheet_name="Sheet1")
    
    st.data_editor(
        df_file,
        hide_index=True,
    )
    
st.markdown("""---""")