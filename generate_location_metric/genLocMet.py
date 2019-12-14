# genLocMet.py
# This contains the genLocMet() object that will be able to
# generate the metrics for each city.

# * imports *
import datetime
import random
import math

class genLocMet():

    # stores the time that we will use to check opening hours (24hrs)
    the_time = int("{0:%H}".format(datetime.datetime.now()))
    # percentage of visitors we base ourself off which we will include in our calculations
    perc_of_visitors = 0.01 # as decimal "percentage"

    def __init__(self):
        # city populations
        self.city_pop = {
        "oslo_norway":1000467,
        "bergen_norway":255464,
        "stavanger_norway":222697,
        "fredrikstad_norway":82301,
        "sandefjord_norway":44046,
        "tromso_norway":39762
        }
        # we will use this variable to calculate a rough estimate
        # of how many horse owners there are in each city.
        self.cit_per_horse = 36
        # dictionary comprehension to calculate horse owners in each city
        self.horses_per_city = {cit: round(pop/self.cit_per_horse) for cit,pop in self.city_pop.items()}
        # opening hours of the store we will use to see if the store is open or closed in our calculations
        self.open_hrs = [x for x in range(7,20)]

    def __repr__(self):
        return "City Population dict: {}\n\nOpening hrs: {}".format(self.horses_per_city,self.open_hrs)

    def calcPurchase(self, city):
        # checks the current time if the store is open
        if self.the_time not in self.open_hrs:
            return 0
        else:
            # picks two random characters
            # if the two matches, then the store gains an extra purchase
            extra_purchases = random.randint(0,20)
            winning_number = random.randint(0,20)
            horses = self.horses_per_city[city]
            # calculates the visitors in the store
            visitors = math.ceil((horses*self.perc_of_visitors)/720)
            sales = 0
            # calculates the odds of a customer purchasing anything
            # (we assume that the odds are 1:4)
            for num in range(0,visitors+1):
                odds = random.randint(0,4)
                if odds == 1:
                    sales += 1
            # if the numbers match we add a sale between 1-2
            if extra_purchases == winning_number:
                sales += random.randint(1,3)
            return sales
