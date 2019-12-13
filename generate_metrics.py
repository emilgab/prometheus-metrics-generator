# File for generating the metrics for prometheus
# This works as the main file which will use the genLocMet() object
# This main file has a job, which is to create the metric file itself.
# Which will look like this (exclude python comments):
# TYPE store_metrics gauge
# HELP store_metrics Contains the metrics read from each store
# store_in_question_1{name="Store_name"} metric
# store_in_question_2{name="Store_name"} metric
# ...
# ...

# * imports *
from generate_location_metric.genLocMet import genLocMet
import os

x = genLocMet()

prom_type_line = "# TYPE store_sales gauge"
prom_help_line = "# HELP store_sales Sales from all of the stores"

with open("metrics","w+") as f:
    f.write("{}\n{}\n".format(prom_type_line,prom_help_line))
    f.write('stores_sales{%s} %s\n' % ('name="oslo"',x.calcPurchase('oslo_norway')))
    f.write('stores_sales{%s} %s\n' % ('name="bergen"',x.calcPurchase('bergen_norway')))
    f.write('stores_sales{%s} %s\n' % ('name="stavanger"',x.calcPurchase('stavanger_norway')))
    f.write('stores_sales{%s} %s\n' % ('name="fredrikstad"',x.calcPurchase('fredrikstad_norway')))
    f.write('stores_sales{%s} %s\n' % ('name="sandefjord"',x.calcPurchase('sandefjord_norway')))
    f.write('stores_sales{%s} %s\n' % ('name="tromso"',x.calcPurchase('tromso_norway')))
