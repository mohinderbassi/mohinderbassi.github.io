import math

def count_candies(starting_amount, new_every):
      if (starting_amount % 2) ==0:
            while starting_amount == 0:
                starting_amount -= 1
                return new_every * new_every
      else:
            while starting_amount == 0:
                  starting_amount -= 1
                  return (new_every * new_every) + 1

print (count_candies(3,2))