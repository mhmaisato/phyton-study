#count down 10 to 0
import os
from time import sleep
os.system('cls')
for count in range(10, -1, -1):
    sleep(0.5)
    print(count)
print('Decolagem')
