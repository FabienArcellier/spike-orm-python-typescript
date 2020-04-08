# coding: utf-8
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, MetaData, Numeric, SmallInteger, String, Table, Text, text

metadata = MetaData()


t_american_football_defensive_stats = Table(
    'american_football_defensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_defensive_stats_id_seq'::regclass)")),
    Column('tackles_total', String(100)),
    Column('tackles_solo', String(100)),
    Column('tackles_assists', String(100)),
    Column('interceptions_total', String(100)),
    Column('interceptions_yards', String(100)),
    Column('interceptions_average', String(100)),
    Column('interceptions_longest', String(100)),
    Column('interceptions_touchdown', String(100)),
    Column('quarterback_hurries', String(100)),
    Column('sacks_total', String(100)),
    Column('sacks_yards', String(100)),
    Column('passes_defensed', String(100))
)


t_american_football_down_progress_stats = Table(
    'american_football_down_progress_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_down_progress_stats_id_seq'::regclass)")),
    Column('first_downs_total', String(100)),
    Column('first_downs_pass', String(100)),
    Column('first_downs_run', String(100)),
    Column('first_downs_penalty', String(100)),
    Column('conversions_third_down', String(100)),
    Column('conversions_third_down_attempts', String(100)),
    Column('conversions_third_down_percentage', String(100)),
    Column('conversions_fourth_down', String(100)),
    Column('conversions_fourth_down_attempts', String(100)),
    Column('conversions_fourth_down_percentage', String(100))
)


t_american_football_fumbles_stats = Table(
    'american_football_fumbles_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_fumbles_stats_id_seq'::regclass)")),
    Column('fumbles_committed', String(100)),
    Column('fumbles_forced', String(100)),
    Column('fumbles_recovered', String(100)),
    Column('fumbles_lost', String(100)),
    Column('fumbles_yards_gained', String(100)),
    Column('fumbles_own_committed', String(100)),
    Column('fumbles_own_recovered', String(100)),
    Column('fumbles_own_lost', String(100)),
    Column('fumbles_own_yards_gained', String(100)),
    Column('fumbles_opposing_committed', String(100)),
    Column('fumbles_opposing_recovered', String(100)),
    Column('fumbles_opposing_lost', String(100)),
    Column('fumbles_opposing_yards_gained', String(100))
)


t_american_football_offensive_stats = Table(
    'american_football_offensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_offensive_stats_id_seq'::regclass)")),
    Column('offensive_plays_yards', String(100)),
    Column('offensive_plays_number', String(100)),
    Column('offensive_plays_average_yards_per', String(100)),
    Column('possession_duration', String(100)),
    Column('turnovers_giveaway', String(100))
)


t_american_football_passing_stats = Table(
    'american_football_passing_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_passing_stats_id_seq'::regclass)")),
    Column('passes_attempts', String(100)),
    Column('passes_completions', String(100)),
    Column('passes_percentage', String(100)),
    Column('passes_yards_gross', String(100)),
    Column('passes_yards_net', String(100)),
    Column('passes_yards_lost', String(100)),
    Column('passes_touchdowns', String(100)),
    Column('passes_touchdowns_percentage', String(100)),
    Column('passes_interceptions', String(100)),
    Column('passes_interceptions_percentage', String(100)),
    Column('passes_longest', String(100)),
    Column('passes_average_yards_per', String(100)),
    Column('passer_rating', String(100)),
    Column('receptions_total', String(100)),
    Column('receptions_yards', String(100)),
    Column('receptions_touchdowns', String(100)),
    Column('receptions_first_down', String(100)),
    Column('receptions_longest', String(100)),
    Column('receptions_average_yards_per', String(100))
)


t_american_football_penalties_stats = Table(
    'american_football_penalties_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_penalties_stats_id_seq'::regclass)")),
    Column('penalties_total', String(100)),
    Column('penalty_yards', String(100)),
    Column('penalty_first_downs', String(100))
)


t_american_football_rushing_stats = Table(
    'american_football_rushing_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_rushing_stats_id_seq'::regclass)")),
    Column('rushes_attempts', String(100)),
    Column('rushes_yards', String(100)),
    Column('rushes_touchdowns', String(100)),
    Column('rushing_average_yards_per', String(100)),
    Column('rushes_first_down', String(100)),
    Column('rushes_longest', String(100))
)


t_american_football_sacks_against_stats = Table(
    'american_football_sacks_against_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_sacks_against_stats_id_seq'::regclass)")),
    Column('sacks_against_yards', String(100)),
    Column('sacks_against_total', String(100))
)


t_american_football_scoring_stats = Table(
    'american_football_scoring_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_scoring_stats_id_seq'::regclass)")),
    Column('touchdowns_total', String(100)),
    Column('touchdowns_passing', String(100)),
    Column('touchdowns_rushing', String(100)),
    Column('touchdowns_special_teams', String(100)),
    Column('touchdowns_defensive', String(100)),
    Column('extra_points_attempts', String(100)),
    Column('extra_points_made', String(100)),
    Column('extra_points_missed', String(100)),
    Column('extra_points_blocked', String(100)),
    Column('field_goal_attempts', String(100)),
    Column('field_goals_made', String(100)),
    Column('field_goals_missed', String(100)),
    Column('field_goals_blocked', String(100)),
    Column('safeties_against', String(100)),
    Column('two_point_conversions_attempts', String(100)),
    Column('two_point_conversions_made', String(100)),
    Column('touchbacks_total', String(100))
)


t_american_football_special_teams_stats = Table(
    'american_football_special_teams_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_special_teams_stats_id_seq'::regclass)")),
    Column('returns_punt_total', String(100)),
    Column('returns_punt_yards', String(100)),
    Column('returns_punt_average', String(100)),
    Column('returns_punt_longest', String(100)),
    Column('returns_punt_touchdown', String(100)),
    Column('returns_kickoff_total', String(100)),
    Column('returns_kickoff_yards', String(100)),
    Column('returns_kickoff_average', String(100)),
    Column('returns_kickoff_longest', String(100)),
    Column('returns_kickoff_touchdown', String(100)),
    Column('returns_total', String(100)),
    Column('returns_yards', String(100)),
    Column('punts_total', String(100)),
    Column('punts_yards_gross', String(100)),
    Column('punts_yards_net', String(100)),
    Column('punts_longest', String(100)),
    Column('punts_inside_20', String(100)),
    Column('punts_inside_20_percentage', String(100)),
    Column('punts_average', String(100)),
    Column('punts_blocked', String(100)),
    Column('touchbacks_total', String(100)),
    Column('touchbacks_total_percentage', String(100)),
    Column('touchbacks_kickoffs', String(100)),
    Column('touchbacks_kickoffs_percentage', String(100)),
    Column('touchbacks_punts', String(100)),
    Column('touchbacks_punts_percentage', String(100)),
    Column('touchbacks_interceptions', String(100)),
    Column('touchbacks_interceptions_percentage', String(100)),
    Column('fair_catches', String(100))
)


