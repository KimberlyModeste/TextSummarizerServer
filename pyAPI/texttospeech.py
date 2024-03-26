import sys
import os
from playsound import playsound
from gtts import gTTS

text = sys.argv[1]
speaker = gTTS(text=text, lang="en", slow=False)
speaker.save("res.mp3")
playsound("res.mp3")
os.remove("res.mp3")

print("Delete")