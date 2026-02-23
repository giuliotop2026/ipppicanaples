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
    st.error("❌ BENZINA MANCANTE NEI SECRETS! IL CANTIERE È BLOCCATO.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 11.0 SPECIALIZED", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 11.0 'SPECIALIZED ARCHITECT' 🚀")
st.markdown("## **MODELLAZIONE A COMPARTIMENTI STAGNI: PERFEZIONE TOTALE** 💙 ☕")

# 3. SELETTORE DEL MODULO (LA CHIAVE PER LA PRECISIONE)
tipologia = st.selectbox("IDENTIFICA IL TIPO DI CANTIERE:", [
    "TROTTO LUNGO / CLASSICO (ITALIA, FRANCIA, SVEZIA)", 
    "OSTACOLI & FANGO (AUTEUIL, OSTACOLI EUROPA)", 
    "HANDICAP & ZAVORRA (UK, AUSTRALIA, SUD AFRICA)",
    "VELOCITÀ & DIRT (USA, ARABIA, POLYTRACK)"
])

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (VISION CLEAR):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA MODULO SPECIALIZZATO 11.0"):
    if not uploaded_files:
        st.warning("CARICA I DATI, ARCHITETTO!")
    else:
        with st.spinner(f"CALIBRAZIONE MODULO {tipologia}... 👁️"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici'.
                NON usare termini ippici. ESTRAI CON RIGORE:
                [INIZIO SOGGETTO]
                - NOME:
                - QUALITÀ (Listed, G1/2/3, Classe):
                - CARICO (Peso):
                - INDICE RILEVANZA (Rating):
                - SEQUENZA STORICA:
                - NOTE CINETICHE (RP, FE, CD, Distacchi):
                [FINE SOGGETTO]
                IDENTIFICA: Superficie e Distanza della sessione.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text

                # FASE 2: ANALISI SPECIALIZZATA (PERPLEXITY SONAR)
                prompt_pplx = f"""
                SIMULAZIONE OMNIVERSE 11.0. MODULO ATTIVO: {tipologia}.
                DATI: {dati_estratti}

                PROTOCOLLI DI PERFEZIONE SPECIFICI:
                - MODULO TROTTO: Focus su 'Ragguaglio al KM'. Sotto 1:14 = MARMO. Elimina soggetti con RP/0/8 o più di un 4° posto (RUGGINE).
                - MODULO OSTACOLI: 'PURE QUALITY' ACTIVE. Se Listed/G1/G2, ignora FE/CD. Su FANGO, Classe > Forma recente. 
                - MODULO HANDICAP: Focus su VANTAGGIO CINETICO (Carico < 56kg). Se Peso >= 60kg e non è Classe Listed, classifica come CREPA.
                - MODULO VELOCITÀ: Beyer/Speed figures crescenti. Sequenza 1-2 obbligatoria.

                FILTRO GENERALE 'WINNER EDGE':
                1. IGNORA LE QUOTE. [cite: 2026-02-20]
                2. ELIMINAZIONE 4° POSTO: Chi arriva spesso 4° manca di CAZZIMMA. [cite: 2026-02-23]
                3. HIGHLANDER: Efficienza = Rating / (Carico * Fattore Distanza). [cite: 2026-02-20]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché questo specifico modulo conferma la superiorità].'
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
