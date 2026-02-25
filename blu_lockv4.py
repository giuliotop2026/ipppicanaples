import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA ROYAL TURF (STILE CORSA IPPICA) ---
st.markdown("""
    <style>
    /* Sfondo principale: Verde Erba da Ippodromo (Dark Turf) */
    .stApp { 
        background-color: #123524; 
        background-image: radial-gradient(circle, #1b4d36 0%, #0d2617 100%);
        color: #f0f4f1; 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
    }
    
    /* Titoli in Oro Corsa */
    h1, h2, h3 { 
        color: #e6c27a !important; 
        text-transform: uppercase; 
        font-weight: 800; 
        letter-spacing: 1px; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6); 
    }
    
    /* Bottone innesco: Terra di pista (Dirt) con bordo Oro */
    .stButton>button { 
        background-color: #6b3e2e !important; 
        color: #ffffff !important; 
        border: 2px solid #e6c27a !important; 
        font-weight: bold; font-size: 1.2em; text-transform: uppercase;
        border-radius: 8px; transition: 0.3s;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.5);
    }
    .stButton>button:hover { 
        background-color: #e6c27a !important; 
        color: #123524 !important; 
    }
    
    /* Finestra del referto (Leggibilità assoluta: Sfondo scuro, Testo chiaro) */
    div[data-testid="stAlert"] {
        background-color: #0a1f14 !important;
        border: 2px solid #e6c27a !important;
        border-left: 8px solid #e6c27a !important;
        border-radius: 5px;
        box-shadow: 4px 4px 12px rgba(0,0,0,0.7);
    }
    div[data-testid="stAlert"] p {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.15em !important;
        line-height: 1.5 !important;
    }
    
    /* Etichette e testi input */
    .stSelectbox label, .stFileUploader label {
        color: #e6c27a !important;
        font-weight: bold;
        font-size: 1.1em;
    }
    </style>
    """, unsafe_allow_html=True)

def play_beep():
    # Rintocco della campana dell'ultimo giro
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/boxing-bell.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# CHIAVI DEL CAVEAU
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI NEI SECRETS!")
    st.stop()

st.title("🏇 SNIPER 34.0: ROYAL TURF ABSOLUTE CORE")
st.markdown("### *'L'odore dell'erba. La freddezza del cemento. Zero errori, zero ruggine.'*")

# MATRICE DINAMICA: L'UTENTE INSERISCE SOLO LA NAZIONE
nazione = st.selectbox("🌍 SELEZIONA LA NAZIONE (Il resto lo estrae lo scanner):", [
    "UK", "USA", "ITALIA", "FRANCIA", "SVEZIA", "CILE", "BRASILE", 
    "SUD AFRICA", "AUSTRALIA", "GIAPPONE", "ALTRO"
])

