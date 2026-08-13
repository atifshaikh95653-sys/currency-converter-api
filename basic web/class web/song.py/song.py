import time
import sys

lyrics = [
    "Arz kiya hai... wah! 👏",
    "Ab kyun ab hosh mein aata nahi",
    "Dil ye mera sambhal jaata nahi",
    "Sochta hoon bas tujhe hi",
    "Par tu nazar kyun aata nahi"
]

print("\n🎤 Shayari Mode ON 🎶\n")
time.sleep(1)

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)   # typing speed
    print()               # next line
    time.sleep(1.2)       # line delay

print("\n✨ Wah Wah ✨")
