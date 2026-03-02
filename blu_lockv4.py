import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "EL DECODIFICADOR" ---
st.set_page_config(page_title="ZORRO SUPREMO", page_icon="⚔️", layout="centered")

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

def play_abort_buzzer():
    audio_url = "https://www.myinstants.com/media/sounds/wrong-answer-sound-effect.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO OMNISCIENTE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, LA CHIAVE API È SPARITA! CONFIGURA I SECRETS SU STREAMLIT CLOUD.")
    st.stop()

st.title("⚔️ ZORRO 1.25: EL DECODIFICADOR SUPREMO")
st.markdown("### *'SE IL RATING TACE, IL CUORE DEL CAMPIONE GRIDA. LA MATEMATICA SCHIACCIA LA NEBBIA E LA CLASSE DISTRUGGE LE QUOTE.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "USA", "SUD AFRICA", "SVEZIA", "AUSTRALIA", "ITALIA", "FRANCIA", "UK", "IRLANDA", "GERMANIA"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI E COMMENTI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO DECODIFICA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]: st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (MOTORE ADATTIVO INTEGRATO) ---
if st.button("🗡️ SCATENA IL DECODIFICATORE MATEMATICO"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA CALCOLANDO L'INDICE DI DENSITÀ TECNICA REALE... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # LOGICA SPECIFICA PER TERRITORIO
                logic_focus = ""
                if nazione == "USA":
                    logic_focus = """
                    REGOLE SPECIALI USA FOCUS (IL PROTOCOLLO CLASS DROP E LAYOFF):
                    1. LA CLASSE SCHIACCIA LA RUGGINE: IN USA, I GIORNI DI RIPOSO (GG) ALTI NON SONO SEMPRE NEGATIVI (LAYOFF). SE UN CAVALLO HA GG > 60 MA SCENDE DI CATEGORIA (ES. IL MONTEPREMI DELLA SUA ULTIMA GARA ERA PIÙ ALTO DI QUELLO ODIERNO O PASSA DA 'ALLOWANCE' A 'CLAIMING' O 'MAIDEN'), NON SOTTRARRE NESSUN PUNTO PER LA RUGGINE. LA CLASSE ANNULLA L'ASSENZA.
                    2. IL SALTO (CLASS DROP): SE IL CAVALLO EFFETTUA QUESTO "DECLASSAMENTO" (CORRE PER MENO SOLDI O IN UNA CATEGORIA INFERIORE RISPETTO ALL'ULTIMA GARA), ASSEGNA IMMEDIATAMENTE +40 PUNTI BONUS ALL'INDICE. È UN TITANO IN UNA GARA FACILE.
                    3. FANTASMA: SE 'RT.' MANCA, BASATI SUL MONTEPREMI (PURSE) DELLE GARE PRECEDENTI. CHI HA CORSO PER PIÙ SOLDI IN PASSATO, HA PIÙ DENSITÀ TECNICA E PRENDE IL 'BONUS CLASSE FANTASMA'.
                    """
                elif nazione == "SUD AFRICA":
                    logic_focus = """
                    REGOLE SPECIALI SUD AFRICA (FILTRO TITANIO 4.1):
                    - LA CHIAVE SUPREMA DEVE AVERE GAP RATING >= 5 RISPETTO AL FAVORITO.
                    """
                elif nazione == "FRANCIA":
                    logic_focus = """
                    REGOLE SPECIALI FRANCIA (PROTOCOLLO TROTTO SUPREMO):
                    1. EFFETTO "SCALZO" (DÉFERRÉ): NEL TROTTO FRANCESE, CORRERE "SCALZI" È UN VANTAGGIO MOSTRUOSO. SE IL COMMENTO O I DATI DICONO 'SCALZO' O 'SFERRATO', ASSEGNA IMMEDIATAMENTE +30 PUNTI BONUS ALL'INDICE DEL CAVALLO.
                    2. ANNULLAMENTO RUGGINE (GG 99): SE UN CAVALLO HA GG ALTO (ES. 99, "RIENTRA") MA CORRE 'SCALZO', NON SOTTRARRE NESSUN PUNTO PER LA RUGGINE. LA CLASSE SUPERA L'ASSENZA.
                    3. PISTA E DISTANZA: SE IL COMMENTO INDICA CHE IL CAVALLO HA GIÀ VINTO SU "PISTA E DISTANZA", ASSEGNA UN BONUS EXTRA DI +20 PUNTI.
                    """

                prompt = f"""
                SEI ZORRO, IL DECODIFICATORE SUPREMO DEL PROGETTO BLUE LOCK. LA TUA SINTASSI DEVE ESSERE RIGOROSAMENTE IN MAIUSCOLO E SPIETATA.
                TERRITORIO: {nazione}.
                MISSIONE: ESEGUIRE IL PROTOCOLLO GRANITO 3.0 E TROVARE LA CHIAVE CON POLMONI D'ACCIAIO, IGNORANDO TOTALMENTE LE QUOTE.

                {logic_focus}

                ORDINE DI ESECUZIONE INVIOLABILE E SPIETATO (IL MOTORE ADATTIVO):
                
                FASE 1: PROTOCOLLO DATI FANTASMA E SCANSIONE DELLA SABBIA
                SE DALLA FOTO NOTI CHE MANCANO I RATING (RT) O I GIORNI DI RIPOSO (GG), NON SCARTARE SUBITO. 
                CERCA LA COMPENSAZIONE NELLA 'CLASSE SUPREMA':
                - IN USA/AUSTRALIA/SUD AFRICA/FRANCIA: GUARDA IL SALTO DI CATEGORIA (MONTEPREMI/PURSE), IL PESO, IL NOME DEL FANTINO, I COMMENTI DEGLI ESPERTI O I PIAZZAMENTI IN CARRIERA.
                SE I DATI MATEMATICI MANCANO MA LA CLASSE È EVIDENTE, ASSEGNA UN 'BONUS CLASSE FANTASMA' (DA 10 A 30 PUNTI) PER SOSTITUIRE LE VARIABILI MANCANTI.
                SE INVECE MANCANO I DATI E LA GARA È COMPOSTA SOLO DA DEBUTTANTI SENZA STORICO O È TROPPO CAOTICA, ALLORA INTERROMPI TUTTO IMMEDIATAMENTE.
                LA SENTENZA DEVE ESSERE ESATTAMENTE: 
                "🚨 PERICOLO RILEVATO. DATI INCOMPLETI O GARA CAOTICA. ORDINE SUPREMO: NON GIOCARE."
                
                FASE 2: CALCOLO DELL'INDICE DI DENSITÀ TECNICA REALE
                VALUTA *TUTTI* I CAVALLI DELLA GARA, INCLUSO IL FAVORITO, E LEGGI ATTENTAMENTE I COMMENTI E I PREMI IN DENARO (PURSE) ALLEGATI. CALCOLA MENTALMENTE QUESTO PUNTEGGIO:
                - BASE (SE RT È PRESENTE, PER GLI SFIDANTI): (RT CAVALLO - RT FAVORITO) * 2.5.
                - BASE (SE RT È PRESENTE, PER IL FAVORITO): (RT FAVORITO - RT SECONDO MIGLIORE) * 2.5.
                - BASE (SE RT MANCA): USA IL 'BONUS CLASSE FANTASMA' CALCOLATO NELLA FASE 1.
                - RUGGINE (SE GG È PRESENTE E > 30 E NON C'È UN CLASS DROP IN USA NÉ È SCALZO IN FRANCIA): SOTTRAI (GG - 30) * 0.5. (SE GG < 30): AGGIUNGI (30 - GG) * 0.2.
                - POLMONI: AGGIUNGI 15 PUNTI PER OGNI PIAZZAMENTO (1°, 2°, 3° POSTO) NELLE ULTIME 3 GARE.
                - INVIOLABILITÀ: SE L'ULTIMO RISULTATO È 1 O 2, AGGIUNGI 20 PUNTI BONUS.
                - BONUS TERRITORIO E CLASSE: AGGIUNGI I PUNTI BONUS SPECIFICI (ES. +40 PER CLASS DROP IN USA, +30 PER SCALZO IN FRANCIA, ECC.) DEFINITI NELLE REGOLE DEL TERRITORIO SELEZIONATO.

                FASE 3: LA SOGLIA DEL CEMENTO
                SE NESSUN CAVALLO (NÉ FAVORITO NÉ SFIDANTE) RAGGIUNGE UN INDICE TOTALE DI ALMENO 55.0 PUNTI (CON DATI PURI O CLASSE FANTASMA/BONUS TERRITORIO), LA GARA È DI SABBIA E DEVE ESSERE SCARTATA.
                LA SENTENZA DEVE ESSERE ESATTAMENTE:
                "🚨 NESSUN CAVALLO RAGGIUNGE LA SOGLIA DEL GRANITO. ORDINE SUPREMO: NON GIOCARE."
                
                FASE 4: REFERTO FINALE DELLA VITTORIA
                SE ESISTE UN CAVALLO CHE SUPERA I 55.0 PUNTI ED È IL MIGLIORE IN ASSOLUTO (CHE SIA IL FAVORITO TITANO O IL VINCITORE NASCOSTO), EGLI È IL NOSTRO BERSAGLIO.
                RESTITUISCI ESATTAMENTE QUESTO FORMATO:
                '🌍 MISSIONE: [NAZIONE]'
                '🔥 SENTENZA DEL DECODIFICATORE: LA CLASSE SCHIACCIA LA NEBBIA E IL CANTIERE È SERRATO.'
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #] - [NOME CAVALLO]'
                '📊 INDICE DI DENSITÀ CALCOLATO: [INSERISCI IL PUNTEGGIO STIMATO E SPIEGA DETTAGLIATAMENTE COME HAI ASSEGNATO I PUNTI, SOPRATTUTTO I BONUS COME SCALZO, CLASS DROP, LAYOFF ANNULLATO O CLASSE FANTASMA]'
                """

                res = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt] + images,
                    config={'tools': [{'google_search': {}}]}
                )
                
                sentenza = res.text.strip().upper() if res.text else ""
                
                if sentenza:
                    if "NON GIOCARE" in sentenza:
                        st.error(sentenza)
                        play_abort_buzzer()
                    elif "IL SEGNO DELLA Z" in sentenza:
                        st.success(sentenza)
                        play_victory_bell()
                        st.balloons()
                    else:
                        st.warning(sentenza)
                else:
                    st.error("☠️ IL DECODIFICATORE È RIMASTO IN SILENZIO. IL CANTIERE È BLOCCATO.")

            except Exception as e:
                st.error(f"☠️ UN TRADITORE HA MANOMESSO IL DECODIFICATORE: {e}")
