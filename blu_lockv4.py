import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA OMNI-CORE (CANTIERE GLOBALE BLINDATO) ---
st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: #e0e0e0; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #d32f2f !important; text-transform: uppercase; font-weight: bold; }
    .stButton>button { background-color: #d32f2f !important; color: white !important; border: 2px solid #ffeb3b !important; font-weight: bold; font-size: 1.2em; text-transform: uppercase; }
    
    /* FIX COLORI REFERTO SCERIFFO: SFONDO SCURO, TESTO GIALLO ACCECANTE */
    div[data-testid="stAlert"] {
        background-color: #121212 !important;
        border: 2px solid #d32f2f !important;
        border-left: 8px solid #d32f2f !important;
    }
    div[data-testid="stAlert"] p {
        color: #ffeb3b !important;
        font-weight: bold !important;
        font-size: 1.15em !important;
        line-height: 1.4 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/ricochet-sound.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# CHIAVI DEL CAVEAU
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI NEI SECRETS!")
    st.stop()

st.title("🌐 SNIPER 31.0: AUTO-SCAN OMNI-CORE 🎯")
st.markdown("### *'Tu scegli la Nazione. Il mirino estrae metri, superficie e ippodromo da solo.'*")

# MATRICE DINAMICA GLOBALE: L'UTENTE INSERISCE SOLO LA NAZIONE
nazione = st.selectbox("🗺️ SELEZIONA LA NAZIONE (Il resto lo estrae lo scanner):", [
    "UK", "USA", "ITALIA", "FRANCIA", "SVEZIA", "CILE", "BRASILE", 
    "SUD AFRICA", "AUSTRALIA", "GIAPPONE", "ALTRO"
])

uploaded_files = st.file_uploader("📸 SCANNER CAVEAU (CARICA GLI SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("💥 INNESCA LA SCANSIONE AUTO-CORE"):
    if not uploaded_files:
        st.warning("CARICA I POSTER DEL CAVEAU, COMANDANTE.")
    else:
        with st.spinner("LETTURA MURI DEL CAVEAU: ESTRAZIONE IPPODROMO, METRI E DATI... 🚬"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                
                # FASE 1: ESTRAZIONE PURA E TOTALE (METADATI + NUMERI)
                prompt_v = f"""
                SCANSIONA QUESTE IMMAGINI DELLA CORSA.
                
                FASE A: ESTRAI LE INFORMAZIONI GENERALI DELLA CORSA (LEGGIBILI IN ALTO NELLE GRAFICHE):
                - IPPODROMO: (es. Kempton Park, Treviso, ecc.)
                - DISTANZA: (es. 1410m, 1200m, ecc.)
                - SUPERFICIE / PISTA: (es. P.All Weather, Erba, Sabbia, ecc.)
                
                FASE B: ESTRAI I DATI DEI CAVALLI (REGOLE CHIRURGICHE INVIOLABILI):
                1. LEGGI ESATTAMENTE RIGA PER RIGA. NON MESCOLARE MAI I DATI DI UN CAVALLO CON QUELLI DI UN ALTRO.
                2. NELLA SEQUENZA, L'ULTIMO ARRIVO (quello più a sinistra) DEVE ESSERE IL PRIMO AD ESSERE SCRITTO.
                3. ESTRAI IN QUESTO FORMATO ESATTO PER OGNI RIGA, IGNORANDO TOTALMENTE I NOMI:
                   # [NUMERO] | RT: [Rating] | GG: [Giorni] | SEQ RECENTE: [Es: 1-2-7-7-6] | QUOTA: [Quota]
                SE UN DATO NON È CHIARO, SCRIVI "N/D".
                """
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_v] + images)
                dati_estratti = res_v.text

                # FASE 2: IL CERVELLO DINAMICO (RICEVE NAZIONE + DATI ESTRATTI DALLA FASE 1)
                prompt_p = f"""
                SISTEMA: PROTOCOLLO GRANITO 3.0. PARLA CON SINTASSI RIGOROSAMENTE IN MAIUSCOLO.
                CONTESTO FORNITO DALL'UTENTE: NAZIONE={nazione}.
                
                DATI ESTRATTI DALLO SCANNER (Leggili con attenzione: contengono Ippodromo, Distanza, Superficie e i Dati dei cavalli blindati):
                {dati_estratti}

                REGOLE UNIVERSALI (IL CEMENTO):
                1. IDENTITÀ: USA ESCLUSIVAMENTE IL NUMERO (#). I NOMI SONO ABISSO. [cite: 2026-01-25]
                2. DENSITÀ TECNICA: IGNORA LE QUOTE COME INDICATORE DI FORZA (TRANNE DOVE SPECIFICATO). CERCA IL SECONDO MIGLIORE CON POLMONI D'ACCIAIO E VOGLIA DI VINCERE. [cite: 2026-02-18, 2026-02-20]
                3. SEQUENZA INVIOLABILE: L'ULTIMA USCITA (IL PRIMO NUMERO DELLA SEQUENZA) DEVE ESSERE 1 O 2. SE È 6, 7, 8, 9, FE, RP, CD, SCARTA IMMEDIATAMENTE IL NUMERO. È RUGGINE. [cite: 2026-02-25]
                4. VERIFICA ANTI-ALLUCINAZIONE: Controlla che il numero che scegli abbia DAVVERO l'ultima uscita buona. Non scambiare le righe.

                CHIAVI REGIONALI DINAMICHE (ATTIVALE LEGGENDO I METADATI ESTRATTI DA GEMINI):
                - SE NAZIONE == 'USA': APPLICA 'MARKET LAW'. IL MARMO DEVE AVERE UN '1' RECENTE. SE GG > 60 = RUGGINE.
                - SE NAZIONE == 'SVEZIA': 'LEPRE BIAS'. SE IL PRIMO NASTRO È PULITO, SCHIACCIA LE QUOTE ALTE.
                - SE NAZIONE IN ['CILE', 'BRASILE'] E LA DISTANZA ESTRATTA È < 1200: 'LATAM SPRINT'. PRIORITÀ ASSOLUTA A CHI HA UN '1' RECENTE. LA CAZZIMMA BATTE LA REGOLARITÀ.
                - SE NAZIONE == 'FRANCIA': SE QUOTA > 12.00 SU TERRENO PESANTE = BURRONE.
                - SE NAZIONE IN ['SUD AFRICA', 'AUSTRALIA']: VELOCITÀ PURA. PRIORITÀ A GG < 30 E RATING MASSIMO.
                - SE L'IPPODROMO ESTRATTO È 'SOUTHWELL': IGNORA FAVORITI SOTTO QUOTA 3.00.

                REFERTO FINALE (SINTASSI MAIUSCOLA OBBLIGATORIA) [cite: 2026-01-20]:
                '💎 SACRO GRAAL INDIVIDUATO: [NUMERO #]' (Se tutti hanno ruggine, scrivi 'NESSUN SACRO GRAAL INDIVIDUATO')
                'PIANO DI FUGA: [SPIEGA COME LA DISTANZA, LA SUPERFICIE E L'IPPODROMO ESTRATTI FAVORISCONO QUESTO NUMERO].'
                'BULLONE SERRATO: [ANALISI DELLA DENSITÀ TECNICA, MOSTRANDO LA SEQUENZA ESATTA E PERCHÉ NON HA CREPE].'
                """
                
                res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
                sentenza = res_p.choices[0].message.content
                
                st.info(sentenza)
                if "NESSUN" not in sentenza.upper() and "GRAAL" in sentenza.upper():
                    play_beep(); st.balloons()
            except Exception as e:
                st.error(f"☠️ ALLARME SCATTATO: {e}")
