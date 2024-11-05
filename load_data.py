from pybaseball import *

all_stats = statcast(start_dt="2024-01-01", end_dt="2024-12-31", verbose=0)

all_stats.to_csv("stats.csv")