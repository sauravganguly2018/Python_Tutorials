# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank -log  - Every 40 minutes
# Eyes - eyes.mp3 - every 30 min - EyeDone -log - Every 30 minutes
# Physical activity - physical.mp3 every -45 min -ExDone -log

# Rules
# pygame module to play audio

from time import time
from datetime import datetime
from pygame import mixer
mixer.init()

def music(song,msg,index):
    mixer.music.load(song)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    i=0
    while True:
        if index==1 and msg=="drunk":
            mixer.music.stop()
            break
        elif index==2 and msg=="relaxed":
            mixer.music.stop()
            break
        elif index==3 and msg=="exercised":
            mixer.music.stop()
            break
        else:
            if i>0:
                print("Invalid Input !")
            if index==1:
                msg=input(f"Enter drunk to stop the music : ")
            elif index==2:
                msg=input(f"Enter relaxed if you relaxed your eyes : ")
            else:
                msg=input("Enter exercised if you finished your physical exercise : ")
        i+=1


init_water=time()
init_eyes=time()
init_exercise=time()
water_inter=10
eyes_inter=30
exercise_inter=55

while True:
    if time()-init_water>water_inter:
        print("Time to drink some water !")
        music("song.mp3","a",1)
        with open("water_time.txt","a") as f:
            f.write(f"Drunk water at {datetime.now()}\n")
        init_water=time()
    elif time()-init_eyes>eyes_inter:
        print("Time to relax your eyes !")
        music("song.mp3","b",2)
        with open("eyes_time.txt","a") as f:
            f.write(f"Relaxed eyes at {datetime.now()}\n")
        init_eyes=time()
    elif time()-init_exercise>exercise_inter:
        print("Time to do physical exercise !")
        music("song.mp3","c",3)
        with open("exercise_time.txt","a") as f:
            f.write(f"Exercised at {datetime.now()}\n")
        init_exercise=time()
    else:
        pass
