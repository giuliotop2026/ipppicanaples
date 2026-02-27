import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "CATEDRAL DE LA JUSTICIA" ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; 
        background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
        color: #1a1a1a; 
        font-family: 'Georgia', serif; 
    }
    h1, h2, h3 { 
        color: #000000 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 2px 2px 4px #8b4513;
        border-bottom: 4px solid #000000;
    }
    .stAlert p { color: #1a1a1a !important; font-size: 1.4rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #000000 !important; color: #ffd700 !important; 
        border: 2px solid #ffd700 !important; font-weight: bold; font-size: 1.8em; 
        width: 100%; border-radius: 50px; height: 3.5em;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #000000 !important; border: 2px solid #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO DEL VENDICATORE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, LA CHIAVE API È SPARITA!")
    st.stop()

st.title("⚔️ ZORRO 1.8: LA VOLUNTAD DE ORO")
st.markdown("### *'Se le tabelle sono mute, interrogo il commento. Se il web mormora di un campione, io incido la Z.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "AUSTRALIA", "USA", "UK", "ITALIA", "FRANCIA", "IRLANDA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO IL TRIBUNALE:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO VOLUNTAD DE ORO) ---
if st.button("🗡️ SCATENA LA DEDUZIONE DI ZORRO (CHIAVE SUPREMA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA FIUTANDO L'ORO TRA LE RIGHE E IL WEB... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, IL GIUDICE SUPREMO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                TERRITORIO: {nazione} - DATA ODIERNA: 27 FEBBRAIO 2026. [cite: 2026-02-27]

                MISSIONE SUPREMA: TROVARE IL VINCITORE ANCHE QUANDO I DATI TABELLARI SONO FRAMMENTATI.

                FASE 0: L'ORECCHIO DEL POPOLO (DEDUZIONE TESTUALE E WEB)
                - SE LE TABELLE SEQ/GG SONO VUOTE: Scansiona il 'COMMENTO CORSA' e le descrizioni testuali. [cite: 2026-02-27]
                - USA 'GOOGLE SEARCH' PER CERCARE SPECIFICAMENTE: 'FORM GUIDE [NOME CAVALLO] [DATA]', 'RACING POST [NOME CAVALLO]', 'PUNTERS.COM.AU [NOME CAVALLO]'.
                - PROTOCOLLO DEDUTTIVO: Se il testo dice 'Beaten narrowly last time' o 'Winner of 2 from 3', questo VALE come conferma per il MURO FORMA e il CUORE IMPAVIDO. [cite: 2026-02-20]

                FASE 1: FILTRI DI GRANITO FLESSIBILE (CAZZIMMA TATTICA)
                - MURO FORMA: Ultimo risultato 1 o 2 (da tabella o da testo). [cite: 2026-02-25]
                - FILTRO RUGGINE: GG < 45. Se il testo dice 'In form' o 'Recent run', assumi GG < 45. [cite: 2026-02-25]
                - CUORE IMPAVIDO: Almeno 2 podi in 3 gare. Accetta conferme verbali (es: 'Consistent performer with many placings'). [cite: 2026-02-25]

                FASE 2: LA CHIAVE SUPREMA (RICERCA DELL'ANOMALIA)
                - IDENTIFICA LA CHIAVE: La particella che unisce miglior RATING (tabellare o web) e miglior CONDIZIONE LIVE (fantino/terreno). [cite: 2026-02-20, 2026-02-27]
                - USA Focus: Favorito tecnico con quota < 8.00. [cite: 2026-02-26]
                - Australia Focus: Se Quota < 3.00 e Commento Positivo, la Pepita è reale. [cite: 2026-02-27]

                FASE 3: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA: [UNA FRASE DI CAZZIMMA DI ZORRO SULL'ORO CHE NON PUÒ ESSERE NASCOSTO].'
                
                SE LA CHIAVE È TROVATA (ANCHE PER DEDUZIONE):
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [SPIEGA PERCHÉ IL TESTO O IL WEB CONFERMANO I POLMONI D'ACCIAIO NONOSTANTE LE TABELLE VUOTE].' [cite: 2026-02-07, 2026-02-20]
                
                SE PROPRIO NON ESISTE NULLA:
                '🌵 NESSUNA PEPITA. NEMMENO LE OMBRE SANNO CHI VINCERÀ OGGI.' [cite: 2026-02-15]
                """

                res = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt] + images,
                    config={'tools': [{'google_search': {}}]}
                )
                sentenza = res.text
                
                st.info(sentenza)
                if "IL SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ UN TRADITORE HA MANOMESSO IL TRIBUNALE: {e}")
