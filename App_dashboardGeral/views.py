from django.shortcuts import render, redirect
from .models import *
import subprocess
from threading import Thread
from django.shortcuts import redirect
from django.http import HttpResponse

def run_streamlit():
    subprocess.run(["streamlit", "run", "dash.py"])

def start_streamlit(request):
    # Roda o Streamlit em um thread separado
    Thread(target=run_streamlit).start()
    
    # Redireciona para o app Streamlit
    return redirect("http://localhost:8501")

def run_streamlit():
    subprocess.run([
        "streamlit",
        "run",
        "dash.py",
        "--server.headless=true"  # Evita abrir navegador
    ])
