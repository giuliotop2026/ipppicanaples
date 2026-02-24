import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA DA SALOON CON SFONDO MUSTANG (CSS CUSTOM) ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(244, 236, 207, 0.85), rgba(244, 236, 207, 0.85)), 
        url('https://images.unsplash.com/photo-1528563351349-3397da0533d1?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #5d4037;
        font-family: 'Georgia', serif;
    }
    h1, h2, h3 { color: #8b4513 !important; text-transform: uppercase; text-shadow: 2px 2px 4px #cdaa7d; }
    .stButton>button { background-color: #8b4513 !important; color: #f4eccf !important; border: 2px solid #3e2723 !important; font-weight: bold; width: 100%; height: 3.5em; text-transform: uppercase; }
    .stSelectbox label, .stFileUploader label, .stTextInput label { color: #3e2723 !important; font-weight: bold; font-size: 1.1em; }
    .stAlert { background-color: rgba(224, 197, 160, 0.95); border: 2px solid #8b4513; }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/ricochet-sound.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 15.15 FINISHER DRIVE", page_icon="🤠", layout="wide")

st.title("🌵 SNIPER 15.15: 'FINISHER DRIVE' 🤠")
st.markdown("### *'In America cerchiamo chi azzanna il traguardo, non chi arriva terzo.'* 🔫 🥃")

# 3. MATRICE GLOBALE
col1, col2, col3 = st.columns(3)

with col1:
    nazione = st.selectbox("🗺️ TERRITORIO DI CACCIA:", [
        "USA", "SVEZIA", "CILE", "BRASILE", "MESSICO", "GERMANIA", "SPAGNA", 
        "UK", "ITALIA", "FRANCIA", "ARGENTINA", "SUD AFRICA", "AUSTRALIA"
    ])

with col2:
    ippodromo = st.text_input("🏟️ INSERISCI IPPODROMO (Identifica il Cantiere):")

with col3:
    if nazione == "USA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (MARKET LAW)"])
    elif nazione in ["UK", "ITALIA", "FRANCIA", "SVEZIA", "GERMANIA", "SPAGNA"]:
        tipologia = st.selectbox("🏇 MODULO:", ["GALOPPO PIANO", "TROTTO (BULLONE SERRATO)", "HANDICAP/NASTRI"])
    elif nazione in ["CILE", "BRASILE", "MESSICO"]:
        tipologia = st.selectbox("🏇 MODULO:", ["SABBIA/DIRT (CEMENTO LATAM)", "GALOPPO PIANO", "HANDICAP/ZAVORRA"])
    else:
        tipologia = st.selectbox("🏇 MODULO:", ["FLAT/PIANO", "HANDICAP/ZAVORRA"])

# 4. CARICAMENTO IDENTIKIT
uploaded_files = st.file_uploader("📜 APPICICA I 'WANTED POSTERS':", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("💥 PREMI IL GRILLETTO (ANALISI CHIRURGICA)"):
    if not uploaded_files or not ippodromo:
        st.warning("EHI COWBOY! CARICA I DATI E IL NOME DEL CANTIERE.")
    else:
        with st.spinner(f"LO SCERIFFO STA SCANSIONANDO LA RUGGINE DI {ippodromo}... 🚬"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH)
                prompt_vision = f"ESTRAI: NOME, QUOTA, RATING, PESO, DISTANZA, GG (GIORNI), SEQUENZA, NOTE PER {ippodromo} ({nazione})."
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"INDIZI RACCOLTI CON GEMINI 2.5 FLASH! 🥃")

                # FASE 2: ANALISI CON PATCH USA 15.15
                prompt_pplx = f"""
                SISTEMA: ANALIZZATORE OFFLINE. PARLA COME UN COWBOY DURO.
                IPPODROMO: {ippodromo}. NAZIONE: {nazione}. DATI: {dati_estratti}

                PARAMETRI DI PERFEZIONE 15.15 (USA FOCUS):
                1. FINISHER DRIVE (USA): Scarta i 'Piazzati Cronici'. Se un mustang ha >= 2 volte '3' o '4' negli ultimi 5 esiti, è ABISSO. Cerca chi ha il vizio del '1' recente con quota tra 2.50 e 4.50. [cite: 2026-02-24]
                2. FRESHNESS FILTER (USA): Se GG > 45, è ruggine. Se GG > 60, scartalo come favorito. Se GG > 150, abisso totale nel tratto finale. [cite: 2026-02-24]
                3. BOLLNÄS/SVEZIA LEPRE BIAS: Primo nastro pulito = Marmo prioritario indipendentemente dalla quota. [cite: 2026-02-24]
                4. CHILE PRECISION: Sprint < 1200m richiede un '1' recente. [cite: 2026-02-24]
                5. SOUTHWELL KEY: Quota < 3.00 = Marmo Instabile. [cite: 2026-02-24]
                6. ZERO TOLLERANZA SVEZIA: No RP, RI, DI, DAI nelle ultime 2 uscite. [cite: 2026-02-24]
                7. UNIVERSALI: BULLONE SERRATO & HIGHLANDER EFFICIENCY. [cite: 2026-02-20]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💰 PEPITA D'ORO INDIVIDUATA: [NOME]. 
                LA SCOMMESSA DEL PISTOLERO: [Analisi chirurgica basata sulla cazzimma finale e sulla freschezza].'
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.info(sentenza)
                if "PEPITA" in sentenza.upper():
                    play_beep(); st.balloons()
            except Exception as e:
                st.error(f"☠️ URTO TECNICO: {e}")
