import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите что-нибудь...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", text)
        return text
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь.")
        return ""
    except sr.RequestError as e:
        print(f"Ошибка при запросе к сервису распознавания речи; {e}")
        return ""

def main():
    speak("Привет! Я - Говорящий Том. Как я могу вам помочь?")

    while True:
        command = listen().lower()

        if "пока" in command:
            speak("До свидания!")
            break
        elif "как дела" in command:
            speak("У меня все отлично, спасибо!")
        else:
            speak("Извините, я не понял ваш запрос. Повторите, пожалуйста.")

if __name__ == "__main__":
    main()
