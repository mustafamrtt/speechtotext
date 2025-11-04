import io
import speech_recognition as sr
from flask import Flask, render_template, request, jsonify
from pydub import AudioSegment


app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    
    
    if 'audio' not in request.files:
        return jsonify({'error': 'Audio file not found'}), 400

    audio_file = request.files['audio']
    
  
  
    

    try:
      
        audio = AudioSegment.from_file(audio_file)
       
        wav_io= io.BytesIO();

        audio.export(wav_io,format="wav")

        wav_io.seek(0);

        recognizer = sr.Recognizer()
        
       
        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)
        
      
        try:
            text = recognizer.recognize_google(audio_data, language='en-EN')
            result = {'text': text}
        except sr.UnknownValueError:
            result = {'error': 'Sound is terrible'}
        except sr.RequestError as e:
            result = {'error': f'Google API error: {e}'}

    except Exception as e:
        result = {'error': f'process error: {str(e)}'}
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)