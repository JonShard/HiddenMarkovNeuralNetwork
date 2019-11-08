import numpy as np
import random as rng
import matplotlib.pyplot as plt

# Blanket Answer:
    # 1: d, h, g, e
    # 2: No, i is not independent of k, because K has a path to a have a path to i. J is irrelevant?
    # 3: 

# Blanket questions:
    # what does it mean when i and j in a network is independent? 
      # Isn't a node A dependent on all nodes that has a path to A?
    
# Hidden Markov questions:
    # What is X and Y? X = Internal state, happy/sad. Y = observasion, wathcing, crying...
    # What does "the probability of X0" / p(X0) mean? Initial state, 
    # What is theta: p(Xt|Xt-1) / transition matrix how to calculate it? 
    # What is phi:  p(Yt|Xt) / observation matrix


# Probabilities:
# Cooking, Crying, Sleeping, Socializing, WatchingTv
#                    CO   CR   SL   SO   W
observationTable = [(0.3, 0.0, 0.3, 0.3, 0.1),  # Sad
                    (0.1, 0.2, 0.4, 0.0, 0.3)]  # Happy
                    
probState = 0.6  # Prob of starting happy.     P(X)

                  # Sad Happy
transitionTable = [(0.8, 0.2), # Sad     P(Xt | Xt-1)
                   (0.1, 0.9)] # Happy

historyX = []   # History of internal states. 0 = sad,  1 = happy.
historyY = []   # History of observations.



def predictX(hX, hY, probState, oTable, tTable, t):
    
    if len(x) == 0:
        print("Error: Can not predict internal state based on empty internal state history.")
        return -1

    if t < 0:
        print("Error: timestep t can not be negative.")
        return -1

    if len(x) != len(y)-1:
        print("Error: Can not predict internal state for timestep t without an observation for t.")
        return -1

    if hY[len(hY)-1] > len(oTable)-1:
        print("Error: Invalid observation Y in the last element of history Y: " + hY[len(hY)-1])
        return -1

    y = int(hY[len(hY)-1])  # Get latest observation out of the history.
    
    ## General Questions: ##
        # Is probState supposed to be a vector of {chance of happy, chance of sad} or just a number?
        # How do I calulate / pick observation probability(P(Yt|Xt)) (in the simplified expression) for an activity wihtout knowing the internal state?
        # Where does transition table come into the picture?
        # I think inbetween every action, the transition table should be used somehow.
        # After the transition table, I think the observation table will be used somehow. Drawing.
        # Was there an exercise with a similar implimentation? Ex5 only had PCA and Neural Networks.

    # Observation = prob of becoming sad when doing Y activity + prob of being happy when doing Y prbab
    observation = oTable[0][y] + oTable[1][y]
    

    prediction = probState          # Probability of starting off happy.
    for i in range(0, len(hY)-1):      # 1:t-1
        prediction *=  oTable[1][hY[i]] # Probability of becoming happy in timestep i

    normalization = 0
    for i in range(0, len(hY)):
        normalization += oTable[i][hY[i]] * oTable[1][hY[i]]

    x = (prediction * observation) / normalization
    
    return x



def initSyntheticHistory():
    addTimestep(3) # So
    addTimestep(3) # So
    addTimestep(0) # Co
    addTimestep(4) # W
    addTimestep(2) # SL



def addTimestep():
    global observationTable, transitionTable, probState, historyX, historyY 

    historyY.append(observation)
    x = predictX(historyX, historyY, probState, observationTable, transitionTable, len(historyY))
    historyX.append(x)



def initRandomHostory(steps):
    for range(0, steps):
        addTimestep(rng.randint(0, len(observationTable)-1))


addTimestep(0) # First timestep: cooking:
