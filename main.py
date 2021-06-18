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
    firstTime = True

    i = randint(0, len(name)-1)  # gets random starting point

    route = [i]  # adding the name of starting point
    print("Program starts at the ", route, " service\n\n")

    while(aux< len(name)-1):

        fullcar = False  # updates empty car

        route = [i]  # adding the name of starting point


        while (fullcar == False):
            volumeSave = volume
            nameSave = name
            distancesIColumn = np.array(dataMatrix[i+1])  # updates dataMatrix for new i'
            distancesIColumn = np.delete(distancesIColumn, 0)
            #distancesIColumn = np.delete(distancesIColumn, i-1)
            #volumeSave = np.delete(volumeSave, i-1)

            candidateList = []  # candidates for next route entry
            w = []
            for j in range(0, len(name)):  # Gets the list of candidates with calculations
                candidateList.append(j)
                w.append(volumeSave[j] + 2*distancesIColumn[j])  #calculation

            for j in range(0 , len(solutions)):
                for k in range(0, len(solutions[j])):
                    if(solutions[j][k] in candidateList):
                        candidateList.remove(solutions[j][k])
                    if (solutions[j][k] in w):
                        w.remove(w[solutions[j][k]])

            for j in range(0 , len(route)):
                if(route[j] in candidateList):
                    candidateList.remove(route[j])
                if (route[j] in w):
                    w.remove(w[route[j]])

            bubbleSort(candidateList, w)
            if (candidateList != []):
                j = candidateList[0]  # selects first of candidateList


            if (totalVolume + volume[j] < 4 and aux <=len(name)-2 ):  # verifies if volume + new volume doesnt overcumbers the car
                route.append(j)  #adds new service to route
                totalVolume += volume[j]   #adds new volume to total volume of route
                totalDist += distancesIColumn[j]#adding distance to total distance

                i = j   #j is new i for next service in route
                aux+=1
            else:
                fullcar = True
                solutions.append(route)
                print(name[route] , totalVolume, totalDist, "\n\n")


                route = []
                totalVolume=0
                totalDist=0





#constructive(dados)
distance(GServiceName, GVolumeCar, dist_matrix)

