import streamlit as st
import pandas as pd

st.title('Hello Streamlit')
view = [100, 150, 30]

st.write('# Youtube View')
st.write('## raw')
view
st.write('## bar chart')
#st.bar_chart(data=view, *, x=None, y=None, color=None, width=0, height=0, use_container_width=True)
st.bar_chart(view)

sview= pd.Series(view)

sview