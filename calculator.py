#calculator.py
import numpy

def averageDiv(numPayments,*dividendValues):
    sum = 0
    for value in dividendValues:
        sum += value
    averageValue = sum/numPayments
    return averageValue

def maxPrice(divYeld, averageValue):
    maxPrice = averageValue/divYeld
    return maxPrice