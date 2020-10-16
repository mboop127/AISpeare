import random


#next to fix: replace WordsReverse and ChosenWords with a dictionary of unique words where words:i for NN purposes and a list of (possibly repeating) words it can use for writing purposes

def evaluate(Pairs, AvgLocation, Frequency, Stdev, output, Neurons, Syllables):

    temp = output

    guess = Neurons[0]

    for a in range(len(temp)):

        a1 = AvgLocation[temp[a]]
        a2 = Frequency[temp[a]]
        a3 = Stdev[temp[a]]
        a4 = Syllables[temp[a]]

        guess = guess -abs(a1[0]  - a)/100 * Neurons[1] + a2[0] * Neurons[2] + a3[0] * Neurons[3] + a * Neurons[4] + a4[0] * Neurons[5]

        try:
            temptext = temp[a - 1] + " " + temp[a]
            try:
                a5 = Pairs[temptext]
                guess = guess + a5[0] * Neurons[6]
            except KeyError:
                guess = guess
        except IndexError:
            guess = guess

    return guess

def readDict(file):


    dictionary = {}

    f = open(file,'r')

    end = 0

    while end == 0:
        temp = f.readline().split(',')
        if temp[0] != '':
            dictionary[temp[0]] = [float(temp[1])]
        else:
            end = 1

    f.close()

    return dictionary

def deepcopy(From,To):
    for i in range(len(From)):
        To[i] = From[i]
    return To

