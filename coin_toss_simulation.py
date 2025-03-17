import random
import argparse
import sys

parser = argparse.ArgumentParser(description='Welcome to the coin toss experiment')

parser.add_argument('--bias', default = 50, type=int, help='Bias for head.Value should be within 0 to 100 inclusive default is 50')

parser.add_argument('--count', default = 100, type=int, help='Enter the number of simulations to be done default is 100')

output_space = [1,0]

outcome = []

args = parser.parse_args()

head = args.bias
sim_count = args.count
  

if head < 0 or head > 100:
    sys.exit("Bias for head.Value should be within 0 to 100 inclusive. It cannot be less than 0 or more than 100")

elif head:    

    tail = 100-head

    bias_array = [head,tail]

for i in range(sim_count):
    output = random.choices(output_space, weights=bias_array,k=1)
    outcome.append(output)

percetage_outcome_head = round(outcome.count([1])/len(outcome)*100,2)

percetage_outcome_tail = round(outcome.count([0])/len(outcome)*100,2)

print("Head came out "+ str(percetage_outcome_head)+"% of time")

print("Tail came out "+ str(percetage_outcome_tail)+"% of time")
