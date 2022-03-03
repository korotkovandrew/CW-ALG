import random
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core.indexing import IndexSlice

from premadeData import *

import sys, os 
sys.path.insert(1, os.path.join(sys.path[0], "../source/hashTable"))
from hashTable import HashTable

def timeSpent(ht, htdata):
    averageFindTime = 0
    averageRemoveTime = 0
    averageAddTime = 0
    rolls = 100
    indices = list(range(0, len(htdata)))
    random.shuffle(indices)
    for _ in range(rolls):
        for i in indices:
            start = time.time()
            ht.find(htdata[i])
            averageFindTime += time.time() - start
            
            start = time.time()
            ht.remove(htdata[i])
            averageRemoveTime += time.time() - start
            
            start = time.time()
            ht.add(htdata[i])
            averageAddTime += time.time() - start
            
    averageFindTime = (averageFindTime/rolls)/len(htdata)
    averageRemoveTime = (averageRemoveTime/rolls)/len(htdata)
    averageAddTime = (averageAddTime/rolls)/len(htdata)
    
    return [averageFindTime, averageRemoveTime, averageAddTime]

def badHash(value, capacity):
    return value % 5 % capacity

def worstHash(value, capacity):
    return value % 2 % capacity

def graph_1(addToBegin = True):
    calculatedTime = []
    
    # Normal hash and normal table size case:
    hashTable = HashTable(1000, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData1)
    calculatedTime.append(timeSpent(hashTable, testData1))

    # Bad hash and normal table size case:
    hashTable = HashTable(1000, badHash, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData1)
    calculatedTime.append(timeSpent(hashTable, testData1))
    
    # Worst hash and normal table size case:
    hashTable = HashTable(1000, worstHash, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData1)
    calculatedTime.append(timeSpent(hashTable, testData1))
    
    # Normal hash and worse table size case:
    hashTable = HashTable(10, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData1)
    calculatedTime.append(timeSpent(hashTable, testData1))

    # Bad hash and worse table size case:
    hashTable = HashTable(10, badHash, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData1)
    calculatedTime.append(timeSpent(hashTable, testData1))
    
    # Worst hash and worse table size case:
    hashTable = HashTable(10, worstHash, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData1)
    calculatedTime.append(timeSpent(hashTable, testData1))
    
    
    labels = ["normal hash & normal size",
              "bad hash & normal size",
              "worst hash & normal size",
              "normal hash & bad size",
              "bad hash & bad size",
              "worst hash & bad size"]
    
    X = np.arange(6)
    width = 0.25
    findBarValues = list(x[0] for x in calculatedTime)
    removeBarValues = list(x[1] for x in calculatedTime)
    addBarValues = list(x[2] for x in calculatedTime)
    
    fig, ax = plt.subplots()
    
    plt.bar(X - 0.325, findBarValues, width, label="find key")
    plt.bar(X - 0.125, removeBarValues, width, label="remove key")
    plt.bar(X + 0.125, addBarValues, width, label="add key")
    
    ax.set_ylabel("Average operation time, sec")
    ax.set_title("Cases on the same data")
    ax.set_xticks(X)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.legend(loc='upper right', fancybox=True, shadow=True)
    fig.tight_layout()
    
    plt.show()
    
def graph_2(addToBegin = True):
    calculatedTime = []
    
    # without repeating keys
    hashTable = HashTable(1000, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData1)
    calculatedTime.append(timeSpent(hashTable, testData1))
    
    # with repeating keys
    hashTable = HashTable(1000, addToBeginOfLinkedList=addToBegin)
    hashTable.add(testData2)
    calculatedTime.append(timeSpent(hashTable, testData2))
    
    #* На случайных данных
    randomTestData = list([random.randint(0, 1000) for i in range(1000)])
    hashTable = HashTable(1000, addToBeginOfLinkedList=addToBegin)
    hashTable.add(randomTestData)
    calculatedTime.append(timeSpent(hashTable, randomTestData))
    
    values = calculatedTime
    labels = ["1000 numbers without duplicate keys",
              "1000 numbers with duplicate keys",
              "1000 random numbers"]
    
    X = np.arange(3)
    width = 0.25
    findBarValues   = list(x[0] for x in calculatedTime)
    removeBarValues = list(x[1] for x in calculatedTime)
    addBarValues    = list(x[2] for x in calculatedTime)
    
    fig, ax = plt.subplots()
    
    plt.bar(X - 0.325, findBarValues,   width, label="find key")
    plt.bar(X - 0.125, removeBarValues, width, label="remove key")
    plt.bar(X + 0.125, addBarValues,    width, label="add key")
    
    ax.set_ylabel("Average operation time, sec")
    ax.set_title("Cases with different data and the same hash function")
    ax.set_xticks(X-0.125)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.legend(loc='upper right', fancybox=True, shadow=True)
    fig.tight_layout()
    
    plt.show()
    

if __name__ == '__main__':
    graph_1(True)
    graph_2(True)
    
    graph_1(False)
    graph_2(False)
    