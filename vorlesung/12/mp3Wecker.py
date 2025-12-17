from playsound3 import playsound
from time import sleep

sekunden = int(input("Bitte Zeit in Sekunden für den Countdown angeben:  "))
while sekunden > 0:
    rest_minuten = int(sekunden/60)
    rest_sekunden = int(sekunden%60)
    print(f"\r{rest_minuten:02d}:{rest_sekunden:02d}", end="")
    sleep(1)
    sekunden -= 1

# Nach Ablauf Alarm schlagen
print('\r00:00 Alarm')
playsound("hellsbells.mp3")
