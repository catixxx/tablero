import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título de la aplicación
st.title("Tablero para dibujo")

# --- Panel lateral con propiedades del tablero ---
with st.sidebar:
    st.subheader("Propiedades del Tablero")

    # Dimensiones del tablero
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Selector de herramienta de dibujo
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Grosor de la línea
    stroke_width = st.slider("Selecciona el ancho de línea", 1, 30, 15)

    # Color del trazo
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")

    # Color de fondo
    bg_color = st.color_picker("Color de fondo", "#000000")

# --- Creación del tablero interactivo ---
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno (naranja semitransparente)
    stroke_width=stroke_width,            # Grosor de línea
    stroke_color=stroke_color,            # Color del trazo
    background_color=bg_color,            # Color de fondo
    height=canvas_height,                 # Alto dinámico
    width=canvas_width,                   # Ancho dinámico
    drawing_mode=drawing_mode,            # Herramienta seleccionada
    key=f"canvas_{canvas_width}_{canvas_height}"  # Clave dinámica para refrescar
)

