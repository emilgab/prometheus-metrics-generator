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
        self.horses_per_city = {cit: round(pop/self.cit_per_horse) for cit,pop in self.city_pop.items()}
        self.open_hrs = [x for x in range(7,20)]

    def __repr__(self):
        return "City Population dict: {}\n\nOpening hrs: {}".format(self.horses_per_city,self.open_hrs)

    def calcPurchase(self, city):
        if self.the_time not in self.open_hrs:
            return 0
        else:
            extra_purchases = random.randint(0,20)
            winning_number = random.randint(0,20)
            horses = self.horses_per_city[city]
            visitors = math.ceil((horses*self.perc_of_visitors)/720)
            sales = 0
            for num in range(0,visitors+1):
                odds = random.randint(0,3)
                if odds == 1:
                    sales += 1
            if extra_purchases == winning_number:
                sales += random.randint(1,3)
            return sales
