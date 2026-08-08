# 🎯 Detector de Objetos en Tiempo Real

Aplicación web que detecta objetos en tiempo real usando la cámara del navegador, construida con **YOLOv8** y **Streamlit**. Identifica hasta 80 categorías de objetos (personas, animales, vehículos, objetos cotidianos) con etiquetas traducidas al español.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Tabla de contenidos

- [Demo](#-demo)
- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Cómo funciona](#-cómo-funciona)
- [Autor](#-autor)

## 🚀 Demo

🔗 **[Ver demo en vivo](https://detector-objetos-yolo-74iz8qxrpsplgpkggbwzfc.streamlit.app/)**
![Demo del detector de objetos](#)
*(agregar captura o GIF de la app funcionando)*

## ✨ Características

- 🎥 Detección de objetos en tiempo real desde la cámara del navegador
- 🌎 80 clases de objetos con etiquetas traducidas al español
- 🎚️ Slider ajustable para el umbral mínimo de confianza
- ⚡ Modelo YOLOv8 Nano — liviano y rápido, corre sin GPU
- 🌐 100% en el navegador, sin necesidad de instalar nada del lado del usuario

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| [Python](https://www.python.org/) | Lenguaje base |
| [Streamlit](https://streamlit.io/) | Interfaz web |
| [Ultralytics YOLOv8](https://docs.ultralytics.com/) | Modelo de detección de objetos |
| [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc) | Captura de video en tiempo real desde el navegador |
| [OpenCV](https://opencv.org/) | Procesamiento de imágenes |

## 💻 Instalación

Clona el repositorio:

```bash
git clone https://github.com/Mayela3018/detector-objetos-yolo.git
cd detector-objetos-yolo
```

Crea y activa un entorno virtual:

```bash
python -m venv venv
.\venv\Scripts\Activate   # Windows
source venv/bin/activate  # macOS/Linux
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Uso

Ejecuta la aplicación:

```bash
streamlit run app.py
```

Se abrirá automáticamente en tu navegador en `http://localhost:8501`. Presiona **START**, acepta el permiso de cámara, y verás las detecciones en tiempo real.

## 📁 Estructura del proyecto

detector-objetos-yolo/
|
├── app.py # Aplicación principal de Streamlit
|
├── requirements.txt # Dependencias del proyecto
|
├── .gitignore
|
└── README.md


## ⚙️ Cómo funciona

1. `streamlit-webrtc` captura el video de la cámara directamente desde el navegador
2. Cada frame se envía al modelo **YOLOv8** (`yolov8n.pt`), que detecta los objetos presentes
3. Las clases detectadas (en inglés, dataset COCO) se traducen al español mediante un diccionario
4. Se dibujan las cajas delimitadoras con la etiqueta y el porcentaje de confianza
5. El frame procesado se muestra en tiempo real en la interfaz

## 👤 Autor

**MAYELA TICONA** — Estudiante de Diseño y Desarrollo de Software en Tecsup
[GitHub: @Mayela3018](https://github.com/Mayela3018)
