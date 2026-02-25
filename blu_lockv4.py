import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA BLUE LOCK (PULITA, CHIRURGICA, NEON CYAN) ---
st.markdown("""
    <style>
    /* Sfondo principale blu scuro abisso */
    .stApp { background-color: #0b132b; color: #e0e1dd; font-family: 'Arial', sans-serif; }
    
    /* Titoli in azzurro neon */
    h1, h2, h3 { color: #00ffcc !important; text-transform: uppercase; font-weight: 800; letter-spacing: 1px; }
    
    /* Bottone innesco */
    .stButton>button { 
        background-color: #1c2541 !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important; 
        font-weight: bold; font-size: 1.2em; text-transform: uppercase;
        border-radius: 8px; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #00ffcc !important; color: #0b132b !important; }
    
    /* Finestra del referto (Stile Terminale Logico) */
    div[data-testid="stAlert"] {
        background-color: #1c2541 !important;
        border: 1px solid #3a506b !important;
        border-left: 8px solid #00ffcc !important;
        border-radius: 5px;
    }
    div[data-testid="stAlert"] p {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 1.15em !important;
        line-height: 1.5 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/scanner-beep.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# CHIAVI DEL CAVEAU
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI NEI SECRETS!")
    st.stop()

st.title("💠 SNIPER 32.0: BLUE LOCK CORE")
st.markdown("### *'Zero statistiche esterne. Solo logica di ferro e filtro forma.'*")

# MATRICE DINAMICA
nazione = st.selectbox("🌐 SELEZIONA LA NAZIONE:", [
    "UK", "USA", "ITALIA", "FRANCIA", "SVEZIA", "CILE", "BRASILE", 
    "SUD AFRICA", "AUSTRALIA", "GIAPPONE", "ALTRO"
])

uploaded_files = st.file_uploader("📸 SCANNER CAVEAU:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("⚡ INNESCA IL FILTRO ASSOLUTO"):
    if not uploaded_files:
        st.warning("CARICA I DATI, COMANDANTE.")
    else:
        with st.spinner("ISOLAMENTO DELLE PARTICELLE IN CORSO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                
                # FASE 1: ESTRAZIONE CHIRURGICA
                prompt_v = f"""
                ESTRAI LE INFORMAZIONI DA QUESTE IMMAGINI PER {nazione}.
                1. TROVA IPPODROMO, DISTANZA E SUPERFICIE.
                2. ESTRAI I DATI DEI CAVALLI RIGA PER RIGA:
                   # [NUMERO] | RT: [Rating] | GG: [Giorni] | SEQ RECENTE: [Es: 1-2-7-7-6]
                ATTENZIONE ALLA SEQUENZA: IL PRIMO NUMERO A SINISTRA È L'ULTIMA CORSA DISPUTATA.
                IGNORA TOTALMENTE I NOMI.
                """
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_v] + images)
                dati_estratti = res_v.text

                # FASE 2: IL CERVELLO (FILTRO OFFLINE BLOCCATO SULLE REGOLE)
                prompt_p = f"""
                SISTEMA: SEI UN FILTRO LOGICO OFFLINE. NON USARE IL WEB PER CERCARE STATISTICHE DI VITTORIA O QUOTE. ATTENITI AL 100% A QUESTE REGOLE.
                
                DATI ESTRATTI:
                {dati_estratti}

                REGOLA DI SBARRAMENTO ASSOLUTO (MURO DELLA FORMA):
                GUARDA IL PRIMO NUMERO DELLA SEQUENZA RECENTE (ES. SE LA SEQUENZA È 6-4-1-4-7, IL PRIMO NUMERO È 6). 
                SE IL PRIMO NUMERO NON È "1" O "2", IL CAVALLO È ELIMINATO ISTANTANEAMENTE. 
                NUMERI COME 3, 4, 5, 6, 7, 8, 9, 0, RP, FE SONO SCARTI TOTALI E NON DEVONO MAI ESSERE SELEZIONATI. NESSUNA ECCEZIONE. [cite: 2026-02-25]

                ISTRUZIONI:
                1. Elimina tutti i cavalli che falliscono la REGOLA DI SBARRAMENTO ASSOLUTO.
                2. Tra i sopravvissuti (quelli con 1 o 2 all'ultima uscita), scegli quello con il GG più basso e la sequenza più costante (polmoni d'acciaio).
                3. Se NESSUN cavallo ha un 1 o un 2 all'ultima uscita, devi dichiarare il fallimento dell'analisi.

                REFERTO FINALE (MAIUSCOLO):
                '💠 SACRO GRAAL INDIVIDUATO: [NUMERO #]' (OPPURE 'NESSUN SACRO GRAAL: TROPPA RUGGINE')
                'PIANO DI FUGA: [Spiega perché questo numero supera il Muro della Forma].'
                'BULLONE SERRATO: [Mostra la sequenza per dimostrare che l'ultimo arrivo è 1 o 2].'
                """
                
                res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
                sentenza = res_p.choices[0].message.content
                
                st.info(sentenza)
                if "NESSUN" not in sentenza.upper() and "GRAAL" in sentenza.upper():
                    play_beep(); st.balloons()
            except Exception as e:
                st.error(f"☠️ ERRORE DI SISTEMA: {e}")
