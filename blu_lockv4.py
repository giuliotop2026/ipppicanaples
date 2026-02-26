import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA ROYAL TURF 2.0 (STILE CANTIERE IPPICO) ---
st.markdown("""
    <style>
    /* Sfondo Verde Erba scuro per massima concentrazione */
    .stApp { 
        background-color: #0e2a1d; 
        background-image: linear-gradient(180deg, #123524 0%, #071a10 100%);
        color: #f0f4f1; 
        font-family: 'Courier New', Courier, monospace; 
    }
    
    /* Titoli Oro per il Sacro Graal */
    h1, h2, h3 { 
        color: #d4af37 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 2px 2px 5px #000;
    }
    
    /* Bottone 'Grilletto' stile cuoio e oro */
    .stButton>button { 
        background-color: #5d4037 !important; 
        color: #ffffff !important; 
        border: 3px solid #d4af37 !important; 
        font-weight: bold; font-size: 1.3em; text-transform: uppercase;
        width: 100%; border-radius: 12px; height: 3em;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    .stButton>button:hover { background-color: #d4af37 !important; color: #0e2a1d !important; }
    
    /* Referto Finale Blindato */
    div[data-testid="stAlert"] {
        background-color: #071a10 !important;
        border: 2px solid #d4af37 !important;
        border-left: 10px solid #d4af37 !important;
        border-radius: 8px;
    }
    div[data-testid="stAlert"] p {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.2em !important;
    }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    # Suono campana ultimo giro
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/boxing-bell.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")
except KeyError:
    st.error("☠️ MUNIZIONI MANCANTI (API KEYS)!")
    st.stop()

st.title("🏇 SNIPER 36.0: OMNI-TAPE ARCHITECT")
st.markdown("### *'Mappatura nastri, metri e polmoni d'acciaio. Zero errori.'*")

# 3. SELEZIONE NAZIONE (AGGIUNTA GERMANIA)
nazione = st.selectbox("🌍 SELEZIONA IL TERRITORIO DI CACCIA:", [
    "UK", "USA", "ITALIA", "FRANCIA", "GERMANIA", "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "AUSTRALIA", "GIAPPONE"
])

# 4. SCANNER MOLECOLARE
uploaded_files = st.file_uploader("📸 CARICA GLI SCREENSHOT DEL CAVEAU:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("🏁 ESEGUI PROTOCOLO GRANITO 3.0"):
    if not uploaded_files:
        st.warning("CARICA I POSTER, COMANDANTE!")
    else:
        with st.spinner("SCANSIONE METRI E PARTICELLE IN CORSO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH)
                prompt_v = f"""
                SCANSIONA LE IMMAGINI PER {nazione}.
                FASE A (METADATI): ESTRAI IPPODROMO, DISTANZA TOTALE (es. 1410m) E TIPO DI CORSA (NASTRI/HANDICAP/PIANO).
                FASE B (PARTICELLE): ESTRAI OGNI RIGA SENZA NOMI.
                FORMATO: # [NUMERO] | NASTRO: [es. 0m, +20m, +40m] | RT: [Rating] | GG: [Giorni] | SEQ: [Es: 1-2-7-7-6] | QUOTA: [Quota]
                REGOLE: 
                - SE IL GG È MANCANTE, SCRIVI "N/D".
                - NELLA SEQUENZA, IL PRIMO NUMERO A SINISTRA È L'ULTIMA CORSA (FORMA RECENTE). [cite: 2026-02-25]
                """
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_v] + images)
                dati_estratti = res_v.text

                # FASE 2: IL CERVELLO (PERPLEXITY SONAR PRO - OFFLINE LOGIC)
                prompt_p = f"""
                SISTEMA: PROTOCOLO GRANITO 3.0 - PIAZZATO BLINDATO. [cite: 2026-02-25]
                SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                DATI ESTRATTI: {dati_estratti}

                PARAMETRI DI PERFEZIONE 15.15:
                1. MURO DELLA FORMA: IL PRIMO NUMERO DELLA SEQUENZA DEVE ESSERE 1 O 2. SE È >2 O RP/RI/FE/DAI, ELIMINA. [cite: 2026-02-25, 2026-02-24]
                2. FILTRO RUGGINE: GG DEVE ESSERE < 45. SE GG È 'N/D' O > 45, ELIMINA (RUGGINE MORTALE). [cite: 2026-02-25, 2026-02-24]
                3. BIAS NASTRI (LEPRE): SE LA CORSA È A NASTRI, IL CEMENTO È IL CAVALLO A 0m (PRIMO NASTRO). 
                   DAI PRIORITÀ ASSOLUTA ALLA LEPRE (0m) SE HA SUPERATO I FILTRI 1 E 2. 
                   UN "CACCIATORE" (+20m/+40m) È ABISSO SE LA LEPRE È CALDA. [cite: 2026-02-24]
                4. BIAS NAPOLI: SE L'IPPODROMO È NAPOLI, TOLLERA UN '4' RECENTE PER POLMONI D'ACCIAIO. [cite: 2026-02-24]
                5. SOUTHWELL KEY: SE IPPODROMO È SOUTHWELL, IGNORA FAVORITI < 3.00. [cite: 2026-02-24]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '🏆 SACRO GRAAL INDIVIDUATO: [NUMERO #]' (O 'NESSUN SACRO GRAAL' SE ZERO SUPERSTITI)
                'PIANO DI CORSA: [ANALISI DEI METRI DI PENALITÀ, DISTANZA E DENSITÀ TECNICA].'
                'BULLONE SERRATO: [CONFERMA SEQ, GG < 45 E POSIZIONE NEL NASTRO].'
                """
                
                res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
                sentenza = res_p.choices[0].message.content
                
                st.info(sentenza)
                if "NESSUN" not in sentenza.upper() and "GRAAL" in sentenza.upper():
                    play_beep(); st.balloons()
            except Exception as e:
                st.error(f"☠️ ALLARME SCATTATO: {e}")