t_baseball_defensive_group = Table(
    'baseball_defensive_group', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_defensive_group_id_seq'::regclass)"))
)


t_baseball_defensive_stats = Table(
    'baseball_defensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_defensive_stats_id_seq'::regclass)")),
    Column('double_plays', Integer),
    Column('triple_plays', Integer),
    Column('putouts', Integer),
    Column('assists', Integer),
    Column('errors', Integer),
    Column('fielding_percentage', Numeric),
    Column('defensive_average', Numeric),
    Column('errors_passed_ball', Integer),
    Column('errors_catchers_interference', Integer)
)


t_baseball_offensive_stats = Table(
    'baseball_offensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_offensive_stats_id_seq'::regclass)")),
    Column('average', Numeric),
    Column('runs_scored', Integer),
    Column('at_bats', Integer),
    Column('hits', Integer),
    Column('rbi', Integer),
    Column('total_bases', Integer),
    Column('slugging_percentage', Numeric),
    Column('bases_on_balls', Integer),
    Column('strikeouts', Integer),
    Column('left_on_base', Integer),
    Column('left_in_scoring_position', Integer),
    Column('singles', Integer),
    Column('doubles', Integer),
    Column('triples', Integer),
    Column('home_runs', Integer),
    Column('grand_slams', Integer),
    Column('at_bats_per_rbi', Numeric),
    Column('plate_appearances_per_rbi', Numeric),
    Column('at_bats_per_home_run', Numeric),
    Column('plate_appearances_per_home_run', Numeric),
    Column('sac_flies', Integer),
    Column('sac_bunts', Integer),
    Column('grounded_into_double_play', Integer),
    Column('moved_up', Integer),
    Column('on_base_percentage', Numeric),
    Column('stolen_bases', Integer),
    Column('stolen_bases_caught', Integer),
    Column('stolen_bases_average', Numeric),
    Column('hit_by_pitch', Integer),
    Column('defensive_interferance_reaches', Integer),
    Column('on_base_plus_slugging', Numeric),
    Column('plate_appearances', Integer),
    Column('hits_extra_base', Integer)
)


t_baseball_pitching_stats = Table(
    'baseball_pitching_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_pitching_stats_id_seq'::regclass)")),
    Column('runs_allowed', Integer),
    Column('singles_allowed', Integer),
    Column('doubles_allowed', Integer),
    Column('triples_allowed', Integer),
    Column('home_runs_allowed', Integer),
    Column('innings_pitched', String(20)),
    Column('hits', Integer),
    Column('earned_runs', Integer),
    Column('unearned_runs', Integer),
    Column('bases_on_balls', Integer),
    Column('bases_on_balls_intentional', Integer),
    Column('strikeouts', Integer),
    Column('strikeout_to_bb_ratio', Numeric),
    Column('number_of_pitches', Integer),
    Column('era', Numeric),
    Column('inherited_runners_scored', Integer),
    Column('pick_offs', Integer),
    Column('errors_hit_with_pitch', Integer),
    Column('errors_wild_pitch', Integer),
    Column('balks', Integer),
    Column('wins', Integer),
    Column('losses', Integer),
    Column('saves', Integer),
    Column('shutouts', Integer),
    Column('games_complete', Integer),
    Column('games_finished', Integer),
    Column('winning_percentage', Numeric),
    Column('event_credit', String(40)),
    Column('save_credit', String(40))
)


t_basketball_defensive_stats = Table(
    'basketball_defensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('basketball_defensive_stats_id_seq'::regclass)")),
    Column('steals_total', String(100)),
    Column('steals_per_game', String(100)),
    Column('blocks_total', String(100)),
    Column('blocks_per_game', String(100))
)


t_basketball_offensive_stats = Table(
    'basketball_offensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('basketball_offensive_stats_id_seq'::regclass)")),
    Column('field_goals_made', Integer),
    Column('field_goals_attempted', Integer),
    Column('field_goals_percentage', String(100)),
    Column('field_goals_per_game', String(100)),
    Column('field_goals_attempted_per_game', String(100)),
    Column('field_goals_percentage_adjusted', String(100)),
    Column('three_pointers_made', Integer),
    Column('three_pointers_attempted', Integer),
    Column('three_pointers_percentage', String(100)),
    Column('three_pointers_per_game', String(100)),
    Column('three_pointers_attempted_per_game', String(100)),
    Column('free_throws_made', String(100)),
    Column('free_throws_attempted', String(100)),
    Column('free_throws_percentage', String(100)),
    Column('free_throws_per_game', String(100)),
    Column('free_throws_attempted_per_game', String(100)),
    Column('points_scored_total', String(100)),
    Column('points_scored_per_game', String(100)),
    Column('assists_total', String(100)),
    Column('assists_per_game', String(100)),
    Column('turnovers_total', String(100)),
    Column('turnovers_per_game', String(100)),
    Column('points_scored_off_turnovers', String(100)),
    Column('points_scored_in_paint', String(100)),
    Column('points_scored_on_second_chance', String(100)),
    Column('points_scored_on_fast_break', String(100))
)


t_basketball_rebounding_stats = Table(
    'basketball_rebounding_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('basketball_rebounding_stats_id_seq'::regclass)")),
    Column('rebounds_total', String(100)),
    Column('rebounds_per_game', String(100)),
    Column('rebounds_defensive', String(100)),
    Column('rebounds_offensive', String(100)),
    Column('team_rebounds_total', String(100)),
    Column('team_rebounds_per_game', String(100)),
    Column('team_rebounds_defensive', String(100)),
    Column('team_rebounds_offensive', String(100))
)


