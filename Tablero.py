import streamlit as st
from streamlit_drawable_canvas import st_canvas

# --- Estilo general con CSS ---
st.markdown("""
    <style>
        /* Fondo general suave */
        .stApp {
            background-color: #f9f5fa;
            font-family: 'Poppins', sans-serif;
        }

        /* Título elegante en color lila */
        h1 {
            color: #a46dbf;
            text-align: center;
            font-weight: 700;
            margin-bottom: 0.5em;
        }

        /* Subtítulos del panel lateral */
        .stSidebar h2, .stSidebar h3 {
            color: #b36bae;
            font-size: 1.2em;
        }

        /* Panel lateral con tono rosado */
        section[data-testid="stSidebar"] {
            background-color: #fce8f5;
            border-radius: 15px;
        }

        /* Sliders, selectboxes y color pickers */
        .stSlider, .stSelectbox, .stColorPicker {
            margin-bottom: 15px !important;
        }

        /* Bordes suaves en los widgets */
        div[data-baseweb="select"] {
            border-radius: 10px;
        }

        /* Canvas enmarcado */
        canvas {
            border-radius: 15px !important;
            border: 3px solid #e6b2d1;
        }
    </style>
""", unsafe_allow_html=True)

# --- Título principal ---
st.title("🎨 Tablero de Dibujo 🌸")

# --- Panel lateral con propiedades ---
with st.sidebar:
    st.subheader("✨ Propiedades del Tablero ✨")

    # Dimensiones del tablero
    st.subheader("📐 Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Selector de herramienta de dibujo
    drawing_mode = st.selectbox(
        "🖌️ Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Grosor de la línea
    stroke_width = st.slider("✏️ Grosor de línea", 1, 30, 10)

    # Color del trazo
    stroke_color = st.color_picker("🎨 Color del trazo", "#b36bae")

    # Color de fondo del lienzo
    bg_color = st.color_picker("🌈 Color de fondo", "#fff9fb")

# --- Creación del tablero interactivo ---
canvas_result = st_canvas(
    fill_color="rgba(255, 182, 193, 0.3)",  # Rosa pastel semitransparente
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}"
)

# --- Mensaje inferior ---
st.markdown("""
<div style='text-align:center; margin-top:20px; font-size:1.1em; color:#a46dbf;'>
💗 Dibuja, crea y expresa tu lado más artístico 💗
</div>
""", unsafe_allow_html=True)