def Sonnet(Neurons, tries, gseed, gneuron1, gneuron2, gChosenWords):

    gfail = 0

    gbest = -10000

    AvgLocation = readDict('stats.txt')
    Pairs = readDict('pairs.txt')
    Frequency = readDict('AllWords.txt')
    Stdev = readDict('stdev.txt')
    WordIndex = readDict('WordIndex.txt')
    Syllables = readDict('Syllables.txt')

    length = 6

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

    while gfail <tries:

        gfail = gfail + 1
        print("Current fails: " + str(gfail))

        output = []

        Neuron1 = gneuron1.copy()
        Neuron2 = gneuron2.copy()

        Neuron1Parent = Neuron1.copy()
        Neuron2Parent = Neuron2.copy()

        ChosenWords = gChosenWords.copy()

        ChosenWordsParent = ChosenWords.copy()


        #for i in range(length):
        #    Neuron1.append(random.uniform(.1,5))
        #    Neuron1Parent.append(1)

        #for i in range(13):
        #    Neuron2.append(random.uniform(.1,5))
        #    Neuron2Parent.append(1)

        best = -1000

        fail = 0

        while fail < 500:

            score = -100
            scoreList = []
            guess = 0

            if gfail != 0:

                for i in range(length):
                    if random.random() < .05:
                        Neuron1[i] = Neuron1[i] * random.uniform(.95,1.05)

                for i in range(len(Neuron2)):
                    if random.random() < .05:
                        Neuron2[i] = Neuron2[i] * random.uniform(.95,1.05)

                for i in range(len(ChosenWords)):
                    if random.random() < .05:
                        ChosenWords[i] = Dictionary[random.randint(1,len(Dictionary)-1)]

            for i in range(1000):

                text = ''
                output = []

                seed = gseed[i]

                for i in range(len(seed)):

                    temp = (seed[i] * Neuron1[0] + i * Neuron1[1] + i*seed[i]*Neuron1[2])

                    if i > 0:
                        temp2,temp3 = WordIndex[output[0]], Syllables[output[0]]
                        temp = temp + int(temp2[0]) * Neuron2[0] + Neuron2[1]*int(temp3[0]) + Neuron2[2]
                    if i > 1:
                        temp2,temp3 = WordIndex[output[1]], Syllables[output[1]]
                        temp = temp + int(temp2[0]) * Neuron2[3] + Neuron2[4]*int(temp3[0]) + 2*Neuron2[5]
                    if i > 2:
                        temp2,temp3 = WordIndex[output[2]], Syllables[output[2]]
                        temp = temp + int(temp2[0]) * Neuron2[6] + Neuron2[7]*int(temp3[0]) + 3*Neuron2[8]
                    if i > 3:
                        temp2,temp3 = WordIndex[output[3]], Syllables[output[3]]
                        temp = temp + int(temp2[0]) * Neuron2[9] + Neuron2[10]*int(temp3[0]) + 4*Neuron2[11]
                    if i > 4:
                        temp2,temp3 = WordIndex[output[4]], Syllables[output[4]]
                        temp = temp + int(temp2[0]) * Neuron2[12] + Neuron2[13]*int(temp3[0]) + 5*Neuron2[14]
                    if i > 5:
                        temp2,temp3 = WordIndex[output[5]], Syllables[output[5]]
                        temp = temp + int(temp2[0]) * Neuron2[15] + Neuron2[16]*int(temp3[0]) + 6*Neuron2[17]

                    output.append(ChosenWords[int(temp%(len(ChosenWords)-1))])

                    text = text + " " + str(output[i])

                temp = text.split(' ')
                while("" in temp) :
                    temp.remove("")
                guess = evaluate(Pairs, AvgLocation, Frequency, Stdev, temp, Neurons, Syllables)

                if guess > Neurons[5]:
                    scoreList.append(1 + min(guess-Neurons[5],40)/10000)
                else:
                    scoreList.append(0)

                guess = 0

            score = sum(scoreList)

            if score > best:

                fail = 0
                best = score

                deepcopy(Neuron1, Neuron1Parent)
                deepcopy(Neuron2, Neuron2Parent)
                ChosenWordsParent = ChosenWords.copy()

                if score > gbest:

                    gbest = score
                    f = open("Neuron.txt", 'w+')

                    for i in range(len(Neuron1)):
                        f.write(str(Neuron1[i]) + ",")
                    f.write('\n')
                    for i in range(len(Neuron2)):
                        f.write(str(Neuron2[i]) + ",")
                    f.write('\n')
                    for i in range(len(ChosenWords)):
                        f.write("'" + ChosenWords[i] + "'" + ",")
                    f.write('\n')

                    f.close()

                    print(text)
                    print("New Best:" + str(score))

                    gneuron1 = Neuron1.copy()
                    gneuron2 = Neuron2.copy()
                    gChosenWords = ChosenWords.copy()

                    FP = []

                    for x in range(2100):

                        text = ""
                        seed = []
                        output = []

                        for i in range(length):
                            seed.append(random.randint(0,9))

                        for i in range(len(seed)):

                            temp = (seed[i] * Neuron1[0] + i * Neuron1[1] + i*seed[i]*Neuron1[2])

                            if i > 0:
                                temp2,temp3 = WordIndex[output[0]], Syllables[output[0]]
                                temp = temp + int(temp2[0]) * Neuron2[0] + Neuron2[1]*int(temp3[0]) + Neuron2[2]
                            if i > 1:
                                temp2,temp3 = WordIndex[output[1]], Syllables[output[1]]
                                temp = temp + int(temp2[0]) * Neuron2[3] + Neuron2[4]*int(temp3[0]) + 2*Neuron2[5]
                            if i > 2:
                                temp2,temp3 = WordIndex[output[2]], Syllables[output[2]]
                                temp = temp + int(temp2[0]) * Neuron2[6] + Neuron2[7]*int(temp3[0]) + 3*Neuron2[8]
                            if i > 3:
                                temp2,temp3 = WordIndex[output[3]], Syllables[output[3]]
                                temp = temp + int(temp2[0]) * Neuron2[9] + Neuron2[10]*int(temp3[0]) + 4*Neuron2[11]
                            if i > 4:
                                temp2,temp3 = WordIndex[output[4]], Syllables[output[4]]
                                temp = temp + int(temp2[0]) * Neuron2[12] + Neuron2[13]*int(temp3[0]) + 5*Neuron2[14]
                            if i > 5:
                                temp2,temp3 = WordIndex[output[5]], Syllables[output[5]]
                                temp = temp + int(temp2[0]) * Neuron2[15] + Neuron2[16]*int(temp3[0]) + 6*Neuron2[17]

                            output.append(ChosenWords[int(temp%(len(ChosenWords)-1))])
                            text = text + " " + str(output[i])

                        FP.append(text)

            else:
                deepcopy(Neuron1Parent,Neuron1)
                deepcopy(Neuron2Parent,Neuron2)
                ChosenWords = ChosenWordsParent.copy()

                fail = fail + 1
                print(str(fail), end='\r')


    f = open("AISpeare.txt",'w+')
    for i in range(len(FP)):
        f.write(str(FP[i]) + '\n')
    f.close()
    return [FP,gneuron1,gneuron2,gChosenWords]

