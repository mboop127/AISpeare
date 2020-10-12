import random

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

def Sonnet(Neurons):

    gfail = 0

    while gfail <100:

        gfail = gfail + 1

        AvgLocation = readDict('stats.txt')
        Pairs = readDict('pairs.txt')
        Frequency = readDict('AllWords.txt')
        Stdev = readDict('stdev.txt')

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

        output = []

        ChosenWords = []
        Neuron1 =[]
        Neuron2 = []

        ChosenWordsParent = []
        Neuron1Parent = []
        Neuron2Parent = []

        gbest = -10000

        while True:

            for i in range(1000):
                ChosenWords.append(Dictionary[random.randint(0,len(Dictionary)-1)])
                ChosenWordsParent.append(1)

            for i in range(length):
                Neuron1.append(random.uniform(.1,5))
                Neuron1Parent.append(1)

            for i in range(13):
                Neuron2.append(random.uniform(.1,5))
                Neuron2Parent.append(1)

            best = -1000

            fail = 0

            while fail < 5000:

                score = -100
                scoreList = []
                guess = 0

                for i in range(length):
                    if random.random() < .05:
                        Neuron1[i] = Neuron1[i] * random.uniform(.95,1.05)

                for i in range(len(Neuron2)):
                    if random.random() < .05:
                        Neuron2[i] = Neuron2[i] * random.uniform(.95,1.05)

                for i in range(len(ChosenWords)):
                    if random.random() < .05:
                        ChosenWords[i] = Dictionary[random.randint(0,len(Dictionary)-1)]

                for i in range(1000):

                    text = ''
                    seed = []
                    output = []

                    for i in range(length):
                        seed.append(random.randint(0,9))

                    guess = Neurons[0]

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

                        for a in range(len(output)):
                            a1 = AvgLocation[output[a]]
                            a2 = Frequency[output[a]]
                            a3 = Stdev[output[a]]

                            guess = guess -abs(a1[0]  - a)/100 * Neurons[1] + a2[0] * Neurons[2] + a3[0] * Neurons[3]

                            try:
                                temptext = output[i - 1] + " " + output[i]
                                try:
                                    a4 = Pairs[temptext]
                                    guess = guess + a4[0] * Neurons[4]
                                except KeyError:
                                    guess = guess
                            except IndexError:
                                guess = guess

                        text = text + " " + str(output[i])

                    if guess > Neurons[5]:
                        scoreList.append(1 + min(guess-Neurons[4],40)/10000)
                    else:
                        scoreList.append(0)

                    guess = 0

                score = sum(scoreList)

                if score > best:

                    fail = 0
                    best = score

                    deepcopy(Neuron1, Neuron1Parent)
                    deepcopy(Neuron2, Neuron2Parent)
                    deepcopy(ChosenWords, ChosenWordsParent)

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

                else:
                    deepcopy(Neuron1Parent,Neuron1)
                    deepcopy(Neuron2Parent,Neuron2)
                    deepcopy(ChosenWordsParent,ChosenWords)

                    fail = fail + 1



    FP = []

    for x in range(2100):

        text = ""
        seed = []

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


        text = text + " " + str(output[i])

        FP.append(text)

    return FP

def Detector(Fakes):

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

    while gfail < 100:

        gfail = gfail + 1

        best = -10000

        fail = 0

        Neurons = []
        NeuronsParent = []

        for i in range(6):
            Neurons.append(random.randint(0,100))
            NeuronsParent.append(1)

        deepcopy(Neurons,NeuronsParent)

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

                temp = 0
                temp = ShakeList[i]

                guess = Neurons[0]

                for a in range(len(temp)):

                    a1 = AvgLocation[temp[a]]
                    a2 = Frequency[temp[a]]
                    a3 = Stdev[temp[a]]

                    guess = guess -abs(a1[0]  - a)/100 * Neurons[1] + a2[0] * Neurons[2] + a3[0] * Neurons[3]

                    try:
                        temptext = temp[i - 1] + " " + temp[i]
                        try:
                            a4 = Pairs[temptext]
                            guess = guess + a4[0] * Neurons[4]
                        except KeyError:
                            guess = guess
                    except IndexError:
                        guess = guess

                guessList.append(guess)

                if guess > Neurons[4] and Rubric[i] == 1:
                    scoreList.append(min(guess - Neurons[4],40)/10000 + 1)
                elif guess < Neurons[4] and Rubric[i] == -1:
                    scoreList.append(min(Neurons[4] - guess,40)/10000 + 1)
                    correct = correct + 1
                elif guess > Neurons[4] and Rubric[i] == -1:
                    scoreList.append(-abs(min(Neurons[4] - guess,40))/10000 - 2)
                else:
                    scoreList.append(-abs(min(Neurons[4] - guess,40))/10000 - 1)

            score = sum(scoreList)

            if score > best:

                deepcopy(Neurons,NeuronsParent)
                best = score
                fail = 0

                if score > gbest:

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

    return Neurons
