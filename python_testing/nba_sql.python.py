import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#     model="code-davinci-002",
#     prompt='#Table Draft\n'+
#            '#"Draft" (\n'+
#            '#"yearDraft" REAL,\n'+
#            '#"numberPickOverall" REAL,\n'+
#            '#"numberRound" REAL,\n'+
#            '#"numberRoundPick" REAL,\n'+
#            '#"namePlayer" TEXT,\n'+
#            '#"slugTeam" TEXT,\n'+
#            '#"nameOrganizationFrom" TEXT,\n'+
#            '#"typeOrganizationFrom" TEXT,\n'+
#            '#"idPlayer" REAL,\n'+
#            '#"idTeam" REAL,\n'+
#            '#"nameTeam" TEXT,\n'+
#            '#"cityTeam" TEXT,\n'+
#            '#"teamName" TEXT,\n'+
#            '#"PLAYER_PROFILE_FLAG" REAL,\n'+
#            '#"slugOrganizationTypeFrom" TEXT,\n'+
#            '#"locationOrganizationFrom" TEXT\n'+
#            '#);\n'+
#            '#Table Player\n'+
#            '#"Player" (\n'+
#            '#"id" TEXT,\n'+
#            '#"full_name" TEXT,\n'+
#            '#"first_name" TEXT,\n'+
#            '#"last_name" TEXT,\n'+
#            '#"is_active" INTEGER\n'+
#            '#);\n'+
#            '#"Player_Attributes" (\n'+
#            '#"ID" TEXT,\n'+
#            '#"FIRST_NAME" TEXT,\n'+
#            '#"LAST_NAME" TEXT,\n'+
#            '#"DISPLAY_FIRST_LAST" TEXT,\n'+
#            '#"DISPLAY_LAST_COMMA_FIRST" TEXT,\n'+
#            '#"DISPLAY_FI_LAST" TEXT,\n'+
#            '#"PLAYER_SLUG" TEXT,\n'+
#            '#"BIRTHDATE" TEXT,\n'+
#            '#"SCHOOL" TEXT,\n'+
#            '#"COUNTRY" TEXT,\n'+
#            '#"LAST_AFFILIATION" TEXT,\n'+
#            '#"HEIGHT" REAL,\n'+
#            '#"WEIGHT" REAL,\n'+
#            '#"SEASON_EXP" INTEGER,\n'+
#            '#"JERSEY" TEXT,\n'+
#            '#"POSITION" TEXT,\n'+
#            '#"ROSTERSTATUS" TEXT,\n'+
#            '#"GAMES_PLAYED_CURRENT_SEASON_FLAG" TEXT,\n'+
#            '#"TEAM_ID" TEXT,\n'+
#            '#"TEAM_NAME" TEXT,\n'+
#            '#"TEAM_ABBREVIATION" TEXT,\n'+
#            '#"TEAM_CODE" TEXT,\n'+
#            '#"TEAM_CITY" TEXT,\n'+
#            '#"PLAYERCODE" TEXT,\n'+
#            '#"FROM_YEAR" TEXT,\n'+
#            '#"TO_YEAR" TEXT,\n'+
#            '#"DLEAGUE_FLAG" TEXT,\n'+
#            '#"NBA_FLAG" TEXT,\n'+
#            '#"GAMES_PLAYED_FLAG" TEXT,\n'+
#            '#"DRAFT_YEAR" TEXT,\n'+
#            '#"DRAFT_ROUND" TEXT,\n'+
#            '#"DRAFT_NUMBER" TEXT,\n'+
#            '#"PTS" REAL,\n'+
#            '#"AST" REAL,\n'+
#            '#"REB" REAL,\n'+
#            '#"ALL_STAR_APPEARANCES" REAL,\n'+
#            '#"PIE" REAL\n'+
#            '#);\n'+
#            '#Table Game\n'+
#            'add a # for each line below\n'+
#            '#"Game" (\n'+
#            '#"GAME_ID" TEXT,\n'+
#            '#"SEASON_ID" TEXT,\n'+
#            '#"TEAM_ID_HOME" TEXT,\n'+
#            '#"TEAM_ABBREVIATION_HOME" TEXT,\n'+
#            '#"TEAM_NAME_HOME" TEXT,\n'+
#            '#"GAME_DATE" TEXT,\n'+
#            '#"MATCHUP_HOME" TEXT,\n'+
#            '#"WL_HOME" TEXT,\n'+
#            '#"MIN_HOME" INTEGER,\n'+
#            '#"FGM_HOME" REAL,\n'+
#            '#"FGA_HOME" TEXT,\n'+
#            '#"FG_PCT_HOME" REAL,\n'+
#            '#"FG3M_HOME" TEXT,\n'+
#            '#"FG3A_HOME" TEXT,\n'+
#            '#"FG3_PCT_HOME" REAL,\n'+
#            '#"FTM_HOME" REAL,\n'+
#            '#"FTA_HOME" REAL,\n'+
#            '#"FT_PCT_HOME" REAL,\n'+
#            '#"OREB_HOME" TEXT,\n'+
#            '#"DREB_HOME" TEXT,\n'+
#            '#"REB_HOME" TEXT,\n'+
#            '#"AST_HOME" TEXT,\n'+
#            '#"STL_HOME" TEXT,\n'+
#            '#"BLK_HOME" TEXT,\n'+
#            '#"TOV_HOME" TEXT,\n'+
#            '#"PF_HOME" REAL,\n'+
#            '#"PTS_HOME" INTEGER,\n'+
#            '#"PLUS_MINUS_HOME" INTEGER,\n'+
#            '#"VIDEO_AVAILABLE_HOME" INTEGER,\n'+
#            '#"TEAM_ID_AWAY" TEXT,\n'+
#            '#"TEAM_ABBREVIATION_AWAY" TEXT,\n'+
#            '#"TEAM_NAME_AWAY" TEXT,\n'+
#            '#"MATCHUP_AWAY" TEXT,\n'+
#            '#"WL_AWAY" TEXT,\n'+
#            '#"MIN_AWAY" INTEGER,\n'+
#            '#"FGM_AWAY" REAL,\n'+
#            '#"FGA_AWAY" TEXT,\n'+
#            '#"FG_PCT_AWAY" REAL,\n'+
#            '#"FG3M_AWAY" TEXT,\n'+
#            '#"FG3A_AWAY" TEXT,\n'+
#            '#"FG3_PCT_AWAY" REAL,\n'+
#            '#"FTM_AWAY" REAL,\n'+
#            '#"FTA_AWAY" REAL,\n'+
#            '#"FT_PCT_AWAY" REAL,\n'+
#            '#"OREB_AWAY" TEXT,\n'+
#            '#"DREB_AWAY" TEXT,\n'+
#            '#"REB_AWAY" TEXT,\n'+
#            '#"AST_AWAY" TEXT,\n'+
#            '#"STL_AWAY" TEXT,\n'+
#            '#"BLK_AWAY" TEXT,\n'+
#            '#"TOV_AWAY" TEXT,\n'+
#            '#"PF_AWAY" REAL,\n'+
#            '#"PTS_AWAY" INTEGER,\n'+
#            '#"PLUS_MINUS_AWAY" INTEGER,\n'+
#            '#"VIDEO_AVAILABLE_AWAY" INTEGER,\n'+
#            '#"GAME_DATE_EST" TEXT,\n'+
#            '#"GAME_SEQUENCE" TEXT,\n'+
#            '#"GAME_STATUS_ID" TEXT,\n'+
#            '#"GAME_STATUS_TEXT" TEXT,\n'+
#            '#"GAMECODE" TEXT,\n'+
#            '#"HOME_TEAM_ID" TEXT,\n'+
#            '#"VISITOR_TEAM_ID" TEXT,\n'+
#            '#"SEASON" TEXT,\n'+
#            '#"LIVE_PERIOD" REAL,\n'+
#            '#"LIVE_PC_TIME" TEXT,\n'+
#            '#"NATL_TV_BROADCASTER_ABBREVIATION" TEXT,\n'+
#            '#"LIVE_PERIOD_TIME_BCAST" TEXT,\n'+
#            '#"WH_STATUS" REAL,\n'+
#            '#"TEAM_CITY_HOME" TEXT,\n'+
#            '#"PTS_PAINT_HOME" TEXT,\n'+
#            '#"PTS_2ND_CHANCE_HOME" TEXT,\n'+
#            '#"PTS_FB_HOME" TEXT,\n'+
#            '#"LARGEST_LEAD_HOME" TEXT,\n'+
#            '#"LEAD_CHANGES_HOME" TEXT,\n'+
#            '#"TIMES_TIED_HOME" TEXT,\n'+
#            '#"TEAM_TURNOVERS_HOME" TEXT,\n'+
#            '#"TOTAL_TURNOVERS_HOME" TEXT,\n'+
#            '#"TEAM_REBOUNDS_HOME" TEXT,\n'+
#            '#"PTS_OFF_TO_HOME" TEXT,\n'+
#            '#"TEAM_CITY_AWAY" TEXT,\n'+
#            '#"PTS_PAINT_AWAY" TEXT,\n'+
#            '#"PTS_2ND_CHANCE_AWAY" TEXT,\n'+
#            '#"PTS_FB_AWAY" TEXT,\n'+
#            '#"LARGEST_LEAD_AWAY" TEXT,\n'+
#            '#"LEAD_CHANGES_AWAY" TEXT,\n'+
#            '#"TIMES_TIED_AWAY" TEXT,\n'+
#            '#"TEAM_TURNOVERS_AWAY" TEXT,\n'+
#            '#"TOTAL_TURNOVERS_AWAY" TEXT,\n'+
#            '#"TEAM_REBOUNDS_AWAY" TEXT,\n'+
#            '#"PTS_OFF_TO_AWAY" TEXT,\n'+
#            '#"LEAGUE_ID" TEXT,\n'+
#            '#"GAME_DATE_DAY" TEXT,\n'+
#            '#"ATTENDANCE" TEXT,\n'+
#            '#"GAME_TIME" TEXT,\n'+
#            '#"TEAM_CITY_NAME_HOME" TEXT,\n'+
#            '#"TEAM_NICKNAME_HOME" TEXT,\n'+
#            '#"TEAM_WINS_LOSSES_HOME" TEXT,\n'+
#            '#"PTS_QTR1_HOME" TEXT,\n'+
#            '#"PTS_QTR2_HOME" TEXT,\n'+
#            '#"PTS_QTR3_HOME" TEXT,\n'+
#            '#"PTS_QTR4_HOME" TEXT,\n'+
#            '#"PTS_OT1_HOME" TEXT,\n'+
#            '#"PTS_OT2_HOME" TEXT,\n'+
#            '#"PTS_OT3_HOME" TEXT,\n'+
#            '#"PTS_OT4_HOME" TEXT,\n'+
#            '#"PTS_OT5_HOME" TEXT,\n'+
#            '#"PTS_OT6_HOME" TEXT,\n'+
#            '#"PTS_OT7_HOME" TEXT,\n'+
#            '#"PTS_OT8_HOME" TEXT,\n'+
#            '#"PTS_OT9_HOME" TEXT,\n'+
#            '#"PTS_OT10_HOME" TEXT,\n'+
#            '#"PTS_HOME_y" REAL,\n'+
#            '#"TEAM_CITY_NAME_AWAY" TEXT,\n'+
#            '#"TEAM_NICKNAME_AWAY" TEXT,\n'+
#            '#"TEAM_WINS_LOSSES_AWAY" TEXT,\n'+
#            '#"PTS_QTR1_AWAY" TEXT,\n'+
#            '#"PTS_QTR2_AWAY" TEXT,\n'+
#            '#"PTS_QTR3_AWAY" TEXT,\n'+
#            '#"PTS_QTR4_AWAY" TEXT,\n'+
#            '#"PTS_OT1_AWAY" TEXT,\n'+
#            '#"PTS_OT2_AWAY" TEXT,\n'+
#            '#"PTS_OT3_AWAY" TEXT,\n'+
#            '#"PTS_OT4_AWAY" TEXT,\n'+
#            '#"PTS_OT5_AWAY" TEXT,\n'+
#            '#"PTS_OT6_AWAY" TEXT,\n'+
#            '#"PTS_OT7_AWAY" TEXT,\n'+
#            '#"PTS_OT8_AWAY" TEXT,\n'+
#            '#"PTS_OT9_AWAY" TEXT,\n'+
#            '#"PTS_OT10_AWAY" TEXT,\n'+
#            '#"LAST_GAME_ID" TEXT,\n'+
#            '#"LAST_GAME_DATE_EST" TEXT,\n'+
#            '#"LAST_GAME_HOME_TEAM_ID" TEXT,\n'+
#            '#"LAST_GAME_HOME_TEAM_CITY" TEXT,\n'+
#            '#"LAST_GAME_HOME_TEAM_NAME" TEXT,\n'+
#            '#"LAST_GAME_HOME_TEAM_ABBREVIATION" TEXT,\n'+
#            '#"LAST_GAME_HOME_TEAM_POINTS" TEXT,\n'+
#            '#"LAST_GAME_VISITOR_TEAM_ID" TEXT,\n'+
#            '#"LAST_GAME_VISITOR_TEAM_CITY" TEXT,\n'+
#            '#"LAST_GAME_VISITOR_TEAM_NAME" TEXT,\n'+
#            '#"LAST_GAME_VISITOR_TEAM_CITY1" TEXT,\n'+
#            '#"LAST_GAME_VISITOR_TEAM_POINTS" TEXT,\n'+
#            '#"HOME_TEAM_WINS" REAL,\n'+
#            '#"HOME_TEAM_LOSSES" REAL,\n'+
#            '#"SERIES_LEADER" TEXT,\n'+
#            '#"VIDEO_AVAILABLE_FLAG" REAL,\n'+
#            '#"PT_AVAILABLE" REAL,\n'+
#            '#"PT_XYZ_AVAILABLE" REAL,\n'+
#            '#"HUSTLE_STATUS" REAL,\n'+
#            '#"HISTORICAL_STATUS" REAL\n'+
#            '#);\n'+
#            '#Table Team\n'+
#            '#"Team" (\n'+
#            '#"id" TEXT,\n'+
#            '#"full_name" TEXT,\n'+
#            '#"abbreviation" TEXT,\n'+
#            '#"nickname" TEXT,\n'+
#            '#"city" TEXT,\n'+
#            '#"state" TEXT,\n'+
#            '#"year_founded" INTEGER\n'+
#            '#);\n'+
#            '#Table Team_Attributes\n'+
#            '#"Team_Attributes" (\n'+
#            '#"ID" TEXT,\n'+
#            '#"ABBREVIATION" TEXT,\n'+
#            '#"NICKNAME" TEXT,\n'+
#            '#"YEARFOUNDED" TEXT,\n'+
#            '#"CITY" TEXT,\n'+
#            '#"ARENA" TEXT,\n'+
#            '#"ARENACAPACITY" REAL,\n'+
#            '#"OWNER" TEXT,\n'+
#            '#"GENERALMANAGER" TEXT,\n'+
#            '#"HEADCOACH" TEXT,\n'+
#            '#"DLEAGUEAFFILIATION" TEXT,\n'+
#            '#"FACEBOOK_WEBSITE_LINK" TEXT,\n'+
#            '#"INSTAGRAM_WEBSITE_LINK" TEXT,\n'+
#            '#"TWITTER_WEBSITE_LINK" TEXT\n'+
#            '#);\n'+
#            '##\n'+
#            'a sql query to find when J.R Smith birthday is',
#     temperature=0,
#     max_tokens=150,
#     top_p=1.0,
#     frequency_penalty=0.0,
#     presence_penalty=0.0,
#     stop=["##"]
# )
response = openai.Completion.create(
    model="curie:ft-student-2022-10-05-13-00-49",
    prompt="A query to list of all players who are under 6 feet tall",
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(response)