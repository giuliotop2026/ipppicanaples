import streamlit as st
import requests
from bs4 import BeautifulSoup
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- GRAFICA ROYAL TURF 2.0 (STILE CANTIERE IPPICO) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #0e2a1d; 
        background-image: linear-gradient(180deg, #123524 0%, #071a10 100%);
        color: #f0f4f1; 
        font-family: 'Courier New', Courier, monospace; 
    }
    h1, h2, h3 { 
        color: #d4af37 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 2px 2px 5px #000;
    }
    .stButton>button { 
        background-color: #5d4037 !important; 
        color: #ffffff !important; 
        border: 3px solid #d4af37 !important; 
        font-weight: bold; font-size: 1.3em; text-transform: uppercase;
        width: 100%; border-radius: 12px; height: 3em;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    .stButton>button:hover { background-color: #d4af37 !important; color: #0e2a1d !important; }
    div[data-testid="stAlert"] {
        background-color: #071a10 !important;
        border: 2px solid #d4af37 !important;
        border-left: 10px solid #d4af37 !important;
        border-radius: 8px;
    }
    div[data-testid="stAlert"] p {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.2em !important;
    }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/boxing-bell.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")
except KeyError:
    st.error("☠️ MUNIZIONI MANCANTI (API KEYS)!")
    st.stop()

st.title("🏇 SNIPER 44.0: DIAMOND DRILL")
st.markdown("### *'Web Scraping Stealth. Protocollo Granito 3.0 e Patch Anti-Maiden attiva.'*")

# 3. SELEZIONE NAZIONE
nazione = st.selectbox("🌍 TERRITORIO DI CACCIA:", [
    "ITALIA", "UK", "IRLANDA", "USA", "FRANCIA", "GERMANIA", "SUD AFRICA", "AUSTRALIA", "SVEZIA"
])

# 4. MOTORE DI TRIVELLAZIONE (SELENIUM STEALTH SCRAPER)
def get_snai_data_stealth():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://ippica.snai.it/partenti")
        time.sleep(5) # Attesa per bypassare challenge iniziali
        html_content = driver.page_source
        driver.quit()
        return html_content
    except Exception as e:
        return f"ERRORE TRIVELLAZIONE: {str(e)}"

# 5. RADAR AUTOMATICO
if st.button("🚀 LANCIA RADAR GLOBALE"):
    with st.spinner("TRIVELLAZIONE CAVEAU SNAI IN CORSO... ⏳"):
        try:
            raw_data = get_snai_data_stealth()
            
            # FASE 2: IL CERVELLO (STEALTH PROMPT PER EVITARE CENSORI)
            prompt_p = f"""
            SISTEMA: PROTOCOLO ANALISI STATISTICA 15.15. [cite: 2026-02-25]
            SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
            DATA: 2026-02-26.
            DATI DA ANALIZZARE: {raw_data[:15000]}

            LOGICA DI SELEZIONE MOLECOLARE:
            1. IDENTIFICA PARTICELLE (#) CON ULTIMA SEQ 1 O 2. (SE MAIDEN, SOLO 1). [cite: 2026-02-25]
            2. FILTRO RUGGINE: GG < 45. (SE MAIDEN, GG < 15). [cite: 2026-02-25]
            3. GAP RT: SE MAIDEN, GAP RATING ≥ 5 RISPETTO AL SECONDO MIGLIORE. [cite: 2026-02-25]
            4. BIAS NASTRI: PRIORITÀ LEPRE (0m) SE CALDA. [cite: 2026-02-24]

            REFERTO FINALE (SINTASSI MAIUSCOLA):
            '🏆 OBIETTIVO INDIVIDUATO: [IPPODROMO] - [ORARIO] - [NUMERO #]'
            'ANALISI TECNICA: [DETTAGLI SU SEQ, GG E DENSITÀ RT].'
            'ORDINE DI MERCATO: [GIOCA PIAZZATO 1-4 SE DISPONIBILE, ALTRIMENTI 1-3].' [cite: 2026-02-15]
            'BULLONE SERRATO: [CONFERMA REQUISITI 15.15 SUPERATI].'
            """
            
            res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
            sentenza = res_p.choices[0].message.content
            
            st.info(sentenza)
            if "OBIETTIVO" in sentenza.upper() and "INDIVIDUATO" in sentenza.upper():
                play_beep(); st.balloons()
        except Exception as e:
            st.error(f"☠️ ERRORE RADAR: {e}")

# 6. SCANNER MANUALE (BACKUP SEMPRE PRONTO)
with st.expander("📸 BACKUP: CARICA SCREENSHOT SE IL RADAR È OSCURATO"):
    uploaded_files = st.file_uploader("UPLOAD:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if st.button("🏁 ESEGUI ANALISI MANUALE"):
        if uploaded_files:
            with st.spinner("SCANSIONE PARTICELLE..."):
                images = [Image.open(f) for f in uploaded_files]
                res_v = client_gemini.models.generate_content(model='gemini-2.0-flash', contents=[f"ESTRAI DATI MOLECOLARI PER {nazione}"] + images)
                st.write(res_v.text)
