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
    .stAlert p { color: #3d2b1f !important; font-size: 1.3rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #a0522d !important; color: #fff8dc !important; 
        border: 3px solid #5a3a22 !important; font-weight: bold; font-size: 1.5em; 
        width: 100%; border-radius: 8px; height: 3.5em;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #0e2a1d !important; }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO OMNISCIENTE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ EHI STRANIERO, MANCANO LE MUNIZIONI (GEMINI_API_KEY)!")
    st.stop()

st.title("🤠 SNIPER 101.0: PERFECT BOUNTY HUNTER")
st.markdown("### *'Patch Maiden Attiva. Bias Nastri. Perdono Squalifiche. Zero Errori.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ TERRITORIO DI CACCIA:", [
    "UK", "USA", "ITALIA", "FRANCIA", "IRLANDA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "AUSTRALIA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (STATISTICHE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI IN BACHECA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (LA FUSIONE TOTALE) ---
if st.button("🐎 SCATENA IL DUELLO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO STA INCROCIANDO TUTTE LE LEGGI... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # IL PROMPT SUPREMO CHE CONTIENE TUTTI I TUOI SEGRETI [cite: 2026-01-20, 2026-02-25]
                prompt = f"""
                SEI L'ARCHITETTO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA
                - Identifica l'IPPODROMO, la DISTANZA e la TIPOLOGIA DI GARA (Maiden, Nastri, Handicap, ecc.).
                - Estrai per ogni riga: Numero, Nome, NASTRO/METRI (se presente), RT/Rec, GG, SEQ, Quota.

                FASE 2: APPLICAZIONE FILTRI (IL PROTOCOLLO DEFINITIVO)
                1. MURO FORMA: SEQ deve iniziare con 1 o 2. [cite: 2026-02-25]
                2. CRISTALLO 2.1 (ANTI-SQUALIFICA): Scarta SOLO se le squalifiche (RP, RI, DAI, FE, CD) sono nelle DUE gare più recenti. Le vecchie squalifiche sono perdonate se ha superato il Muro Forma.
                3. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                4. POLMONI D'ACCIAIO & MOTORE CIECO: Identifica il miglior valore tecnico (RT/Rec). Se "N/A" ma il cavallo ha VINTO (SEQ 1) ed è fresco (GG < 45), passa per manifesta forma in pista. Ignora le quote. [cite: 2026-02-20]
                
                PROTOCOLLI SPECIALI (PRIORITÀ ASSOLUTA):
                5. PATCH ANTI-MAIDEN: SE LA CORSA È "MAIDEN", ACCETTA SOLO SEQ "1" (il "2" si scarta). ACCETTA SOLO GG < 15. IL GAP RT DEVE ESSERE >= 5 SUL SECONDO. Se fallisce, scrivi 'NESSUN SACRO GRAAL: INSTABILITÀ MAIDEN'. [cite: 2026-02-25]
                6. BIAS NASTRI (LEPRE): Nelle corse a nastri, il cemento è il cavallo a 0m (primo nastro). Dai priorità assoluta alla lepre se passa i filtri 1 e 2.
                7. BIAS NAPOLI: Se l'ippodromo è NAPOLI, tollera un '4' recente per Polmoni d'Acciaio.
                8. SOUTHWELL KEY: Se l'ippodromo è SOUTHWELL, ignora favoriti < 3.00.

                FASE 3: REFERTO FINALE
                '🌍 BERSAGLIO: [NAZIONE] - [IPPODROMO] - [TIPO GARA]'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - [NOME CAVALLO]: PASSATO (GG [X], SEQ [Y], RT/REC [Z], NASTRO [W se presente])
                (Elenca solo i superstiti. Mostra i dati.)

                SE C'È UN SACRO GRAAL:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [Motivazione su RT, Nastri, Maiden o Motore Cieco].'
                
                SE NON C'È PERFEZIONE: 
                '🌵 NESSUNA PEPITA IN QUESTO FIUME.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA RISCOSSA" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
