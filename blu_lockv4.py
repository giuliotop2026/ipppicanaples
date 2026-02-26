import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA WESTERN SALOON (LIGHT THEME) ---
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

st.title("🤠 SNIPER 100.0: THE OMNISCIENT SHERIFF")
st.markdown("### *'Filtro Cristallo Anti-Squalifica. Visione Totale.'*")

# --- 3. SELEZIONE TERRITORIO ---
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
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO ESPERTO DINAMICO + CRISTALLO 2.0) ---
if st.button("🐎 SCATENA IL DUELLO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO STA SCANSIONANDO L'ABISSO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI L'ESPERTO DINAMICO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA (VISION)
                - Identifica l'IPPODROMO e la TIPOLOGIA DI GARA (Maiden, Nastri, Trotto, Galoppo).
                - Nel TROTTO, leggi 'REC' (Record) come valore tecnico. [cite: 2026-02-25]
                - Estrai per ogni riga: Numero, Nome, RT/Rec, GG, SEQ, Quota e Metri.

                FASE 2: APPLICAZIONE FILTRI (GRANITO 3.0 + CRISTALLO 2.0)
                1. MURO FORMA: SEQ deve iniziare con 1 o 2. [cite: 2026-02-25]
                2. FILTRO CRISTALLO (ANTI-SQUALIFICA): 
                   - SE L'ULTIMO ESITO È RP, RI, DAI, SCARTA IMMEDIATAMENTE (INSTABILITÀ). [cite: 2026-02-15]
                   - CONTA LE SQUALIFICHE (RP, RI, DAI) NELLA SEQUENZA DI 5 GARE. SE SONO >= 2, IL CAVALLO È RADIOATTIVO. ELIMINA. [cite: 2026-02-20]
                3. FILTRO RUGGINE: GG < 45. (Eccezione: 'Iron Lung' se RT/Rec è dominante). [cite: 2026-02-25]
                4. SENTINELLA QUOTE: Se Quota > 15.00, richiede RT/Rec superiore di almeno 5 punti. [cite: 2026-02-20]
                5. BIAS NASTRI: Priorità alla 'Lepre' (0m) se pulita. [cite: 2026-02-24]

                FASE 3: REFERTO FINALE
                '🌍 BERSAGLIO: [NAZIONE] - [IPPODROMO] - [TIPO GARA]'
                '🏆 SACRO GRAAL INDIVIDUATO: PARTICELLA [NUMERO #] - [NOME]'
                'ANALISI: [Dettaglio su RT/Rec, GG e assenza di squalifiche ripetute].'
                'BULLONE SERRATO: [Conferma stabilità andatura e requisiti].'
                
                SE NON C'È PERFEZIONE: '🌵 NESSUNA PEPITA IN QUESTO FIUME.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "SACRO GRAAL" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
