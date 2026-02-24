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
    .stSelectbox label, .stFileUploader label { color: #3e2723 !important; font-weight: bold; font-size: 1.1em; }
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

st.set_page_config(page_title="SNIPER 15.4 TRACK ANALYTICS", page_icon="🤠", layout="wide")

st.title("🌵 SNIPER 15.4: 'LA LEGGE DEL WEST' 🤠")
st.markdown("### *'Ogni ippodromo ha la sua polvere, ogni polvere ha il suo Marmo.'* 🔫 🥃")

# 3. SISTEMA DI SELEZIONE A MATRICE TOTALE (CON AGGIUNTA IPPODROMO)
col1, col2, col3 = st.columns(3)

with col1:
    nazione = st.selectbox("🗺️ TERRITORIO DI CACCIA:", [
        "USA", "ITALIA", "FRANCIA", "ARGENTINA", "UK", "SVEZIA", "SUD AFRICA", "AUSTRALIA"
    ])

with col2:
    # DOSE AGGIUNTIVA: BIAS IPPODROMO
    if nazione == "ITALIA":
        ippodromo = st.selectbox("🏟️ IPPODROMO (BIAS PISTA):", [
            "NAPOLI (PISTA GRANDE)", "FIRENZE (TECNICA)", "ROMA CAPANNELLE", "MILANO SAN SIRO", "ALTRO"
        ])
    elif nazione == "USA":
        ippodromo = st.selectbox("🏟️ IPPODROMO (MARKET LAW):", ["MAHONING VALLEY", "SUNLAND PARK", "THISTLEDOWN", "GULFSTREAM", "ALTRO"])
    else:
        ippodromo = st.text_input("🏟️ INSERISCI IPPODROMO (Es: Vincennes, Catterick):")

with col3:
    if nazione == "USA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (MARKET LAW)"])
    elif nazione in ["ITALIA", "FRANCIA", "SVEZIA"]:
        tipologia = st.selectbox("🏇 MODULO:", ["TROTTO (BULLONE SERRATO)", "GALOPPO PIANO", "HANDICAP/NASTRI"])
    else:
        tipologia = st.selectbox("🏇 MODULO:", ["FLAT/PIANO", "HANDICAP/ZAVORRA"])

# 4. CARICAMENTO IDENTIKIT
uploaded_files = st.file_uploader("📜 APPICICA I 'WANTED POSTERS':", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("💥 PREMI IL GRILLETTO (ANALISI IPPODROMO)"):
    if not uploaded_files:
        st.warning("EHI COWBOY! CARICA I DATI.")
    else:
        with st.spinner(f"LO SCERIFFO STA ANALIZZANDO {ippodromo}... 🚬"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH)
                prompt_vision = f"ESTRAI: NOME, QUOTA, RATING, PESO, SEQUENZA, NOTE PER {ippodromo} ({nazione})."
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"INDIZI RACCOLTI CON GEMINI 2.5 FLASH! 🥃")

                # FASE 2: ANALISI DELLO SCERIFFO CON DOSE 'TRACK ANALYTICS'
                prompt_pplx = f"""
                SISTEMA: ANALIZZATORE OFFLINE. PARLA COME UN COWBOY DURO.
                IPPODROMO: {ippodromo}. NAZIONE: {nazione}. DATI: {dati_estratti}

                PARAMETRI 15.4 (LE DOSI MANCANTI):
                1. BIAS NAPOLI (PISTA GRANDE): Se l'ippodromo è Napoli, TOLLERA UN '4' RECENTE. La dirittura è lunga, chi arriva 4° spesso ha POLMONI D'ACCIAIO per il finale. [cite: 2026-02-24]
                2. BIAS FIRENZE/PISTE CORTE: Il BULLONE SERRATO deve essere perfetto al via. Se un cavallo perde terreno in partenza, è ABISSO. [cite: 2026-02-24]
                3. MARKET LAW (USA): Identifica i cavalli con le QUOTE PIÙ BASSE. Il MARMO deve essere tra i favoriti. [cite: 2026-02-23]
                4. PATCH FANGO (FRANCIA): Se quota > 12.00 in Francia, scartalo (BURRONE). [cite: 2026-02-24]
                5. UNIVERSALI: BULLONE SERRATO (No RP, RI, DAI, FE, T, 0), HIGHLANDER (Rating/Peso), NO 4° POSTI CRONICI. [cite: 2026-02-20, 2026-02-23]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💰 PEPITA D'ORO INDIVIDUATA: [NOME]. 
                LA SCOMMESSA DEL PISTOLERO: [Analisi specifica per {ippodromo} con citazione western].'
                TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA, BULLONE SERRATO, TRACK ANALYTICS.
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
