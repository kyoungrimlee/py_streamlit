import streamlit as st
import pandas as pd
import pymysql as db

conn = db.connect(
    host='10.1.100.30',
    user='cybertel',
    password='Everytalk2359@#%(',
    database='mcptt_server',
    charset='utf8'
)


st.title('Mysql DB 연동')

# Query the database and load data into a DataFrame
#query = "SELECT KEYDATE, sum(DURATION) FROM pttkey_history group by KEYDATE"

tab1, tab2, tab3 = st.tabs(["sec_sprov", "sec_init", "ptt_admin"])

with tab1:
   st.header("sec_sprov DATA")
   query = "SELECT * FROM sec_sprov "
   df = pd.read_sql(query, conn)
   df

with tab2:
   st.header("sec_init DATA")
   query = "SELECT * FROM sec_init "
   df = pd.read_sql(query, conn)
   df

with tab3:
   st.header("ptt_admin DATA")
   query = "SELECT * FROM ptt_admin "
   df = pd.read_sql(query, conn)
   df



# Close the database connection
conn.close()
