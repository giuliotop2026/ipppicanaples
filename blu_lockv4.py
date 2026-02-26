import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA ROYAL TURF 2.0 (STILE CANTIERE IPPICO) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #0e2a1d; 
        background-image: linear-gradient(180deg, #123524 0%, #071a10 100%);
        color: #f0f4f1; 
        font-family: 'Courier New', Courier, monospace; 
    }
    h1, h2, h3 { 
        color: #d4af37 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 2px 2px 5px #000;
    }
    .stButton>button { 
        background-color: #5d4037 !important; 
        color: #ffffff !important; 
        border: 3px solid #d4af37 !important; 
        font-weight: bold; font-size: 1.3em; text-transform: uppercase;
        width: 100%; border-radius: 12px; height: 3em;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    .stButton>button:hover { background-color: #d4af37 !important; color: #0e2a1d !important; }
    div[data-testid="stAlert"] {
        background-color: #071a10 !important;
        border: 2px solid #d4af37 !important;
        border-left: 10px solid #d4af37 !important;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/boxing-bell.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API (MUNIZIONI GEMINI)
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ MUNIZIONI MANCANTI (GEMINI_API_KEY)!")
    st.stop()

st.title("🏇 SNIPER 39.1: THE ANALYTIC BEAST")
st.markdown("### *'Cervello Gemini potenziato. Analisi molecolare attiva. Zero costi.'*")

nazione = st.selectbox("🌍 SELEZIONA IL TERRITORIO DI CACCIA:", [
    "UK", "IRLANDA", "USA", "ITALIA", "FRANCIA", "GERMANIA", "SVEZIA", "SUD AFRICA", "AUSTRALIA"
])

uploaded_files = st.file_uploader("📸 CARICA GLI SCREENSHOT DEL CAVEAU:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("🏁 ESEGUI PROTOCOLO GRANITO 3.0"):
    if not uploaded_files:
        st.warning("CARICA I POSTER, COMANDANTE!")
    else:
        with st.spinner("GEMINI STA ANALIZZANDO L'ABISSO CON LOGICA PERPLEXITY... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                
                # PROMPT POTENZIATO: LOGICA DI FERRO [cite: 2026-02-25]
                prompt = f"""
                SISTEMA: PROTOCOLO GRANITO 3.0 - ANALISI MOLECOLARE.
                RUOLO: ANALISTA IPPICO SENIOR (PHILOSOPHY: BLUE LOCK). [cite: 2026-01-19]
                SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                NAZIONE: {nazione}

                FASE 1: SCANSIONE CINETICA
                Identifica ogni particella (#). Estrai con precisione chirurgica:
                - # [NUMERO]
                - RT [RATING TECNICO]
                - GG [GIORNI DALL'ULTIMA CORSA]
                - SEQ [SEQUENZA RISULTATI - IL PRIMO A SINISTRA È IL PIÙ RECENTE]

                FASE 2: FILTRI INVIOLABILI (PROCESSO DI ELIMINAZIONE) [cite: 2026-02-25]
                1. MURO DELLA FORMA: Scarta chi non ha 1 o 2 come primo numero a sinistra.
                2. FILTRO RUGGINE: Scarta chi ha GG > 45 (o dati mancanti).
                3. PARAMETRO MAIDEN: Se la corsa è Maiden, accetta solo SEQ 1 e GG < 15.

                FASE 3: ANALISI DENSITÀ TECNICA (IL SECONDO MIGLIORE) [cite: 2026-02-20]
                Ignora le quote. Cerca chi ha "Polmoni d'Acciaio". Identifica il vincitore nascosto che schiaccia il favorito di carta.

                REFERTO FINALE:
                '🏆 SACRO GRAAL INDIVIDUATO: PARTICELLA [NUMERO #]' (OPPURE 'NESSUN SACRO GRAAL: INSTABILITÀ')
                'PIANO DI CORSA: [ANALISI DETTAGLIATA DELLA SUPERIORITÀ TECNICA].' [cite: 2026-02-18]
                'BULLONE SERRATO: [CONFERMA GG E SEQ INVIOLABILI].'
                """
                
                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "NESSUN" not in sentenza.upper() and "GRAAL" in sentenza.upper():
                    play_beep()
                    st.balloons()
            except Exception as e:
                st.error(f"☠️ ERRORE DI SISTEMA: {e}")
