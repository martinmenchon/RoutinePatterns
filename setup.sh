mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"martinmenchon@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

#echo "\
#[server]\n\
#headless = true\n\
#enableCORS=false\n\
#enableStaticServing=true\n\
#port = $PORT\n\
#" > ~/.streamlit/config.toml