import numpy as np
import matplotlib.pyplot as plt

# Probabilities:
# Cooking, Crying, Sleeping, Socializing, WatchingTv
#                             CO   CR   SL   SO   W
observationTable = np.array([(0.1, 0.2, 0.4, 0.0, 0.3), # Happy 
                             (0.3, 0.1, 0.3, 0.3, 0.1)])  # Sad
                    
initState = np.array([0.6, 0.4])[np.newaxis]  # Prob of starting happy.     P(X)

                           #Happy Sad
transitionTable = np.array([(0.9, 0.1), # Happy     P(Xt | Xt-1)
                            (0.2, 0.8)]) # Sad


def normalizeState(state):
  normState = np.array([0, 0])
  if state[0] > state[1]:
    ratio = state[1] / state[0]
    normState = (1-ratio, ratio)
  else:
    ratio = state[0] / state[1]
    normState = (ratio, 1-ratio)
  return normState


# Predicts the internal state X from timestep t form state.
def predict(state, observation):
    global observationTable, transitionTable

    updatedObservation =  state.T * observationTable
    
    # normalization = (np.sum(observationTable))
    # normalization = (np.prod(observationTable[0]) + np.prod(observationTable[1]))
    # updatedObservation /= normalization

    newState = (updatedObservation[0][observation], updatedObservation[1][observation])
    normState = normalizeState(newState)
    return normState


def update (state, t = 1):
    global observationTable, transitionTable
   
    if int(t) < 1:
        print("Error: timestep t must be non-zero a positive intiger")
        return (0, 0)

    newState = state.T    # Transpose the state so it canbe multiplied by transiton matrix.
    for i in range(0, t):
        newState = transitionTable.dot(newState)
        #newState =  transitionTable * newState

    newState = newState.T    

    return newState


def addObservation(state, obs):
  state = update(initState)
  newState = predict(state, obs)
  print("State: " + str(newState))
  return 


print("Inital state: " + str(initState))
state = addObservation(initState, 3) # So
state = addObservation(state, 3)     # So
state = addObservation(state, 0)     # Co
state = addObservation(state, 4)     # W
state = addObservation(state, 2)     # SL
