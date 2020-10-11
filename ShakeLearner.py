from Sonnet import *

Neurons = []
Fakes = []

f = open("AISpeare.txt",'r')

for i in range(2100):
    Fakes.append(f.readline())

f.close()

while True:

    Neurons = Detector(Fakes)
    Fakes = Sonnet(Neurons)
