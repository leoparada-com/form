from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ------------------------------------------
@app.route('/', methods=['GET'])
def index():
    return render_template('formulario.html')
# ------------------------------------------


# ------------------------------------------
@app.route('/recibe_datos', methods=['POST'])


def recibe_datos():
# ------------------------------------------    
    valor_a = int(request.form.get('valor_a'))
    valor_b = int(request.form.get('valor_b'))
# ------------------------------------------
    resultado = valor_a + valor_b
    return jsonify({'a': valor_a, 'b': valor_b, 'resultado': resultado})
# ------------------------------------------

if __name__ == '__main__':
    app.run()
