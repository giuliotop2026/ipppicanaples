import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "EL DECODIFICADOR" (INVARIATA) ---
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

st.title("⚔️ ZORRO 1.35: EL DECODIFICADOR SUPREMO (TITAN)")
st.markdown("### *'Se il rating tace, il cuore del campione grida nei commenti. Il Titan analizza, il Flash colpisce.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "USA", "UK", "SVEZIA", "AUSTRALIA", "ITALIA", "FRANCIA", "IRLANDA", "GERMANIA"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO DECODIFICA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]: st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO AGGIORNATO USA 4.0) ---
if st.button("🗡️ SCATENA IL DECODIFICATORE (CHIAVE SUPREMA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA DECODIFICANDO L'ANIMA DELLA GARA... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                usa_logic = ""
                if nazione == "USA":
                    usa_logic = """
                    REGOLE SPECIALI USA FOCUS:
                    - SE 'RT.' MANCA, USA GOOGLE SEARCH PER TROVARE I 'BEYER SPEED FIGURES' O 'EQUIBASE SPEED FIGURES' RECENTI DI OGNI PARTICELLA.
                    - ANALIZZA LA 'CLASSE': SE UN CAVALLO SCENDE DA 'ALLOWANCE' O 'STAKES' A 'CLAIMING', È UN TITANO ANCHE SE L'ULTIMO RISULTATO È UN 4.
                    - REGOLA DEL TITANO LEGITTIMO: SE IL FAVORITO HA QUOTA < 2.00 E HA IL MIGLIOR SPEED FIGURE CERCATO ONLINE, BLINDALO COME CHIAVE.
                    - SE IL FAVORITO HA GG > 45 O SPEED FIGURE DEBOLE, CERCA IL CHALLENGER CON GAP RATING >= 5.
                    """

                prompt = f"""
                SEI ZORRO, IL DECODIFICATORE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO.
                TERRITORIO: {nazione} - DATA: 27 FEBBRAIO 2026.

                {usa_logic}

                MISSIONE SUPREMA: IDENTIFICARE LA CHIAVE CHE BATTE OGNI FILTRO USANDO LA SINTESI TECNICA E LA RICERCA LIVE.

                FASE 1: ANALISI FONDAMENTALE (MANIFESTO + WEB)
                - ESTRAI GG E SEQ. (LETTURA: TOP BOX = LATEST).
                - IDENTIFICA IL FAVORITO E IL SECONDO FAVORITO.
                - SE 'RT.' MANCA O SE SIAMO IN USA, ANALIZZA I COMMENTI E I DATI DI VELOCITÀ (SPEED FIGURES) ONLINE.

                FASE 2: FILTRI DI GRANITO (10000% CERTEZZA)
                1. MURO FORMA: ULTIMO RISULTATO 1 O 2 (O COMMENTO DI VITTORIA RECENTE/CLASS DROP).
                2. FILTRO RUGGINE: GG < 45. SCARTA FAVORITI ARRUGGINITI (> 45 GG).
                3. CUORE IMPAVIDO: ALMENO DUE PODI NELLE ULTIME 3 GARE.

                FASE 3: LA CHIAVE SUPREMA (SINTESI)
                - LA CHIAVE SUPREMA È LA PARTICELLA CHE:
                    A) PASSA I FILTRI (FORMA 1-2, GG < 45) O È UN TITANO LEGITTIMO USA.
                    B) HA IL MIGLIOR RATING TECNICO (RT O SPEED FIGURE CERCATO).
                    C) SCHIACCIA UN FAVORITO DEBOLE (GG > 45 O CATEGORIA INFERIORE).

                FASE 4: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA DEL DECODIFICATORE: [FRASE DI CAZZIMMA DI ZORRO].'
                
                SE LA CHIAVE ESISTE:
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #]'
                'BULLONE SERRATO: [SPIEGA PERCHÉ QUESTA È LA CHIAVE SUPREMA: EVIDENZIA IL CONTRASTO TRA IL FAVORITO ARRUGGINITO E IL CHALLENGER IN FORMA].'
                
                SE È ANCORA ROULETTE: '🌵 NESSUNA PEPITA. LA NEBBIA È TROPPO FITTA PER COLPIRE CON CERTEZZA.'
                """

                # --- SISTEMA DI SICUREZZA MULTI-TITANO (AGGIORNATO) ---
                try:
                    # PROVA IL TITANO PRO (MASSIMA POTENZA LOGICA)
                    res = client_gemini.models.generate_content(
                        model='gemini-3.1-pro-preview', 
                        contents=[prompt] + images,
                        config={'tools': [{'google_search': {}}]}
                    )
                except Exception as e:
                    # SE LA QUOTA È ESAURITA (429), PASSA AL NUCLEO FLASH (VELOCE)
                    st.warning("⚠️ QUOTA PRO ESAURITA! SCATENO IL NUCLEO FLASH PER NON PERDERE LA GARA.")
                    res = client_gemini.models.generate_content(
                        model='gemini-3-flash-preview', 
                        contents=[prompt] + images,
                        config={'tools': [{'google_search': {}}]}
                    )
                
                sentenza = res.text
                st.info(sentenza)
                if "IL SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ UN TRADITORE HA MANOMESSO IL DECODIFICATORE: {e}")
