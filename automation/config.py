"""
Configurations for the automation (static and dynamic)
"""

class SingletonMeta(type):
    """
    Referenced from https://refactoring.guru/design-patterns/singleton/python/example#example-0
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    # When in DEBUG mode, more texts will be printed
    debug_mode = True

    # The loop & screenshot cycle of automation in milliseconds
    one_cycle_ms = 500
    
    # The location of the mirrored board
    game_location = None
    board_location = None

    # These values shouldn't be changed
    orb_template_size = (140, 140)
    board_uniform_size = (830, 690)

    # Resize for game ratio 2:1, 16:9 and 3:2
    game_screen_size_2_1  = (1000, 1950)
    game_screen_size_16_9 = (1000, 1720)
    game_screen_size_3_2  = (1000, 1440)

    # On Mac OS, the scale might be 2 instead of 1 because of the retina display
    screen_scale = 1

    # Added paddings to images
    boarder_length = 1

    # This is used to ignore similar matches by how close they are using this offset
    sort_offset = 100

    # 20, 30 or 42
    orb_count = 30


if __name__ == "__main__":
    c1 = Config()
    c2 = Config()
    assert(id(c1) == id(c2))
    