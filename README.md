# 🎙️ URL to MP3 Converter

A Python-based tool that extracts text from online articles and converts it into high-quality speech (MP3). This project was built to demonstrate web scraping, natural language processing, and Text-to-Speech (TTS) integration.

## ✨ Features
- **Smart Extraction**: Uses `newspaper3k` to bypass cookie banners and ads, extracting only the relevant article text.
- **Natural Phrasing**: Integrated with `NLTK` for better sentence tokenization.
- **Human-like Voice**: Powered by Google Text-to-Speech (`gTTS`).
- **Custom Headers**: Includes User-Agent configuration to handle access permissions on major news sites.

## 🛠️ Technologies & Libraries
- **Language**: Python 3.12
- **Environment**: Conda
- **Libraries**: 
  - `gTTS` (Google Text-to-Speech)
  - `newspaper3k` (Article scraping & curation)
  - `nltk` (Natural Language Toolkit)
  - `lxml_html_clean` (HTML cleaning)

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/NuriMaes/Project1.git](https://github.com/NuriMaes/Project1.git)
   cd Project1
2. **Create and activate the environment**:

   ```bash
   conda create -n voz python=3.12
   conda activate voz
3. **Install dependencies**:

   ```bash
   pip install gtts newspaper3k nltk lxml_html_clean
   
## 🚀 **How to Use**:

1. Open main.py.

2. Replace the mi_url variable with the link of the article you want to listen to.

3. Run the script:

   ```bash
   python main.py
4. Find your generated audio file as articulo_voz.mp3 in the project folder.
