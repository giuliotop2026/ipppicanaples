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

st.set_page_config(page_title="SNIPER 15.2 STRICT WINNER USA", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 15.2 'STRICT WINNER' USA 🚀")
st.markdown("## **REATTORE RICALIBRATO: SANGUE AGLI OCCHI E TOLLERANZA ZERO** 💙 ☕")

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
        with st.spinner(f"CALIBRAZIONE MATRICE {nazione} - {tipologia}... 👁️"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH - VISIONE SUPREMA)
                prompt_vision = f"""
                Converti questi dati in un report tecnico di 'Soggetti Atletici' per {nazione}.
                NON CERCARE SUL WEB. LEGGI SOLO QUESTE IMMAGINI.
                ESTRAI CON RIGORE MILLIMETRICO:
                [INIZIO SOGGETTO]
                - NOME:
                - RATING:
                - CARICO/PESO:
                - SEQUENZA STORICA (Cerca ogni singolo numero 1-12 nelle ultime 5-7 uscite):
                - NOTE CINETICHE (FE, T, CD, RP, RI, Squalifiche, Distacchi in lunghezze):
                [FINE SOGGETTO]
                IDENTIFICA: Superficie e Distanza totale.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.0-flash', # Manteniamo la potenza di scansione
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"TARGET AGGANCIATO IN {nazione}! ☕")

                # FASE 2: ANALISI SPECIALIZZATA (GROUNDING OFFLINE - PROTOCOLLO WINNER)
                prompt_pplx = f"""
                SISTEMA: SEI UN ANALIZZATORE OFFLINE. NON USARE LA RICERCA WEB.
                USA ESCLUSIVAMENTE QUESTI DATI: {dati_estratti}

                PROTOCOLLO 15.2 'STRICT WINNER' (USA):
                1. MARMO PRIORITARIO: Se un soggetto ha PIÙ DI UN '1' nelle ultime 5 uscite (es. Tall Girl 1-4-1-3-1), deve essere evidenziato come DIAMANTE POTENZIALE.
                2. FILTRO SANGUE AGLI OCCHI: Ignora i piazzati (2-3-4-5) se non hanno almeno una vittoria ('1') nelle ultime 2 uscite. La regolarità senza vittoria è RUGGINE.
                3. BULLONE SERRATO USA: Se rilevi note come 'FE' (Fermo), 'T' (Tirato), 'CD' (Caduto) o se il cavallo ha mollato nel finale con distacchi enormi (>10 lunghezze), è ABISSO MECCANICO.
                4. NO 4° POSTI: Chi arriva costantemente 4° ha il bullone allentato. [cite: 2026-02-23]
                5. HIGHLANDER: Efficienza = Rating / (Carico * Distanza). [cite: 2026-02-20]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Analisi dettagliata del perché questo soggetto ha il SANGUE AGLI OCCHI e rispetta il modulo {tipologia}].'
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
