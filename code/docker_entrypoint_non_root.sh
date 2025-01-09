"/bin/sh" ./generate_envconfig.sh > ./.env
ls -aL
"/bin/bash" -c "streamlit run app.py --server.port=8080"