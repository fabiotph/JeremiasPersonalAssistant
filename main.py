from src.microphone import Microphone
from src.speaker import Speaker
while(True):
    mph = Microphone(language='pt-br')
    response = mph.listen()
    spk = Speaker(language='pt-br')
    spk.play(value=response)