t_basketball_team_stats = Table(
    'basketball_team_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('basketball_team_stats_id_seq'::regclass)")),
    Column('timeouts_left', String(100)),
    Column('largest_lead', String(100)),
    Column('fouls_total', String(100)),
    Column('turnover_margin', String(100))
)


t_core_stats = Table(
    'core_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('core_stats_id_seq'::regclass)")),
    Column('score', String(100)),
    Column('score_opposing', String(100)),
    Column('score_attempts', String(100)),
    Column('score_attempts_opposing', String(100)),
    Column('score_percentage', String(100)),
    Column('score_percentage_opposing', String(100))
)


t_db_info = Table(
    'db_info', metadata,
    Column('version', String(100), nullable=False, index=True, server_default=text("16"))
)


t_display_names = Table(
    'display_names', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('display_names_id_seq'::regclass)")),
    Column('language', String(100), nullable=False),
    Column('entity_type', String(100), nullable=False),
    Column('entity_id', Integer, nullable=False),
    Column('full_name', String(100)),
    Column('first_name', String(100)),
    Column('middle_name', String(100)),
    Column('last_name', String(100)),
    Column('alias', String(100)),
    Column('abbreviation', String(100)),
    Column('short_name', String(100)),
    Column('prefix', String(20)),
    Column('suffix', String(20))
)


t_document_classes = Table(
    'document_classes', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('document_classes_id_seq'::regclass)")),
    Column('name', String(100), index=True)
)


t_document_packages = Table(
    'document_packages', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('document_packages_id_seq'::regclass)")),
    Column('package_key', String(100)),
    Column('package_name', String(100)),
    Column('date_time', Date)
)


t_ice_hockey_action_participants = Table(
    'ice_hockey_action_participants', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('ice_hockey_action_participants_id_seq'::regclass)")),
    Column('ice_hockey_action_play_id', Integer, nullable=False),
    Column('person_id', Integer, nullable=False),
    Column('participant_role', String(100), nullable=False),
    Column('point_credit', Integer)
)


t_ice_hockey_action_plays = Table(
    'ice_hockey_action_plays', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('ice_hockey_action_plays_id_seq'::regclass)")),
    Column('ice_hockey_event_state_id', Integer, nullable=False),
    Column('play_type', String(100)),
    Column('score_attempt_type', String(100)),
    Column('play_result', String(100)),
    Column('comment', String(255))
)


t_ice_hockey_defensive_stats = Table(
    'ice_hockey_defensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('ice_hockey_defensive_stats_id_seq'::regclass)")),
    Column('shots_power_play_allowed', String(100)),
    Column('shots_penalty_shot_allowed', String(100)),
    Column('goals_power_play_allowed', String(100)),
    Column('goals_penalty_shot_allowed', String(100)),
    Column('goals_against_average', String(100)),
    Column('saves', String(100)),
    Column('save_percentage', String(100)),
    Column('penalty_killing_amount', String(100)),
    Column('penalty_killing_percentage', String(100)),
    Column('shots_blocked', String(100)),
    Column('takeaways', String(100)),
    Column('shutouts', String(100)),
    Column('minutes_penalty_killing', String(100)),
    Column('hits', String(100)),
    Column('goals_empty_net_allowed', String(100)),
    Column('goals_short_handed_allowed', String(100)),
    Column('goals_shootout_allowed', String(100)),
    Column('shots_shootout_allowed', String(100))
)


t_ice_hockey_offensive_stats = Table(
    'ice_hockey_offensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('ice_hockey_offensive_stats_id_seq'::regclass)")),
    Column('goals_game_winning', String(100)),
    Column('goals_game_tying', String(100)),
    Column('goals_power_play', String(100)),
    Column('goals_short_handed', String(100)),
    Column('goals_even_strength', String(100)),
    Column('goals_empty_net', String(100)),
    Column('goals_overtime', String(100)),
    Column('goals_shootout', String(100)),
    Column('goals_penalty_shot', String(100)),
    Column('assists', String(100)),
    Column('points', String(100)),
    Column('power_play_amount', String(100)),
    Column('power_play_percentage', String(100)),
    Column('shots_penalty_shot_taken', String(100)),
    Column('shots_penalty_shot_missed', String(100)),
    Column('shots_penalty_shot_percentage', String(100)),
    Column('giveaways', String(100)),
    Column('minutes_power_play', String(100)),
    Column('faceoff_wins', String(100)),
    Column('faceoff_losses', String(100)),
    Column('faceoff_win_percentage', String(100)),
    Column('scoring_chances', String(100))
)


t_ice_hockey_player_stats = Table(
    'ice_hockey_player_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('ice_hockey_player_stats_id_seq'::regclass)")),
    Column('plus_minus', String(100))
)


t_key_roots = Table(
    'key_roots', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('key_roots_id_seq'::regclass)")),
    Column('key_type', String(100), index=True)
)


t_locations = Table(
    'locations', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('locations_id_seq'::regclass)")),
    Column('timezone', String(100)),
    Column('latitude', String(100)),
    Column('longitude', String(100)),
    Column('country_code', String(100), index=True)
)


t_motor_racing_qualifying_stats = Table(
    'motor_racing_qualifying_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('motor_racing_qualifying_stats_id_seq'::regclass)")),
    Column('grid', String(100)),
    Column('pole_position', String(100)),
    Column('pole_wins', String(100)),
    Column('qualifying_speed', String(100)),
    Column('qualifying_speed_units', String(100)),
    Column('qualifying_time', String(100)),
    Column('qualifying_position', String(100))
)


t_motor_racing_race_stats = Table(
    'motor_racing_race_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('motor_racing_race_stats_id_seq'::regclass)")),
    Column('time_behind_leader', String(100)),
    Column('laps_behind_leader', String(100)),
    Column('time_ahead_follower', String(100)),
    Column('laps_ahead_follower', String(100)),
    Column('time', String(100)),
    Column('points', String(100)),
    Column('points_rookie', String(100)),
    Column('bonus', String(100)),
    Column('laps_completed', String(100)),
    Column('laps_leading_total', String(100)),
    Column('distance_leading', String(100)),
    Column('distance_completed', String(100)),
    Column('distance_units', String(40)),
    Column('speed_average', String(40)),
    Column('speed_units', String(40)),
    Column('status', String(40)),
    Column('finishes_top_5', String(40)),
    Column('finishes_top_10', String(40)),
    Column('starts', String(40)),
    Column('finishes', String(40)),
    Column('non_finishes', String(40)),
    Column('wins', String(40)),
    Column('races_leading', String(40)),
    Column('money', String(40)),
    Column('money_units', String(40)),
    Column('leads_total', String(40))
)


