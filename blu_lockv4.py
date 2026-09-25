import time
import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- 1. CONFIGURAZIONE PAGINA E GRAFICA ---
st.set_page_config(page_title="Zorro 1.15", page_icon="⚔️", layout="centered")

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
    # Nota: L'autoplay potrebbe essere bloccato da alcuni browser (come Chrome/Safari) se l'utente non ha interagito con la pagina.
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONTROLLO CHIAVI API ---
GEMINI_KEY = st.secrets.get("GEMINI_API_KEY")
PERPLEXITY_KEY = st.secrets.get("PERPLEXITY_API_KEY")

if not GEMINI_KEY or not PERPLEXITY_KEY:
    st.error("☝️ CABALLERO, MANCANO LE CHIAVI! ASSICURATI DI AVERE SIA 'GEMINI_API_KEY' CHE 'PERPLEXITY_API_KEY' NELLE SECRETS.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_KEY)
client_perplex = OpenAI(api_key=PERPLEXITY_KEY, base_url="https://api.perplexity.ai")

st.title("⚔️ ZORRO 1.15: MOTORE IBRIDO SUPREMO")
st.markdown("### *'L'OCCHIO DI GOOGLE, IL CERVELLO DI PERPLEXITY. LA CHIAVE È IL CEMENTO CHE BLINDA IL CANTIERE.'*")

# --- 3. FUNZIONI CORE ---
def estrai_dati_gemini(images, max_tentativi=3):
    """Estrazione visiva forzando Gemini a restituire una struttura a tabella."""
    prompt_ocr = """
    SEI UN ESTRATTORE DI DATI DI ALTISSIMA PRECISIONE. 
    LEGGI QUESTE IMMAGINI RELATIVE A CORSE DI CAVALLI E TRASCRIVI I DATI.
    
    REGOLA FONDAMENTALE: RESTITUISCI I DATI ESCLUSIVAMENTE IN UNA TABELLA MARKDOWN ORDINATA.
    COLONNE RICHIESTE:
    | PARTICELLA (NUMERO) | QUOTA | GG (GIORNI DALL'ULTIMA CORSA) | SEQ | FORMA | COMMENTO DELLA CORSA |
    
    NON FARE NESSUNA ANALISI, LIMITATI A TRASCRIVERE FEDELMENTE CIÒ CHE LEGGI.
    """
    for tentativo in range(max_tentativi):
        try:
            res_vision = client_gemini.models.generate_content(
                model='gemini-2.5-flash', 
                contents=[prompt_ocr] + images
            )
            return res_vision.text
        except Exception as e:
            if "503" in str(e).upper() or "UNAVAILABLE" in str(e).upper():
                if tentativo < max_tentativi - 1:
                    time.sleep(2 ** tentativo)
                else:
                    raise Exception("L'OCCHIO DI GOOGLE È CIECO (503 SERVER ERROR).")
            else:
                raise Exception(f"ERRORE SCONOSCIUTO VISIONE: {str(e)}")

def analizza_con_perplexity(dati_estratti, nazione, max_tentativi=4):
    """Analisi logica con Perplexity basata sui dati tabellari estratti."""
    prompt_analisi = f"""
    TERRITORIO: {nazione} - DATA: OGGI.
    
    ECCO I DATI GREZZI ESTRATTI (IN FORMATO TABELLARE):
    {dati_estratti}

    MISSIONE SUPREMA: IDENTIFICARE IL PIAZZATO BLINDATO TRA I 3 FAVORITI USANDO LA SINTESI TECNICA E IL PROTOCOLLO 'GRANITO 3.0 - PIAZZATO BLINDATO', APPLICANDO I 'PARAMETRI DI PERFEZIONE 15.15 (USA FOCUS)'. IL FALLIMENTO NON È AMMESSO. ZERO ERRORI.

    FASE 1: ISOLAMENTO DELLE 3 PARTICELLE
    - INDIVIDUA ESATTAMENTE I 3 CAVALLI CON LE QUOTE PIÙ BASSE BASANDOTI SULLA TABELLA FORNITA.
    - IDENTIFICALI SOLO TRAMITE LA LORO PARTICELLA (NUMERO) PER EVITARE ERRORI. NON USARE MAI I NOMI DEI CAVALLI.
    - DA QUESTO MOMENTO, IGNORA COMPLETAMENTE LE QUOTE E CONCENTRATI SULLA DENSITÀ TECNICA.

    FASE 2: FILTRI DI GRANITO SUI 3 SOSPETTATI
    1. MURO FORMA: LA FORMA RECENTE DEVE ESSERE INVIOLABILE (NESSUN ERRORE CONSENTITO).
    2. FILTRO RUGGINE: GG < 45. SCARTA CHIUNQUE SIA ARRUGGINITO.
    3. MOTORE D'ACCIAIO: ANALIZZA IL COMMENTO PER TROVARE CHI HA "POLMONI D'ACCIAIO E VOGLIA DI VINCERE".

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

    for tentativo in range(max_tentativi):
        try:
            res_analisi = client_perplex.chat.completions.create(
                model='sonar-pro', 
                messages=[
                    {"role": "system", "content": "SEI ZORRO, IL DECODIFICATORE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. MANTIENI UN TONO AUTOREVOLE E TAGLIENTE."},
                    {"role": "user", "content": prompt_analisi}
                ]
            )
            return res_analisi.choices[0].message.content
        except Exception as e:
            errore_str = str(e).upper()
            if "503" in errore_str or "UNAVAILABLE" in errore_str or "RATE LIMIT" in errore_str:
                if tentativo < max_tentativi - 1:
                    time.sleep(3 * (2 ** tentativo))
                else:
                    raise Exception("LE LINEE DI SINTESI SONO CADUTE. MISSIONE ABORTITA.")
            else:
                raise Exception(f"TRADITORE SCONOSCIUTO HA MANOMESSO IL CERVELLO: {errore_str}")

# --- 4. SELEZIONE E INTERFACCIA ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "SVEZIA", "AUSTRALIA", "ITALIA", "FRANCIA", "USA", "UK", "IRLANDA", "GERMANIA"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI PER L'OCCHIO DI GOOGLE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 👁️ SOSPETTATI SOTTO SCANSIONE VISIVA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]: st.image(file, caption=f"MANIFESTO #{i+1}", use_column_width=True)

# --- 5. ESECUZIONE (IL GRILLETTO) ---
if st.button("🗡️ SCATENA IL DECODIFICATORE IBRIDO (CHIAVE SUPREMA)"):
    if not uploaded_files:
        st.warning("⚠️ CARICA I MANIFESTI PER L'ESTRAZIONE VISIVA, CABALLERO!")
    else:
        images = [Image.open(f) for f in uploaded_files]
        
        # Usiamo st.status per una visualizzazione dell'elaborazione molto più bella e moderna
        with st.status("🕵️ Avvio Protocollo Granito 3.0...", expanded=True) as status:
            try:
                # STADIO 1
                st.write("👁️ STADIO 1: L'Occhio di Google sta estraendo i dati grezzi in formato tabellare...")
                dati_estratti = estrai_dati_gemini(images)
                st.write("✅ Dati estratti con successo!")
                
                # STADIO 2
                st.write("🧠 STADIO 2: Il Cervello Perplexity sta applicando il protocollo di analisi...")
                sentenza = analizza_con_perplexity(dati_estratti, nazione)
                
                status.update(label="🎯 Protocollo completato!", state="complete", expanded=False)
                
                # Mostriamo i dati nel menu a tendina
                with st.expander("📄 VISUALIZZA I DATI GREZZI ESTRATTI (TABELLA)"):
                    st.markdown(dati_estratti)
                
                # Sentenza finale
                st.success("### 📜 REFERTO DEL DECODIFICATORE:")
                st.info(sentenza)
                
                # Vittoria
                if "IL SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell()
                    st.balloons()

            except Exception as e:
                status.update(label="❌ Errore durante il protocollo", state="error", expanded=True)
                st.error(f"⚠️ ATTENZIONE: {str(e)}")
