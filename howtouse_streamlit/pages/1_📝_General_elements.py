import streamlit as st

st.set_page_config(
    page_title='입출력 둘러보기',
    page_icon='📝',
    layout='centered',
)

button_result=st.button('Click me')
st.success(f'button status is {button_result}')
st.markdown("""---""")

check_result=st.checkbox('I agree')
st.success(f'checkbox status is {check_result}')
st.markdown("""---""")

radio_result=st.radio('Pick one', ['cats', 'dogs'])
st.success(f'radio status is {radio_result}')
st.markdown("""---""")

selectbox_result=st.selectbox('Pick one', ['cats', 'dogs'])
st.success(f'selectbox is {selectbox_result}')
st.markdown("""---""")

multiselect_result=st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.info(f'multiselect status is {multiselect_result}', icon='ℹ️')
st.markdown("""---""")

slider_result=st.slider('Pick a number', 0, 100)
st.info(f'slider status is {slider_result}')
st.markdown("""---""")

select_slider_result=st.select_slider('Pick a size', ['S', 'M', 'L'])
st.info(f'select_slider status is {select_slider_result}')
st.markdown("""---""")

text_input_result=st.text_input('First name')
st.info(f'text_input is [{text_input_result}]')
st.markdown("""---""")

number_result=st.number_input('Pick a number', 0, 10)
st.info(f'number is {number_result}')
st.write(number_result)
st.markdown("""---""")

text_result=st.text_area('Text to translate')
st.info(f'Text is [{text_result}]')
st.markdown("""---""")

date_result=st.date_input('Your birthday')
st.info(f'Date is {date_result}')
st.markdown("""---""")

time_result=st.time_input('Meeting time')
st.info(f'time is {time_result}')
st.markdown("""---""")

file_result=st.file_uploader('Upload a file')
st.info(f'filename is {file_result}')
st.markdown("""---""")

color_result=st.color_picker('Pick a color')
st.info(f'color is {color_result}')
st.markdown("""---""")