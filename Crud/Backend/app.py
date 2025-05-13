# Importación de librerías necesarias
from flask import Flask, jsonify, request  # Flask para crear la API, jsonify para respuestas JSON, request para obtener datos del cliente
from flask_cors import CORS  # Para permitir solicitudes desde otros dominios (CORS)
import pymysql  # Conector para MySQL
import bcrypt  # Para cifrar contraseñas
from flasgger import Swagger  # Para documentación Swagger (OpenAPI)

# Inicialización de la aplicación Flask
app = Flask(__name__)  # Crea una instancia de la aplicación Flask
CORS(app)  # Habilita CORS en la aplicación para permitir solicitudes desde otros dominios
swagger = Swagger(app)  # Habilita Swagger para la documentación interactiva de la API

# Configuración de la conexión a la base de datos MySQL
DB_HOST = 'localhost'  # Dirección del host de la base de datos
DB_USER = 'root'  # Nombre de usuario para conectarse a la base de datos
DB_PASS = '0875'  # Contraseña para el usuario de la base de datos
DB_NAME = 'gestor_contrasena'  # Nombre de la base de datos a utilizar

# Función para conectar a la base de datos
def conectar():
    """
    Establece la conexión con la base de datos MySQL.
    :return: objeto de conexión de pymysql
    """
    return pymysql.connect(
        host=DB_HOST,  # Dirección del host
        user=DB_USER,  # Nombre de usuario
        password=DB_PASS,  # Contraseña
        db=DB_NAME,  # Nombre de la base de datos
        charset='utf8mb4'  # Codificación de caracteres
    )

# Ruta para obtener todos los registros del baúl de contraseñas
@app.route("/", methods=['GET'])
def consulta_general():
    """
    Consulta general del baúl de contraseñas.
    ---
    responses:
      200:
        description: Lista de registros del baúl de contraseñas
    """
    try:
        conn = conectar()  # Conexión a la base de datos
        cur = conn.cursor()  # Creación de un cursor para ejecutar la consulta SQL
        cur.execute("SELECT * FROM baul")  # Ejecuta la consulta SQL para obtener todos los registros
        datos = cur.fetchall()  # Recupera todos los resultados de la consulta
        # Estructura los datos en formato JSON
        data = [{'id_baul': row[0], 'Plataforma': row[1], 'usuario': row[2], 'clave': row[3]} for row in datos]
        cur.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos
        return jsonify({'baul': data, 'mensaje': 'Baúl de contraseñas'})  # Devuelve los resultados en formato JSON
    except Exception as ex:
        print(ex)  # Imprime cualquier excepción en la consola
        return jsonify({'mensaje': 'Error'})  # Retorna un mensaje de error en caso de fallo

# Ruta para consultar un registro individual por ID
@app.route('/consulta_individual/<codigo>', methods=['GET'])
def consulta_individual(codigo):
    """
    Consulta individual por ID.
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Registro encontrado
    """
    try:
        conn = conectar()  # Conexión a la base de datos
        cur = conn.cursor()  # Creación de un cursor para ejecutar la consulta SQL
        cur.execute("SELECT * FROM baul WHERE id_baul = %s", (codigo,))  # Consulta por ID específico
        datos = cur.fetchone()  # Recupera un único registro
        cur.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos
        # Si existe el registro, lo devuelve en formato JSON
        if datos:
            dato = {'id_baul': datos[0], 'Plataforma': datos[1], 'usuario': datos[2], 'clave': datos[3]}
            return jsonify({'baul': dato, 'mensaje': 'Registro encontrado'})
        else:
            return jsonify({'mensaje': 'Registro no encontrado'})  # Si no encuentra el registro
    except Exception as ex:
        print(ex)  # Imprime cualquier excepción en la consola
        return jsonify({'mensaje': 'Error'})  # Retorna un mensaje de error

# Ruta para registrar una nueva contraseña
@app.route("/registro", methods=['POST'])
def registro():
    """
    Registra nueva contraseña en el baúl.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            plataforma:
              type: string
            usuario:
              type: string
            clave:
              type: string
    responses:
      200:
        description: Registro agregado correctamente
    """
    try:
        data = request.get_json()  # Obtiene los datos enviados por el cliente en formato JSON
        plataforma = data['plataforma']  # Extrae el nombre de la plataforma
        usuario = data['usuario']  # Extrae el nombre de usuario
        # Cifra la contraseña antes de almacenarla
        clave = bcrypt.hashpw(data['clave'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Conexión a la base de datos
        conn = conectar()
        cur = conn.cursor()
        # Inserta un nuevo registro en la base de datos
        cur.execute("INSERT INTO baul (plataforma, usuario, clave) VALUES (%s, %s, %s)",
                    (plataforma, usuario, clave))
        conn.commit()  # Realiza el commit para guardar los cambios
        cur.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos
        return jsonify({'mensaje': 'Registro agregado'})  # Respuesta en formato JSON
    except Exception as ex:
        print(ex)  # Imprime cualquier excepción en la consola
        return jsonify({'mensaje': 'Error'})  # Retorna un mensaje de error

# Ruta para eliminar un registro por ID
@app.route("/eliminar/<codigo>", methods=['DELETE'])
def eliminar(codigo):
    """
    Eliminar registro por ID.
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Registro eliminado correctamente
    """
    try:
        conn = conectar()  # Conexión a la base de datos
        cur = conn.cursor()  # Creación de un cursor para ejecutar la consulta SQL
        cur.execute("DELETE FROM baul WHERE id_baul = %s", (codigo,))  # Elimina el registro por ID
        conn.commit()  # Realiza el commit para guardar los cambios
        cur.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos
        return jsonify({'mensaje': 'Eliminado'})  # Respuesta en formato JSON
    except Exception as ex:
        print(ex)  # Imprime cualquier excepción en la consola
        return jsonify({'mensaje': 'Error'})  # Retorna un mensaje de error

# Ruta para actualizar un registro existente
@app.route("/actualizar/<codigo>", methods=['PUT'])
def actualizar(codigo):
    """
    Actualizar registro por ID.
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            plataforma:
              type: string
            usuario:
              type: string
            clave:
              type: string
    responses:
      200:
        description: Registro actualizado correctamente
    """
    try:
        data = request.get_json()  # Obtiene los datos enviados por el cliente en formato JSON
        plataforma = data['plataforma']  # Extrae el nombre de la plataforma
        usuario = data['usuario']  # Extrae el nombre de usuario
        # Cifra la nueva contraseña antes de actualizar
        clave = bcrypt.hashpw(data['clave'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = conectar()  # Conexión a la base de datos
        cur = conn.cursor()
        # Actualiza el registro en la base de datos
        cur.execute("UPDATE baul SET plataforma = %s, usuario = %s, clave = %s WHERE id_baul = %s",
                    (plataforma, usuario, clave, codigo))
        conn.commit()  # Realiza el commit para guardar los cambios
        cur.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión a la base de datos
        return jsonify({'mensaje': 'Registro actualizado'})  # Respuesta en formato JSON
    except Exception as ex:
        print(ex)  # Imprime cualquier excepción en la consola
        return jsonify({'mensaje': 'Error'})  # Retorna un mensaje de error

# Punto de entrada de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)  # Inicia la aplicación en modo depuración (debug)