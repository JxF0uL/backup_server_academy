# start_all.py
from AOEP.settings import BASE_DIR
import subprocess
import threading
import os 

def run_django():
    subprocess.run(["python", "manage.py", "runserver"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "dash.py"])

# Rodar os dois ao mesmo tempo
if __name__ == "__main__":
    threading.Thread(target=run_django).start()
    threading.Thread(target=run_streamlit).start()
