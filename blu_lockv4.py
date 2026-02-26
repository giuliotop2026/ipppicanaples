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

st.title("🤠 SNIPER 100.1: OMNISCIENT SHERIFF")
st.markdown("### *'Filtro Cristallo 2.1. Eccezione Motore Cieco. Visione Totale.'*")

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

# --- 4. IL GRILLETTO (PROTOCOLLO ESPERTO DINAMICO) ---
if st.button("🐎 SCATENA IL DUELLO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO STA SCANSIONANDO L'ABISSO E I MOTORI CIECHI... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI L'ESPERTO DINAMICO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA (VISION)
                - Identifica l'IPPODROMO e la TIPOLOGIA DI GARA (Maiden, Nastri, Trotto, Galoppo).
                - Nel TROTTO, leggi 'REC' (Record) come valore tecnico. Nel GALOPPO leggi RT. [cite: 2026-02-25]
                - Estrai per ogni riga: Numero, Nome, RT/Rec, GG, SEQ (primo a sinistra = gara più recente), Quota. Le sigle RP, RI, DAI, FE, CD sono squalifiche/cadute.

                FASE 2: APPLICAZIONE FILTRI (GRANITO 3.0 + CRISTALLO 2.1)
                1. MURO FORMA: SEQ deve iniziare con 1 o 2. [cite: 2026-02-25]
                2. FILTRO CRISTALLO 2.1 (FLESSIBILITÀ ANTI-SQUALIFICA): 
                   - Scarta il cavallo SOLO se presenta squalifiche (RP, RI, DAI, FE, CD) nelle sue DUE gare più recenti (i primi due valori a sinistra della SEQ).
                   - Se la squalifica è vecchia (terza, quarta o quinta posizione) ma il cavallo ha superato il Muro Forma recente (1 o 2), IL CAVALLO È PERDONATO E PASSA.
                3. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                4. POLMONI D'ACCIAIO E "MOTORE CIECO" (CRITICO): 
                   - Cerca chi ha il miglior valore tecnico (RT/Rec). Se l'RT è debole e non da vertice, DEVE ESSERE SCARTATO.
                   - ECCEZIONE MOTORE CIECO: Se il valore RT/Rec è "N/A", "ASSENTE", "NON DISPONIBILE" o vuoto, MA il cavallo ha VINTO l'ultima corsa (SEQ inizia con '1') ed è fresco (GG < 45), PASSA IL FILTRO DI DIRITTO per manifesta forma cinetica in pista. IGNORA LA QUOTA. [cite: 2026-02-20]

                FASE 3: REFERTO FINALE SINTETICO
                '🌍 BERSAGLIO: [NAZIONE] - [IPPODROMO] - [TIPO GARA]'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - [NOME CAVALLO 1]: PASSATO (GG [X], SEQ [Y], RT/REC [Z])
                (Elenca solo chi passa i filtri. OBBLIGATORIO mostrare GG, SEQ e RT/Rec).

                SE C'È UN VERO SACRO GRAAL:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [Motivazione rapida su forma, superiorità tecnica o eccezione motore cieco].'
                
                SE NON C'È PERFEZIONE O I SUPERSTITI SONO DEBOLI: 
                '🌵 NESSUNA PEPITA IN QUESTO FIUME. I SUPERSTITI MANCANO DI POLMONI D'ACCIAIO O STABILITÀ.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA RISCOSSA" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
                
