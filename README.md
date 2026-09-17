# 🎙️ Python Desktop Virtual Assistant

This Python virtual assistant blends voice and text commands to automate tasks. It handles local app launching, web searching, and Spotify music control. Powered by Ollama and Llama 3, it provides an intelligent conversational fallback, creating a robust, privacy-focused, and highly adaptable desktop AI companion for your daily computer workflow.

## ✨ Features

* **Dual Input Modes:** Switch seamlessly between voice recognition (`speak`) and terminal text input (`text`).
* **App Launching & Web Fallback:** Opens local desktop applications (supports Windows, macOS, and Linux). If an app isn't found, it automatically falls back to searching for its website.
* **Web Searching:** Perform quick web searches using default commands.
* **Spotify Integration:** Search for and play music directly on your active Spotify devices.
* **Local AI Chat:** Any command that isn't a predefined system action is passed to **Ollama (Llama 3)** for an intelligent, offline, and private AI response.
* **Text-to-Speech:** Responds to you audibly upon startup.

## 🛠️ Prerequisites

Before running the assistant, ensure you have the following installed on your system:

1. **Python 3.8+**
2. [**Ollama**](https://ollama.com/): Must be installed and running locally.
   * You need to pull the Llama 3 model by running: `ollama run llama3` in your terminal.
3. **Spotify Developer Credentials**:
   * Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   * Create an app and get your `CLIENT_ID` and `CLIENT_SECRET`.
   * Set the Redirect URI in your Spotify app settings to `http://127.0.0.1:9090/callback`.
4. **PyAudio System Dependencies**:
   * *Windows:* Installed automatically via pip.
   * *macOS:* `brew install portaudio`
   * *Linux:* `sudo apt-get install portaudio19-dev python3-pyaudio`

## 📦 Installation

1. Clone or download this repository.
2. Install the required Python libraries using pip:
   ```bash
   pip install SpeechRecognition pyaudio prompt_toolkit pyttsx3 spotipy ollama
   ```
3. Open the script and replace the Spotify configuration variables with your credentials:
   ```python
   CLIENT_ID = "YOUR_CLIENT_ID_HERE"
   CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"
   REDIRECT_URI = "http://127.0.0.1:9090/callback"
   ```

## 🚀 Usage

Run the script from your terminal:

```bash
python assistant.py
```

### Supported Commands

* **`open [app_name]` / `run [app_name]`**: Launches a local application (e.g., `open calculator`, `run notepad`).
* **`search [query]`**: Searches the web for your query (e.g., `search python documentation`).
* **`play [song_name]`**: Plays a specific song on your active Spotify device. *(Note: Ensure Spotify is open on your computer or phone first!)*
* **`change mode [speak/text]`**: Switches how you interact with the assistant.
* **`stop`**: Exits the program safely.
* **Any other phrase**: Chat freely! If the command doesn't match the above, it will be sent to the local Llama 3 model to answer your questions.

## ⚠️ Notes

* **Microphone:** When in `speak` mode, wait for the "Listening..." prompt before speaking. If it misunderstands you, you will have a brief moment to edit your transcribed text in the terminal.
* **Spotify Device:** The `play` command requires an *active* Spotify device. Simply open the Spotify app on your phone or desktop before running a play command.

## 📚 References & Credits

This project relies on the following incredible open-source tools and APIs:

* [**Ollama**](https://ollama.com/) - For running large language models (like Llama 3) locally.
* [**Spotify Web API**](https://developer.spotify.com/documentation/web-api) & [**Spotipy**](https://spotipy.readthedocs.io/) - For music playback and device integration.
* [**SpeechRecognition**](https://pypi.org/project/SpeechRecognition/) - For robust speech-to-text conversion.
* [**pyttsx3**](https://pyttsx3.readthedocs.io/) - For offline text-to-speech functionality.
* [**prompt_toolkit**](https://python-prompt-toolkit.readthedocs.io/) - For building powerful interactive command line applications.
