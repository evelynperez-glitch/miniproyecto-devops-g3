# API CRUD de Pokémon con Flask

Este proyecto es una API REST que permite gestionar información de Pokémon mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar). 
La información se mantiene en memoria durante la ejecución de la aplicación.

## Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone <https://github.com/evelynperez-glitch/miniproyecto-devops-g3.git>
cd miniproyecto-devops
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

O instalar Flask directamente:
```bash
pip install flask
```

## Ejecución

Para iniciar la API, ejecutar:

```bash
python api-pokemons.py
```

La API estará disponible en `http://localhost:5000`

## Rutas de la API

### 1. Obtener todos los Pokémon
**GET** `/pokemons`

Retorna una lista con todos los Pokémon registrados.

**Ejemplo:**
```powershell
Invoke-RestMethod -Method Get -Uri "http://localhost:5000/pokemons"
```

### 2. Obtener un Pokémon por ID
**GET** `/pokemons/<id>`

Retorna la información de un Pokémon específico.

**Ejemplo:**
```powershell
Invoke-RestMethod -Method Get -Uri "http://localhost:5000/pokemons"
```

### 3. Crear un nuevo Pokémon
**POST** `/pokemons`

Crea un nuevo Pokémon con los datos proporcionados en el archivo `pokemon.json`.

**Ejemplo (PowerShell):**
```powershell
$body = Get-Content "pokemon.json" -Raw; Invoke-RestMethod -Uri "http://localhost:5000/pokemons" -Method Post -Body $body -ContentType "application/json"
```

**Ejemplo (PowerShell):**
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/pokemons/1" -Method Put -Body $body -ContentType "application/json"
```

### 4. Actualizar un Pokémon
**PUT** `/pokemons/<id>`

Actualiza la información de un Pokémon existente. Solo se actualizan los campos proporcionados.

**Ejemplo:**
```powershell
$body = @{ nombre = "Pikachu Actualizado"; caracteristicas = @{ fuerza = 60 } } | ConvertTo-Json -Depth 10; Invoke-RestMethod -Uri "http://localhost:5000/pokemons/1" -Method Put -Body $body -ContentType "application/json"
```

### 5. Eliminar un Pokémon
**DELETE** `/pokemons/<id>`

Elimina un Pokémon de la lista.

**Ejemplo:**
```powershell
Invoke-RestMethod -Method Delete -Uri "http://localhost:5000/pokemons/1"
```

## Estructura de Datos

Cada Pokémon tiene la siguiente estructura:

```json
{
  "id": 1,
  "nombre": "Pikachu",
  "imagen": "https://link_a_imagen.jpg",
  "caracteristicas": {
    "peso": 6.0,
    "altura": 0.4,
    "fuerza": 55,
    "edad": 5
  },
  "habilidades": ["Impactrueno", "Cola férrea"],
  "tipo": "Eléctrico",
  "habitat": "Bosques"
}
```