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

st.set_page_config(page_title="SNIPER 15.0 MECHANICAL PERFECTION", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 15.0 'MECHANICAL PERFECTION' 🚀")
st.markdown("## **PROTOCOLLO ANTI-SQUALIFICA: ZERO ERRORI MECCANICI** 💙 ☕")

# 3. SISTEMA DI SELEZIONE A MATRICE EVOLUTA
col1, col2 = st.columns(2)

with col1:
    nazione = st.selectbox("🌍 IDENTIFICA LA NAZIONE:", [
        "ITALIA", "FRANCIA", "SVEZIA", "USA", "UK", "SUD AFRICA", 
        "AUSTRALIA", "GERMANIA", "ARABIA SAUDITA", "BRASILE/CILE/MESSICO"
    ])

with col2:
    if nazione in ["ITALIA", "SVEZIA", "FRANCIA"]:
        tipologia = st.selectbox("🏇 MODULO STABILITÀ:", ["TROTTO (BULLONE SERRATO)", "GALOPPO PIANO", "HANDICAP NASTRI/PESO"])
    elif nazione == "USA" or nazione == "UK":
        tipologia = st.selectbox("🏇 MODULO AGGRESSIVITÀ:", ["DIRT/SPEED (WINNER ONLY)", "HANDICAP/ZAVORRA", "FLAT/TURF"])
    else:
        tipologia = st.selectbox("🏇 TIPOLOGIA SCONTRO:", ["FLAT/PIANO", "HANDICAP/ZAVORRA", "DIRT/SPEED"])

# 4. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA MODULO ARCHITECT 15.0"):
    if not uploaded_files:
        st.warning("SOCIO, IL CANTIERE È VUOTO! CARICA I DATI.")
    else:
        with st.spinner(f"CALIBRAZIONE MATRICE {nazione} - {tipologia}... 👁️"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH RIPRISTINATO)
                prompt_vision = f"""
                Converti questi dati in un report tecnico di 'Soggetti Atletici' per {nazione}.
                NON usare termini ippici. ESTRAI CON RIGORE ASSOLUTO OGNI DETTAGLIO SU ERRORI MECCANICI:
                [INIZIO SOGGETTO]
                - NOME:
                - CATEGORIA:
                - CARICO/PESO/HANDICAP:
                - INDICE RILEVANZA (Rating):
                - SEQUENZA STORICA (Cerca numeri 1-12):
                - ERRORI MECCANICI (RP, RI, DAI, Squalifiche, Rotture, 0):
                [FINE SOGGETTO]
                IDENTIFICA: Superficie e Distanza totale.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"TARGET AGGANCIATO IN {nazione} CON GEMINI 2.5! ☕")

                # FASE 2: ANALISI SPECIALIZZATA (PERPLEXITY SONAR)
                prompt_pplx = f"""
                SIMULAZIONE STRUTTURALE 15.0. NAZIONE: {nazione} | MODULO: {tipologia}.
                DATI ESTRATTI: {dati_estratti}

                PARAMETRI DI PERFEZIONE MECCANICA:
                1. PROTOCOLLO 'BULLONE SERRATO' (TROTTO): Parametro ELIMINATORIO. Se un soggetto ha anche una sola segnalazione di 'RP', 'RI', 'DAI', 'Squalificato' o '0' nelle ultime 5 uscite, deve essere classificato come ABISSO. Il MARMO deve essere meccanicamente perfetto.
                2. PROTOCOLLO 'WINNER ONLY' (USA/UK): Ignora i piazzati (2-3-4). Solo chi ha un '1' nelle ultime 2 uscite è MARMO. La regolarità senza vittorie è ABISSO.
                3. NO 4° POSTI: Chi arriva spesso 4° è ruggine cronica. [cite: 2026-02-23]
                4. HIGHLANDER: Efficienza = Rating / (Carico * Fattore Distanza). [cite: 2026-02-20]
                5. POLMONI D'ACCIAIO: Nelle corse lunghe (>2500m), la sequenza finale deve essere senza crolli.

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché {nazione}/{tipologia} conferma la perfezione meccanica e la superiorità Highlander].'
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
