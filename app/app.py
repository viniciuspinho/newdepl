from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Nova versão deploy automático de novo com notificação de e-mail🔥"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
