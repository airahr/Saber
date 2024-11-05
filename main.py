from pybaseball import *
import json
import pandas as pd

from classes.outfield_alignments import OutfieldAlignments
from classes.pitch_types import PitchTypes

from classes.pitch import Pitch

# assert(False)

stats_arr = pd.read_csv("stats.csv")

rows = stats_arr.iterrows()
rows_dict_list = stats_arr.to_dict('records')

# row = next(rows)[1]
# print(row)

pitches_arr = []
results = {}
for idx, row in enumerate(rows_dict_list):
    try:
        pitches_arr.append(Pitch(row))
    except ValueError as err:
        if idx:
            print(err, idx)
        continue

    if not row['events'] in results.keys():
        results[row['events']] = 1
    else:
        results[row['events']] += 1

    if (idx + 1) % 100000 == 0: print(idx + 1)

print(len(pitches_arr), 'Pitches this year')
# print(results)

pitches_arr.reverse()
plate_appearances = {}

for idx, pitch in enumerate(pitches_arr):
    if pitch.game_pk not in plate_appearances.keys():
        plate_appearances[pitch.game_pk] = [[] for _ in range(200)]

    plate_appearances[pitch.game_pk][pitch.at_bat_number].append(pitch)

for game_pk in plate_appearances.keys():
    while len(plate_appearances[game_pk][-1]) == 0:
        plate_appearances[game_pk] = plate_appearances[game_pk][:-1]

for game_pk in plate_appearances.keys():
    for plate_appearance in plate_appearances[game_pk]:
        plate_appearance.sort(key=lambda x: x.pitch_number)

# for pitch in plate_appearances[775298][2]:
#     print(pitch.pitch_type, pitch.zone, pitch.pitch_number)

keys = list(plate_appearances.keys())
pas_dict = dict(
    zip(
        keys, [[[ball.to_map() for ball in pas] for pas in plate_appearances[game]] for game in keys]
    )
),

json.dump(pas_dict, open('index_by_plate_appearances.json', 'w'))
# toMap() function needed in class Pitch
