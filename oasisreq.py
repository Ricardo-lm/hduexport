import requests
import json

# Configuración
jira_url = "Aqui va la url de tu proyecto en Jira"
auth = ("Aqui va tu correo", "Aqui va el token API")
query = {
    "jql": "project = TU_PROYECTO AND issuetype = Historia",  # Cambia TU_PROYECTO por la clave de tu proyecto
    "maxResults": 100,  # Número máximo de historias que deseas obtener
    "fields": ["summary", "description"]  # Campos que deseas incluir
}

# Llamada a la API
response = requests.get(jira_url, auth=auth, params=query)

if response.status_code == 200:
    issues = response.json().get("issues", [])
    
    # Procesar cada historia de usuario
    for issue in issues:
        key = issue["key"]  # Identificador de la historia (e.g., ABC-123)
        fields = issue["fields"]
        summary = fields.get("summary", "Sin resumen")
        description = fields.get("description", "Sin descripción")
        
        # Crear contenido del archivo
        content = f"""Historia de Usuario: {key}
====================
Resumen: {summary}

Descripción:
{description}


"""
        # Crear el archivo .txt
        with open(f"{summary}.txt", "w", encoding="utf-8") as file:
            file.write(content)

    print("Historias de usuario exportadas exitosamente a archivos .txt")
else:
    print(f"Error al conectarse a Jira: {response.status_code} - {response.text}")
