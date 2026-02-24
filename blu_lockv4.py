import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA DA SALOON (CSS CUSTOM) ---
st.markdown("""
    <style>
    .stApp { background-color: #f4eccf; color: #5d4037; font-family: 'Georgia', serif; }
    h1, h2, h3 { color: #8b4513 !important; text-transform: uppercase; text-shadow: 2px 2px 4px #cdaa7d; }
    .stButton>button { background-color: #8b4513 !important; color: #f4eccf !important; border: 2px solid #3e2723 !important; font-weight: bold; width: 100%; height: 3.5em; text-transform: uppercase; }
    .stSelectbox label, .stFileUploader label, .stTextInput label { color: #3e2723 !important; font-weight: bold; font-size: 1.1em; }
    .stAlert { background-color: #e0c5a0; border: 2px solid #8b4513; }
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

st.set_page_config(page_title="SNIPER 15.14 FRESHNESS FILTER", page_icon="🤠", layout="wide")

st.title("🌵 SNIPER 15.14: 'LA LEGGE DEL WEST' 🤠")
st.markdown("### *'Se il mustang ha la ruggine addosso, il tratto finale sarà un abisso.'* 🔫 🥃")

# 3. MATRICE GLOBALE (TOTAL WORLD)
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
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.0 FLASH)
                prompt_vision = f"ESTRAI DALLE IMMAGINI PER {ippodromo} ({nazione}): NOME, QUOTA, RATING, PESO, DISTANZA, GG (GIORNI), SEQUENZA, NOTE."
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"INDIZI RACCOLTI CON GEMINI 2.0 FLASH! 🥃")

                # FASE 2: ANALISI CON FRESHNESS FILTER 15.14
                prompt_pplx = f"""
                SISTEMA: ANALIZZATORE OFFLINE. PARLA COME UN COWBOY DURO.
                IPPODROMO: {ippodromo}. NAZIONE: {nazione}. DATI: {dati_estratti}

                PARAMETRI DI PERFEZIONE 15.14:
                1. FRESHNESS FILTER (USA/GLOBALE): Se GG > 45, il cavallo non è MARMO ma PARTICELLA INSTABILE. Se GG > 60, scartalo come favorito. Se GG > 150, è ABISSO TOTALE: non resisterà nel finale. [cite: 2026-02-23, 2026-02-24]
                2. MARKET LAW (USA): Il MARMO deve avere GG < 30 per essere CEMENTO. [cite: 2026-02-24]
                3. BOLLNÄS/SVEZIA LEPRE BIAS: Nel primo nastro, SEQUENZA PULITA = MARMO PRIORITARIO anche con quota > 20.00. [cite: 2026-02-24]
                4. CHILE PRECISION: Distanza < 1200m richiede PRIORITÀ ASSOLUTA a chi ha un '1' recente. [cite: 2026-02-24]
                5. SOUTHWELL KEY: Ignora favorito sotto quota 3.00. [cite: 2026-02-24]
                6. ZERO TOLLERANZA SVEZIA: No RP, RI, DI, DAI nelle ultime 3 uscite. [cite: 2026-02-24]
                7. UNIVERSALI: BULLONE SERRATO (No FE, T, 0), HIGHLANDER (Rating/Peso). [cite: 2026-02-20, 2026-02-23]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💰 PEPITA D'ORO INDIVIDUATA: [NOME]. 
                LA SCOMMESSA DEL PISTOLERO: [Analisi specifica basata sulla freschezza e sul tracciato].'
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
