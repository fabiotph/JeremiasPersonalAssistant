from gtts import gTTS
from playsound import playsound


class Speaker():
    def __init__(self, language='en'):
        super().__init__()
        self.language = language

    def play(self, value='', audioName='response'):
        tts = gTTS(value, lang=self.language)
        tts.save(audioName+'.mp3')
        playsound(audioName+'.mp3')
