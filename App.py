from flask import Flask,request,jsonify,render_template
import sqlite3
from datetime import datetime


app = Flask (__name__)
DB = "creditos.db"

#Conexión a la base de datos
def conectar():
    return sqlite3.connect(DB)

#Validación de la fecha
def validar_fecha(fecha):
    try:
        datetime.strptime(fecha,"%Y-%m-%d")
        return True
    except ValueError:
        return False
    
#Crear tabla en la base de datos
conexion = conectar()
cursor = conexion.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS creditos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT NOT NULL,
        monto REAL NOT NULL,
        tasa_interes REAL NOT NULL,
        plazo INTEGER NOT NULL,
        fecha_otorgamiento TEXT NOT NULL
        );
        """)
conexion.commit()
conexion.close()


#API CRUD
#Mostrar
@app.route("/api/creditos",methods=["GET"])
def mostrar_creditos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM creditos")
    rows = cursor.fetchall()
    conexion.close()

    creditos = [
        {
            "id": row[0],
            "cliente": row[1],
            "monto": row[2],
            "tasa_interes": row[3],
            "plazo": row[4],
            "fecha_otorgamiento": row[5]
        }
        for row in rows
    ]
    return jsonify(creditos)

#Insertar creditos
@app.route("/api/creditos",methods=["POST"])
def insertar_credito():
    data = request.get_json()
    cliente = data.get("cliente")
    monto = data.get("monto")
    tasa_interes = data.get("tasa_interes")
    plazo = data.get("plazo")
    fecha_otorgamiento = data.get("fecha_otorgamiento")

    if not validar_fecha(fecha_otorgamiento):
        return jsonify({"error": "La fecha debe contener el siguiente formato YYYY-MM-DD"}),400
    
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
       INSERT INTO creditos (cliente,monto,tasa_interes,plazo,fecha_otorgamiento)
       VALUES (?,?,?,?,?)
       """, (cliente,monto,tasa_interes,plazo,fecha_otorgamiento))
    conexion.commit()
    credito_id = cursor.lastrowid
    conexion.close()

    return jsonify({"id": credito_id}),201

#Editar creditos
@app.route("/api/creditos/<int:credito_id>",methods=["PUT"])
def actualizar_credito(credito_id):
    data = request.get_json()

    campos = []
    valores = []
    
    for db_fecha, validar in data.items():
        if db_fecha == "fecha_otorgamiento" and not validar_fecha(validar):
            return jsonify({"error":"La fecha debe contener el siguiente formato YYYY-MM-DD"}),400
        if db_fecha in ("cliente","monto","tasa_interes","plazo","fecha_otorgamiento"):
            campos.append(f"{db_fecha} = ?")
            valores.append(validar)

    if not campos:
        return jsonify({"error": "Campos no validos para actualizar"}),400
    
    valores.append(credito_id)

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(f"UPDATE creditos SET {','.join(campos)} WHERE id = ?", valores)
    conexion.commit()
    actualizado = cursor.rowcount
    conexion.close()

    if actualizado:
        return jsonify({"mensaje": "Credito actualizado"})
    else:
        return jsonify({"error": "Credito no actualizado"}),404

#Eliminar creditos
@app.route("/api/creditos/<int:credito_id>",methods=["DELETE"])
def eliminar_credito(credito_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM creditos WHERE id= ?",(credito_id,))
    conexion.commit()
    eliminado = cursor.rowcount
    conexion.close()
    
    if eliminado:
        return jsonify({"mensaje": "Credito eliminado"})
    else:
        return jsonify({"error": "Credito no encontrado"}),400
    
#Llamar al frontend
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    


