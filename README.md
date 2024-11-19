# HDU Export Script 📝

Este proyecto es un **script en Python** diseñado para **exportar historias de usuario** desde un proyecto en Jira a archivos de texto (`.txt`). Cada archivo generado utiliza como nombre el **título (summary)** de la historia de usuario y contiene la información detallada de esta.

---


## 🚀 **Funcionalidades**

- **Conexión a Jira:** Utiliza la API de Jira para extraer las historias de usuario de un proyecto específico.
- **Exportación eficiente:** Genera archivos `.txt` con los detalles de cada historia de usuario automáticamente.
- **Nombres descriptivos:** Los archivos `.txt` utilizan el título de la historia de usuario como nombre.


## 🛠️ **Requisitos**

- Python 3.7 o superior
- Librerías necesarias (instalarlas con `pip`):
  ```bash
  pip install requests python-decouple

- Acceso a un proyecto en Jira con las credenciales y permisos adecuados.


## 💡 **Notas Importantes**
El script verifica que la conexión a Jira sea exitosa antes de continuar.
Si una historia de usuario no tiene un título, se asignará un nombre genérico para evitar errores.


## 🧑‍💻 **Contribuciones**
¡Las contribuciones son bienvenidas! Si deseas mejorar este script, crea un fork, realiza tus cambios y envía un Pull Request.

¡Gracias por usar este proyecto! 😊