def Detector(Fakes, tries, GNeurons):

    gfail = 0

    ShakeList = []
    Rubric = []

    gbest = -100000
    best = -10000
    score = -1000
    fail = 0

    AvgLocation = readDict('stats.txt')
    Pairs = readDict('pairs.txt')
    Frequency = readDict('AllWords.txt')
    Stdev = readDict('stdev.txt')
    Syllables = readDict('Syllables.txt')

    Real = []
    Fake = []

    f = open("Sonnets.txt",'r')

    for i in range(2100):
        Real.append(f.readline())

    f.close()


    for i in range(2100):
        ShakeList.append(Real[i])
        Rubric.append(1)

    for i in range(2100):
        ShakeList.append(Fakes[i])
        Rubric.append(-1)

    for i in range(len(ShakeList)):

        ShakeList[i] = ShakeList[i].replace("\n",'')
        temp = ShakeList[i].split(' ')
        while("" in temp) :
            temp.remove("")

        ShakeList[i] = temp

    while gfail < tries:

        gfail = gfail + 1
        print("Current fails: " + str(gfail))

        best = -10000

        fail = 0

        Neurons = GNeurons.copy()

        NeuronsParent = Neurons.copy()
        #print("New Species")

        while fail < 500:

            for i in range(len(Neurons)):
                if random.random() < .1:
                    Neurons[i] = Neurons[i] * random.uniform(.9,1.1)
                if random.random() < .05:
                    Neurons[i] = Neurons[i] - 1
                if random.random() < .05:
                    Neurons[i] = Neurons[i] + 1

            scoreList = []
            guessList = []
            correct = 0

            for i in range(len(ShakeList)):

                temp = ShakeList[i]

                guess = evaluate(Pairs, AvgLocation, Frequency, Stdev, temp, Neurons, Syllables)

                guessList.append(guess)

                if guess > Neurons[5] and Rubric[i] == 1:
                    scoreList.append(min(guess - Neurons[5],40)/10000 + 1)
                elif guess < Neurons[5] and Rubric[i] == -1:
                    scoreList.append(min(Neurons[5] - guess,40)/10000 + 1)
                    correct = correct + 1
                elif guess > Neurons[5] and Rubric[i] == -1:
                    scoreList.append(-abs(min(Neurons[5] - guess,40))/10000 - 2)
                else:
                    scoreList.append(-abs(min(Neurons[5] - guess,40))/10000 - 1)

            score = sum(scoreList)

            if score > best:

                deepcopy(Neurons,NeuronsParent)
                best = score
                fail = 0

                if score > gbest:

                    deepcopy(Neurons, GNeurons)

                    gbest = score

                    f = open("DetectorNeurons.txt",'w+')
                    for i in range(len(Neurons)):
                        f.write(str(Neurons[i]) + ",")
                    f.close()

                    print("New Best: " + str(score) + ", " + str(correct/21) + "% correct")

            else:
                deepcopy(NeuronsParent,Neurons)
                fail = fail + 1
                print(str(fail), end='\r')

    return GNeurons
