import streamlit as st
import atexit
from db.db_functions import *

st.set_page_config(
    page_title='🎨 GUI 개발도구 소개',
    page_icon='🛠️',
    layout='wide',
)

def main():
    st.subheader("🎨 Streamlit : A Popular GUI Development Tool")

    st.markdown("""---""")
    
    st.markdown("""
    :star: Streamlit은 Python으로 웹 애플리케이션을 개발하기 위한 프레임워크입니다.\n
    :smile: Streamlit을 사용하면 간단한 코드만으로 데이터 시각화, 웹 양식, 대화형 요약 등 다양한 기능을 갖춘 웹 애플리케이션을 개발할 수 있습니다.\n
    ##
    📑 :red[**Streamlit의 주요 특징**]\n
    :coffee: Streamlit은 Python으로 개발된 라이브러리이기 때문에, Python에 대한 기본적인 지식이 있으면 누구나 쉽게 사용할 수 있습니다.\n
    :coffee: 빠른 개발 Streamlit은 HTML, CSS, JavaScript를 사용하지 않고 Python으로만 개발되기 때문에 빠르게 개발할 수 있습니다.\n
    :coffee: 데이터 시각화, 웹 양식, 대화형 요약 등 다양한 기능을 사용하여 사용자에게 직관적인 경험을 제공할 수 있습니다.\n
    ##
    📑 :green[**Streamlit의 용도**]\n
    :coffee: 데이터 시각화 Streamlit을 사용하여 데이터를 시각적으로 표현할 수 있습니다.\n
    :coffee: 웹 양식 Streamlit을 사용하여 사용자로부터 데이터를 입력받을 수 있습니다.\n
    :coffee: 대화형 요약 Streamlit을 사용하여 데이터를 대화식으로 요약할 수 있습니다.\n
    ##
    📑 :blue[**Streamlit의 장점**]\n
    :coffee: 배우기 쉽습니다. Streamlit은 Python으로 개발되므로, Python에 대한 기본적인 지식이 있으면 누구나 쉽게 사용할 수 있습니다.\n
    :coffee: 빠르게 개발할 수 있습니다. Streamlit은 HTML, CSS, JavaScript를 사용하지 않고 Python으로만 개발되기 때문에 빠르게 개발할 수 있습니다.\n
    :coffee: 강력하고 다양한 기능을 제공합니다. 데이터 시각화, 웹 양식, 대화형 요약 등 다양한 기능을 사용하여 사용자에게 직관적인 경험을 제공할 수 있습니다.         
    """)
    
    st.markdown("##")
    
    
    # --- Program 종료 시 후 처리 기능 등록 
    
    def on_exit():
        connection.close()

    atexit.register(on_exit)

if __name__ == '__main__':
    main()