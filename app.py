import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
from ultralytics import YOLO
import av

# Configuración de la página
st.set_page_config(page_title="Detector de Objetos en Tiempo Real", page_icon="🎯", layout="wide")

st.title("🎯 Detector de Objetos en Tiempo Real")
st.markdown("Detector de objetos usando **YOLOv8** y tu cámara web, en vivo desde el navegador.")

# Cargar el modelo YOLO (se descarga automáticamente la primera vez)
@st.cache_resource
def cargar_modelo():
    return YOLO("yolov8n.pt")

modelo = cargar_modelo()

# Slider para ajustar la confianza mínima de detección
confianza = st.sidebar.slider("Confianza mínima de detección", 0.0, 1.0, 0.5, 0.05)

st.sidebar.markdown("---")
st.sidebar.markdown("**Clases detectables:** 80 objetos (personas, animales, vehículos, objetos cotidianos, etc.)")

# Configuración RTC (necesaria para que funcione en la nube)
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

# Diccionario de traducción de las 80 clases de COCO
TRADUCCIONES = {
    "person": "persona", "bicycle": "bicicleta", "car": "carro", "motorcycle": "moto",
    "airplane": "avión", "bus": "bus", "train": "tren", "truck": "camión", "boat": "bote",
    "traffic light": "semáforo", "fire hydrant": "hidrante", "stop sign": "señal de alto",
    "parking meter": "parquímetro", "bench": "banca", "bird": "ave", "cat": "gato",
    "dog": "perro", "horse": "caballo", "sheep": "oveja", "cow": "vaca", "elephant": "elefante",
    "bear": "oso", "zebra": "cebra", "giraffe": "jirafa", "backpack": "mochila",
    "umbrella": "paraguas", "handbag": "cartera", "tie": "corbata", "suitcase": "maleta",
    "frisbee": "frisbee", "skis": "esquís", "snowboard": "snowboard", "sports ball": "pelota",
    "kite": "cometa", "baseball bat": "bate", "baseball glove": "guante", "skateboard": "patineta",
    "surfboard": "tabla de surf", "tennis racket": "raqueta", "bottle": "botella",
    "wine glass": "copa de vino", "cup": "taza", "fork": "tenedor", "knife": "cuchillo",
    "spoon": "cuchara", "bowl": "tazón", "banana": "plátano", "apple": "manzana",
    "sandwich": "sándwich", "orange": "naranja", "broccoli": "brócoli", "carrot": "zanahoria",
    "hot dog": "hot dog", "pizza": "pizza", "donut": "dona", "cake": "torta", "chair": "silla",
    "couch": "sofá", "potted plant": "planta", "bed": "cama", "dining table": "mesa",
    "toilet": "inodoro", "tv": "televisor", "laptop": "laptop", "mouse": "mouse",
    "remote": "control remoto", "keyboard": "teclado", "cell phone": "celular",
    "microwave": "microondas", "oven": "horno", "toaster": "tostadora", "sink": "lavabo",
    "refrigerator": "refrigeradora", "book": "libro", "clock": "reloj", "vase": "florero",
    "scissors": "tijeras", "teddy bear": "oso de peluche", "hair drier": "secadora de pelo",
    "toothbrush": "cepillo de dientes"
}

# Función que procesa cada frame de video
def procesar_frame(frame):
    img = frame.to_ndarray(format="bgr24")

    # Ejecutar la detección de objetos
    resultados = modelo(img, conf=confianza, verbose=False)

    # Traducir los nombres de las clases al español
    for r in resultados:
        r.names = {k: TRADUCCIONES.get(v, v) for k, v in r.names.items()}

    # Dibujar las cajas y etiquetas sobre la imagen
    img_anotada = resultados[0].plot()

    return av.VideoFrame.from_ndarray(img_anotada, format="bgr24")

# Iniciar el stream de la cámara
webrtc_streamer(
    key="deteccion-objetos",
    video_frame_callback=procesar_frame,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
)

st.markdown("---")
st.caption("Proyecto de portafolio — Detector de objetos con YOLOv8 y Streamlit")






