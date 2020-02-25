import speech_recognition as sr
LANGUAGE = 'pt-br'


def listen_microphone():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source=source)
        audio = microphone.listen(source)

    try:
        phrase = microphone.recognize_google(audio, language=LANGUAGE)
        print(phrase)

    except sr.UnknownValueError:
        print("Não entendi.")


listen_microphone()