uploaded_files = st.file_uploader("📸 SCATTA LA FOTO AL TOTALIZZATORE:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("🏁 INNESCA IL FILTRO ASSOLUTO"):
    if not uploaded_files:
        st.warning("CARICA I DATI, COMANDANTE.")
    else:
        with st.spinner("ISOLAMENTO DELLE PARTICELLE IN CORSO SULLA PISTA... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                
                # FASE 1: ESTRAZIONE CHIRURGICA (METADATI + NUMERI)
                prompt_v = f"""
                SCANSIONA QUESTE IMMAGINI DELLA CORSA PER {nazione}.
                
                FASE A: ESTRAI LE INFORMAZIONI GENERALI DELLA CORSA (LEGGIBILI IN ALTO NELLE GRAFICHE):
                - IPPODROMO: (es. Kempton Park, Treviso, ecc.)
                - DISTANZA: (es. 1410m, 1200m, ecc.)
                - SUPERFICIE / PISTA: (es. P.All Weather, Erba, Sabbia, ecc.)
                
                FASE B: ESTRAI I DATI DEI CAVALLI (REGOLE CHIRURGICHE INVIOLABILI):
                1. LEGGI ESATTAMENTE RIGA PER RIGA. NON MESCOLARE MAI I DATI DI UN CAVALLO CON QUELLI DI UN ALTRO.
                2. NELLA SEQUENZA, L'ULTIMO ARRIVO (quello più a sinistra) DEVE ESSERE IL PRIMO AD ESSERE SCRITTO.
                3. ESTRAI IN QUESTO FORMATO ESATTO PER OGNI RIGA, IGNORANDO TOTALMENTE I NOMI:
                   # [NUMERO] | RT: [Rating] | GG: [Giorni] | SEQ RECENTE: [Es: 1-2-7-7-6] | QUOTA: [Quota]
                SE IL DATO "GIORNI" (GG) NON È PRESENTE O NON È LEGGIBILE, SCRIVI TASSATIVAMENTE "N/D".
                """
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_v] + images)
                dati_estratti = res_v.text

                # FASE 2: IL CERVELLO (FILTRO OFFLINE BLOCCATO SULLE REGOLE DI PERFEZIONE 15.15 E FILTRO RUGGINE)
                prompt_p = f"""
                SISTEMA: SEI UN FILTRO LOGICO OFFLINE. NON USARE IL WEB PER CERCARE STATISTICHE DI VITTORIA O QUOTE. ATTENITI AL 100% A QUESTE REGOLE.
                
                CONTESTO FORNITO DALL'UTENTE: NAZIONE={nazione}.
                
                DATI ESTRATTI DALLO SCANNER:
                {dati_estratti}

                REGOLA 1: SBARRAMENTO ASSOLUTO (MURO DELLA FORMA)
                GUARDA IL PRIMO NUMERO DELLA SEQUENZA RECENTE. SE NON È "1" O "2", IL CAVALLO È ELIMINATO ISTANTANEAMENTE. 
                NUMERI COME 3, 4, 5, 6, 7, 8, 9, 0, RP, FE SONO SCARTI TOTALI. NESSUNA ECCEZIONE. [cite: 2026-02-25]

                REGOLA 2: FILTRO RUGGINE INVALICABILE (IL FATTORE GG)
                SE IL DATO 'GG' È 'N/D' (NON DISPONIBILE) O SE IL 'GG' È MAGGIORE DI 45, IL CAVALLO DEVE ESSERE ELIMINATO IMMEDIATAMENTE.
                UN "1" OTTENUTO TROPPI GIORNI FA O IN DATA IGNOTA È UN'ILLUSIONE MORTALE. IL MOTORE DEVE ESSERE CALDO *ORA*. [cite: 2026-02-25]
                
                REGOLE DELLA NAZIONE:
                SE {nazione} == 'USA': LA QUOTA BASSA COMANDA SE HA UN 1 RECENTE E GG BASSO.
                SE {nazione} != 'USA': IGNORA LE QUOTE, CERCANDO SEMPRE IL SECONDO MIGLIORE PER DENSITÀ TECNICA E POLMONI D'ACCIAIO. [cite: 2026-02-20]

                ISTRUZIONI DI SELEZIONE:
                1. Applica la REGOLA 1 (Forma) e la REGOLA 2 (GG) in modo SPIETATO. Se manca il GG o è >45, elimina la particella.
                2. IL SOPRAVVISSUTO:
                   - SE RIMANE UN SOLO CAVALLO che ha superato ENTRAMBE le regole, QUELLO È IL SACRO GRAAL ASSOLUTO. [cite: 2026-02-20]
                   - SE RIMANGONO PIÙ CAVALLI, scegli quello con il GG (Giorni) più basso in assoluto e la sequenza totale più costante (il cemento che blinda il cantiere). [cite: 2026-02-20]
                3. FALLIMENTO: Dichiara 'NESSUN SACRO GRAAL' *SOLO ED ESCLUSIVAMENTE* se TUTTI i cavalli sono stati eliminati (zero superstiti).

                REFERTO FINALE (SINTASSI RIGOROSAMENTE IN MAIUSCOLO) [cite: 2026-01-20]:
                '🏆 SACRO GRAAL INDIVIDUATO: [NUMERO #]' (OPPURE 'NESSUN SACRO GRAAL: TROPPA RUGGINE NEI MOTORI' se zero superstiti)
                'PIANO DI CORSA: [Spiega perché questo numero supera il Muro della Forma E il Filtro Ruggine].'
                'BULLONE SERRATO: [Mostra la sequenza esatta per dimostrare che l'ultimo arrivo è 1 o 2 e CONFERMA CHE IL GG È < 45].'
                """
                
                res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
                sentenza = res_p.choices[0].message.content
                
                st.info(sentenza)
                # La condizione non suona se dice "NESSUN"
                if "NESSUN" not in sentenza.upper() and "GRAAL" in sentenza.upper():
                    play_beep(); st.balloons()
            except Exception as e:
                st.error(f"☠️ CADUTA SULL'OSTACOLO: {e}")
