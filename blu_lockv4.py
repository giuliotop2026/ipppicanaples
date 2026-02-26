import streamlit as st
import time
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# --- GRAFICA ROYAL TURF 2.0 (OTTIMIZZATA PER CELLULARE) ---
st.set_page_config(page_title="SNIPER 46", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0e2a1d; color: #f0f4f1; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #d4af37 !important; text-transform: uppercase; font-weight: 900; }
    .stButton>button { background-color: #5d4037 !important; color: #ffffff !important; border: 3px solid #d4af37 !important; width: 100%; border-radius: 12px; height: 3em; font-weight: bold; }
    div[data-testid="stAlert"] { background-color: #071a10 !important; border-left: 10px solid #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/boxing-bell.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")
except KeyError:
    st.error("☠️ MUNIZIONI MANCANTI NEL CAVEAU SECRETS!")
    st.stop()

st.title("🏇 SNIPER 46.0: MOBILE PHANTOM")
st.markdown("### *'Infiltrazione Cloud. Certezza 10000% sul palmo della mano.'*")

nazione = st.selectbox("🌍 TERRITORIO DI CACCIA:", ["ITALIA", "UK", "IRLANDA", "SUD AFRICA", "USA", "FRANCIA"])

# --- MOTORE INVISIBILE PER STREAMLIT CLOUD ---
def esegui_scansione_stealth():
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    try:
        driver = uc.Chrome(options=options)
        driver.get("https://ippica.snai.it/partenti")
        time.sleep(8) # ATTESA TATTICA PER SUPERARE CLOUDFLARE
        dati_grezzi = driver.find_element(By.TAG_NAME, "body").text
        driver.quit()
        return dati_grezzi
    except Exception as e:
        return f"BLOCCO_401"

def analizza_dati_con_ia(dati_testo):
    prompt_p = f"""
    SISTEMA: PROTOCOLO ANALISI STATISTICA 15.15. [cite: 2026-02-25]
    SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
    DATI: {dati_testo[:10000]}

    ORDINE DI ESECUZIONE:
    1. MURO FORMA: ISOLA SOLO CHI INIZIA CON SEQ 1 O 2. (SOLO 1 SE MAIDEN). [cite: 2026-02-25]
    2. FILTRO RUGGINE: VERIFICA GG < 45. (GG < 15 SE MAIDEN). [cite: 2026-02-25]
    3. GAP RT: SE MAIDEN, CONFERMA GAP RATING >= 5. [cite: 2026-02-25]

    REFERTO FINALE:
    '🏆 OBIETTIVO INDIVIDUATO: [IPPODROMO] - [CAVALLO #]' (OPPURE 'NESSUN SACRO GRAAL')
    'ANALISI: [DENSITÀ TECNICA E POLMONI D'ACCIAIO].' [cite: 2026-02-20]
    'MERCATO: GIOCA PIAZZATO 1-4 (O 1-3 SE MASSIMO PROFITTO).' [cite: 2026-02-15]
    'BULLONE SERRATO: [CONFERMA FILTRI 15.15].'
    """
    res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
    return res_p.choices[0].message.content

# --- INTERFACCIA DI COMANDO ---
if st.button("🚀 LANCIA RADAR MOBILE"):
    with st.spinner("INFILTRAZIONE SERVER IN CORSO... ⏳"):
        dati_estratti = esegui_scansione_stealth()
        
        if dati_estratti == "BLOCCO_401":
            st.error("☠️ CLOUDFLARE HA BLOCCATO IL SERVER STREAMLIT. USA LO SCANNER MANUALE QUI SOTTO.")
        else:
            sentenza = analizza_dati_con_ia(dati_estratti)
            st.info(sentenza)
            if "OBIETTIVO INDIVIDUATO" in sentenza:
                play_beep(); st.balloons()

st.markdown("---")
st.markdown("### 📸 SCUDO DI EMERGENZA (SCANNER MANUALE)")
uploaded_files = st.file_uploader("CARICA SCREENSHOT SE IL RADAR È BLOCCATO:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("🏁 ESEGUI ANALISI FOTOGRAFICA"):
    if uploaded_files:
        with st.spinner("SCANSIONE PARTICELLE..."):
            images = [Image.open(f) for f in uploaded_files]
            prompt_v = f"ESTRAI DATI MOLECOLARI (#, RT, GG, SEQ) PER {nazione}. POI APPLICA IL PROTOCOLO 15.15 E INDIVIDUA IL SACRO GRAAL IN MAIUSCOLO."
            res_v = client_gemini.models.generate_content(model='gemini-2.0-flash', contents=[prompt_v] + images)
            st.info(res_v.text)
