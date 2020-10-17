from Sonnet import *

Neurons = []
Fakes = []
gseed = []

Neuron1 = []
Neuron2 = []

ChosenWords = []

Neurons = []

length = []

tries = 1

f = open("Sonnets.txt",'r')
Dictionary = f.read().replace('\n', ' ')
f.close()

Dictionary = Dictionary.replace('   ',' ')
Dictionary = Dictionary.replace(',',' ')
Dictionary = Dictionary.replace('"',' ')
Dictionary = Dictionary.replace(')',' ')
Dictionary = Dictionary.replace('(',' ')
Dictionary = Dictionary.replace('!',' ')
Dictionary = Dictionary.replace('?',' ')
Dictionary = Dictionary.replace(':',' ')
Dictionary = Dictionary.replace(';',' ')
Dictionary = Dictionary.replace('.',' ')
Dictionary = Dictionary.replace('-','')
Dictionary = Dictionary.split(' ')

i = 0

while i != len(Dictionary):
    if Dictionary[i] == ' ' or Dictionary[i] == '':
        Dictionary.remove(Dictionary[i])
    i = i + 1

Dictionary = list(dict.fromkeys(Dictionary))

for i in range(6):
    Neuron1.append(random.uniform(.1,5))

for i in range(25):
    Neuron2.append(random.uniform(.1,5))

for i in range(1000):
    ChosenWords.append(Dictionary[random.randint(0,len(Dictionary)-1)])

for i in range(9):
    Neurons.append(random.randint(0,100))

for i in range(3000):
    length.append(random.randint(5,9))

f = open("AISpeare.txt",'r')
for i in range(2100):
    Fakes.append(f.readline())
f.close()

for i in range(2200):
    temp = []
    for a in range(10):
        temp.append(random.randint(0,9))
    gseed.append(temp)

#debug sonnet
#temp = Sonnet([1,1,1,1,1,1,1,1,1,1,1,1], tries, gseed, Neuron1, Neuron2, ChosenWords, length)

while True:

    Neurons = Detector(Fakes, tries, Neurons)
    temp = Sonnet(Neurons, tries, gseed, Neuron1, Neuron2, ChosenWords, length)

    Fakes = temp[0]
    Neuron1 = temp[1]
    Neuron2 = temp[2]
    ChosenWords = temp[3]
    length = temp[4]
