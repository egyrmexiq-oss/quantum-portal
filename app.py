import streamlit as st

# Configuración de la página (El nombre que sale en la pestaña)
st.set_page_config(page_title="Quantum AI Ecosystem", page_icon="🌐", layout="wide")

# --- ESTILOS CSS (El toque futurista) ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #00C2FF;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.5s;
    }
    .stButton>button:hover {
        background-color: #FF5733;
        box-shadow: 0 0 15px #FF5733;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: 0.3s;
    }
    .card:hover {
        border: 1px solid #00C2FF;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.image("https://unsplash.com/es/fotos/textil-redondo-azul-sobre-fondo-negro-7Ne_rNvQldw?auto=format&fit=crop&q=80&w=1000", use_container_width=True) # Imagen abstracta de IA
st.title("🌐 Quantum AI Ecosystem")
st.markdown("### *Donde la lógica de datos potencia el bienestar humano*")
st.divider()

# --- SECCIÓN: QUIÉNES SOMOS ---
with st.expander("📖 Nuestra Filosofía (El Manifiesto Quantum)"):
    st.write("""
        Somos un ecosistema nacido de la experiencia y la visión tecnológica. 
        Creemos que la Inteligencia Artificial no debe ser fría, sino una herramienta 
        que potencie la Mente, el Cuerpo y la Nutrición. 
        Quantum es el puente entre los algoritmos avanzados y la salud integral.
    """)

st.write("## Selecciona tu Módulo de Optimización:")

# --- FILA DE TARJETAS (La Trinidad) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🧠")
    st.subheader("Quantum Mind")
    st.write("Salud mental y equilibrio cognitivo asistido por IA.")
    st.link_button("Ingresar", "AQUI_VA_TU_LINK_DE_MIND")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🌿")
    st.subheader("Quantum Herbal")
    st.write("Directorio médico y sabiduría botánica de precisión.")
    st.link_button("Ingresar", "AQUI_VA_TU_LINK_DE_HERBAL")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("⚡")
    st.subheader("Quantum Supplements")
    st.write("Rendimiento físico y suplementación estratégica.")
    st.link_button("Ingresar", "AQUI_VA_TU_LINK_DE_SUPPLEMENTS")
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🩺")
    st.subheader("Quantum Health")
    st.write("Portal médico integral y herbolaria avanzada.")
    st.link_button("Ingresar", "TU_LINK_DE_HEALTH_AQUI")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.divider()
st.caption("Quantum AI 2026 | Arquitectura de Sistemas de Vanguardia")