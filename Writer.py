import random

f = open("Neuron.txt",'r')
Neuron1 = f.readline().split(',')
Neuron2 = f.readline().split(',')
ChosenWords = f.readline().split(',')
f.close()

length = 6

for i in range(len(Neuron1)-1):
    Neuron1[i] = float(Neuron1[i])

for i in range(len(Neuron2)-1):
    Neuron2[i] = float(Neuron2[i])

for i in range(2100):
    text = ''
    seed = []
    output = []

    for i in range(length):
        seed.append(random.randint(0,9))

    for i in range(len(seed)):

        temp = (seed[i] * Neuron1[0] + i * Neuron1[1] + i*seed[i]*Neuron1[2])
        if i > 0:
            temp = temp + ChosenWords.index(output[0]) * Neuron2[0] + Neuron2[1]
        if i > 1:
            temp = temp + ChosenWords.index(output[1]) * Neuron2[2] + 2*Neuron2[3]
        if i > 2:
            temp = temp + ChosenWords.index(output[2]) * Neuron2[4] + 3*Neuron2[5]
        if i > 3:
            temp = temp + ChosenWords.index(output[3]) * Neuron2[6] + 4*Neuron2[7]
        if i > 4:
            temp = temp + ChosenWords.index(output[4]) * Neuron2[8] + 5*Neuron2[9]
        if i > 5:
            temp = temp + ChosenWords.index(output[5]) * Neuron2[10] + 6*Neuron2[11]

        output.append(ChosenWords[int(temp%(len(ChosenWords)-1))])

        text = text + " " + output[i]

    f = open("SafeAISpeare.txt","a+")
    f.write(text + '\n')
    f.close()
