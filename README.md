Audio file to text web application with Flask
-

-Features 
  -Format Conversation: Uses pydub to convert any audio format into the required .wav format.\n
  Using io.BytesIO process is handled in-memory\n
  Transcribes the audio with SpeechRecognition library(Google API)\n
  The fetch API provides a smooth user experience, showing results without reloading the page.

 -Dependency:
     ffmpeg (Must be installed on the system for Pydub to read and write audio files.)

```bash
git clone https://github.com/mustafamrtt/speechtotext.git
cd speechtotext
```
2. (Important) Install ffmpeg

Pydub requires ffmpeg to function.

    Windows: Download from ffmpeg.dev and add the bin folder to your system's PATH.
    ```bash
    macOS (using Homebrew): brew install ffmpeg
    ```
    ```bash
    Linux (using apt): sudo apt update && sudo apt install ffmpeg
    ```
3.Install Python Dependencies 
  Create a requirements.txt file in the project root with the following content:
  
    Flask
    pydub
    SpeechRecognition

 ```bash   
 pip install -r requirements.txt
 ```
