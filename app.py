from flask import Flask;

app = Flask(__name__);

# Raiz de la API
@app.route('/')
def home():
    return "Hola Mundo"

# Iniciar la ejecución de la API
if __name__ == '__main__':
    app.run(debug = True);