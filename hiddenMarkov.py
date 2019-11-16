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



    ## Questions: ##
      
      ## About Structure:
        # Is the array of internal state an array of probailities of being happy or a bool array? {h, s}
        # Is probState supposed to be a vector of {chance of happy, chance of sad} or just a number? veector.
      
      ## About Algorithm:
        # How do I calulate / pick observation probability(P(Yt|Xt)) (in the simplified expression) for an activity wihtout knowing the internal state?
        # Where does transition table come into the picture?
        # I think inbetween every action, the transition table should be used somehow.
        # After the transition table, I think the observation table will be used somehow. Drawing.
        # The starting state for X is the inital probability of being happy, what is the corresponding action for that X value?

      ## General:
        # Was there an exercise with a similar implimentation? Ex5 only had PCA and Neural Networks.
        # NO HISTORY!

    ## New Questions: ##
        # In question 3 it asks what the proability of being heppy now is, given that I was happy in the previous
        # timestep and that I'm watching TV in this timestep. How is the info about the observation important? 
        # i though we only used the timesptep t for the calculation? 
        # Same goes for question 4, how do the observations SO, SO, CO, SL, W play a role for the prediction, I thought we only used the tables?

        

    # Observation = prob of becoming sad when doing Y activity + prob of being happy when doing Y prbab
    # observation = oTable[0][y] + oTable[1][y]
    
    # prediction = probState          # Probability of starting off happy.
    # for i in range(0, len(hY)-1):      # 1:t-1
    #     prediction *=  oTable[1][hY[i]] # Probability of becoming happy in timestep i

    # normalization = 0
    # for i in range(0, len(hY)):
    #     normalization += oTable[i][hY[i]] * oTable[1][hY[i]]

    # x = (prediction * observation) / normalization
    



# Probabilities:
# Cooking, Crying, Sleeping, Socializing, WatchingTv
#                             CO   CR   SL   SO   W
observationTable = np.array([(0.2, 0.1, 0.3, 0.3, 0.1),  # Sad
                             (0.1, 0.1, 0.4, 0.1, 0.3)])  # Happy
                    
initState = np.array([0.4, 0.6])[np.newaxis]  # Prob of starting happy.     P(X)

                           # Sad Happy
transitionTable = np.array([(0.8, 0.2), # Sad     P(Xt | Xt-1)
                            (0.1, 0.9)]) # Happy

# Predicts the internal state X from timestep t form state.
def predict(oldState, t, observation):
    global observationTable, transitionTable
   
    if int(t) < 1:
        print("Error: timestep t must be non-zero a positive intiger")
        return (0, 0)

    # First time, old state is (0.6, 0.4)
    newState = oldState.T
    for i in range(0, t):
        newState = transitionTable.T.dot(newState)

    updatedObservation =  newState * observationTable
     
    # normalization = (np.sum(observationTable))
    # normalization = (np.prod(observationTable[0]) + np.prod(observationTable[1]))

    # updatedObservation /= normalization

    newState = (updatedObservation[0][observation], updatedObservation[1][observation])

    print("State changed from " + str(oldState) + " to " + str(newState) + "\n")    
    return newState

def update ():
    global observationTable, transitionTable


# def syntheticData():
#     getTimestep(3) # So
#     getTimestep(3) # So
#     getTimestep(0) # Co
#     getTimestep(4) # W
#     getTimestep(2) # SL



# syntheticData()

for i in range(1, 20): 
  # update()
  predict(initState, i, 0)