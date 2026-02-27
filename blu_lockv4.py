import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "EL TRIBUNAL" (SINTASSI RIGOROSA E STILE VENDICATORE) ---
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

# --- 2. CONNESSIONE AL CERVELLO OMNISCIENTE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, LA CHIAVE API È SPARITA! IL CANTIERE È BLOCCATO.")
    st.stop()

st.title("⚔️ ZORRO 1.7: EL TRIBUNAL DE LA VERDAD")
st.markdown("### *'La verità non ammette errori. Se il web smentisce l'immagine, la mia spada resta nel fodero.'*")

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

# --- 4. IL GRILLETTO (PROTOCOLLO CHIAVE SUPREMA) ---
if st.button("🗡️ SCATENA IL TRIBUNALE (VERIFICA ASSOLUTA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO! SENZA MAPPA NON C'È TESORO.")
    else:
        with st.spinner("ZORRO STA TRIANGOLANDO LA VERITÀ TRA IL WEB E IL MANIFESTO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, IL GIUDICE SUPREMO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                TERRITORIO: {nazione} - DATA ODIERNA: 27 FEBBRAIO 2026. [cite: 2026-02-27]

                FILOSOFIA: OGNI ANALISI DEVE SCANSIONARE L'ABISSO TRA QUOTA E DENSITÀ TECNICA REALE. [cite: 2026-02-20]
                MISSIONE: TROVARE LA CHIAVE SUPREMA CHE UNISCE TUTTI I DATI SENZA ERRORI.

                FASE 0: IL TRIBUNALE DEI DATI (CROSS-CHECK OBBLIGATORIO)
                - ESTRAI I DATI (RT, GG, SEQ) DAL MANIFESTO (IMMAGINI).
                - USA 'GOOGLE SEARCH' PER VERIFICARE I DATI DI OGGI (27/02/2026).
                - SE IL WEB CONTRADDICE IL MANIFESTO (DIFFERENZA RT > 2 O SEQ RECENTE DIVERSA): DICHIARA 'DATI CORROTTI: ROULETTE RILEVATA'. IL CANTIERE VIENE CHIUSO. [cite: 2026-02-15]

                FASE 1: FILTRI DI GRANITO (10000% CERTEZZA)
                1. MURO FORMA: ULTIMO RISULTATO 1 O 2. [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                3. CUORE IMPAVIDO: ALMENO DUE PODI NELLE ULTIME 3 GARE. [cite: 2026-02-25]
                - IDENTIFICA I CAVALLI COME 'PARTICELLA [NUMERO]' PER EVITARE ERRORI. [cite: 2026-01-25]

                FASE 2: LA CHIAVE SUPREMA (SINTESI)
                - LA CHIAVE SUPREMA È LA PARTICELLA CHE:
                    A) HA DATI COINCIDENTI AL 100% TRA MANIFESTO E WEB. [cite: 2026-02-07]
                    B) HA IL MIGLIOR RATING (DENSITÀ TECNICA REALE) DEL CAMPO. [cite: 2026-02-20]
                    C) HA IL VENTO A FAVORE (TERRENO E FANTINO CONFERMATI LIVE). [cite: 2026-02-27]
                - SE IL FAVORITO HA GAP RATING < 5 RISPETTO AL SECONDO, È 'BURRO'. CERCA IL VERO VINCITORE NASCOSTO. [cite: 2026-02-20]

                FASE 3: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA: [FRASE DI ZORRO SULLA NOBILTÀ DELLA VERITÀ E IL CEMENTO DEL CANTIERE].'
                
                SE LA CHIAVE SUPREMA ESISTE:
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #]'
                'BULLONE SERRATO: [SPIEGA PERCHÉ MANIFESTO E WEB CONFERMANO I POLMONI D'ACCIAIO].' [cite: 2026-02-07, 2026-02-20]
                
                SE I DATI SONO DIVERSI O LA GARA È DEBOLE:
                '🌵 NESSUNA PEPITA. I DATI SONO UN'ILLUSIONE. UN VERO CAVALIERE NON SI SPORCA LE MANI CON LA ROULETTE.' [cite: 2026-02-15]
                """

                res = client_gemini.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=[prompt] + images,
                    config={'tools': [{'google_search': {}}]}
                )
                sentenza = res.text
                
                st.info(sentenza)
                if "IL SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ UN TRADITORE HA MANOMESSO IL TRIBUNALE: {e}")