t_publishers = Table(
    'publishers', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('publishers_id_seq'::regclass)")),
    Column('publisher_key', String(100), nullable=False, index=True),
    Column('publisher_name', String(100))
)


t_roles = Table(
    'roles', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('roles_id_seq'::regclass)")),
    Column('role_key', String(100), nullable=False, index=True),
    Column('role_name', String(100)),
    Column('comment', String(100))
)


t_soccer_defensive_stats = Table(
    'soccer_defensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('soccer_defensive_stats_id_seq'::regclass)")),
    Column('shots_penalty_shot_allowed', String(100)),
    Column('goals_penalty_shot_allowed', String(100)),
    Column('goals_against_average', String(100)),
    Column('goals_against_total', String(100)),
    Column('saves', String(100)),
    Column('save_percentage', String(100)),
    Column('catches_punches', String(100)),
    Column('shots_on_goal_total', String(100)),
    Column('shots_shootout_total', String(100)),
    Column('shots_shootout_allowed', String(100)),
    Column('shots_blocked', String(100)),
    Column('shutouts', String(100))
)


t_soccer_foul_stats = Table(
    'soccer_foul_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('soccer_foul_stats_id_seq'::regclass)")),
    Column('fouls_suffered', String(100)),
    Column('fouls_commited', String(100)),
    Column('cautions_total', String(100)),
    Column('cautions_pending', String(100)),
    Column('caution_points_total', String(100)),
    Column('caution_points_pending', String(100)),
    Column('ejections_total', String(100))
)


t_soccer_offensive_stats = Table(
    'soccer_offensive_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('soccer_offensive_stats_id_seq'::regclass)")),
    Column('goals_game_winning', String(100)),
    Column('goals_game_tying', String(100)),
    Column('goals_overtime', String(100)),
    Column('goals_shootout', String(100)),
    Column('goals_total', String(100)),
    Column('assists_game_winning', String(100)),
    Column('assists_game_tying', String(100)),
    Column('assists_overtime', String(100)),
    Column('assists_total', String(100)),
    Column('points', String(100)),
    Column('shots_total', String(100)),
    Column('shots_on_goal_total', String(100)),
    Column('shots_hit_frame', String(100)),
    Column('shots_penalty_shot_taken', String(100)),
    Column('shots_penalty_shot_scored', String(100)),
    Column('shots_penalty_shot_missed', String(40)),
    Column('shots_penalty_shot_percentage', String(40)),
    Column('shots_shootout_taken', String(40)),
    Column('shots_shootout_scored', String(40)),
    Column('shots_shootout_missed', String(40)),
    Column('shots_shootout_percentage', String(40)),
    Column('giveaways', String(40)),
    Column('offsides', String(40)),
    Column('corner_kicks', String(40)),
    Column('hat_tricks', String(40))
)


t_stats = Table(
    'stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('stats_id_seq'::regclass)")),
    Column('stat_repository_type', String(100), index=True),
    Column('stat_repository_id', Integer, nullable=False, index=True),
    Column('stat_holder_type', String(100), index=True),
    Column('stat_holder_id', Integer, index=True),
    Column('stat_coverage_type', String(100), index=True),
    Column('stat_coverage_id', Integer, index=True),
    Column('context', String(40), nullable=False, index=True)
)


t_team_american_football_stats = Table(
    'team_american_football_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('team_american_football_stats_id_seq'::regclass)")),
    Column('yards_per_attempt', String(100)),
    Column('average_starting_position', String(100)),
    Column('timeouts', String(100)),
    Column('time_of_possession', String(100)),
    Column('turnover_ratio', String(100))
)


t_tennis_action_points = Table(
    'tennis_action_points', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('tennis_action_points_id_seq'::regclass)")),
    Column('sub_period_id', String(100)),
    Column('sequence_number', String(100)),
    Column('win_type', String(100))
)


t_tennis_action_volleys = Table(
    'tennis_action_volleys', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('tennis_action_volleys_id_seq'::regclass)")),
    Column('sequence_number', String(100)),
    Column('tennis_action_points_id', Integer),
    Column('landing_location', String(100)),
    Column('swing_type', String(100)),
    Column('result', String(100)),
    Column('spin_type', String(100)),
    Column('trajectory_details', String(100))
)


t_tennis_return_stats = Table(
    'tennis_return_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('tennis_return_stats_id_seq'::regclass)")),
    Column('returns_played', String(100)),
    Column('matches_played', String(100)),
    Column('first_service_return_points_won', String(100)),
    Column('first_service_return_points_won_pct', String(100)),
    Column('second_service_return_points_won', String(100)),
    Column('second_service_return_points_won_pct', String(100)),
    Column('return_games_played', String(100)),
    Column('return_games_won', String(100)),
    Column('return_games_won_pct', String(100)),
    Column('break_points_played', String(100)),
    Column('break_points_converted', String(100)),
    Column('break_points_converted_pct', String(100))
)


t_tennis_service_stats = Table(
    'tennis_service_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('tennis_service_stats_id_seq'::regclass)")),
    Column('services_played', String(100)),
    Column('matches_played', String(100)),
    Column('aces', String(100)),
    Column('first_services_good', String(100)),
    Column('first_services_good_pct', String(100)),
    Column('first_service_points_won', String(100)),
    Column('first_service_points_won_pct', String(100)),
    Column('second_service_points_won', String(100)),
    Column('second_service_points_won_pct', String(100)),
    Column('service_games_played', String(100)),
    Column('service_games_won', String(100)),
    Column('service_games_won_pct', String(100)),
    Column('break_points_played', String(100)),
    Column('break_points_saved', String(100)),
    Column('break_points_saved_pct', String(100))
)


t_addresses = Table(
    'addresses', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('addresses_id_seq'::regclass)")),
    Column('location_id', ForeignKey('locations.id'), nullable=False, index=True),
    Column('language', String(100)),
    Column('suite', String(100)),
    Column('floor', String(100)),
    Column('building', String(100)),
    Column('street_number', String(100)),
    Column('street_prefix', String(100)),
    Column('street', String(100)),
    Column('street_suffix', String(100)),
    Column('neighborhood', String(100)),
    Column('district', String(100)),
    Column('locality', String(100), index=True),
    Column('county', String(100)),
    Column('region', String(100), index=True),
    Column('postal_code', String(100), index=True),
    Column('country', String(100))
)


