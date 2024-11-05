import json

with open('index_by_plate_appearances.json', 'r') as json_file:
    pas_dict = json.load(json_file)

print('Loaded')


# for game, pas in pas_dict[0].items():
#     for pa_idx, pa in enumerate(pas):
#         if pa_idx == 0:
#             continue
#         for pitch_idx, pitch in enumerate(pa):
#             print(str(pitch['game_pk']), game)
#             if str(pitch['game_pk']) != game:
#                 print(game, pa_idx, pitch_idx)

game_types = {}

for game, pas in pas_dict[0].items():
    if pas[1][0]['game_type'] not in game_types:
        game_types[pas[1][0]['game_type']] = 1
    else:
        game_types[pas[1][0]['game_type']] += 1

print(game_types)