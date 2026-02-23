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
    st.error("❌ BENZINA MANCANTE NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 15.3 HYBRID ARCHITECT", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 15.3 'HYBRID ARCHITECT' 🚀")
st.markdown("## **LOGICA DOPPIA: MARKET LAW (USA) & BULLONE SERRATO (EU)** 💙 ☕")

# 3. MATRICE DI SELEZIONE
col1, col2 = st.columns(2)
with col1:
    nazione = st.selectbox("🌍 IDENTIFICA LA NAZIONE:", [
        "USA", "UK", "SVEZIA", "FRANCIA", "ITALIA", "SUD AFRICA", "AUSTRALIA"
    ])
with col2:
    if nazione == "USA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (MARKET LAW)"])
    else:
        tipologia = st.selectbox("🏇 MODULO:", ["TROTTO (BULLONE SERRATO)", "GALOPPO PIANO"])

# 4. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA MODULO ARCHITECT 15.3"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA I DATI!")
    else:
        with st.spinner(f"CALIBRAZIONE {nazione} CON GEMINI 2.5 FLASH... 👁️"):
            try:
                # FASE 1: ESTRAZIONE CON GEMINI 2.5 FLASH
                prompt_vision = f"""
                Converti questi dati in un report tecnico per {nazione}. 
                NON CERCARE SUL WEB. LEGGI SOLO QUESTE IMMAGINI.
                ESTRAI: NOME, QUOTA (Odds), RATING, PESO, SEQUENZA, NOTE (RP, RI, DAI, FE, T).
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text

                # FASE 2: ANALISI CON LOGICA DIFFERENZIATA
                prompt_pplx = f"""
                SISTEMA: ANALIZZATORE OFFLINE. USA SOLO: {dati_estratti}

                PARAMETRI 15.3:
                - SE NAZIONE == 'USA': Applica MARKET LAW. Identifica i 2-3 con quota più bassa (i favoriti). Tra loro, il migliore deve avere almeno un '1' recente. Scarta i favoriti senza vittorie. Il DIAMANTE deve essere tra questi.
                - SE NAZIONE != 'USA': IGNORA LE QUOTE. Cerca il migliore per densità tecnica reale.
                - REGOLA UNIVERSALE: BULLONE SERRATO. RP, RI, DAI, 0, Squal, FE, T = ABISSO immediato.
                - HIGHLANDER: Efficienza = Rating / (Carico * Distanza).

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché questo soggetto schiaccia gli altri secondo la logica specifica di {nazione}].'
                TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA, BULLONE SERRATO.
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
