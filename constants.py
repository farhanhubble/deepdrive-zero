SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_MARGIN = 50
MAP_WIDTH = SCREEN_WIDTH - SCREEN_MARGIN * 2
MAP_HEIGHT = SCREEN_HEIGHT - SCREEN_MARGIN * 2
PLAYER_TURN_RADIANS_PER_KEYSTROKE = 1 / 64
SCREEN_TITLE = 'spud'  # self-play unreal driving?
CHARACTER_SCALING = 1/4
USE_VOYAGE = True

if USE_VOYAGE:
    PLAYER_MOVEMENT_SPEED = 5  # pixels per frame Pacifica Hybrid
    VEHICLE_PNG = "images/voyage-van-up.png"
else:
    PLAYER_MOVEMENT_SPEED = 10  # pixels per frame Model 3
    VEHICLE_PNG = "images/tesla-up.png"
TESLA_LENGTH = 4.694
VOYAGE_VAN_LENGTH = 5.17652

