from Sonnet import *

Neurons = []
Fakes = []
gseed = []

tries = 20

f = open("AISpeare.txt",'r')

for i in range(2100):
    Fakes.append(f.readline())

f.close()

for i in range(2200):
    temp = []
    for a in range(6):
        temp.append(random.randint(0,9))
    gseed.append(temp)

while True:

    Neurons = Detector(Fakes, tries)
    Fakes = Sonnet(Neurons, tries, gseed)
