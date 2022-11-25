# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import person
import random
import matplotlib.pyplot as plt
totalPopulation = 1000
populationArray = list()
numberOfRounds = 2000
lengthOfInfection = 20
Alpha = .005
Beta = .05
for x in range(totalPopulation):
  populationArray.append(person.Person(0,0))

plot_round = []
susceptible = []
infected = []



for z in range(numberOfRounds):
    x = 0
    y = 0
    currentNumInfections = 0
    populationArray[0].infectionStatus = 1
    populationArray[0].turnsRemaining = lengthOfInfection
    while x < totalPopulation :
        y = x + 1
        if populationArray[x].turnsRemaining > 0:
            if populationArray[x].infectionStatus == 1:
                while y < totalPopulation:
                    if random.random() <= Alpha:
                        if populationArray[y].infectionStatus == 0:
                            if random.random() <= Beta:
                                populationArray[y].infectionStatus = 1
                                #negative one turn remaining avoids the node infecting others until the next round
                                populationArray[y].turnsRemaining = -1
                    y += 1
            populationArray[x].turnsRemaining -= 1
        elif populationArray[x].turnsRemaining == -1:
            populationArray[x].turnsRemaining = lengthOfInfection


        x += 1
    for k in range(totalPopulation):
        if populationArray[k].infectionStatus == 1:
            currentNumInfections += 1
    print("Round: "+str(z) +" -->" +str(currentNumInfections))
    plot_round.append(z)
    susceptible.append(totalPopulation - currentNumInfections)
    infected.append(currentNumInfections)


plt.xlabel('Round')
plt.ylabel('Population')
plt.plot(plot_round, susceptible, label = "Susceptible", color = "blue")
plt.plot(plot_round, infected, label = "Infected", color = "red")
plt.legend()
plt.show()





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {populationArray[0].infectionStatus, populationArray[1].infectionStatus}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
