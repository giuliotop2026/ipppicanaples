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

st.set_page_config(page_title="SNIPER 12.0 STRUCTURAL", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 12.0 'STRUCTURAL ARCHITECT' 🚀")
st.markdown("## **MODELLAZIONE A MATRICE NAZIONALE: PERFEZIONE TOTALE** 💙 ☕")

# 3. SISTEMA DI SELEZIONE A COMPARTIMENTI STAGNI
col1, col2 = st.columns(2)

with col1:
    nazione = st.selectbox("🌍 IDENTIFICA LA NAZIONE:", [
        "ITALIA", "FRANCIA", "SUD AFRICA", "USA", "AUSTRALIA", 
        "UK", "GERMANIA", "SVEZIA", "ARABIA SAUDITA", "BRASILE/CILE/MESSICO"
    ])

with col2:
    # Tipologie dinamiche in base alla nazione
    if nazione == "ITALIA" or nazione == "SVEZIA":
        tipologia = st.selectbox("🏇 TIPOLOGIA SCONTRO:", ["TROTTO", "GALOPPO PIANO", "HANDICAP NASTRI/PESO"])
    elif nazione == "FRANCIA":
        tipologia = st.selectbox("🏇 TIPOLOGIA SCONTRO:", ["OSTACOLI/AUTEUIL", "GALOPPO PIANO", "TROTTO LUNGO METRAGGIO"])
    else:
        tipologia = st.selectbox("🏇 TIPOLOGIA SCONTRO:", ["FLAT/PIANO", "HANDICAP/ZAVORRA", "DIRT/SPEED"])

# 4. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA MODULO ARCHITECT 12.0"):
    if not uploaded_files:
        st.warning("SOCIO, IL CANTIERE È VUOTO! CARICA I DATI.")
    else:
        with st.spinner(f"CALIBRAZIONE MATRICE {nazione} - {tipologia}... 👁️"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH)
                prompt_vision = f"""
                Converti questi dati in un report tecnico di 'Soggetti Atletici' per {nazione}.
                NON usare termini ippici. ESTRAI CON RIGORE ASSOLUTO:
                [INIZIO SOGGETTO]
                - NOME:
                - CATEGORIA (G1, Listed, Classe, Handicap):
                - CARICO/PESO/HANDICAP (Meters or Kg):
                - INDICE RILEVANZA (Rating):
                - SEQUENZA STORICA:
                - NOTE CINETICHE (RP, FE, CD, Distacchi reali):
                [FINE SOGGETTO]
                IDENTIFICA: Superficie e Distanza totale.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"TARGET AGGANCIATO IN {nazione}! ☕")

                # FASE 2: ANALISI SPECIALIZZATA (PERPLEXITY SONAR)
                prompt_pplx = f"""
                SIMULAZIONE STRUTTURALE 12.0. NAZIONE: {nazione} | MODULO: {tipologia}.
                DATI: {dati_estratti}

                PARAMETRI DI PERFEZIONE SPECIFICI:
                - SE {nazione} == 'ITALIA' AND {tipologia} == 'HANDICAP': Analizza distacco nastri o peso. Il vantaggio cinetico (<55kg o +0 metri) schiaccia il rating.
                - SE {nazione} == 'ITALIA' AND {tipologia} == 'TROTTO': Ragguaglio KM < 1:14 = MARMO. Elimina soggetti con RP/0/8 o più di un 4° posto.
                - SE {nazione} == 'FRANCIA' AND {tipologia} == 'OSTACOLI': PURE QUALITY. Se G1/Listed, ignora FE. Su FANGO, Classe > Forma.
                - SE {tipologia} == 'TROTTO LUNGO METRAGGIO': Priorità assoluta ai POLMONI D'ACCIAIO (Sequenza finale senza crolli).
                - SE {nazione} == 'SUD AFRICA': DUAL-PLACE 1-1/1-2. Polytrack: Carico < 58kg è MARMO.

                PROTOCOLLO WINNER EDGE:
                1. IGNORA LE QUOTE. [cite: 2026-02-20]
                2. NO 4° POSTI: Chi non vince o non arriva 2° regolarmente è RUGGINE. [cite: 2026-02-23]
                3. HIGHLANDER: Efficienza = Rating / (Carico * Fattore Distanza). [cite: 2026-02-20]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché questo specifico modulo {nazione}/{tipologia} conferma la superiorità].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA.
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
                st.error(f"URTO TECNICO: {e}")
