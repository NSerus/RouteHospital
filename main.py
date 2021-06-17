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

    aux = 0  #
    full_car = False  # verifies if car is full
    volume_air = 0  #

    table = np.column_stack((service_id, service_des, volume_cars))
    print("\n")
    print(table)


def distanceWtest(name, volume, dataMatrix):
    solutions = []  # all routes are saved here??
    totaldist = 0  # total distance of route
    totalVolume = 0  # total volume of route
    fullcar = False  # if car is full

    i = randint(1, len(name))  # gets random starting point
    distancesIColumn = np.array(dataMatrix[i])
    distancesIColumn = np.delete(distancesIColumn,0)
    distancesIColumn = np.delete(distancesIColumn, i-1) #There is probably a better way to do this but i removed the name and the null value
    volume = np.delete(volume, i-1)


    route = [name[i]]  # adding the name of starting point

    print("Program starts at the ", route, " service\n\n")

    while (fullcar == False):
        candidateList = []  # candidates for next route entry
        w = []
        for j in range(0, len(name)-1):  # Gets the list of candidates with calculations
            candidateList.append(j)

            w.append(volume[j] + 2*distancesIColumn[j])  # TODO: Learn how the calculation works  DONE
        print(w, "\n")
        np.sort(w)  # TODO: order CandidateList by less to more  DONE?
        print(w, "\n")
        fullcar = True


def distance(name, volume, dataMatrix):

    solutions = []  #all routes are saved here??
    totaldist = 0  #total distance of route
    totalVolume= 0 #total volume of route
    fullcar = False  #if car is full

    i = randint(1, len(name))  # gets random starting point
    distancesIColumn = np.array(dataMatrix[name[i]])

    route = [name[i]] #adding the name of starting point

    print("Program starts at the ", route, " service\n\n")

    while (fullcar == False):
        candidateList = []        #candidates for next route entry
        w = []
        for j in range(1,len(name)+1):  #Gets the list of candidates with calculations
            candidateList.append(j)
            w[j] = volume[j] + 2*distancesIColumn[j]#TODO: Learn how the calculation works  DONE?

        for j in range(1, route):   #removes services in route from the list
            candidateList.splice(j, 1)

        np.sort(candidateList) #TODO: order CandidateList by less to more  DONE?
        j = candidateList[0]  #selects first of candidateList

        if (totalVolume + volume[j] < 4):  # verifies if volume + new volume doesnt overcumbers the car
            route.append(j)  #adds new service to route
            totalVolume += volume[j]   #adds new volume to total volume of route
            totaldist += distancesIColumn[j]#TODO: add Distance to total distance DONE?

            i = j   #j is new i for next service in route
            distancesIColumn = np.array(dataMatrix[name[i]])

        else:
            fullcar = true
            solutions.append(route)
            print(route, totalVolume, totaldist)
            route = []





#constructive(dados)
distanceWtest(GServiceName, GVolumeCar, dist_matrix)

"""
import random


def funcao():
    candidatelist = []
    nservices = 35
    initialsolution = 0
    route = []
    fullcar = False

    i = 0
    k = 1
    while len(route) != 35:
        for k in range(nservices):

            i = random.randint(1, nservices)

            if i not in route:
                route.append(i)
                print(i)

            while fullcar == False:
                j = 1
                for j in range(nservices):
                    candidatelist.append(j)
                    # calculo

                for j in len(route):
                    candidatelist.remove(j)


funcao()



"""
