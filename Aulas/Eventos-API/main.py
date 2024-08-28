from flask import Flask, jsonify
from evento import Evento
from evento_online import EventoOnline
import json

app = Flask(__name__)


ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")
ev = Evento("Aula de Python", "Santa Catarina")
eventos = [ev_online, ev2_online, ev]

@app.route("/")
def index():
    return "<h1> Flask é configurado com sucesso!</h1>"

@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
        eventos_dict.append(ev.__dict__)
    return jsonify(eventos_dict)