mkdir -p ~/.streamlit
mkdir -p ~/files

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml