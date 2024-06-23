import os
import random
import string
import time

print("VITAL MESSAGE")

continue_playing = 'yes'

while continue_playing.lower() in ['yes', 'y']:
    while True:
        D = int(input("Difficulty level? (4-10) "))
        if 4 <= D <= 10:
            break

  # Використовуємо літери та цифри для формування повідомлення
    possible_characters = string.ascii_lowercase + string.digits

    m = ""
    for i in range(D):
      m += random.choice(possible_characters)
    print("SEND THIS MESSAGE: ", m)
    time.sleep(0.5 * D)  # Provide time for memorizing the message
    os.system("cls||clear")  # Clears the screen

    n = input("What was the message? ")
    if n == m:
        print("Correct!")
    else:
        print("Wrong!")

    continue_playing = input("One more? (yes/no) ")

print("Thanks for playing!")
