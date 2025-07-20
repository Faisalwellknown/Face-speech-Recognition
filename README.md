# Face Recognition and Speech Translation System

This project contains two Python-based applications:

1. **Face Recognition** using OpenCV and `face_recognition` library.
2. **Speech Translation**: Converts English speech to Hindi using `speech_recognition`, `gTTS`, and `deep_translator`.



## 📁 Project Structure

.
├── face.py # Real-time face recognition using webcam
├── import speech_recognition as sr.py # English to Hindi speech translator with evaluation metrics
├── README.md



## 1️⃣ Face Recognition (`face.py`)

### Description
- Loads a known image (`Faisal Shaikh.jpg`) and encodes the face.
- Uses webcam input to recognize faces in real-time.
- Displays "Faisal Shaikh" on the screen if a match is found, otherwise "Unknown".

### Dependencies
- `opencv-python`
- `face_recognition`

### How to Run

```bash
pip install opencv-python face_recognition
python face.py
Note: Place a reference image named Faisal Shaikh.jpg in the same directory.

2️⃣ Speech Translator (import speech_recognition as sr.py)
Description
Captures English speech from the microphone.

Converts it to text.

Translates the text to Hindi.

Converts the translated text to speech using gTTS.

Plays the translated speech.

Calculates accuracy, precision, recall, and F1-score based on expected vs recognized text.

Dependencies

pip install SpeechRecognition gTTS deep_translator scikit-learn
How to Run

python "import speech_recognition as sr.py"
Note: Ensure your microphone is working and internet is connected (for APIs and TTS).

💡 Features
Real-time face detection and name labeling.

Interactive English-to-Hindi voice translator.

Evaluation of speech recognition output using standard ML metrics.

📌 Requirements
Python 3.x

Microphone (for speech input)

Webcam (for face recognition)

Internet connection (for speech recognition and translation services)

🛠️ Future Enhancements
Add GUI using Tkinter or PyQt.

Support multiple known faces.

Improve evaluation with larger datasets.



👨‍💻 Author
Faisal Shaikh