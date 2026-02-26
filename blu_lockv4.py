import streamlit as st
from google import genai
from PIL import Image
import base64
import io
import streamlit.components.v1 as components

# --- 1. GRAFICA 'MEZZOGIORNO DI FUOCO' (LIGHT THEME) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; 
        background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
        color: #3d2b1f; 
        font-family: 'Courier New', Courier, monospace; 
    }
    h1, h2, h3 { 
        color: #8b4513 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 1px 1px 2px #cda26e;
        border-bottom: 3px solid #5a3a22;
    }
    .stAlert p { color: #3d2b1f !important; font-size: 1.4rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #a0522d !important; color: #fff8dc !important; 
        border: 3px solid #5a3a22 !important; font-weight: bold; font-size: 1.6em; 
        width: 100%; border-radius: 8px; height: 3.5em;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #0e2a1d !important; }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO GEMINI ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ EHI STRANIERO, MANCANO LE MUNIZIONI (GEMINI_API_KEY)!")
    st.stop()

st.title("🤠 SNIPER 77.0: TOTAL ELIMINATOR")
st.markdown("### *'Protocollo Infallibile. Sentinella delle Quote. Zero Margine di Errore.'*")

# --- 3. BACHECA DEI RICERCATI ---
nazione = st.selectbox("🗺️ TERRITORIO DI CACCIA:", [
    "UK", "IRLANDA", "USA", "ITALIA", "FRANCIA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "AUSTRALIA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (STATISTICHE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI IN BACHECA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_container_width=True)

# --- 4. IL GRILLETTO (ALGORITMO DEFINITIVO) ---
if st.button("🐎 SCATENA IL DUELLO (TROVA LA MULTIPLA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO STA SCANSIONANDO L'ABISSO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # IL PROMPT CHE FONDE TUTTA LA NOSTRA STORIA
                prompt = f"""
                SISTEMA: PROTOCOLO BLUE LOCK - ANALISI MOLECOLARE DEFINITIVA.
                SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                NAZIONE: {nazione}

                FASE 1: GABBIA DI LETTURA CHIRURGICA
                - Identifica: Numero, Nome, RT (Rating/Rec), GG (Giorni), SEQ (Ultimi Arrivi), Quota.
                - CRITICO: NON scambiare PESO con RT. [cite: 2026-02-25]

                FASE 2: LE LEGGI DELLA FRONTIERA (GRANITO 3.0 + IRON LUNG)
                1. MURO FORMA: SEQ deve iniziare con 1 o 2. (SOLO 1 se Maiden). [cite: 2026-02-25]
                2. FILTRO RUGGINE (IRON LUNG): GG deve essere < 45. TOLLERA fino a 90 solo se RT è dominante (+5 punti sul secondo). [cite: 2026-02-25]
                3. SENTINELLA DEL MERCATO: Se la QUOTA è > 15.00, il cavallo DEVE avere un RT superiore di almeno 5 punti rispetto agli altri. Altrimenti, SCARTA: è instabilità. [cite: 2026-02-20]
                4. BIAS NASTRI/NAPOLI: Se Nastri, priorità 0m. Se Napoli, tollera '4' recente.

                FASE 3: REFERTO FINALE
                Voglio solo la verità nuda e cruda. Se non c'è perfezione, scarta la gara.

                REFERTO:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'COLPO SICURO: [Analisi su RT schiacciante, GG e Sentinella Quote].'
                'BULLONE SERRATO: [Conferma SEQ e Cemento Tecnico].'
                
                SE NON C'È PERFEZIONE:
                '🌵 NESSUNA PEPITA: [MOTIVO BREVE].'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA" in sentenza.upper() and "NESSUNA" not in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
