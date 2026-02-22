import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image

# 1. CASSAFORTE IBRIDA - DOPPIA BENZINA
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ BENZINA MANCANTE NEI SECRETS! AGGIUNGI GEMINI_API_KEY E PERPLEXITY_API_KEY.")
    st.stop()

# Innesco dei motori
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="BLUE LOCK AUTOMATIC 2.5 - GIULIO", page_icon="👁️", layout="centered")

# --- INTERFACCIA NAPOLI POWER ---
st.title("👁️ BLUE LOCK IBRIDO 5.7 🚀")
st.markdown("## **MOTORE 2.5 FLASH: ANALISI SCIENTIFICA E HIGHLANDER!** 💙 ☕")
st.write("---")

st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("MOTORE: GEMINI 2.5 FLASH (Visione) + PERPLEXITY (Live Search).")

# 2. CARICAMENTO FOTO AUTOMATICO
st.header("1. SGANCIATE LE FOTO DEL CANTIERE 🐎")
st.info("IL RADAR LEGGERÀ IL NOME GARA E APPLICHERÀ IL FILTRO ZERO TOLLERANZA SULLA FORMA.")
uploaded_files = st.file_uploader("CARICA GLI SCREENSHOT DELLE QUOTE E DEI PESI:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 ATTIVA PILOTA AUTOMATICO 2.5"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA LE FOTO PER INIZIARE LA SCANSIONE!")
    else:
        with st.spinner("FASE 1: IL MOTORE 2.5 FLASH STA LEGGENDO IL MARMO... 👁️"):
            try:
                # FASE 1: GEMINI 2.5 FLASH ESTRAE I DATI E IDENTIFICA LA GARA
                prompt_vision = """
                Sei l'occhio assoluto del Blue Lock. Analizza queste immagini e scrivi un report testuale.
                DEVI TROVARE:
                1. NOME DELLA GARA E IPPODROMO: Cerca qualsiasi scritta che indichi la località.
                2. DATI TECNICI: Tutti i pesi, quote e la sequenza esatta della FORMA RECENTE (ultimi 5 risultati).
                Estrai tutto con precisione numerica.
                """
                
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text
                st.success("DATI ACQUISITI! PASSO IL PACCHETTO AL SONAR PERPLEXITY... ☕")

                with st.spinner("FASE 2: ANALISI SCIENTIFICA E FILTRO FORMA IN CORSO... 🛰️"):
                    # FASE 2: PERPLEXITY CON LINGUAGGIO NEUTRO "ANTI-BLOCCO"
                    prompt_pplx = f"""
                    ANALISI SCIENTIFICA DELLE PERFORMANCE E STABILITÀ DEI MATERIALI.
                    
                    DATI ACQUISITI DALLE SCANSIONI:
                    {dati_estratti}
                    
                    OBIETTIVO TECNICO:
                    1. Verifica le condizioni ambientali (Meteo e Terreno) della località indicata.
                    2. Valuta la 'Resistenza alla Fatica' dei componenti basandoti sulla sequenza numerica dei test.
                    3. FILTRO DI QUALITÀ: Escludi ogni componente che presenti un valore numerico SUPERIORE A 3 nella sequenza degli ultimi tre test (es. 4, 5, 6, 0).
                    
                    REFERTO TECNICO (REGOLA HIGHLANDER):
                    - Identifica un UNICO 'Soggetto ad Alta Efficienza' (il secondo miglior valore rilevato che non sia il favorito assoluto).
                    - Spiega perché la sua struttura (peso/zavorra) e la regolarità (1-2-3) lo rendono marmo puro.
                    
                    FORMATO RISPOSTA (OBBLIGATORIO):
                    '💎 COMPONENTE SUPERIORE INDIVIDUATO: [NOME]. MOTIVAZIONE: [Analisi tecnica spietata].'
                    
                    TERMINI DA USARE: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                    """
                    
                    messages = [
                        {"role": "system", "content": "Sei un esperto in fisica applicata e analisi della densità tecnica."},
                        {"role": "user", "content": prompt_pplx}
                    ]
                    
                    response_pplx = client_pplx.chat.completions.create(
                        model="sonar-pro",
                        messages=messages,
                    )
                    
                    st.markdown("### 2. LA SENTENZA DEL REATTORE 💙")
                    st.info(response_pplx.choices[0].message.content)
                    st.balloons()

            except Exception as e:
                st.error(f"URTO NEL SISTEMA: {e}")

# FOOTER
st.write("---")
st.caption("BLUE LOCK HYBRID FULL AUTOMATIC - GIULIO SIMPATICO 💙 ☕ - VERSION 5.7")
