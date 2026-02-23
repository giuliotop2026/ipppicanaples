import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# 1. NOTIFICA SONORA
def play_beep():
    beep_html = '<audio autoplay><source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ CHIAVI MANCANTI!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="PERFORMANCE ANALYTICS 6.9.1", page_icon="📈", layout="centered")

st.title("📈 PERFORMANCE ANALYTICS 6.9.1 🚀")
st.markdown("## **PROTOCOLLO OCCHIO ASSOLUTO: DATI REALI > NEWS** 💙 ☕")
st.write("---")

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 AVVIA MODELLAZIONE ANALITICA"):
    if not uploaded_files:
        st.warning("CARICA LE FOTO!")
    else:
        with st.spinner("SCANSIONE ABISSO IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE GEMINI
                prompt_vision = """
                Analizza questi dati e convertili in formato testuale professionale.
                ESTRAI: Località, Data (2026), Numero partenti, Quota, Peso/Zavorra, e Sequenza Risultati Recenti con distacchi.
                """
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text
                st.success("DATI ESTRATTI DAGLI SCREENSHOT ACQUISITI! ☕")

                # FASE 2: ANALISI PERPLEXITY (SONAR) - RICALIBRATA
                prompt_pplx = f"""
                ISTRUZIONE MANDATORIA: Esegui l'analisi basandoti PRIMARIAMENTE sui DATI DI INPUT forniti sotto. 
                Usa la tua ricerca online SOLO per integrare informazioni su Meteo, Superficie o News dell'ultimo minuto. 
                NON dichiarare che i dati mancano se sono presenti nei DATI DI INPUT.

                DATI DI INPUT (ESTRATTI DAGLI SCREENSHOT): 
                {dati_estratti}

                PROTOCOLLO FRANCIA (PSF/TURF):
                - Se Peso ≥ 58kg e forma recente contiene 3 o 4: ABISSO (Zavorra critica). [cite: 2026-02-23]
                - 4° posto è MARMO solo se distacco < 2.5 lunghezze. Oltre è RUGGINE. [cite: 2026-02-23]

                PROTOCOLLO SUD AFRICA (LUNGHEZZE):
                - 4°/5° posto con distacco < 2.0 lunghezze = MARMO. [cite: 2026-02-23]
                - Dual-Place (2 piazzati): Accetta solo 1-1, 1-2 o MARMO 4/5. 8°, 9° o 0 = ABISSO. [cite: 2026-02-23]

                PROTOCOLLO USA:
                - Focus Beyer crescenti 2026. Sequenza 1-2 obbligatoria. [cite: 2026-02-23]

                REFERTO FINALE:
                '💎 SOGGETTO AD ALTA EFFICIENZA: [NOME]. 
                MOTIVAZIONE: [Analisi basata sui dati di input e condizioni live].'
                USA TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA. SINTASSI MAIUSCOLA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 2. SENTENZA TECNICA 💙")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper() or "SOGGETTO" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
