# genLocMet.py
# This contains the genLocMet() object that will be able to
# generate the metrics for each city.

# * imports *
import datetime

class genLocMet():

    # stores the time that we will use to check opening hours (24hrs)
    the_time = int("{0:%H}".format(datetime.datetime.now()))

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
        self.open_hrs = [x for x in range(7,21)]

    def __repr__(self):
        return "{}".format(self.horses_per_city)
