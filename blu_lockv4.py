import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA OMNI-CORE (CANTIERE GLOBALE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: #e0e0e0; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #d32f2f !important; text-transform: uppercase; font-weight: bold; }
    .stButton>button { background-color: #d32f2f !important; color: white !important; border: 2px solid #ffeb3b !important; font-weight: bold; font-size: 1.2em; text-transform: uppercase; }
    .stAlert { background-color: #1a1a1a; border-left: 5px solid #d32f2f; }
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

st.title("🌐 SNIPER 30.0: OMNI-CORE 🎯")
st.markdown("### *'Un solo algoritmo. Ogni nazione. Zero errori. Solo Particelle (#).'*")

# MATRICE DINAMICA GLOBALE
col1, col2, col3, col4 = st.columns(4)
with col1:
    nazione = st.selectbox("🗺️ NAZIONE:", ["SVEZIA", "USA", "CILE", "BRASILE", "UK", "ITALIA", "FRANCIA", "SUD AFRICA", "AUSTRALIA", "GIAPPONE", "ALTRO"])
with col2:
    ippodromo = st.text_input("🏟️ IPPODROMO:")
with col3:
    superficie = st.selectbox("🛤️ SUPERFICIE:", ["ERBA (TURF)", "SABBIA (DIRT)", "ALL WEATHER (AW)", "NASTRI/NEVE"])
with col4:
    distanza = st.number_input("📏 DISTANZA (metri):", min_value=800, max_value=4000, value=1200)

uploaded_files = st.file_uploader("📸 SCANNER CAVEAU:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("💥 INNESCA LA SCANSIONE OMNI-CORE"):
    if not uploaded_files or not ippodromo:
        st.warning("INSERISCI I POSTER E IL CANTIERE, COMANDANTE.")
    else:
        with st.spinner("SCANSIONE DELLE PARTICELLE IN CORSO... 🚬"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                
                # FASE 1: ESTRAZIONE PURA (SOLO NUMERI)
                prompt_v = f"""
                ESTRAI I DATI PER {ippodromo} ({nazione}). 
                IGNORA I NOMI DEI CAVALLI. USA SOLO IL NUMERO (#).
                DATI: NUMERO (#), QUOTA, PESO, RATING, GG (GIORNI), SEQUENZA ULTIME 5 (Dal più recente), NOTE.
                """
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_v] + images)
                dati_raw = res_v.text

                # FASE 2: IL CERVELLO DINAMICO
                prompt_p = f"""
                SISTEMA: PROTOCOLLO GRANITO 3.0. PARLA CON SINTASSI RIGOROSAMENTE IN MAIUSCOLO.
                CONTESTO: NAZIONE={nazione}, IPPODROMO={ippodromo}, SUPERFICIE={superficie}, DISTANZA={distanza}.
                DATI DA SCANSIONARE: {dati_raw}

                REGOLE UNIVERSALI (IL CEMENTO):
                1. IDENTITÀ: USA ESCLUSIVAMENTE IL NUMERO (#). I NOMI SONO ABISSO. [cite: 2026-01-25]
                2. DENSITÀ TECNICA: IGNORA LE QUOTE COME INDICATORE DI FORZA (TRANNE NEGLI USA). CERCA IL SECONDO MIGLIORE CON POLMONI D'ACCIAIO E VOGLIA DI VINCERE CHE SCHIACCIA IL FAVORITO DI CARTA. [cite: 2026-02-20, 2026-02-18]
                3. SEQUENZA INVIOLABILE: NO RP, RI, DI, DAI, FE, T. SE PRESENTI = SCARTA IMMEDIATAMENTE. [cite: 2026-02-24]

                CHIAVI REGIONALI DINAMICHE (SI ATTIVANO IN BASE AL CONTESTO):
                - SE {nazione} == 'USA': APPLICA 'MARKET LAW' & 'FINISHER DRIVE'. IL MARMO DEVE AVERE UN '1' RECENTE. SE GG > 60 = RUGGINE. [cite: 2026-02-24]
                - SE {nazione} == 'SVEZIA': 'LEPRE BIAS'. SE IL PRIMO NASTRO È PULITO, SCHIACCIA LE QUOTE ALTE. ZERO TOLLERANZA PER ROTTURE. [cite: 2026-02-24]
                - SE {nazione} IN ['CILE', 'BRASILE'] E {distanza} < 1200: 'LATAM SPRINT'. PRIORITÀ ASSOLUTA A CHI HA UN '1' RECENTE. LA CAZZIMMA BATTE LA REGOLARITÀ. [cite: 2026-02-24]
                - SE {nazione} == 'FRANCIA': IGNORA LE QUOTE, MA SE > 12.00 SU TERRENO PESANTE = BURRONE. [cite: 2026-02-24]
                - SE {nazione} IN ['SUD AFRICA', 'AUSTRALIA']: VELOCITÀ PURA. PRIORITÀ A GG < 30 E RATING MASSIMO. IL MOTORE DEVE ESSERE CALDISSIMO ORA.
                - SE {ippodromo} == 'SOUTHWELL': IGNORA FAVORITI SOTTO QUOTA 3.00. [cite: 2026-02-24]

                REFERTO FINALE (SINTASSI MAIUSCOLA OBBLIGATORIA) [cite: 2026-01-20]:
                '💎 SACRO GRAAL INDIVIDUATO: [NUMERO #]'
                'PIANO DI FUGA: [PERCHÉ QUESTO NUMERO SCHIACCIA IL CAVEAU IN BASE ALLA CHIAVE REGIONALE].'
                'BULLONE SERRATO: [ANALISI DELLA DENSITÀ TECNICA E DEI POLMONI D'ACCIAIO].'
                """
                
                res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
                sentenza = res_p.choices[0].message.content
                
                st.info(sentenza)
                if "GRAAL" in sentenza.upper():
                    play_beep(); st.balloons()
            except Exception as e:
                st.error(f"☠️ ALLARME SCATTATO: {e}")
