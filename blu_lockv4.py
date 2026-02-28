import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "EL DECODIFICADOR" (INALTERATA) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
        color: #1a1a1a; font-family: 'Georgia', serif; 
    }
    h1, h2, h3 { 
        color: #000000 !important; text-transform: uppercase; font-weight: 900; 
        text-shadow: 2px 2px 4px #8b4513; border-bottom: 4px solid #000000;
    }
    .stAlert p { color: #1a1a1a !important; font-size: 1.4rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #000000 !important; color: #ffd700 !important; 
        border: 2px solid #ffd700 !important; font-weight: bold; font-size: 1.8em; 
        width: 100%; border-radius: 50px; height: 3.5em; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO OMNISCIENTE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, LA CHIAVE API È SPARITA!")
    st.stop()

st.title("⚔️ ZORRO 1.25: EL DECODIFICADOR SUPREMO")
st.markdown("### *'Se il rating tace, il cuore del campione grida nei commenti. USA: la classe schiaccia la nebbia.'*")

# --- 3. SELEZIONE TERRITORIO (SUD AFRICA AGGIUNTO) ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "SUD AFRICA", "USA", "SVEZIA", "AUSTRALIA", "ITALIA", "FRANCIA", "UK", "IRLANDA", "GERMANIA"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO DECODIFICA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]: st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO AGGIORNATO 4.1) ---
if st.button("🗡️ SCATENA IL DECODIFICATORE (CHIAVE SUPREMA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA DECODIFICANDO L'ANIMA DELLA GARA... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # LOGICA SPECIFICA PER TERRITORIO
                logic_focus = ""
                if nazione == "USA":
                    logic_focus = """
                    REGOLE SPECIALI USA FOCUS:
                    - SE 'RT.' MANCA, USA GOOGLE SEARCH PER TROVARE I 'BEYER SPEED FIGURES'. [cite: 2026-02-27]
                    - ANALIZZA LA 'CLASSE': SE SCENDE DA 'STAKES' A 'CLAIMING', È UN TITANO. [cite: 2026-02-26]
                    """
                elif nazione == "SUD AFRICA":
                    logic_focus = """
                    REGOLE SPECIALI SUD AFRICA (FILTRO TITANIO 4.1):
                    - ANALIZZA I DATI DI 'COMPUTAFORM' E 'SIGNPOSTS'. [cite: 2026-02-25]
                    - FILTRO TITANIO: SE IL FAVORITO HA IL MIGLIOR RT ED È SEGNALATO COME 'BEST BET' NEI SIGNPOSTS, NON SCHIACCIARLO. È UN TITANO INVIOLABILE.
                    - LA CHIAVE SUPREMA DEVE AVERE GAP RATING >= 5 RISPETTO AL FAVORITO PER SCHIACCIARLO. [cite: 2026-02-20]
                    - IGNORA LE QUOTE: LA CHIAVE È IL SECONDO MIGLIORE PER DENSITÀ TECNICA E POLMONI D'ACCIAIO. [cite: 2026-02-20]
                    """

                prompt = f"""
                SEI ZORRO, IL DECODIFICATORE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                TERRITORIO: {nazione} - DATA: 28 FEBBRAIO 2026.

                {logic_focus}

                MISSIONE SUPREMA: IDENTIFICARE LA CHIAVE CHE BATTE OGNI FILTRO (10000% CERTEZZA). [cite: 2026-02-07]

                FASE 1: ANALISI FONDAMENTALE (MANIFESTO + WEB)
                - ESTRAI GG E SEQ. (LETTURA: TOP BOX = LATEST). [cite: 2026-02-27]
                - IDENTIFICA IL FAVORITO E IL SECONDO FAVORITO. [cite: 2026-02-26]

                FASE 2: FILTRI DI GRANITO
                1. MURO FORMA: ULTIMO RISULTATO 1 O 2. [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                3. CUORE IMPAVIDO: ALMENO DUE PODI NELLE ULTIME 3 GARE. [cite: 2026-02-25]

                FASE 3: LA CHIAVE SUPREMA (SINTESI)
                - LA CHIAVE SUPREMA È LA PARTICELLA CHE PASSA TUTTI I FILTRI E SCHIACCIA IL FAVORITO DEBOLE (GG > 45 O GAP RATING NEGATIVO). [cite: 2026-02-20]

                FASE 4: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA DEL DECODIFICATORE: [FRASE DI CAZZIMMA DI ZORRO].'
                SE LA CHIAVE ESISTE: '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #]'.
                ALTRIMENTI: '🌵 NESSUNA PEPITA. LA NEBBIA È TROPPO FITTA.' [cite: 2026-02-15]
                """

                res = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt] + images,
                    config={'tools': [{'google_search': {}}]}
                )
                
                sentenza = res.text if res.text else ""
                
                if sentenza:
                    st.info(sentenza)
                    if "IL SEGNO DELLA Z" in sentenza.upper():
                        play_victory_bell(); st.balloons()
                else:
                    st.error("☠️ IL DECODIFICATORE È RIMASTO IN SILENZIO. RIPROVA IL COLPO!")

            except Exception as e:
                st.error(f"☠️ UN TRADITORE HA MANOMESSO IL DECODIFICATORE: {e}")
