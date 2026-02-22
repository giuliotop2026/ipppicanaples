import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image

# 1. CASSAFORTE - DOPPIA BENZINA
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ CHIAVI MANCANTI NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="PERFORMANCE ANALYTICS 6.0", page_icon="📈", layout="centered")

# --- INTERFACCIA IN ALTO —--
st.title("📈 PERFORMANCE ANALYTICS 6.0 🚀")
st.markdown("## **MODELLAZIONE ANALITICA E STABILITÀ TECNICA** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 6.0: PROTOCOLLO PROFESSIONALE DATA-SCIENCE.")

# 2. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT DELLE PRESTAZIONI:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 AVVIA MODELLAZIONE ANALITICA"):
    if not uploaded_files:
        st.warning("CARICA LE FOTO PER INIZIARE!")
    else:
        with st.spinner("ELABORAZIONE MODELLO STOCASTICO... 👁️"):
            try:
                # FASE 1: GEMINI 2.5 FLASH ESTRAE I DATI PROFESSIONALI
                prompt_vision = """
                Analizza questi dati di performance atletica e convertili in formato testuale.
                ESTRAI CON RIGORE: 
                1. Località e data della sessione sportiva.
                2. Elenco dei partecipanti con: Indice di Mercato (Quota), Carico (Peso/Zavorra), e Sequenza Risultati Recenti (numeri esatti).
                Sii estremamente preciso, non omettere nulla.
                """
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text

                # FASE 2: PERPLEXITY - ANALISI TECNICA PROFESSIONALE
                # NOTA: Rimosso ogni riferimento a 'Blue Lock' per evitare confusione con l'anime
                prompt_pplx = f"""
                VALUTAZIONE TECNICA SULLA STABILITÀ DELLE PERFORMANCE ATLETICHE PROFESSIONALI.
                
                DATI DI INPUT:
                {dati_estratti}
                
                PROTOCOLLO DI ANALISI DATA-SCIENCE:
                1. Identifica le variabili ambientali (Meteo e Tipologia Superficie) per la località indicata.
                2. FILTRO DI AFFIDABILITÀ: Esamina la sequenza degli ultimi 3 test numerici. 
                   Qualsiasi partecipante con un valore numerico superiore a 3 (es. 4, 5, 0, RP, squalifica) deve essere classificato come 'Soggetto Instabile' ed escluso dall'analisi di affidabilità.
                3. Identifica il 'Soggetto con Efficienza Ottimale': deve essere il valore più competitivo che rispetti rigorosamente il filtro di stabilità (piazzamenti 1, 2 o 3) e che NON sia il leader assoluto del mercato (favorito di carta).
                
                REFERTO FINALE (LINGUAGGIO ANALITICO):
                '💎 SOGGETTO AD ALTA EFFICIENZA INDIVIDUATO: [NOME]. 
                MOTIVAZIONE TECNICA: [Analisi del rapporto tra carico/zavorra e costanza 1-2-3 per garantire la tenuta sulle condizioni odierne].'
                
                Usa i termini tecnici: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                messages = [
                    {"role": "system", "content": "Sei un analista senior esperto in modellazione statistica applicata allo sport professionistico."},
                    {"role": "user", "content": prompt_pplx}
                ]
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                )
                
                st.markdown("### 2. SENTENZA TECNICA 💙")
                st.info(response_pplx.choices[0].message.content)
                st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
