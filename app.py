import os
import pandas as pd
from sqlalchemy import create_engine, text
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def ping():
    data = {
        "code": 200,
        "response": "Respuesta desde API en Docker"
	}
    return jsonify(data)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
@app.route('/productos')
def productos():
    
    query = "SELECT * FROM productos LIMIT 10"
    
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)

    if not df.empty:
        
        lista_productos = []
        
        for _, row in df.iterrows():
            item = {
                "id": int(row['id']),
                "name": row['nombre'], 
                "price": float(row['precio'])
            }
            lista_productos.append(item)
            
        return jsonify({
            "code": 200,
            "total": len(lista_productos),
            "data": lista_productos
        })
    
    return jsonify({"code": 404, "message": "No se encontraron productos"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
