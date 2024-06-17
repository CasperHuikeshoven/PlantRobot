import time

class State:
    def main(self):
        print("Running main")

class ReadState(State):
    def main(self):
        return self.read()

    def read(self):
        yn = input("Water correct level?: ")
        if yn == "no":
            print("Switch to FillWaterState")
            return 1
        else: 
            return 0


class FillWaterState(State):
    def main(self):
        print("Filling Water")

class FillPlantFoodState(State):
    def main(self):
        print("Filling Plant Food")

class StateHandler: 
    def __init__(self):
        self.activeState = State()
        self.lastState = self.activeState

    def main(self):
        return self.activeState.main()

    def changeState(self, newState):
        self.lastState = self.activeState
        self.activeState = newState

stateHandler = StateHandler()

while True:
    stateNumber = stateHandler.main()
    print(stateNumber)
    time.sleep(1)
    yn = input("Do you want to keep reading?: ")
    if(yn == "no"):
        newStateInput = input("What state to change to?: ")
        if(newStateInput == "FillWater"):
            newState = FillWaterState()
            stateHandler.changeState(newState)
        if(newStateInput == "FillPlantFood"):
            newState = FillPlantFood()
            stateHandler.changeState(newState)
        if(newStateInput == "Reading"):
            newState = ReadState()
            stateHandler.changeState(newState)
