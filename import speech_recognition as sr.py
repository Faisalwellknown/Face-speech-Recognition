import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
import os
import platform
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score  # Evaluation Metrics

def translate_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something in English...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Convert speech to text (English)
            text = recognizer.recognize_google(audio, language="en")
            print(f"Recognized Text (English): {text}")

            # Translate text from English to Hindi
            translated_text = GoogleTranslator(source="en", target="hi").translate(text)
            print(f"Translated Text (Hindi): {translated_text}")

            # Convert translated text to speech (Hindi)
            tts = gTTS(translated_text, lang="hi")
            tts.save("translated_speech.mp3")

            # Play the audio based on OS
            if platform.system() == "Windows":
                os.system("start translated_speech.mp3")  # For Windows
            else:
                os.system("mpg321 translated_speech.mp3")  # For Linux/macOS (requires mpg321 installed)

            # Placeholder for Evaluation Metrics
            y_true = ["hello"]  # Expected text (Modify as needed)
            y_pred = [text]  # Predicted text

            # Accuracy
            accuracy = accuracy_score(y_true, y_pred) if len(y_true) == len(y_pred) else 0
            print(f"Accuracy: {accuracy:.2f}")

            # Precision
            precision = precision_score(y_true, y_pred, average="macro", zero_division=1) if len(y_true) == len(y_pred) else 0
            print(f"Precision: {precision:.2f}")

            # Recall
            recall = recall_score(y_true, y_pred, average="macro", zero_division=1) if len(y_true) == len(y_pred) else 0
            print(f"Recall: {recall:.2f}")

            # F1-Score
            f1 = f1_score(y_true, y_pred, average="macro", zero_division=1) if len(y_true) == len(y_pred) else 0
            print(f"F1-Score: {f1:.2f}")

        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError:
            print("Error with the Speech Recognition service.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    translate_speech()
