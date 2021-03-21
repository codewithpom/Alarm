import datetime
import gtts
import playsound
import keyboard
time_to_wake_up = input("Enter time in HH:MM:SS")
time_to_wake_up = time_to_wake_up.replace(" ", "")
statement = input("What should I say when the time has reached")
audio = gtts.gTTS(text=statement, lang="en", slow=True)
print(audio)
audio.save("Sound.mp3")
print("Alarm set for "+time_to_wake_up)


while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    if time_to_wake_up == now:
        print("Wake up")

        while True:

            if keyboard.is_pressed("s"):
                break

            playsound.playsound("Sound.mp3")

        break