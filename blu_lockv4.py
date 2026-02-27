import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. ESTETICA "EL TEMPLO DEL BLUE LOCK" ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; 
        background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
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

# --- 2. CONNESSIONE AL CERVELLO SUPREMO ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CHIAVE API MANCANTE! IL VENDICATORE È DISARMATO.")
    st.stop()

st.title("⚔️ ZORRO 1.10: EL OMNIPOTENTE")
st.markdown("### *'Il codice universale per la gloria eterna. Analizzo l'abisso, trovo la verità, incido l'oro.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI MONDIALI:", [
    "AUSTRALIA", "USA", "UK", "FRANCIA", "SUD AFRICA", "ITALIA", "GERMANIA", "IRLANDA", "GIAPPONE", "BRASILE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO SUPREMO ---
if st.button("🗡️ INCIDI LA 'Z' (ANALISI OMNIPOTENTE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA SCANSIONANDO IL MONDO PER TE... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, IL GIUDICE SUPREMO DEL 'PROGETTO BLUE LOCK'. [cite: 2026-01-19]
                SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                TERRITORIO: {nazione} - DATA: 27 FEBBRAIO 2026. [cite: 2026-02-27]

                MISSIONE: TROVARE LA CHIAVE SUPREMA IN QUALSIASI CIRCUITO O CONDIZIONE. [cite: 2026-02-21]

                FASE 0: RILEVAMENTO AMBIENTE (PROTOCOLLO LIVE)
                - IDENTIFICA TERRENO (PANTANO/SOFT/HEAVY/MUDDY vs GOOD/FIRM). [cite: 2026-02-27]
                - IDENTIFICA RITIRATI (GHOST PROTOCOL). SE > 35%, DICHIARA ROULETTE. [cite: 2026-01-19]
                - USA 'GOOGLE SEARCH' PER VERIFICARE LA 'CAZZIMMA' DEL FANTINO E IL METEO LIVE. [cite: 2026-02-27]

                FASE 1: IL TRIBUNALE DEI DATI (TRIANGOLAZIONE)
                - ESTRAI DATI (RT, GG, SEQ) DAL MANIFESTO. SE MANCANO, USI 'GOOGLE SEARCH' PER REPERIRLI. [cite: 2026-02-27]
                - CONFRONTA MANIFESTO E WEB. SE CONTRASTANO, IL MANIFESTO È LEGGE, IL WEB È SOSPETTO. [cite: 2026-02-07]

                FASE 2: FILTRI DI GRANITO 3.0 (POLMONI D'ACCIAIO) [cite: 2026-02-25]
                1. MURO FORMA: ULTIMO RISULTATO 1 O 2. [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. (ECCEZIONE: SE IL WEB DICE 'TRAINING EXCELLENT' O 'TRIAL WINNER'). [cite: 2026-02-25]
                3. CUORE IMPAVIDO: ALMENO 2 PODI IN ULTIME 3 GARE. [cite: 2026-02-25]
                - USA SOLO 'PARTICELLA [NUMERO]' PER EVITARE ERRORI. [cite: 2026-01-25]

                FASE 3: LA CHIAVE SUPREMA (DENSITÀ TECNICA) [cite: 2026-02-20]
                - REGOLA DEL GAP: IL TITANO DEVE AVERE RATING (RT) GAP >= 5 RISPETTO AL SECONDO. [cite: 2026-02-20]
                - TEST DEL BURRO: SE IL FAVORITO HA GAP < 5, È 'BURRO'. CERCA IL SECONDO MIGLIORE CON POLMONI D'ACCIAIO. [cite: 2026-02-20]
                - VETO PANTANO: SE TERRENO PESANTE, IL CANDIDATO DEVE AVERE ALMENO 1 VITTORIA PASSATA NEL FANGO. [cite: 2026-02-27]

                FASE 4: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA: [UNA FRASE DI CAZZIMMA DI ZORRO SUL DISTRUGGERE LA ROULETTE].' [cite: 2026-02-15]
                
                SE LA CHIAVE È VIVA:
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [SPIEGA PERCHÉ QUESTA CHIAVE È CEMENTO, CITANDO RT, SEQ, TERRENO E GAP].' [cite: 2026-02-07, 2026-02-20]
                
                SE È ROULETTE: '🌵 NESSUNA PEPITA NEL DESERTO. RINFODERO LA SPADA PER SALVARE L'ORO.' [cite: 2026-01-19, 2026-02-15]
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
                st.error(f"☠️ UN TRADITORE HA MANOMESSO IL CODICE: {e}")
