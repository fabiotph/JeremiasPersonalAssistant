import speech_recognition as sr


class Microphone():
    def __init__(self, language='en'):
        super().__init__()
        self.language = language

    def listen(self):
        microphone = sr.Recognizer()
        with sr.Microphone() as source:
            microphone.adjust_for_ambient_noise(source=source)
            audio = microphone.listen(source)
        try:
            phrase = microphone.recognize_google(audio, language=self.language)

        except sr.UnknownValueError:
            phrase = "Não Entendi"  # config.exception
        return phrase
