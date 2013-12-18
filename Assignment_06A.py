#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Change Problem
Assignment #: 06
Problem ID: A
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/An-Introduction-to-Dynamic-Programming-The-Change-Problem-243/#step-8
'''


def DPChange(amount, coin_list):
    '''Gives the minimum number of coins of denomination in coint_list necessary to create the given amount.'''
    # Initiate the amounts larger than zero as a number greater than the upper bound.
    min_coins = [0]+[(amount/min(coin_list))+1]*amount
    # Use dynamic programming to build up to the desired amount.
    for m in xrange(1,amount+1):
        for coin in coin_list:
            if m >= coin:
                if min_coins[m-coin] + 1 < min_coins[m]:
                    min_coins[m] = min_coins[m-coin] + 1
    return min_coins[amount]

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_6a.txt') as input_data:
        money = int(input_data.readline().strip())
        coins = map(int, input_data.readline().strip().split(','))

    # Get the desired minimum number of coins.
    min_number = str(DPChange(money, coins))

    # Print and save the answer.
    print min_number
    with open('output/Assignment_06A.txt', 'w') as output_data:
        output_data.write(min_number)
