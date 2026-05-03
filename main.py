import nltk
from newspaper import Article, Config
from gtts import gTTS

# Tell nltk how to split sentences:
nltk.download('punkt')

def convertir_articulo(url):
    # 1. User-agent configuration (the "disguise")
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent

    print(f"Reading article from: {url}...")

    # 2. Initialize, download, and parse
    article = Article(url, config=config) # Applying the custom config
    article.download()
    article.parse()

    # 3. Extract the text
    titulo = article.title
    cuerpo = article.text
    
    texto_completo = f"Title: {titulo}. Content: {cuerpo}"
    
    print(f"Text successfully extracted: {titulo[:50]}...")

    # 4. Convert to speech
    print("Converting to audio... this might take a while.")
    tts = gTTS(text=texto_completo, lang='es')
    tts.save("articulo_voz.mp3")
    print("Done! You can find 'articulo_voz.mp3' in your folder.")

# Test with a URL
mi_url = 'https://es.wikipedia.org/wiki/Invasión_rusa_de_Ucrania'
convertir_articulo(mi_url)