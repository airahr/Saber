from enum import Enum


# Type of Game. E = Exhibition, S = Spring Training, R = Regular Season, F = Wild Card, D = Divisional Series,
# L = League Championship Series, W = World Series
class GameType(Enum):
    E = 'E'  # = 'Exhibition'
    S = 'S'  # = 'Spring Training'
    R = 'R'  # = 'Regular Season'
    F = 'F'  # = 'Wild Card'
    D = 'D'  # = 'Divisional Series'
    L = 'L'  # = 'League Championship Series'
    W = 'W'  # = 'World Series'
