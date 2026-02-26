import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA GOLDEN EYE (CONTRASTO MASSIMO) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #05140b; 
        background-image: radial-gradient(circle, #0e2a1d 0%, #05140b 100%);
        color: #ffffff; 
        font-family: 'Courier New', Courier, monospace; 
    }
    h1, h2, h3 { 
        color: #ffd700 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 3px 3px 6px #000;
        border-bottom: 2px solid #ffd700;
    }
    /* Miglioramento leggibilità testo nelle info */
    .stAlert p {
        color: #ffffff !important;
        font-size: 1.2rem !important;
        line-height: 1.6 !important;
        text-shadow: 1px 1px 2px #000;
    }
    .stButton>button { 
        background-color: #8b0000 !important; 
        color: #ffffff !important; 
        border: 2px solid #ffd700 !important; 
        font-weight: bold; font-size: 1.4em; text-transform: uppercase;
        border-radius: 0px; height: 3.5em;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.7);
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PROTOCOLLO SONORO (GONG DELLA VITTORIA) ---
def play_victory_sound():
    # Suono di campana da pugilato per annunciare il Sacro Graal
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    sound_html = f"""
        <audio autoplay>
            <source src="{audio_url}" type="audio/mpeg">
        </audio>
    """
    components.html(sound_html, height=0, width=0)

# --- 3. CASSAFORTE API ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ MUNIZIONI MANCANTI (GEMINI_API_KEY)!")
    st.stop()

st.title("🏇 SNIPER 40.0: GOLDEN EYE")
st.markdown("### *'Contrasto sbloccato. Radar acustico attivo. Mappatura Rec/RT integrata.'*")

nazione = st.selectbox("🌍 TERRITORIO DI CACCIA:", [
    "UK", "IRLANDA", "USA", "ITALIA", "FRANCIA", "SUD AFRICA", "AUSTRALIA"
])

uploaded_files = st.file_uploader("📸 CARICA GLI SCREENSHOT (TABELLA STATISTICHE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("🏁 ESEGUI PROTOCOLO GRANITO 3.0"):
    if not uploaded_files:
        st.warning("CARICA I POSTER, COMANDANTE!")
    else:
        with st.spinner("SCANSIONE MOLECOLARE IN CORSO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                
                # PROMPT CALIBRATO SULLA MATRICE SNAI
                prompt = f"""
                SISTEMA: PROTOCOLO GRANITO 3.0 - ANALISI IPPICA SENIOR. [cite: 2026-02-25]
                SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                NAZIONE: {nazione}

                FASE 1: ESTRAZIONE (Cerca la tabella 'STATISTICHE')
                Identifica ogni riga della tabella. Mappa i dati così:
                - # [NUMERO]
                - NOME CAVALLO (Dalla colonna 'Partente')
                - RT [Dalla colonna 'Rec.']
                - GG [Dalla colonna 'GG']
                - SEQ [Dalla colonna 'Ultimi Arrivi']

                FASE 2: FILTRI DI ELIMINAZIONE 15.15 [cite: 2026-02-25]
                1. MURO FORMA: Il primo quadratino a sinistra in 'Ultimi Arrivi' deve essere 1 o 2.
                2. FILTRO RUGGINE: GG deve essere < 45. Se è un DEBUTTANTE (N/A), scarta.
                3. SE MAIDEN: Accetta solo SEQ 1 e GG < 15.

                FASE 3: DENSITÀ TECNICA (POLMONI D'ACCIAIO) [cite: 2026-02-20]
                Confronta l'RT (Rec.) dei superstiti. Identifica il vincitore nascosto.

                REFERTO FINALE:
                '🏆 SACRO GRAAL INDIVIDUATO: PARTICELLA [NUMERO #] - [NOME]' (O 'NESSUN SACRO GRAAL')
                'PIANO DI CORSA: [ANALISI DETTAGLIATA SU GG E DENSITÀ TECNICA RT].' [cite: 2026-02-18]
                'BULLONE SERRATO: [CONFERMA REQUISITI SUPERATI].'
                """
                
                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                # Visualizzazione con stile ad alto contrasto
                st.info(sentenza)
                
                # TRIGGER SONORO E VISIVO
                if "NESSUN" not in sentenza.upper() and "GRAAL" in sentenza.upper():
                    play_victory_sound()
                    st.balloons()
                    st.success("✅ OBIETTIVO IDENTIFICATO. PROCEDERE AL MERCATO.")
                    
            except Exception as e:
                st.error(f"☠️ ERRORE DI SISTEMA: {e}")
