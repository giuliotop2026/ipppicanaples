import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# 1. NOTIFICA SONORA - PROTOCOLLO SONIC
def play_beep():
    beep_html = """
    <audio autoplay>
      <source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg">
    </audio>
    """
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE - DOPPIA BENZINA
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ CHIAVI MANCANTI NEI SECRETS! AGGIUNGI GEMINI_API_KEY E PERPLEXITY_API_KEY.")
    st.stop()

# Innesco motori
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="PERFORMANCE ANALYTICS 6.7", page_icon="📈", layout="centered")

# --- INTERFACCIA ---
st.title("📈 PERFORMANCE ANALYTICS 6.7 🚀")
st.markdown("## **MODELLAZIONE ANALITICA: PROTOCOLLO LUNGHEZZE** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 6.7: PATCH LUNGHEZZE SUD AFRICA + USA BEYER.")

# 3. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 AVVIA MODELLAZIONE ANALITICA"):
    if not uploaded_files:
        st.warning("CARICA LE FOTO PER INIZIARE!")
    else:
        with st.spinner("SCANSIONE ABISSO IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE
                prompt_vision = """
                Analizza questi dati e convertili in formato testuale professionale.
                ESTRAI CON RIGORE: 
                1. Località e data (Cerca riferimenti 2026).
                2. Numero di partenti e piazzati totali (es. 1-2 o 1-3).
                3. Elenco partecipanti con: Quota, Peso/Zavorra, e Sequenza Risultati Recenti (numeri E distacchi in lunghezze se presenti).
                """
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text
                st.success("DATI ACQUISITI! INNESCAMENTO SONAR 6.7... ☕")

                # FASE 2: ANALISI PERPLEXITY 6.7
                prompt_pplx = f"""
                VALUTAZIONE TECNICA SULLA STABILITÀ DELLE PERFORMANCE 2026.
                DATI DI INPUT: {dati_estratti}

                PROTOCOLLO SUD AFRICA (PATCH 6.7 - LUNGHEZZE):
                1. Se località Sud Africa (Greyville, Kenilworth, ecc.):
                2. REGOLA LUNGHEZZE: Un 4° o 5° posto è MARMO solo se il distacco è < 2.5 lunghezze. Se distacco > 5 lunghezze, il soggetto è ABISSO (anche se è arrivato 1° o 2° in passato).
                3. DUAL-PLACE (2 PIAZZATI): Se la gara ha solo 2 piazzati, accetta solo 1-1, 1-2 o un '4° lunghezze marmo'. Ogni altra sequenza è RUGGINE.

                PROTOCOLLO USA (DIRT/BEYER):
                - Se USA DIRT: Ignora peso. Cerca Beyer Speed Figures crescenti nel 2026. 
                - Requisito: Sequenza 1-2 nelle ultime due gare. Il 3° è ABISSO.

                PROTOCOLLO EUROPA (TURF):
                - FILTRO FORMA: Qualsiasi valore > 3 è ABISSO.
                - REGOLA HIGHLANDER: Identifica il 'Secondo Migliore' per densità tecnica (Rating/Peso).

                REFERTO FINALE:
                '💎 SOGGETTO AD ALTA EFFICIENZA: [NOME]. 
                MOTIVAZIONE: [Analisi distacchi e densità per garantire il MARMO oggi].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA. SINTASSI MAIUSCOLA.
                """
                
                messages = [
                    {"role": "system", "content": "Sei un analista senior esperto in modellazione statistica sportiva."},
                    {"role": "user", "content": prompt_pplx}
                ]
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 2. SENTENZA TECNICA 💙")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper() or "SOGGETTO" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
