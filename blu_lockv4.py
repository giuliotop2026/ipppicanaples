import time
import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "EL DECODIFICADOR" ---
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
    .stAlert p { color: #1a1a1a !important; font-size: 1.4rem !important; font-weight: bold; text-transform: uppercase; }
    .stButton>button { 
        background-color: #000000 !important; color: #ffd700 !important; 
        border: 2px solid #ffd700 !important; font-weight: bold; font-size: 1.8em; 
        width: 100%; border-radius: 50px; height: 3.5em; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
        text-transform: uppercase;
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
    st.error("☝️ CABALLERO, LA CHIAVE API È SPARITA!")
    st.stop()

st.title("⚔️ ZORRO 1.15: EL DECODIFICADOR SUPREMO - GRANITO 3.0")
st.markdown("### *'IL MOTORE DI CARTA È INSTABILE; LA MIA CHIAVE È IL CEMENTO CHE BLINDA IL CANTIERE.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "SVEZIA", "AUSTRALIA", "ITALIA", "FRANCIA", "USA", "UK", "IRLANDA", "GERMANIA"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧠 SOSPETTATI SOTTO DECODIFICA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]: st.image(file, caption=f"MANIFESTO #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO CHIAVE SUPREMA GRANITO 3.0) ---
if st.button("🗡️ SCATENA IL DECODIFICATORE (CHIAVE SUPREMA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA SCANSIONANDO L'ABISSO TRA QUOTA E DENSITÀ TECNICA REALE... ⏳"):
            images = [Image.open(f) for f in uploaded_files]

            prompt = f"""
            SEI ZORRO, IL DECODIFICATORE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO.
            TERRITORIO: {nazione} - DATA: OGGI.

            MISSIONE SUPREMA: IDENTIFICARE IL PIAZZATO BLINDATO TRA I 3 FAVORITI USANDO LA SINTESI TECNICA E IL PROTOCOLLO 'GRANITO 3.0 - PIAZZATO BLINDATO', APPLICANDO I 'PARAMETRI DI PERFEZIONE 15.15 (USA FOCUS)'. IL FALLIMENTO NON È AMMESSO. ZERO ERRORI.

            FASE 1: ISOLAMENTO DELLE 3 PARTICELLE
            - INDIVIDUA ESATTAMENTE I 3 CAVALLI CON LE QUOTE PIÙ BASSE.
            - IDENTIFICALI SOLO TRAMITE LA LORO PARTICELLA (NUMERO) PER EVITARE ERRORI. NON USARE MAI I NOMI DEI CAVALLI.
            - DA QUESTO MOMENTO, IGNORA COMPLETAMENTE LE QUOTE E CONCENTRATI SULLA DENSITÀ TECNICA.
            - ESTRAI GG, SEQ E COMMENTO CORSA SOLO PER QUESTE 3 PARTICELLE.

            FASE 2: FILTRI DI GRANITO SUI 3 SOSPETTATI
            1. MURO FORMA: LA FORMA RECENTE DEVE ESSERE INVIOLABILE (NESSUN ERRORE CONSENTITO).
            2. FILTRO RUGGINE: GG < 45. SCARTA CHIUNQUE SIA ARRUGGINITO.
            3. MOTORE D'ACCIAIO: ANALIZZA IL COMMENTO PER TROVARE CHI HA "ACAZZIAM POLMONEI DACCIAAIO E VOGLIA DI VINCERE".

            FASE 3: LA CHIAVE SUPREMA (IL CEMENTO CHE BLINDA IL CANTIERE)
            - IL FAVORITO DI CARTA È UNA PARTICELLA SPESSO INSTABILE.
            - LA CHIAVE È SEMPRE IL SECONDO MIGLIORE (O IL TERZO) PER DENSITÀ TECNICA E POLMONI D'ACCIAIO.
            - IL VERO VINCITORE NASCOSTO È IL PIAZZATO SCELTO PER REGOLARITÀ CHE SCHIACCIA IL FAVORITO.
            - SCANSIONA L'ABISSO TRA QUOTA E DENSITÀ TECNICA REALE. SELEZIONA L'UNICO TRA I 3 CHE OFFRE CERTEZZA AL 10000%.

            FASE 4: REFERTO FINALE
            '🌍 MISSIONE: {nazione}'
            '🔥 SENTENZA DEL DECODIFICATORE: [UNA FRASE DI CAZZIMMA DI ZORRO SUL PIAZZATO BLINDATO CHE SCHIACCIA L'INSTABILITÀ].'
            
            SE LA CHIAVE ESISTE (IL PIAZZATO D'ACCIAIO TRA I 3 CHE HA SUPERATO TUTTI I FILTRI DI GRANITO):
            '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #]'
            'BULLONE SERRATO: [SPIEGA PERCHÉ QUESTA PARTICELLA È IL CEMENTO CHE BLINDA IL CANTIERE, EVIDENZIANDO I SUOI POLMONI D'ACCIAIO E LA SUA REGOLARITÀ CONTRO L'INSTABILITÀ DEL FAVORITO DI CARTA].'
            
            SE NESSUNO DEI 3 OFFRE 10000% CERTEZZA, SE CI SONO DUBBI O RUGGINE: 
            '🌵 NESSUNA PEPITA. LA NEBBIA È TROPPO FITTA PER COLPIRE CON CERTEZZA. MISSIONE ABORTITA PER SALVAGUARDARE IL CAPITALE.'
            """

            # IL MOTORE D'ACCIAIO NEL CODICE: CICLO DI TENTATIVI PER SCHIACCIARE IL 503
            max_tentativi = 4
            for tentativo in range(max_tentativi):
                try:
                    res = client_gemini.models.generate_content(
                        model='gemini-2.5-flash', 
                        contents=[prompt] + images,
                        config={'tools': [{'google_search': {}}]}
                    )
                    sentenza = res.text
                    
                    st.info(sentenza.upper())
                    if "IL SEGNO DELLA Z" in sentenza.upper():
                        play_victory_bell()
                        st.balloons()
                    
                    # SE ARRIVA QUI, IL DECODIFICATORE HA COLPITO. INTERROMPI IL CICLO.
                    break 

                except Exception as e:
                    errore_str = str(e).upper()
                    if "503" in errore_str or "UNAVAILABLE" in errore_str or "OVERLOADED" in errore_str:
                        if tentativo < max_tentativi - 1:
                            attesa = 2 ** tentativo # ATTESA ESPONENZIALE PER AGGIRARE L'OSTACOLO
                            st.warning(f"⚠️ SERVER SOVRACCARICO (503). IL DECODIFICATORE NON MOLLA. SCANSIONE ALTERNATIVA TRA {attesa} SECONDI... ({tentativo + 1}/{max_tentativi})")
                            time.sleep(attesa)
                        else:
                            st.error("❌ IL TRADITORE HA MANOMESSO LE LINEE TROPPO A LUNGO. ZERO ERRORI, MISSIONE ABORTITA. RIPROVA PIÙ TARDI.")
                    else:
                        st.error(f"☝️ UN TRADITORE SCONOSCIUTO HA MANOMESSO IL DECODIFICATORE: {errore_str}")
                        break # SE È UN ERRORE DIVERSO DAL 503, FERMATI SUBITO
