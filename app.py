from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def ping():
    data = {
        "code": 200,
        "response": "Respuesta desde API en Docker"
	}
    return jsonify(data)


@app.route('/productos')
def productos():
    data = {
	"code"  : 200,
        "id"    : 1,
        "name"  : "Martillo",
	"price" : 5000,
	"img"   : "https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/512x512/hammer.png"
        }
  
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
