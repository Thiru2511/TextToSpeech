from gtts import gTTS
import os

# file openning

abc=open("1.txt.txt")
text=abc.read()

language="en"

obj=gTTS(text=text,lang=language,slow=False)

obj.save("sample.mp3")