t_affiliations = Table(
    'affiliations', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('affiliations_id_seq'::regclass)")),
    Column('affiliation_key', String(100), nullable=False, index=True),
    Column('affiliation_type', String(100), index=True),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False, index=True)
)


t_bookmakers = Table(
    'bookmakers', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('bookmakers_id_seq'::regclass)")),
    Column('bookmaker_key', String(100)),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False),
    Column('location_id', ForeignKey('locations.id'))
)


t_document_fixtures = Table(
    'document_fixtures', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('document_fixtures_id_seq'::regclass)")),
    Column('fixture_key', String(100), index=True),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False, index=True),
    Column('name', String(100)),
    Column('document_class_id', ForeignKey('document_classes.id'), nullable=False, index=True)
)


t_key_aliases = Table(
    'key_aliases', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('key_aliases_id_seq'::regclass)")),
    Column('key_id', Integer, nullable=False, index=True),
    Column('key_root_id', ForeignKey('key_roots.id'), nullable=False)
)


t_persons = Table(
    'persons', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('persons_id_seq'::regclass)")),
    Column('person_key', String(100), nullable=False, index=True),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False, index=True),
    Column('gender', String(20)),
    Column('birth_date', String(30)),
    Column('death_date', String(30)),
    Column('birth_location_id', ForeignKey('locations.id')),
    Column('hometown_location_id', ForeignKey('locations.id')),
    Column('residence_location_id', ForeignKey('locations.id')),
    Column('death_location_id', ForeignKey('locations.id'))
)


t_sites = Table(
    'sites', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('sites_id_seq'::regclass)")),
    Column('site_key', Integer, nullable=False, index=True),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False, index=True),
    Column('location_id', ForeignKey('locations.id'), index=True)
)


t_documents = Table(
    'documents', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('documents_id_seq'::regclass)")),
    Column('doc_id', String(75), nullable=False, index=True),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False, index=True),
    Column('date_time', DateTime, index=True),
    Column('title', String(255)),
    Column('language', String(100)),
    Column('priority', String(100), index=True),
    Column('revision_id', String(75), index=True),
    Column('stats_coverage', String(100)),
    Column('document_fixture_id', ForeignKey('document_fixtures.id'), nullable=False, index=True),
    Column('source_id', ForeignKey('publishers.id'), index=True),
    Column('db_loading_date_time', DateTime)
)


t_events = Table(
    'events', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('events_id_seq'::regclass)")),
    Column('event_key', String(100), nullable=False, index=True),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False, index=True),
    Column('start_date_time', DateTime),
    Column('site_id', ForeignKey('sites.id'), index=True),
    Column('site_alignment', String(100)),
    Column('event_status', String(100)),
    Column('duration', String(100)),
    Column('attendance', String(100)),
    Column('last_update', DateTime)
)


t_media = Table(
    'media', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('media_id_seq'::regclass)")),
    Column('object_id', Integer),
    Column('source_id', Integer),
    Column('revision_id', Integer),
    Column('media_type', String(100)),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False),
    Column('date_time', String(100)),
    Column('credit_id', ForeignKey('persons.id'), nullable=False),
    Column('db_loading_date_time', DateTime),
    Column('creation_location_id', ForeignKey('locations.id'), nullable=False)
)


t_positions = Table(
    'positions', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('positions_id_seq'::regclass)")),
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False, index=True),
    Column('abbreviation', String(100), nullable=False, index=True)
)


t_seasons = Table(
    'seasons', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('seasons_id_seq'::regclass)")),
    Column('season_key', Integer, nullable=False, index=True),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False, index=True),
    Column('league_id', ForeignKey('affiliations.id'), nullable=False, index=True),
    Column('start_date_time', DateTime),
    Column('end_date_time', DateTime)
)


t_teams = Table(
    'teams', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('teams_id_seq'::regclass)")),
    Column('team_key', String(100), nullable=False),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False),
    Column('home_site_id', ForeignKey('sites.id'))
)


t_affiliation_phases = Table(
    'affiliation_phases', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('affiliation_phases_id_seq'::regclass)")),
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False),
    Column('ancestor_affiliation_id', ForeignKey('affiliations.id')),
    Column('start_season_id', ForeignKey('seasons.id')),
    Column('start_date_time', DateTime),
    Column('end_season_id', ForeignKey('seasons.id')),
    Column('end_date_time', DateTime)
)


t_affiliations_documents = Table(
    'affiliations_documents', metadata,
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False),
    Column('document_id', ForeignKey('documents.id'), nullable=False)
)


t_affiliations_events = Table(
    'affiliations_events', metadata,
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False),
    Column('event_id', ForeignKey('events.id'), nullable=False)
)


t_affiliations_media = Table(
    'affiliations_media', metadata,
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False),
    Column('media_id', ForeignKey('media.id'), nullable=False)
)


t_american_football_event_states = Table(
    'american_football_event_states', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_event_states_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('current_state', SmallInteger, index=True),
    Column('sequence_number', Integer),
    Column('period_value', Integer),
    Column('period_time_elapsed', String(100)),
    Column('period_time_remaining', String(100)),
    Column('clock_state', String(100)),
    Column('down', Integer),
    Column('team_in_possession_id', ForeignKey('teams.id')),
    Column('distance_for_1st_down', Integer),
    Column('field_side', String(100)),
    Column('field_line', Integer),
    Column('context', String(40))
)


t_baseball_defensive_players = Table(
    'baseball_defensive_players', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_defensive_players_id_seq'::regclass)")),
    Column('baseball_defensive_group_id', ForeignKey('baseball_defensive_group.id'), nullable=False),
    Column('player_id', ForeignKey('persons.id'), nullable=False),
    Column('position_id', ForeignKey('positions.id'), nullable=False)
)


