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

st.set_page_config(page_title="SNIPER 7.2 VISION CLEAR", page_icon="🎯", layout="centered")

st.title("🎯 SNIPER 7.2 'VISION CLEAR' 🚀")
st.markdown("## **SISTEMA A COMPARTIMENTI STAGNI: ZERO ALLUCINAZIONI** 💙 ☕")
st.write("---")

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 ATTIVA SCANSIONE SNIPER 7.2"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA LE FOTO PER IL PUNTAMENTO!")
    else:
        with st.spinner("ESTRAZIONE DATI BLINDATI IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE "VISION CLEAR" (ESTRAZIONE STRUTTURATA)
                prompt_vision = """
                Analizza questi dati e crea una lista RIGIDAMENTE SEPARATA. 
                USA QUESTO FORMATO PER OGNI SOGGETTO:
                [INIZIO SOGGETTO]
                - NOME:
                - QUOTA:
                - PESO:
                - SEQUENZA RISULTATI (Esatta):
                - NOTE TECNICHE (FE/CD/DISTACCHI):
                [FINE SOGGETTO]
                NON mischiare i dati tra i soggetti. Se un dato non è presente, scrivi N.D.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI CON MURI DI CEMENTO! ☕")

                # FASE 2: SONAR IBRIDO (LOGICA ANTIPANICO)
                prompt_pplx = f"""
                ANALIZZA I SEGUENTI DATI BLINDATI:
                {dati_estratti}

                PROTOCOLLO CECCHINO 7.2:
                1. IDENTIFICAZIONE: Rileva ippodromo e nazione.
                2. FILTRO FRANCIA/EUROPA: Peso ≥58kg + forma recente 3/4 = ABISSO. Ogni FE (Caduta) o CD (Distanziato) = ELIMINAZIONE ISTANTANEA.
                3. FILTRO SUD AFRICA: Applica Patch 6.8 (Lunghezze < 2.5L = MARMO). Solo Dual-Place 1-1 o 1-2.
                4. FILTRO USA: Sequenza 1-2 obbligatoria, Beyer crescenti.
                5. HIGHLANDER: Trova il 'Secondo Migliore' per densità ($Rating / Peso$) se il favorito ha zavorra critica.

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché i polmoni d'acciaio vinceranno oggi].'
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 🎯 SENTENZA DELLA PATCH 7.2")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")

st.write("---")
st.caption("SNIPER 7.2 'VISION CLEAR' - THE ULTIMATE ARCHITECT 💙 ☕")
