from flask import Flask, jsonify, request, abort

app = Flask(__nam
temas = []
categorias = []

@app.route('/temas', methods=['GET'])
def get_temas():
    return jsonify(temas)

@app.route('/temas', methods=['POST'])
def create_tema():
    if not request.json or not 'nome' in request.json:
        abort(400)
    novo_tema = {
        'id': len(temas) + 1,
        'nome': request.json['nome']
    }
    temas.append(novo_tema)
    return jsonify(novo_tema), 201

@app.route('/temas/<int:tema_id>', methods=['PUT'])
def update_tema(tema_id):
    tema = next((t for t in temas if t['id'] == tema_id), None)
    if tema is None:
        abort(404)
    if not request.json:
        abort(400)
    tema['nome'] = request.json.get('nome', tema['nome'])
    return jsonify(tema)

@app.route('/temas/<int:tema_id>', methods=['DELETE'])
def delete_tema(tema_id):
    tema = next((t for t in temas if t['id'] == tema_id), None)
    if tema is None:
        abort(404)
    temas.remove(tema)
    return '', 204

@app.route('/categorias', methods=['GET'])
def get_categorias():
    return jsonify(categorias)

@app.route('/categorias', methods=['POST'])
def create_categoria():
    if not request.json or not 'nome' in request.json:
        abort(400)
    nova_categoria = {
        'id': len(categorias) + 1,
        'nome': request.json['nome']
    }
    categorias.append(nova_categoria)
    return jsonify(nova_categoria), 201

@app.route('/categorias/<int:categoria_id>', methods=['PUT'])
def update_categoria(categoria_id):
    categoria = next((c for c in categorias if c['id'] == categoria_id), None)
    if categoria is None:
        abort(404)
    if not request.json:
        abort(400)
    categoria['nome'] = request.json.get('nome', categoria['nome'])
    return jsonify(categoria)

@app.route('/categorias/<int:categoria_id>', methods=['DELETE'])
def delete_categoria(categoria_id):
    categoria = next((c for c in categorias if c['id'] == categoria_id), None)
    if categoria is None:
        abort(404)
    categorias.remove(categoria)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
