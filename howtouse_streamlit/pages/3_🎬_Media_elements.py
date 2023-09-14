import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title='미디어 둘러보기',
    page_icon='🎬',
    layout='centered',
)
    
def player_audio():
    sample_rate = 44100  # 44100 samples per second
    seconds = 2  # Note duration of 2 seconds

    frequency_la = 440  # Our played note will be 440 Hz

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * sample_rate, False)

    # Generate a 440 Hz sine wave
    note_la = np.sin(frequency_la * t * 2 * np.pi)
    st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg')

def player_video(video_url):
    video_player = st.video(video_url, format='video/mp4', start_time=0)
    return video_player

def take_a_picture():
    picture = st.camera_input("👁️‍🗨️ Take a picture")
    if picture:
        st.image(picture, caption='...')
    
def display_a_picture(picture):    
    st.image(picture, caption='a woman sitting on a rock')

selectedOption = ''
selectedOption = st.selectbox('Select an option from the selectbox', ['None', 'Audio', 'Video', 'Camera', 'Image'])

if selectedOption == 'Audio':
    player_audio()
elif selectedOption == 'Video':
    video_url = "https://www.youtube.com/watch?v=vbvyNnw8Qjg"
    player_video(video_url)
elif selectedOption == 'Camera':
    take_a_picture()
elif selectedOption == 'Image':
    display_a_picture('woman.jpg')
elif selectedOption == 'None':
    st.info('Please select a right option.', icon='ℹ️')
else:
    pass

# ------------ Sidebar side
sidebarOption = ''
sidebarOption = st.sidebar.selectbox('Select an option from the sidebar.', ['None', 'Audio', 'Video', 'Camera', 'Image'])

if sidebarOption == 'Audio':
    player_audio()
elif sidebarOption == 'Video':
    video_url = "https://www.youtube.com/watch?v=vbvyNnw8Qjg"
    player_video(video_url)
elif sidebarOption == 'Camera':
    take_a_picture()
elif sidebarOption == 'Image':
    display_a_picture('woman.jpg')
elif sidebarOption == 'None':
    st.sidebar.success('Please select a right option.')
else:
    pass
