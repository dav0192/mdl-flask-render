from flask import Flask, request, render_template, jsonify;
import joblib;
import pandas as pd;
import logging;

# Creando la instancia de flask
app = Flask(__name__);

# Configurando el registro
logging.basicConfig(level = logging.DEBUG);

# Cargando el modelo entrenado
model = joblib.load('model.pkl');
app.logger.debug('Modelo cargado correctamente.');

# Raiz de la API
@app.route('/')
def home():
    # Devuelve el formulario html
    return render_template("formulario.html");

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # obtener los datos enviados en el request
        plength = float(request.form['plength']);
        pwidth = float(request.form['pwidth']);

        # Crear un DataFrame con los Datos
        data_df = pd.DataFrame([[plength, pwidth]], columns=['PetalLengthCm', 'PetalWidthCm']);
        app.logger.debug(f'Dataframe creado: {data_df}');

        # Realizar predicciones
        prediction = model.predict(data_df);
        app.logger.debug(f'Prediccion: {prediction[0]}');

        # Devolver la respuesta JSON
        return jsonify({'specie': prediction[0]}), 200;
    except Exception as e:
        app.logger.error(f'Error en la predicción: ', {str(e)});
        return jsonify({'error': str(e)}), 400;

# Iniciar la ejecución de la API
if __name__ == '__main__':
    app.run(debug = True);