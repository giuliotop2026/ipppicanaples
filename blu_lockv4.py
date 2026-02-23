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
                VALUTAZIONE TECNICA GLOBALE SULLA STABILITÀ DELLE PERFORMANCE ATLETICHE PROFESSIONALI.
                
                DATI DI INPUT:
                {dati_estratti}
                
                REQUISITO TEMPORALE: Usa esclusivamente dati del 2026. Ignora i dati storici precedenti.
                
                PROTOCOLLO 1: ANALISI UNIVERSALE (EUROPA/TURF)
                1. Identifica Meteo e Tipologia Superficie (ERBA/TURF o SABBIA/DIRT).
                2. FILTRO 'FORMA INVIOLABILE': Analizza gli ultimi 3 test. Se un soggetto ha un valore > 3 (4, 5, RP, Squalifica), è ABISSO.
                3. REGOLA HIGHLANDER: Identifica il 'Secondo Migliore' per densità tecnica (Rating/Peso). Deve schiacciare il favorito di carta.
                
                PROTOCOLLO 2: MODULO USA/DIRT (SABBIA AMERICANA)
                - Se la superficie è DIRT USA: Ignora la zavorra (peso) come fattore primario.
                - FOCUS: Cerca 'Speed Figures' o 'Beyer' del 2026. Cerca CAZZIMMA ESPLOSIVA (valori crescenti).
                - FILTRO STRETTISSIMO: Richiesta sequenza 1-2 nelle ultime due gare. Il 3° posto è ABISSO.
                
                PROTOCOLLO 3: MODULO SUD AFRICA (CELERITAS - 2 PIAZZATI)
                - Se Sud Africa (Kenilworth, Greyville, ecc.): Verifica se il campo è ridotto (solo 2 piazzati disponibili).
                - REGOLA DUAL-PLACE: Forma recente obbligatoria 1-1 o 1-2. Se c'è un 3 recente, il cantiere chiude.
                - FOCUS: 'Closing Speed' sul rettilineo lungo. Identifica il fondista veloce che non affonda nel CEMENTO.
                
                REFERTO FINALE (LINGUAGGIO ANALITICO):
                '💎 SOGGETTO AD ALTA EFFICIENZA INDIVIDUATO: [NOME]. 
                MOTIVAZIONE TECNICA: [Analisi del rapporto carico/zavorra o esplosività Beyer e costanza 1-2 per garantire il MARMO oggi].'
                
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
