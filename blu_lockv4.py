import time
import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. CONFIGURAZIONE PAGINA E GRAFICA ---
st.set_page_config(page_title="Moneyball 1.1", page_icon="⚾", layout="centered")

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
        transition: all 0.3s ease;
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #000000 !important; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONTROLLO CHIAVI API ---
GEMINI_KEY = st.secrets.get("GEMINI_API_KEY")

if not GEMINI_KEY:
    st.error("☝️ ATTENZIONE: MANCA LA CHIAVE! ASSICURATI DI AVERE 'GEMINI_API_KEY' NELLE SECRETS.")
    st.stop()

# Inizializza il client Gemini
client_gemini = genai.Client(api_key=GEMINI_KEY)

st.title("⚾ MONEYBALL 1.1: ALGORITMO QUANTITATIVO")
st.markdown("### *'IL BASEBALL CI HA INSEGNATO A VINCERE CON LA MATEMATICA. ORA LO APPLICHIAMO AI CAVALLI.'*")

# --- 3. FUNZIONI CORE CON ANTI-BLOCCO (FLASH 2.5) ---
def estrai_dati_visione(images, max_tentativi=3):
    prompt_ocr = """
    COMPITO: Estrai i dati dei cavalli da queste immagini e fondili in un'unica tabella Markdown.
    
    COME LEGGERE LE IMMAGINI:
    - FOTO 1 (Statistiche): Da qui devi estrarre il N. (Particella), il numero esatto sotto la colonna "GG" (Giorni), e la sequenza sotto "Ultimi Arrivi" (es. 1 2 RP 4).
    - FOTO 2 (Quote): Da qui devi estrarre la QUOTA (il numero nel bottone grigio Vincente) e abbinarla alla giusta Particella.
    
    TABELLA RICHIESTA:
    | PARTICELLA | QUOTA (V) | FANTINO / ALLENATORE | PESO | GG (GIORNI) | FORMA | COMMENTO |
    
    Sforzati di non lasciare MAI vuote le colonne GG e FORMA. Se vedi i quadratini verdi/rossi nella prima foto, trascrivi cosa c'è scritto dentro! Se manca un dato minore come Peso o Commento, metti "-".
    """
    for tentativo in range(max_tentativi):
        try:
            res_vision = client_gemini.models.generate_content(
                model='gemini-2.5-flash', 
                contents=[prompt_ocr] + images
            )
            return res_vision.text
        except Exception as e:
            error_msg = str(e).upper()
            if "503" in error_msg or "UNAVAILABLE" in error_msg or "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                if tentativo < max_tentativi - 1:
                    time.sleep(15)
                else:
                    raise Exception("HAI SUPERATO IL LIMITE VELOCITÀ DI GOOGLE. ASPETTA 1 MINUTO E RIPROVA.")
            else:
                raise Exception(f"ERRORE OCR: {str(e)}")

