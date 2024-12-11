# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos en el contenedor
COPY requirements.txt .


# Copia todo el código fuente al contenedor
COPY . .

# Expone el puerto en el que la aplicación se ejecuta (por ejemplo, 5000 para una app Flask)
EXPOSE 5000

# Comando para ejecutar la aplicación (ajusta esto según tu aplicación)
CMD ["python", "app.py"]
