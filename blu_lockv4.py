import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "EL BALUARTE" (SINTASSI RIGOROSA) ---
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

# --- 2. CONNESSIONE AL CERVELLO DEL VENDICATORE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, LA CHIAVE API È SPARITA!")
    st.stop()

st.title("⚔️ ZORRO 1.12: EL GUARDIÁN UNIVERSAL")
st.markdown("### *'Se il rating manca, il Record parla. Se il record tace, il Peso grida. Cerco la verità in ogni numero.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "AUSTRALIA", "ITALIA", "FRANCIA", "USA", "UK", "IRLANDA", "GERMANIA", "SVEZIA", "CILE", "BRASILE", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO SCANSIONE:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]: st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO CHIAVE SUPREMA AGGIORNATO) ---
if st.button("🗡️ SCATENA IL GUARDIANO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA TRIANGOLANDO LA DENSITÀ TECNICA... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, IL GUARDIANO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                TERRITORIO: {nazione} - DATA: 27 FEBBRAIO 2026. [cite: 2026-02-27]

                MISSIONE SUPREMA: TROVARE LA CHIAVE TECNICA ANCHE SENZA IL RATING (RT).

                FASE 1: SCANSIONE DENSITÀ TECNICA (SOSTITUZIONE DATI)
                - SE 'RT.' È MANCANTE: 
                    A) IN FRANCIA/ITALIA: USA 'REC.' (RECORD AL KM) COME INDICATORE DI VELOCITÀ.
                    B) IN AUSTRALIA: USA IL 'PESO' (WEIGHT) COME INDICATORE DI CLASSE.
                    C) USA 'GOOGLE SEARCH' PER TROVARE IL 'TIMEFORM RATING' O 'OFFICIAL RATING' ODIERNO. [cite: 2026-02-27]

                FASE 2: FILTRI DI GRANITO (10000% CERTEZZA)
                1. MURO FORMA: ULTIMO RISULTATO 1 O 2 (O PIAZZATO NELLE ULTIME 2 SE CATEGORIA TOP). [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                3. CUORE IMPAVIDO: ALMENO DUE PODI NELLE ULTIME 3 GARE. [cite: 2026-02-25]
                - IDENTIFICA COME 'PARTICELLA [NUMERO]' PER EVITARE ERRORI. [cite: 2026-01-25]

                FASE 3: LA CHIAVE SUPREMA (IL CEMENTO)
                - LA CHIAVE È IL SECONDO MIGLIORE PER DENSITÀ (RT, REC O PESO) CHE SCHIACCIA IL FAVORITO DI CARTA. [cite: 2026-02-20]
                - SE IL FAVORITO HA UN VANTAGGIO (GAP) SCHIACCIANTE (> 5 PUNTI RT O > 1 SEC REC), LUI È IL CAMPIONE LEGITTIMO. [cite: 2026-02-20]

                FASE 4: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA: [UNA FRASE DI CAZZIMMA DI ZORRO SULLA CLASSE CHE NON TRADISCE].'
                
                SE LA CHIAVE ESISTE:
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #]'
                'BULLONE SERRATO: [SPIEGA QUALE DATO TECNICO (RT, REC O PESO) CONFERMA I POLMONI D'ACCIAIO].' [cite: 2026-02-07, 2026-02-20]
                
                SE È ROULETTE: '🌵 NESSUNA PEPITA. I DATI SONO TROPPO DEBOLI PER BLINDARE IL CANTIERE.' [cite: 2026-02-15]
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
                st.error(f"☠️ UN TRADITORE HA MANOMESSO LA SPADA: {e}")
                
