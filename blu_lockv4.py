import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# 1. NOTIFICA SONORA (PROTOCOLLO SONIC)
def play_beep():
    beep_html = '<audio autoplay><source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ BENZINA MANCANTE NEI SECRETS! IL CANTIERE È FERMO.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 15.2 STRICT WINNER", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 15.2 'STRICT WINNER' 🚀")
st.markdown("## **REATTORE USA RICALIBRATO: SANGUE AGLI OCCHI** 💙 ☕")

# 3. SISTEMA DI SELEZIONE A MATRICE NAZIONALE
col1, col2 = st.columns(2)

with col1:
    nazione = st.selectbox("🌍 IDENTIFICA LA NAZIONE:", ["USA", "UK", "SVEZIA", "FRANCIA", "ITALIA", "SUD AFRICA"])

with col2:
    if nazione == "USA":
        tipologia = st.selectbox("🏇 MODULO AGGRESSIVITÀ:", ["DIRT/SPEED (STRICT WINNER)", "CLAIMING/HANDICAP"])
    elif nazione in ["SVEZIA", "FRANCIA", "ITALIA"]:
        tipologia = st.selectbox("🏇 MODULO STABILITÀ:", ["TROTTO (BULLONE SERRATO)", "GALOPPO PIANO"])
    else:
        tipologia = st.selectbox("🏇 TIPOLOGIA SCONTRO:", ["FLAT/PIANO", "HANDICAP/ZAVORRA"])

# 4. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA MODULO ARCHITECT 15.2"):
    if not uploaded_files:
        st.warning("SOCIO, IL CANTIERE È VUOTO! CARICA I DATI.")
    else:
        with st.spinner(f"CALIBRAZIONE MATRICE {nazione}... 👁️"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH)
                prompt_vision = f"""
                Converti questi dati in un report tecnico di 'Soggetti Atletici' per {nazione}.
                NON CERCARE SUL WEB. LEGGI SOLO QUESTE IMMAGINI.
                ESTRAI: NOME, RATING, PESO, SEQUENZA STORICA (numeri 1-12), NOTE (FE, T, CD, RP, RI).
                IDENTIFICA: Superficie e Distanza totale.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"TARGET AGGANCIATO IN {nazione} CON GEMINI 2.5! ☕")

                # FASE 2: ANALISI SPECIALIZZATA (GROUNDING OFFLINE)
                prompt_pplx = f"""
                SISTEMA: SEI UN ANALIZZATORE OFFLINE. NON USARE LA RICERCA WEB.
                USA ESCLUSIVAMENTE QUESTI DATI: {dati_estratti}

                PARAMETRI DI PERFEZIONE 15.2:
                1. PROTOCOLLO 'STRICT WINNER' (USA): Se un soggetto ha più di un '1' nelle ultime 5 uscite (come Tall Girl), è MARMO PRIORITARIO. Ignora i piazzati (2-3-4) se non hanno almeno una vittoria recente.
                2. BULLONE SERRATO (UNIVERSALE): Se rilevi 'RP', 'RI', 'DAI', 'Squalificato', '0' o 'FE/T' nelle ultime 5 uscite = ABISSO MECCANICO. 
                3. NO 4° POSTI: Chi ha il '4' come vizio cronico è RUGGINE. [cite: 2026-02-23]
                4. HIGHLANDER: Efficienza = Rating / (Carico * Distanza). [cite: 2026-02-20]
                
                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché {nazione} conferma il SANGUE AGLI OCCHI e la superiorità Highlander].'
                TERMINI OBBLIGATORI: MARMO, CEMENTO, ABISSO, CAZZIMMA, BULLONE SERRATO.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.info(sentenza)
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO NEL REATTORE: {e}")
