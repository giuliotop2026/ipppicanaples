import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA WESTERN CHIARA ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; 
        background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
        color: #3d2b1f; 
        font-family: 'Courier New', Courier, monospace; 
    }
    h1, h2, h3 { 
        color: #8b4513 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 1px 1px 2px #cda26e;
        border-bottom: 3px solid #5a3a22;
    }
    .stAlert p { color: #3d2b1f !important; font-size: 1.2rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #a0522d !important; color: #fff8dc !important; 
        border: 3px solid #5a3a22 !important; font-weight: bold; font-size: 1.5em; 
        width: 100%; border-radius: 8px; height: 3.5em;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { background-color: #8b4513 !important; color: #ffd700 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. RADAR ACUSTICO ---
def play_victory_sound():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 3. CONNESSIONE A GEMINI ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ EHI STRANIERO, MANCANO LE MUNIZIONI (GEMINI_API_KEY)!")
    st.stop()

st.title("🤠 SALOON 'EL GRANITO'")
st.markdown("### *'Scansione rapida. Nessun superstite ignorato.'*")

# --- 4. BACHECA DEI RICERCATI ---
nazione = st.selectbox("🗺️ TERRITORIO DI FRONTIERA:", [
    "UK", "IRLANDA", "USA", "ITALIA", "FRANCIA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "AUSTRALIA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI IN BACHECA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 5. IL GRILLETTO ---
if st.button("🐎 SCATENA IL DUELLO (ANALIZZA)"):
    if not uploaded_files:
        st.warning("EHI COMPADRE, CARICA I MANIFESTI PRIMA DI SPARARE!")
    else:
        with st.spinner("LO SCERIFFO GEMINI STA ELIMINANDO I BERSAGLI... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # PROMPT IBRIDO: RAGIONAMENTO + SINTESI [cite: 2026-02-25]
                prompt = f"""
                SEI LO SCERIFFO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO.
                TERRITORIO: {nazione}

                LE LEGGI DELLA FRONTIERA (GRANITO 3.0):
                1. MURO FORMA: SEQ deve iniziare con 1 o 2. [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                3. SE MAIDEN: Accetta solo SEQ '1' e GG < 15. [cite: 2026-02-25]
                4. DENSITÀ TECNICA: Scegli il vero vincitore nascosto tra i superstiti. [cite: 2026-02-20]
                
                FORMATO OUTPUT RICHIESTO (SII BREVE MA MOSTRA I FILTRI):
                
                '🔍 SCANSIONE SUPERSTITI:'
                - [NOME CAVALLO 1]: PASSATO (GG [X], SEQ [Y])
                - [NOME CAVALLO 2]: PASSATO (GG [X], SEQ [Y])
                (Scrivi solo chi passa i filtri 1 e 2. Se nessuno passa, scrivi 'NESSUN SOPRAVVISSUTO').

                SE C'È ALMENO UN SUPERSTITE:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO] - [NOME]'
                'BULLONE SERRATO: [Motivo per cui ha polmoni d'acciaio].'
                
                SE NON C'È NULLA:
                '🌵 NESSUNA PEPITA D'ORO IN QUESTO FIUME.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                
                if "TAGLIA" in sentenza.upper() and "NESSUNA" not in sentenza.upper():
                    play_victory_sound(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE (ERRORE): {e}")
                
