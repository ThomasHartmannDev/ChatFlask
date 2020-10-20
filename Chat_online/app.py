from flask import Flask, render_template, request, url_for, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
Socketio = SocketIO(app)


@app.route("/") 
def index():
    return render_template("html/index.html")

@Socketio.on('message')
def messagereceived(data):
    emit('message',data, broadcast=True)


if __name__ == "__main__": 
    Socketio.run(app,use_reloader=True) 