import streamlit as st
from PIL import Image
import json

# import SessionState
# session_state = SessionState.get(loaded=False,day=[],upload_key = None,values_to_keep=[], trasnparency=-1)
# import pathlib

# STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
# DOWNLOADS_PATH = (STREAMLIT_STATIC_PATH / "downloads")
# if not DOWNLOADS_PATH.is_dir():
#     DOWNLOADS_PATH.mkdir()


# Paths
original_path = "graphics_results/original/"
farinella_path = "graphics_results/Farinella/"
our_algorithm_path = "graphics_results/our_algorithm/"
patterns_path = "patterns/our_algorithm/"
ngrams_path = "ngrams/"

st.set_page_config(
    page_title="Behavioural patterns discovery for lifestyle analysis from egocentric photo-streams",
    page_icon="favicon.png",
    layout="wide",
    #initial_sidebar_state="expanded",
)

#Remove button
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#Containers
header = st.beta_container()
body = st.beta_container()
body1 = st.beta_container()
body2 = st.beta_container()

with header:
    st.markdown("<h1 style='text-align: center;'>Behavioural patterns discovery for lifestyle analysis from egocentric photo-streams</h1>", unsafe_allow_html=True)
    st.markdown("* [Martín Menchón](mailto:mmenchon@exa.unicen.edu.ar)", unsafe_allow_html=True)
    st.markdown("* [Estefanía Talavera](mailto:e.talavera.martinez@rug.nl)", unsafe_allow_html=True)
    st.markdown("* [José M. Massa](mailto:jmassa@exa.unicen.edu.ar)", unsafe_allow_html=True)
    st.markdown("* [Petia I. Radeva](mailto:petia.ivanova@ub.edu)", unsafe_allow_html=True)
with body:
    users = ["user_01","user_02","user_03","user_04","user_05","user_06","user_07","user_08","user_09","user_10","user_11","user_12","user_13","user_14"]
    user = st.selectbox('Select an user',users)
    'You selected: ', user

    image = Image.open(original_path+user+'.jpg')
    st.image(image)
    st.write("---")

    options = ["Our algorithm","Organizing egocentric videos of daily living activities"]
    option = st.selectbox('Select an algorithm',options)

    if option == 'Our algorithm':
        thresholds = ["0.02","0.03","0.035","0.04","0.05"]
        threshold = st.selectbox('Select a threshold',thresholds)
        try:
            im = Image.open(our_algorithm_path+user+'/'+threshold+'.jpg')
            st.image(im)
            st.write("---")
            st.write('## Patterns for '+user+" at "+threshold)

            if st.button('Show found patterns'):
                json_path = patterns_path+user+"/"+threshold+".json"
                with open(json_path) as json_file:
                    data = json.load(json_file)
                for p in data:
                    my_expander = st.beta_expander("Pattern "+str(p), expanded=False)
                    with my_expander:
                        st.write(data[p])
                        pattern_image_path = patterns_path+user+"/"+threshold+"/"+p+".jpg"
                        pattern_image = Image.open(pattern_image_path)
                        st.image(pattern_image)
            
            st.write('## Ngrams for '+user+" at "+threshold)
            if st.button('Show found ngrams'):
                json_path = ngrams_path+user+"/"+threshold+".json"
                with open(json_path) as json_file:
                    dic_of_ngrams = json.load(json_file)
                # print(data)
                patterns_days = dic_of_ngrams["Day as patterns"]
                st.write('### Day as patterns:')
                for p in patterns_days:
                    st.write(p)
                

                ngrams = dic_of_ngrams["Found n-grams"]
                st.write('### Found n-grams:')
                for n in ngrams:
                    st.write(n)
                im = Image.open(ngrams_path+user+'/'+threshold+'.jpg')
                st.image(im)
        
        except:
            st.write("There is no patterns for this threshold")

    else:
        im = Image.open(farinella_path+user+'.jpg')
        st.image(im)