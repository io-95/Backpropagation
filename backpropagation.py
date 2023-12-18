from random import random

def backpropagation(data, learningrate):
    weight_layer_1 = []
    weight_layer_2 = []
    weight_layer_1, weight_layer_2 = initialize_weight(weight_layer_1, weight_layer_2)
    
    neuron = [0, 0]
    y = 0
    for i in range(len(data)):
        neuron[0] = data[i][0] * weight_layer_1[0][0] + data[i][1] * weight_layer_1[1][0]
        neuron[1] = data[i][0] * weight_layer_1[0][1] + data[i][1] * weight_layer_1[1][1] 

def initialize_weight(weight_layyer1, weight_layer_2):
    #initilize a list with 4 rows and 2 columns
    weight_layer_1 = [[0]*2]*2
    weight_layer_2 = []

    for i in range(2):
        for j in range(2):
            weight_layer_1[i][j] = random()

    for i in range(2):
        weight_layer_2.append(random())

    return weight_layer_1, weight_layer_2
