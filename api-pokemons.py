# pyrefly: ignore [missing-import]
from flask import Flask, jsonify, request

app = Flask(__name__)

# Almacenamiento en memoria
pokemons = []
next_id = 1

# Estructura de datos de un Pokémon:
# {
#     "id": int,
#     "nombre": str,
#     "imagen": str,
#     "caracteristicas": {
#         "peso": float,
#         "altura": float,
#         "fuerza": int,
#         "edad": int
#     },
#     "habilidades": list[str],
#     "tipo": str,
#     "habitat": str
# }

@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    """Lista todos los Pokémon"""
    return jsonify(pokemons), 200

@app.route('/pokemons/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    """Obtiene un Pokémon específico por ID"""
    pokemon = next((p for p in pokemons if p['id'] == pokemon_id), None)
    if pokemon:
        return jsonify(pokemon), 200
    return jsonify({"error": "Pokémon no encontrado"}), 404

@app.route('/pokemons', methods=['POST'])
def create_pokemon():
    """Crea un nuevo Pokémon"""
    global next_id
    
    data = request.get_json()
    
    # Validar campos requeridos
    required_fields = ['nombre', 'imagen', 'caracteristicas', 'habilidades', 'tipo', 'habitat']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo '{field}' es requerido"}), 400
    
    # Validar características
    caracteristicas = data['caracteristicas']
    caracteristicas_required = ['peso', 'altura', 'fuerza', 'edad']
    for field in caracteristicas_required:
        if field not in caracteristicas:
            return jsonify({"error": f"Campo 'caracteristicas.{field}' es requerido"}), 400
    
    new_pokemon = {
        "id": next_id,
        "nombre": data['nombre'],
        "imagen": data['imagen'],
        "caracteristicas": {
            "peso": float(caracteristicas['peso']),
            "altura": float(caracteristicas['altura']),
            "fuerza": int(caracteristicas['fuerza']),
            "edad": int(caracteristicas['edad'])
        },
        "habilidades": data['habilidades'],
        "tipo": data['tipo'],
        "habitat": data['habitat'],
        "color": data ['color']
    }
    
    pokemons.append(new_pokemon)
    next_id += 1
    
    return jsonify(new_pokemon), 201

@app.route('/pokemons/<int:pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    """Actualiza la información de un Pokémon por ID"""
    pokemon = next((p for p in pokemons if p['id'] == pokemon_id), None)
    
    if not pokemon:
        return jsonify({"error": "Pokémon no encontrado"}), 404
    
    data = request.get_json()
    
    # Actualizar campos si se proporcionan
    if 'nombre' in data:
        pokemon['nombre'] = data['nombre']
    if 'imagen' in data:
        pokemon['imagen'] = data['imagen']
    if 'caracteristicas' in data:
        caracteristicas = data['caracteristicas']
        if 'peso' in caracteristicas:
            pokemon['caracteristicas']['peso'] = float(caracteristicas['peso'])
        if 'altura' in caracteristicas:
            pokemon['caracteristicas']['altura'] = float(caracteristicas['altura'])
        if 'fuerza' in caracteristicas:
            pokemon['caracteristicas']['fuerza'] = int(caracteristicas['fuerza'])
        if 'edad' in caracteristicas:
            pokemon['caracteristicas']['edad'] = int(caracteristicas['edad'])
    if 'habilidades' in data:
        pokemon['habilidades'] = data['habilidades']
    if 'tipo' in data:
        pokemon['tipo'] = data['tipo']
    if 'habitat' in data:
        pokemon['habitat'] = data['habitat']
    
    return jsonify(pokemon), 200

@app.route('/pokemons/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    """Elimina un Pokémon por ID"""
    pokemon = next((p for p in pokemons if p['id'] == pokemon_id), None)
    
    if not pokemon:
        return jsonify({"error": "Pokémon no encontrado"}), 404
    
    pokemons.remove(pokemon)
    return jsonify({"message": "Pokémon eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
