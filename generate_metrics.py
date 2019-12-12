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
