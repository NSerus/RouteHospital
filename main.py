import pandas as pd
import numpy as np
from random import *

# This is a project Python script.

# Press Shift+F10 to execute it or replace it with your code.

dados = pd.read_excel(r"/home/nserus/Downloads/pythonProject2/Fonte.xlsm", sheet_name="Dados")
dist_matrix = pd.read_excel(r"/home/nserus/Downloads/pythonProject2/Fonte.xlsm", sheet_name="Distance Matrix")


# Constructive Heuristic

GVolumeCar = np.array(dados['VolumeAsCars'])
GServiceName = np.array(dados['ServiceDes'])

def constructive(data):
    service_id = np.array(data['ServiceID'])  # ID
    service_des = np.array(data['ServiceDes'])  # Name
    volume = np.array(data['Volume']) #Volume in m³ (worthless)
    volume_cars = np.array(data['VolumeAsCars']) #Volume in Cars

    #for i in range(1, len(service_id)):
     #   print(service_id[i], service_des[i], volume_cars[i], volume[i])  # prints for testing purposes


    table = np.column_stack((service_id, service_des, volume_cars))
    print("\n")
    print(table)


def bubbleSort(id, value):   #bubbleSorter - got it here https://www.geeksforgeeks.org/bubble-sort/
    n = len(id)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if value[j] > value[j + 1]:
                value[j], value[j + 1] = value[j + 1], value[j]
                id[j], id[j + 1] = id[j + 1], id[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break

def distance(name, volume, dataMatrix):
    solutions = []  # all routes are saved here??
    totalDist = 0  # total distance of route
    totalVolume = 0  # total volume of route
    aux=0      #service counter
    candidateList = []  # candidates for next route entry
    w = []
    firstTime = True

    i = randint(0, len(name)-1)  # gets random starting point

    #distancesIColumn = np.delete(distancesIColumn, i - 1)  # There is probably a better way to do this but i removed the name and the null value
    #volume = np.delete(volume, i - 1)

    route = [name[i]]  # adding the name of starting point
    print("Program starts at the ", route, " service\n\n")

    while(aux< len(name)):
        print(aux)
        fullcar = False  # updates empty car

        distancesIColumn = np.array(dataMatrix[i])  #updates dataMatrix for new i'
        distancesIColumn = np.delete(distancesIColumn, 0)
        while (fullcar == False):

            if(firstTime == True):
                for j in range(0, len(name)-1):  # Gets the list of candidates with calculations
                    candidateList.append(j)
                    w.append(volume[j] + 2*distancesIColumn[j])  #calculation
                firstTime = False
                candidateList.remove(i)
                bubbleSort(candidateList, w)

            if(candidateList != []):
                j = candidateList[0]  # selects first of candidateList
            #for j in range(0, len(route)-1):   #removes services in route from the list

            candidateList.remove(candidateList[0])

            print(candidateList)

            if (totalVolume + volume[j] < 4 and candidateList !=[]):  # verifies if volume + new volume doesnt overcumbers the car
                route.append(name[j])  #adds new service to route
                totalVolume += volume[j]   #adds new volume to total volume of route
                totalDist += distancesIColumn[j]#adding distance to total distance

                i = j   #j is new i for next service in route

            else:
                fullcar = True
                solutions.append(route)
                print(route, "\n" , totalVolume, totalDist, "\n")
                aux+=len(route)
                route = []
                totalVolume=0
                totalDist=0





#constructive(dados)
distance(GServiceName, GVolumeCar, dist_matrix)

