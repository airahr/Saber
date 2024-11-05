from classes.top_bot import TopBot
from classes.pitch_result import PitchResult
from classes.game_types import GameType
from classes.sides import Side
from classes.pitch_types import PitchTypes
from classes.infield_alignments import InfieldAlignments
from classes.outfield_alignments import OutfieldAlignments


class Pitch:
    pitch_type: PitchTypes
    # The type of pitch derived from Statcast.

    game_date: str
    # Date of the Game.

    release_speed: float
    # Pitch velocities from 2008-16 are via Pitch F/X, and adjusted to roughly out-of-hand release point. All
    # velocities from 2017 and beyond are Statcast, which are reported out-of-hand.

    release_pos_x: float
    # Horizontal Release Position of the ball measured in feet from the catcher's perspective.

    release_pos_z: float
    # Vertical Release Position of the ball measured in feet from the catcher's perspective.

    player_name: str = ''
    # Player's name tied to the event of the search.

    batter: int
    # MLB Player Id tied to the play event.

    pitcher: int
    # MLB Player Id tied to the play event.

    events: str | None
    # Event of the resulting Plate Appearance.

    description: str
    # Description of the resulting pitch.

    zone: int
    # Zone location of the ball when it crosses the plate from the CATCHER'S perspective.
    '''
    11  11  |   12  12
    11  1   2   3   12
    --  4   5   6   --
    13  7   8   9   14
    13  13  |   14  14
    '''

    des: str

    game_type: GameType
    # Type of Game. E = Exhibition, S = Spring Training, R = Regular Season, F = Wild Card, D = Divisional Series,
    # L = League Championship Series, W = World Series

    stand: Side
    # Side of the plate batter is standing.

    p_throws: Side
    # Hand pitcher throws with.

    home_team: str
    # Abbreviation of home team.

    away_team: str
    # Abbreviation of away team.

    type_: PitchResult
    # Short hand of pitch result. B = ball, S = strike, X = in play.

    hit_location: int | None
    # Position of first fielder to touch the ball.

    bb_type: str
    # Batted ball type, ground_ball, line_drive, fly_ball, popup.

    balls: int
    # Pre-pitch number of balls in count.

    strikes: int
    # Pre-pitch number of strikes in count.

    game_year: int
    # Year game took place.

    pfx_x: float
    # Horizontal movement in feet from the catcher's perspective.

    pfx_z: float
    # Vertical movement in feet from the catcher's perspective.

    plate_x: float
    # Horizontal position of the ball when it crosses home plate from the catcher's perspective.

    plate_z: float
    # Vertical position of the ball when it crosses home plate from the catcher's perspective.

    on_3b: int | None
    # Pre-pitch MLB Player Id of Runner on 3B.

    on_2b: int | None
    # Pre-pitch MLB Player Id of Runner on 2B.

    on_1b: int | None
    # Pre-pitch MLB Player Id of Runner on 1B.

    outs_when_up: int
    # Pre-pitch number of outs.

    inning: int
    # Pre-pitch inning number.

    inning_top_bot: TopBot
    # Pre-pitch top or bottom of inning.

    hc_x: float | None
    # Hit coordinate X of batted ball.

    hc_y: float | None
    # Hit coordinate Y of batted ball.

    fielder_2: int
    # Pre-pitch MLB Player Id of Catcher.

    sv_id: None
    # Non-unique Id of play event per game.

    vx0: float
    # The velocity of the pitch, in feet per second, in x-dimension, determined at y=50 feet.

    vy0: float
    # The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet.

    vz0: float
    # The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet.

    ax: float
    # The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet.

    ay: float
    # The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet.

    az: float
    # The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet.

    sz_top: float
    # Top of the batter's strike zone set by the operator when the ball is halfway to the plate.

    sz_bot: float
    # Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate.

    hit_distance: int | None
    # Projected hit distance of the batted ball.

    launch_speed: float | None
    # Exit velocity of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked
    # directly, estimates are included based on the process described here.

    launch_angle: float | None
    # Launch angle of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked
    # directly, estimates are included based on the process described here.

    effective_speed: float
    # Derived speed based on the the extension of the pitcher's release.

    release_spin: int
    # Spin rate of pitch tracked by Statcast.

    release_extension: float
    # Release extension of pitch in feet as tracked by Statcast.

    game_pk: int
    # Unique Id for Game.

    fielder_3: int
    # MLB Player Id for 1B.

    fielder_4: int
    # MLB Player Id for 2B.

    fielder_5: int
    # MLB Player Id for 3B.

    fielder_6: int
    # MLB Player Id for SS.

    fielder_7: int
    # MLB Player Id for LF.

    fielder_8: int
    # MLB Player Id for CF.

    fielder_9: int
    # MLB Player Id for RF.

    release_pos_y: float
    # Release position of pitch measured in feet from the catcher's perspective.

    estimated_ba_using_speedangle: float | None
    # Estimated Batting Avg based on launch angle and exit velocity.

    estimated_woba_using_speedangle: float | None
    # Estimated wOBA based on launch angle and exit velocity.

    woba_value: float | None
    # wOBA value based on result of play.

    woba_denom: int | None
    # wOBA denominator based on result of play.

    babip_value: int | None
    # BABIP value based on result of play.

    iso_value: int | None
    # ISO value based on result of play.

    launch_speed_angle: int | None
    '''
    Launch speed/angle zone based on launch angle and exit velocity.
    1: Weak
    2: Topped
    3: Under
    4: Flare/Burner
    5: Solid Contact
    6: Barrel
    '''

    at_bat_number: int
    # Plate appearance number of the game.

    pitch_number: int
    # Total pitch number of the plate appearance.

    pitch_name: PitchTypes
    # The name of the pitch derived from the Statcast Data.

    home_score: int
    # Pre-pitch home score

    away_score: int
    # Pre-pitch away score

    bat_score: int
    # Pre-pitch bat team score

    fld_score: int
    # Pre-pitch field team score

    post_away_score: int
    # Post-pitch away score

    post_home_score: int
    # Post-pitch home score

    post_bat_score: int
    # Post-pitch bat team score

    post_fld_score: int
    # Post-pitch field team score

    if_fielding_alignment: InfieldAlignments | None
    # Infield fielding alignment at the time of the pitch.

    of_fielding_alignment: OutfieldAlignments | None
    # Outfield fielding alignment at the time of the pitch.

    spin_axis: int
    # The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball
    # and 0 degrees represents a pure topspin (12-6) curveball

    delta_home_win_exp: float
    # The change in Win Expectancy before the Plate Appearance and after the Plate Appearance

    delta_run_exp: float
    # The change in Run Expectancy before the Pitch and after the Pitch

    bat_speed: float | None

    swing_length: float | None

    def __init__(self, obj: dict, ):
        super().__init__()
        self.pitch_type = obj['pitch_type']
        self.game_date = obj['game_date']
        self.release_speed = obj['release_speed']
        self.release_pos_x = obj['release_pos_x']
        self.release_pos_z = obj['release_pos_z']
        self.player_name = obj['player_name']
        self.batter = obj['batter']
        self.pitcher = obj['pitcher']
        self.events = obj['events']
        self.description = obj['description']
        self.zone = obj['zone']
        self.des = obj['des']
        self.game_type = GameType(obj['game_type'])
        self.stand = Side(obj['stand'])
        self.p_throws = Side(obj['p_throws'])
        self.home_team = obj['home_team']
        self.away_team = obj['away_team']
        self.type_ = PitchResult(obj['type'])
        self.hit_location = obj['hit_location']
        self.bb_type = obj['bb_type']
        self.balls = obj['balls']
        self.strikes = obj['strikes']
        self.game_year = obj['game_year']
        self.pfx_x = obj['pfx_x']
        self.pfx_z = obj['pfx_z']
        self.plate_x = obj['plate_x']
        self.plate_z = obj['plate_z']
        self.on_3b = obj['on_3b']
        self.on_2b = obj['on_2b']
        self.on_1b = obj['on_1b']
        self.outs_when_up = obj['outs_when_up']
        self.inning = obj['inning']
        self.inning_top_bot = TopBot(obj['inning_topbot'])
        self.hc_x = obj['hc_x']
        self.hc_y = obj['hc_y']
        self.fielder_2 = obj['fielder_2']
        self.sv_id = obj['sv_id']
        self.vx0 = obj['vx0']
        self.vy0 = obj['vy0']
        self.vz0 = obj['vz0']
        self.ax = obj['ax']
        self.ay = obj['ay']
        self.az = obj['az']
        self.sz_top = obj['sz_top']
        self.sz_bot = obj['sz_bot']
        self.hit_distance = obj['hit_distance_sc']  # I have no idea what the sc is for
        self.launch_speed = obj['launch_speed']
        self.launch_angle = obj['launch_angle']
        self.effective_speed = obj['effective_speed']
        self.release_spin = obj['release_spin_rate']
        self.release_extension = obj['release_extension']
        self.game_pk = obj['game_pk']
        self.fielder_3 = obj['fielder_3']
        self.fielder_4 = obj['fielder_4']
        self.fielder_5 = obj['fielder_5']
        self.fielder_6 = obj['fielder_6']
        self.fielder_7 = obj['fielder_7']
        self.fielder_8 = obj['fielder_8']
        self.fielder_9 = obj['fielder_9']
        self.release_pos_y = obj['release_pos_y']
        self.estimated_ba_using_speedangle = obj['estimated_ba_using_speedangle']
        self.estimated_woba_using_speedangle = obj['estimated_woba_using_speedangle']
        self.woba_value = obj['woba_value']
        self.woba_denom = obj['woba_denom']
        self.babip_value = obj['babip_value']
        self.iso_value = obj['iso_value']
        self.launch_speed_angle = obj['launch_speed_angle']
        self.at_bat_number = obj['at_bat_number']
        self.pitch_number = obj['pitch_number']
        self.pitch_name = obj['pitch_name']
        self.home_score = obj['home_score']
        self.away_score = obj['away_score']
        self.bat_score = obj['bat_score']
        self.fld_score = obj['fld_score']
        self.post_away_score = obj['post_away_score']
        self.post_home_score = obj['post_home_score']
        self.post_bat_score = obj['post_bat_score']
        self.post_fld_score = obj['post_fld_score']
        if obj['if_fielding_alignment'] in InfieldAlignments._value2member_map_:
            self.if_fielding_alignment = InfieldAlignments(obj['if_fielding_alignment'])
        else:
            self.if_fielding_alignment = None
        if obj['of_fielding_alignment'] in OutfieldAlignments._value2member_map_:
            self.of_fielding_alignment = OutfieldAlignments(obj['of_fielding_alignment'])
        else:
            self.of_fielding_alignment = None
        self.spin_axis = obj['spin_axis']
        self.delta_home_win_exp = obj['delta_home_win_exp']
        self.delta_run_exp = obj['delta_run_exp']
        self.bat_speed = obj['bat_speed']
        self.swing_length = obj['swing_length']

    def to_map(self):
        return {
            'pitch_type': self.pitch_type,
            'game_date': self.game_date,
            'release_speed': self.release_speed,
            'release_pos_x': self.release_pos_x,
            'release_pos_z': self.release_pos_z,
            'player_name': self.player_name,
            'batter': self.batter,
            'pitcher': self.pitcher,
            'events': self.events,
            'description': self.description,
            'game_type': self.game_type.value,
            'stand': self.stand.value,
            'p_throws': self.p_throws.value,
            'zone': self.zone,
            'des': self.des,
            'home_team': self.home_team,
            'away_team': self.away_team,
            'type': self.type_.value,
            'hit_location': self.hit_location,
            'bb_type': self.bb_type,
            'balls': self.balls,
            'strikes': self.strikes,
            'game_year': self.game_year,
            'pfx_x': self.pfx_x,
            'pfx_z': self.pfx_z,
            'plate_x': self.plate_x,
            'plate_z': self.plate_z,
            'on_3b': self.on_3b,
            'on_2b': self.on_2b,
            'on_1b': self.on_1b,
            'outs_when_up': self.outs_when_up,
            'inning': self.inning,
            'topbot': self.inning_top_bot.value,
            'hc_x': self.hc_x,
            'hc_y': self.hc_y,
            'fielder_2': self.fielder_2,
            'sv_id': self.sv_id,
            'vx0': self.vx0,
            'vy0': self.vy0,
            'vz0': self.vz0,
            'ax': self.ax,
            'ay': self.ay,
            'az': self.az,
            'sz_top': self.sz_top,
            'sz_bot': self.sz_bot,
            'hit_distance': self.hit_distance,
            'launch_speed': self.launch_speed,
            'launch_angle': self.launch_angle,
            'effective_speed': self.effective_speed,
            'release_spin': self.release_spin,
            'release_extension': self.release_extension,
            'game_pk': self.game_pk,
            'fielder_3': self.fielder_3,
            'fielder_4': self.fielder_4,
            'fielder_5': self.fielder_5,
            'fielder_6': self.fielder_6,
            'fielder_7': self.fielder_7,
            'fielder_8': self.fielder_8,
            'fielder_9': self.fielder_9,
            'release_pos_y': self.release_pos_y,
            'estimated_ba_using_speedangle': self.estimated_ba_using_speedangle,
            'estimated_woba_using_speedangle': self.estimated_woba_using_speedangle,
            'woba_value': self.woba_value,
            'woba_denom': self.woba_denom,
            'babip_value': self.babip_value,
            'iso_value': self.iso_value,
            'launch_speed_angle': self.launch_speed_angle,
            'at_bat_number': self.at_bat_number,
            'pitch_number': self.pitch_number,
            'pitch_name': self.pitch_name,
            'home_score': self.home_score,
            'away_score': self.away_score,
            'bat_score': self.bat_score,
            'fld_score': self.fld_score,
            'post_away_score': self.post_away_score,
            'post_home_score': self.post_home_score,
            'post_bat_score': self.post_bat_score,
            'post_fld_score': self.post_fld_score,
            'if_fielding_alignment': self.if_fielding_alignment.value if self.if_fielding_alignment else None,
            'of_fielding_alignment': self.of_fielding_alignment.value if self.of_fielding_alignment else None,
            'spin_axis': self.spin_axis,
            'delta_home_win_exp': self.delta_home_win_exp,
            'delta_run_exp': self.delta_run_exp,
            'bat_speed': self.bat_speed,
            'swing_length': self.swing_length,
        }
