import time
import os
import pygame

pygame.init()
pygame.mixer.init()

flag = True
os.system('cls')
t1 = int(input('Enter timer 1 - hours: ')) * 3600 + int(input('Enter timer 1 - minutes: ')) * 60 + int(
    input('Enter timer 1 - second: '))
print('')
t2 = int(input('Enter timer 2 - hours: ')) * 3600 + int(input('Enter timer 2 - minutes: ')) * 60 + int(
    input('Enter timer 2 - second: '))
print('')
s = int(input('Enter the number of reps: '))*2
if s == 0: s = 1000
t = t1
tt = t1
ct = time.time()
cct = time.time()
while s != 0:
    os.system('cls')
    print('Start timer')
    os.system('cls')
    print('Repetitions remained: ', s//2)
    if flag:
        print("Work")
    else:
        print("Take a break")
    while True:

        print('\r', end='')
        print("wait: ", end='')
        if (tt // 3600) % 24 < 10:
            print('0', end='')
        print((tt // 3600) % 24, end=':')
        if (tt // 60) % 60 < 10:
            print('0', end='')
        print((tt // 60) % 60, end=':')
        if tt % 60 < 10:
            print('0', end='')
        print(tt % 60, end='')

        if int(time.time()-cct >= 1):
            cct = int(time.time())
            tt -= 1

        if int(time.time()-ct) >= t:
            ct = time.time()
            break

    print('')
    os.system('cls')
    print('Time is up')
    sound = pygame.mixer.Sound(file='time.wav')
    sound.play(loops=0)
    # sleep(4)
    os.system('cls')
    print('start timer')

    if flag:
        t = t2
        tt = t2
        flag = False
    else:
        t = t1
        tt = t1
        flag = True

    s -= 1
print('Timer hes expired')
input('Press "Enter" to exit')
