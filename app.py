import os
import io
import tempfile
import whisper
from flask import Flask, render_template, request, jsonify
from pydub import AudioSegment



app = Flask(__name__,template_folder=('templates'),static_folder=('static'))

model = whisper.load_model('base')
@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    
    
    if 'audio' not in request.files:
        return jsonify({'error': 'Audio file not found'}), 400

    audio_file = request.files['audio']
    
    if audio_file.filename == '':
        return jsonify ({'error': 'File is not selected'}),400
  
  
    

    try:
      
        audio = AudioSegment.from_file(audio_file)
       
        wav_io= io.BytesIO();

        audio.export(wav_io,format="wav")

        wav_io.seek(0);

    
    

        
    except Exception as e:
        return jsonify({'error':f'pydub error:{str(e)}'}), 500
       
        
    temp_path = None;
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav",delete=False) as temp_file:
         temp_file.write(wav_io.getvalue())
         temp_path = temp_file.name;
         result = model.transcribe(temp_path)   
         text = result.get("text");
         return jsonify({'text':text})
    except Exception as e:
        return jsonify({'error':"whisper error "}+str(e)), 500
    
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