t_baseball_event_states = Table(
    'baseball_event_states', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_event_states_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('current_state', SmallInteger, index=True),
    Column('sequence_number', Integer),
    Column('at_bat_number', Integer),
    Column('inning_value', Integer),
    Column('inning_half', String(100)),
    Column('outs', Integer),
    Column('balls', Integer),
    Column('strikes', Integer),
    Column('runner_on_first_id', ForeignKey('persons.id')),
    Column('runner_on_second_id', ForeignKey('persons.id')),
    Column('runner_on_third_id', ForeignKey('persons.id')),
    Column('runner_on_first', SmallInteger),
    Column('runner_on_second', SmallInteger),
    Column('runner_on_third', SmallInteger),
    Column('runs_this_inning_half', Integer),
    Column('pitcher_id', ForeignKey('persons.id')),
    Column('batter_id', ForeignKey('persons.id')),
    Column('batter_side', String(100)),
    Column('context', String(40))
)


t_basketball_event_states = Table(
    'basketball_event_states', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('basketball_event_states_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('current_state', Integer),
    Column('sequence_number', Integer),
    Column('period_value', String(100)),
    Column('period_time_elapsed', String(100)),
    Column('period_time_remaining', String(100)),
    Column('context', String(40))
)


t_core_person_stats = Table(
    'core_person_stats', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('core_person_stats_id_seq'::regclass)")),
    Column('time_played_event', String(40)),
    Column('time_played_total', String(40)),
    Column('time_played_event_average', String(40)),
    Column('events_played', Integer),
    Column('events_started', Integer),
    Column('position_id', ForeignKey('positions.id'))
)


t_document_contents = Table(
    'document_contents', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('document_contents_id_seq'::regclass)")),
    Column('document_id', ForeignKey('documents.id'), nullable=False, index=True),
    Column('sportsml', String(200)),
    Column('abstract', Text)
)


t_document_fixtures_events = Table(
    'document_fixtures_events', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('document_fixtures_events_id_seq'::regclass)")),
    Column('document_fixture_id', ForeignKey('document_fixtures.id'), nullable=False, index=True),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('latest_document_id', ForeignKey('documents.id'), nullable=False, index=True),
    Column('last_update', DateTime)
)


t_document_package_entry = Table(
    'document_package_entry', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('document_package_entry_id_seq'::regclass)")),
    Column('document_package_id', ForeignKey('document_packages.id'), nullable=False),
    Column('rank', String(100)),
    Column('document_id', ForeignKey('documents.id'), nullable=False),
    Column('headline', String(100)),
    Column('short_headline', String(100))
)


t_events_documents = Table(
    'events_documents', metadata,
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('document_id', ForeignKey('documents.id'), nullable=False)
)


t_events_media = Table(
    'events_media', metadata,
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('media_id', ForeignKey('media.id'), nullable=False)
)


t_ice_hockey_event_states = Table(
    'ice_hockey_event_states', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('ice_hockey_event_states_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('current_state', Integer),
    Column('sequence_number', Integer),
    Column('period_value', String(100)),
    Column('period_time_elapsed', String(100)),
    Column('period_time_remaining', String(100)),
    Column('context', String(40))
)


t_injury_phases = Table(
    'injury_phases', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('injury_phases_id_seq'::regclass)")),
    Column('person_id', ForeignKey('persons.id'), nullable=False, index=True),
    Column('injury_status', String(100), index=True),
    Column('injury_type', String(100)),
    Column('injury_comment', String(100)),
    Column('disabled_list', String(100)),
    Column('start_date_time', DateTime, index=True),
    Column('end_date_time', DateTime, index=True),
    Column('season_id', ForeignKey('seasons.id'), index=True),
    Column('phase_type', String(100)),
    Column('injury_side', String(100))
)


t_latest_revisions = Table(
    'latest_revisions', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('latest_revisions_id_seq'::regclass)")),
    Column('revision_id', String(75), nullable=False, index=True),
    Column('latest_document_id', ForeignKey('documents.id'), nullable=False, index=True)
)


t_media_captions = Table(
    'media_captions', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('media_captions_id_seq'::regclass)")),
    Column('media_id', ForeignKey('media.id'), nullable=False),
    Column('caption_type', String(100)),
    Column('caption', String(100)),
    Column('caption_author_id', ForeignKey('persons.id'), nullable=False),
    Column('language', String(100)),
    Column('caption_size', String(100))
)


t_media_contents = Table(
    'media_contents', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('media_contents_id_seq'::regclass)")),
    Column('media_id', ForeignKey('media.id'), nullable=False),
    Column('object', String(100)),
    Column('format', String(100)),
    Column('mime_type', String(100)),
    Column('height', String(100)),
    Column('width', String(100)),
    Column('duration', String(100)),
    Column('file_size', String(100)),
    Column('resolution', String(100))
)


t_media_keywords = Table(
    'media_keywords', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('media_keywords_id_seq'::regclass)")),
    Column('keyword', String(100)),
    Column('media_id', ForeignKey('media.id'), nullable=False)
)


t_motor_racing_event_states = Table(
    'motor_racing_event_states', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('motor_racing_event_states_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('current_state', Integer),
    Column('sequence_number', Integer),
    Column('lap', String(100)),
    Column('laps_remaining', String(100)),
    Column('time_elapsed', String(100)),
    Column('flag_state', String(100)),
    Column('context', String(40))
)


t_participants_events = Table(
    'participants_events', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('participants_events_id_seq'::regclass)")),
    Column('participant_type', String(100), nullable=False, index=True),
    Column('participant_id', Integer, nullable=False, index=True),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('alignment', String(100), index=True),
    Column('score', String(100)),
    Column('event_outcome', String(100), index=True),
    Column('rank', Integer)
)


t_person_event_metadata = Table(
    'person_event_metadata', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('person_event_metadata_id_seq'::regclass)")),
    Column('person_id', ForeignKey('persons.id'), nullable=False, index=True),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('status', String(100), index=True),
    Column('health', String(100)),
    Column('weight', String(100)),
    Column('role_id', ForeignKey('roles.id'), index=True),
    Column('position_id', ForeignKey('positions.id'), index=True),
    Column('team_id', ForeignKey('teams.id'), index=True),
    Column('lineup_slot', Integer),
    Column('lineup_slot_sequence', Integer)
)


t_person_phases = Table(
    'person_phases', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('person_phases_id_seq'::regclass)")),
    Column('person_id', ForeignKey('persons.id'), nullable=False, index=True),
    Column('membership_type', String(40), nullable=False, index=True),
    Column('membership_id', Integer, nullable=False, index=True),
    Column('role_id', ForeignKey('roles.id')),
    Column('role_status', String(40)),
    Column('phase_status', String(40), index=True),
    Column('uniform_number', String(20)),
    Column('regular_position_id', ForeignKey('positions.id'), index=True),
    Column('regular_position_depth', String(40)),
    Column('height', String(100)),
    Column('weight', String(100)),
    Column('start_date_time', DateTime),
    Column('start_season_id', ForeignKey('seasons.id')),
    Column('end_date_time', DateTime),
    Column('end_season_id', ForeignKey('seasons.id')),
    Column('entry_reason', String(40)),
    Column('exit_reason', String(40)),
    Column('selection_level', Integer),
    Column('selection_sublevel', Integer),
    Column('selection_overall', Integer)
)


t_persons_documents = Table(
    'persons_documents', metadata,
    Column('person_id', ForeignKey('persons.id'), nullable=False),
    Column('document_id', ForeignKey('documents.id'), nullable=False)
)


t_persons_media = Table(
    'persons_media', metadata,
    Column('person_id', ForeignKey('persons.id'), nullable=False),
    Column('media_id', ForeignKey('media.id'), nullable=False)
)


t_soccer_event_states = Table(
    'soccer_event_states', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('soccer_event_states_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('current_state', Integer),
    Column('sequence_number', Integer),
    Column('period_value', String(100)),
    Column('period_time_elapsed', String(100)),
    Column('period_time_remaining', String(100)),
    Column('minutes_elapsed', String(100)),
    Column('period_minute_elapsed', String(100)),
    Column('context', String(40))
)


t_sub_seasons = Table(
    'sub_seasons', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('sub_seasons_id_seq'::regclass)")),
    Column('sub_season_key', String(100), nullable=False, index=True),
    Column('season_id', ForeignKey('seasons.id'), nullable=False, index=True),
    Column('sub_season_type', String(100), nullable=False, index=True),
    Column('start_date_time', DateTime),
    Column('end_date_time', DateTime)
)


t_team_phases = Table(
    'team_phases', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('team_phases_id_seq'::regclass)")),
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('start_season_id', ForeignKey('seasons.id')),
    Column('end_season_id', ForeignKey('seasons.id')),
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False),
    Column('start_date_time', String(100)),
    Column('end_date_time', String(100)),
    Column('phase_status', String(40)),
    Column('role_id', ForeignKey('roles.id'))
)


t_teams_documents = Table(
    'teams_documents', metadata,
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('document_id', ForeignKey('documents.id'), nullable=False)
)


t_teams_media = Table(
    'teams_media', metadata,
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('media_id', ForeignKey('media.id'), nullable=False)
)


t_tennis_event_states = Table(
    'tennis_event_states', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('tennis_event_states_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('current_state', Integer),
    Column('sequence_number', Integer),
    Column('tennis_set', String(100)),
    Column('game', String(100)),
    Column('server_person_id', Integer),
    Column('server_score', String(100)),
    Column('receiver_person_id', Integer),
    Column('receiver_score', String(100)),
    Column('service_number', String(100)),
    Column('context', String(40))
)


t_wagering_moneylines = Table(
    'wagering_moneylines', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('wagering_moneylines_id_seq'::regclass)")),
    Column('bookmaker_id', ForeignKey('bookmakers.id'), nullable=False),
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('date_time', DateTime),
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('person_id', Integer),
    Column('rotation_key', String(100)),
    Column('comment', String(100)),
    Column('vigorish', String(100)),
    Column('line', String(100)),
    Column('line_opening', String(100)),
    Column('prediction', String(100))
)


t_wagering_odds_lines = Table(
    'wagering_odds_lines', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('wagering_odds_lines_id_seq'::regclass)")),
    Column('bookmaker_id', ForeignKey('bookmakers.id'), nullable=False),
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('date_time', DateTime),
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('person_id', Integer),
    Column('rotation_key', String(100)),
    Column('comment', String(100)),
    Column('numerator', String(100)),
    Column('denominator', String(100)),
    Column('prediction', String(100)),
    Column('payout_calculation', String(100)),
    Column('payout_amount', String(100))
)


t_wagering_runlines = Table(
    'wagering_runlines', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('wagering_runlines_id_seq'::regclass)")),
    Column('bookmaker_id', ForeignKey('bookmakers.id'), nullable=False),
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('date_time', DateTime),
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('person_id', Integer),
    Column('rotation_key', String(100)),
    Column('comment', String(100)),
    Column('vigorish', String(100)),
    Column('line', String(100)),
    Column('line_opening', String(100)),
    Column('line_value', String(100)),
    Column('prediction', String(100))
)


t_wagering_straight_spread_lines = Table(
    'wagering_straight_spread_lines', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('wagering_straight_spread_lines_id_seq'::regclass)")),
    Column('bookmaker_id', ForeignKey('bookmakers.id'), nullable=False),
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('date_time', DateTime),
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('person_id', Integer),
    Column('rotation_key', String(100)),
    Column('comment', String(100)),
    Column('vigorish', String(100)),
    Column('line_value', String(100)),
    Column('line_value_opening', String(100)),
    Column('prediction', String(100))
)


t_wagering_total_score_lines = Table(
    'wagering_total_score_lines', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('wagering_total_score_lines_id_seq'::regclass)")),
    Column('bookmaker_id', ForeignKey('bookmakers.id'), nullable=False),
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('date_time', DateTime),
    Column('team_id', ForeignKey('teams.id'), nullable=False),
    Column('person_id', Integer),
    Column('rotation_key', String(100)),
    Column('comment', String(100)),
    Column('vigorish', String(100)),
    Column('line_over', String(100)),
    Column('line_under', String(100)),
    Column('total', String(100)),
    Column('total_opening', String(100)),
    Column('prediction', String(100))
)


t_weather_conditions = Table(
    'weather_conditions', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('weather_conditions_id_seq'::regclass)")),
    Column('event_id', ForeignKey('events.id'), nullable=False, index=True),
    Column('temperature', String(100)),
    Column('temperature_units', String(40)),
    Column('humidity', String(100)),
    Column('clouds', String(100)),
    Column('wind_direction', String(100)),
    Column('wind_velocity', String(100)),
    Column('weather_code', String(100))
)


t_american_football_action_plays = Table(
    'american_football_action_plays', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_action_plays_id_seq'::regclass)")),
    Column('american_football_event_state_id', ForeignKey('american_football_event_states.id'), nullable=False, index=True),
    Column('play_type', String(100), index=True),
    Column('score_attempt_type', String(100), index=True),
    Column('drive_result', String(100), index=True),
    Column('points', Integer),
    Column('comment', String(255))
)


t_baseball_action_plays = Table(
    'baseball_action_plays', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_action_plays_id_seq'::regclass)")),
    Column('baseball_event_state_id', ForeignKey('baseball_event_states.id'), nullable=False, index=True),
    Column('play_type', String(100), index=True),
    Column('notation', String(100)),
    Column('notation_yaml', Text),
    Column('baseball_defensive_group_id', Integer),
    Column('comment', String(255)),
    Column('runner_on_first_advance', Integer),
    Column('runner_on_second_advance', Integer),
    Column('runner_on_third_advance', Integer),
    Column('outs_recorded', Integer),
    Column('rbi', Integer),
    Column('runs_scored', Integer),
    Column('earned_runs_scored', String(100))
)


t_baseball_action_substitutions = Table(
    'baseball_action_substitutions', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_action_substitutions_id_seq'::regclass)")),
    Column('baseball_event_state_id', ForeignKey('baseball_event_states.id'), nullable=False),
    Column('sequence_number', Integer),
    Column('person_type', String(100)),
    Column('person_original_id', ForeignKey('persons.id')),
    Column('person_original_position_id', ForeignKey('positions.id')),
    Column('person_original_lineup_slot', Integer),
    Column('person_replacing_id', ForeignKey('persons.id')),
    Column('person_replacing_position_id', ForeignKey('positions.id')),
    Column('person_replacing_lineup_slot', Integer),
    Column('substitution_reason', String(100)),
    Column('comment', String(100))
)


t_documents_media = Table(
    'documents_media', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('documents_media_id_seq'::regclass)")),
    Column('document_id', ForeignKey('documents.id'), nullable=False),
    Column('media_id', ForeignKey('media.id'), nullable=False),
    Column('media_caption_id', ForeignKey('media_captions.id'), nullable=False)
)


t_events_sub_seasons = Table(
    'events_sub_seasons', metadata,
    Column('event_id', ForeignKey('events.id'), nullable=False),
    Column('sub_season_id', ForeignKey('sub_seasons.id'), nullable=False)
)


t_periods = Table(
    'periods', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('periods_id_seq'::regclass)")),
    Column('participant_event_id', ForeignKey('participants_events.id'), nullable=False, index=True),
    Column('period_value', String(100)),
    Column('score', String(100))
)


t_standings = Table(
    'standings', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('standings_id_seq'::regclass)")),
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False),
    Column('standing_type', String(100)),
    Column('sub_season_id', ForeignKey('sub_seasons.id'), nullable=False),
    Column('last_updated', String(100)),
    Column('duration_scope', String(100)),
    Column('competition_scope', String(100)),
    Column('competition_scope_id', String(100)),
    Column('alignment_scope', String(100)),
    Column('site_scope', String(100)),
    Column('scoping_label', String(100)),
    Column('publisher_id', ForeignKey('publishers.id'), nullable=False),
    Column('source', String(100))
)


t_american_football_action_participants = Table(
    'american_football_action_participants', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('american_football_action_participants_id_seq'::regclass)")),
    Column('american_football_action_play_id', ForeignKey('american_football_action_plays.id'), nullable=False, index=True),
    Column('person_id', ForeignKey('persons.id'), nullable=False, index=True),
    Column('participant_role', String(100), nullable=False, index=True),
    Column('score_type', String(100), index=True),
    Column('field_line', Integer),
    Column('yardage', Integer),
    Column('score_credit', Integer),
    Column('yards_gained', Integer)
)


t_baseball_action_pitches = Table(
    'baseball_action_pitches', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_action_pitches_id_seq'::regclass)")),
    Column('baseball_action_play_id', ForeignKey('baseball_action_plays.id'), nullable=False),
    Column('sequence_number', Integer),
    Column('baseball_defensive_group_id', ForeignKey('baseball_defensive_group.id'), index=True),
    Column('umpire_call', String(100), index=True),
    Column('pitch_location', String(100)),
    Column('pitch_type', String(100), index=True),
    Column('pitch_velocity', Integer),
    Column('comment', Text),
    Column('trajectory_coordinates', String(100)),
    Column('trajectory_formula', String(100)),
    Column('ball_type', String(40)),
    Column('strike_type', String(40))
)


t_standing_subgroups = Table(
    'standing_subgroups', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('standing_subgroups_id_seq'::regclass)")),
    Column('standing_id', ForeignKey('standings.id'), nullable=False),
    Column('affiliation_id', ForeignKey('affiliations.id'), nullable=False)
)


t_sub_periods = Table(
    'sub_periods', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('sub_periods_id_seq'::regclass)")),
    Column('period_id', ForeignKey('periods.id'), nullable=False, index=True),
    Column('sub_period_value', String(100)),
    Column('score', String(100))
)


t_baseball_action_contact_details = Table(
    'baseball_action_contact_details', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('baseball_action_contact_details_id_seq'::regclass)")),
    Column('baseball_action_pitch_id', ForeignKey('baseball_action_pitches.id'), nullable=False),
    Column('location', String(100)),
    Column('strength', String(100)),
    Column('velocity', Integer),
    Column('comment', Text),
    Column('trajectory_coordinates', String(100)),
    Column('trajectory_formula', String(100))
)


t_outcome_totals = Table(
    'outcome_totals', metadata,
    Column('id', Integer, nullable=False, unique=True, server_default=text("nextval('outcome_totals_id_seq'::regclass)")),
    Column('standing_subgroup_id', ForeignKey('standing_subgroups.id'), nullable=False),
    Column('outcome_holder_type', String(100)),
    Column('outcome_holder_id', Integer),
    Column('rank', String(100)),
    Column('wins', String(100)),
    Column('losses', String(100)),
    Column('ties', String(100)),
    Column('undecideds', String(100)),
    Column('winning_percentage', String(100)),
    Column('points_scored_for', String(100)),
    Column('points_scored_against', String(100)),
    Column('points_difference', String(100)),
    Column('standing_points', String(100)),
    Column('streak_type', String(100)),
    Column('streak_duration', String(100)),
    Column('streak_total', String(100)),
    Column('streak_start', Date),
    Column('streak_end', Date)
)