def calcola_scoring_logico(dati_estratti, nazione, max_tentativi=3):
    prompt_analisi = f"""
    RUOLO: SEI IL MOTORE MATEMATICO DEL 'PROGETTO MONEYBALL 1.1'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. 

    TERRITORIO: {nazione}
    DATI GREZZI (TABELLA):
    {dati_estratti}

    MISSIONE: IDENTIFICARE IL PIAZZATO BLINDATO.
    
    REGOLE DI SELEZIONE INIZIALE:
    - Cerca i 3 cavalli con la QUOTA più bassa.
    - PIANO B (ANTICRASH): Se le quote sono assenti o con trattini ("-"), NON ABORTIRE LA MISSIONE. Elabora lo score matematico per TUTTI I CAVALLI DELLA TABELLA.
    
    CRITERI DI SCORING MATEMATICO:
    1. FORMA RECENTE (Max 50 punti): Numeri 1, 2, 3 presenti nelle ultime corse = +50 punti. Zeri (0) o lettere (p,c,f,RP,RI,FE) = -30 punti (Instabilità).
    2. RUGGINE / GG (Max 30 punti): GG inferiore a 40 = +30 punti. GG > 45 = -20 punti.
    3. BONUS EXTRA (Max 20 punti): Commento molto positivo = +20. Se vuoto = 0.

    ELABORA LO SCORE PER I CAVALLI SELEZIONATI:
    - Nome/Particella:
    - Punti Forma: ...
    - Punti Ruggine (GG): ...
    - Punti Bonus Extra: ...
    - TOTALE SCORE: .../100

    LA CHIAVE SUPREMA: 
    Il cavallo con lo Score più alto è il PIAZZATO BLINDATO, SOLO SE supera i 75 PUNTI.

    REFERTO FINALE:
    '🌍 MISSIONE: {nazione}'
    '📊 SCORE MONEYBALL: [Riassumi i punteggi]'
    
    SE ESISTE ALMENO UN CAVALLO CON SCORE >= 75/100:
    '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO]'
    'BULLONE SERRATO: [Spiega la solidità del cavallo. REGOLA DI SPAREGGIO: Se due o più cavalli hanno lo STESSO punteggio altissimo, eleggi come vincitore assoluto quello con la QUOTA PIÙ BASSA, per massimizzare la probabilità di successo e blindare le Multiple].'
    
    SE NESSUN CAVALLO IN ASSOLUTO RAGGIUNGE I 75 PUNTI:
    '🌵 NESSUN MARGINE STATISTICO. I FAVORITI SONO INSTABILI. MISSIONE ABORTITA.'
    """

    for tentativo in range(max_tentativi):
        try:
            res_analisi = client_gemini.models.generate_content(
                model='gemini-2.5-flash', 
                contents=prompt_analisi
            )
            return res_analisi.text
        except Exception as e:
            error_msg = str(e).upper()
            if "503" in error_msg or "UNAVAILABLE" in error_msg or "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                if tentativo < max_tentativi - 1:
                    time.sleep(15)
                else:
                    raise Exception("HAI SUPERATO IL LIMITE VELOCITÀ DI GOOGLE. ASPETTA 1 MINUTO E RIPROVA.")
            else:
                raise Exception(f"ERRORE DI SISTEMA LOGICO: {str(e)}")

# --- 4. SELEZIONE E INTERFACCIA ---
nazione = st.selectbox("🗺️ SELEZIONA IL TERRITORIO OPERATIVO:", [
    "ITALIA", "FRANCIA", "UK", "IRLANDA", "SVEZIA", "DANIMARCA", "GERMANIA", "USA", "AUSTRALIA", "SUDAFRICA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 CARICA LE SCHEDE (DATI DA INSERIRE NEL MOTORE MONEYBALL):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 👁️ DATI SOTTO SCANSIONE:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        img = Image.open(file)
        with cols[i]: 
            st.image(img, caption=f"Scheda #{i+1}", use_container_width=True)
        file.seek(0)

# --- 5. ESECUZIONE (IL GRILLETTO) ---
if st.button("⚾ AVVIA MONEYBALL 1.1 (CALCOLO SCORING)"):
    if not uploaded_files:
        st.warning("⚠️ CARICA LE SCHEDE PRIMA DI AVVIARE L'ALGORITMO!")
    else:
        images = [Image.open(f) for f in uploaded_files]
        
        with st.status("🕵️ Avvio Algoritmo Moneyball 1.1...", expanded=True) as status:
            try:
                # STADIO 1: Visione
                st.write("👁️ STADIO 1: Estrazione parametri con Gemini 2.5 FLASH (Anti-Errore e Anti-Blocco)...")
                dati_estratti = estrai_dati_visione(images)
                st.write("✅ Dati strutturati con successo in Tabella!")
                
                # STADIO 2: Calcolo Logico
                st.write("🧠 STADIO 2: Calcolo Scoring...")
                sentenza = calcola_scoring_logico(dati_estratti, nazione)
                
                status.update(label="🎯 Elaborazione Moneyball Completata!", state="complete", expanded=False)
                
                # Visualizzazione Dati Grezzi
                with st.expander("📄 VISUALIZZA IL DATABASE ESTRATTO (TABELLA)"):
                    st.markdown(dati_estratti)
                
                # Sentenza Finale
                st.success("### 📜 REFERTO MONEYBALL:")
                st.info(sentenza)
                
                # Controllo Vittoria
                if "IL SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell()
                    st.balloons()

            except Exception as e:
                status.update(label="❌ Errore durante il calcolo", state="error", expanded=True)
                st.error(f"⚠️ ATTENZIONE: {str(e)}")
