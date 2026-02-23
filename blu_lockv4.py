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

st.set_page_config(page_title="SNIPER 15.3 GLOBAL HYBRID", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 15.3 'GLOBAL HYBRID' 🚀")
st.markdown("## **LOGICA SEPARATA: MARKET LAW (USA) & DENSITÀ REALE (EU/ARG/ROW)** 💙 ☕")

# 3. SISTEMA DI SELEZIONE A MATRICE TOTALE
col1, col2 = st.columns(2)

with col1:
    nazione = st.selectbox("🌍 IDENTIFICA LA NAZIONE:", [
        "USA", "ARGENTINA", "ITALIA", "FRANCIA", "SVEZIA", "UK", "SUD AFRICA", 
        "AUSTRALIA", "GERMANIA", "ARABIA SAUDITA", "BRASILE/CILE/MESSICO"
    ])

with col2:
    if nazione == "USA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (MARKET LAW)"])
    elif nazione == "ARGENTINA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (DENSITÀ REALE)", "HANDICAP/ZAVORRA"])
    elif nazione in ["ITALIA", "FRANCIA", "SVEZIA"]:
        tipologia = st.selectbox("🏇 MODULO:", ["TROTTO (BULLONE SERRATO)", "GALOPPO PIANO", "HANDICAP/NASTRI"])
    else:
        tipologia = st.selectbox("🏇 MODULO:", ["FLAT/PIANO", "HANDICAP/ZAVORRA", "DIRT/SPEED"])

# 4. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA MODULO ARCHITECT 15.3"):
    if not uploaded_files:
        st.warning("SOCIO, IL CANTIERE È VUOTO! CARICA I DATI.")
    else:
        with st.spinner(f"CALIBRAZIONE {nazione} CON GEMINI 2.5 FLASH... 👁️"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH)
                prompt_vision = f"""
                Converti questi dati in un report tecnico per {nazione}.
                NON CERCARE SUL WEB. LEGGI SOLO QUESTE IMMAGINI.
                ESTRAI: NOME, QUOTA (Odds), RATING, PESO, SEQUENZA, NOTE (FE, T, CD, RP, RI).
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"TARGET AGGANCIATO IN {nazione} CON GEMINI 2.5! ☕")

                # FASE 2: ANALISI SPECIALIZZATA (OFFLINE)
                prompt_pplx = f"""
                SISTEMA: SEI UN ANALIZZATORE OFFLINE. NON USARE LA RICERCA WEB.
                USA ESCLUSIVAMENTE QUESTI DATI: {dati_estratti}

                PARAMETRI DI PERFEZIONE 15.3:
                1. SE NAZIONE == 'USA': Applica MARKET LAW. Identifica i cavalli con le QUOTE PIÙ BASSE. Confrontali e scegli il migliore tra i favoriti. Deve avere almeno un '1' recente.
                2. SE NAZIONE != 'USA': IGNORA LE QUOTE. Cerca il secondo migliore per densità tecnica reale, regolarità e polmoni d'acciaio. [cite: 2026-02-20]
                3. BULLONE SERRATO (UNIVERSALE): RP, RI, DAI, 0, Squalificato, FE o T = ABISSO MECCANICO immediato. [cite: 2026-02-23]
                4. HIGHLANDER: Efficienza = Rating / (Carico * Distanza). [cite: 2026-02-20]
                5. NO 4° POSTI: Chi arriva spesso 4° è RUGGINE. [cite: 2026-02-23]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Analisi specifica per {nazione} basata sulla logica corretta].'
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
                st.error(f"URTO TECNICO NEL REATTORE: {e}")a
