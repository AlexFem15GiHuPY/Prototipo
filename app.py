from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Clave secreta para la gestión de sesiones

# Lista de productos (puedes ampliarla según sea necesario)
productos = [
    {"id": 1, "nombre": "Chamarra Guchi", "imagen": "producto1.png", "descripcion": "Chamarra calidad/precio, negra con blanco", "precio": 20.00},
    {"id": 2, "nombre": "Crop Top Gotic", "imagen": "Crop Top gotic.png", "descripcion": "Crop Top Gotic", "precio": 25.00}
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/producto/<int:producto_id>', methods=['POST'])
def producto(producto_id):
    producto = next((p for p in productos if p["id"] == producto_id), None)

    if request.method == 'POST' and request.form.get('accion') == 'comprar':
        # Guardar el producto_id en la sesión
        session['producto_id'] = producto_id
        return redirect(url_for('producto_confirmacion'))  # Redirigir a la página de confirmación

    return render_template('producto.html', producto=producto)

@app.route('/confirmacion')
def producto_confirmacion():
    # Obtener el producto_id desde la sesión o de alguna otra manera según tu implementación
    producto_id = session.get('producto_id')  # Esto es solo un ejemplo, ajusta según tu lógica

    # Recuperar información del producto (sustituye esto con tu lógica)
    producto = next((p for p in productos if p["id"] == producto_id), None)

    return render_template('confirmacion.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)
