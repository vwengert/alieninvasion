class Settings():
    """A Class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Bildschirmeinstellungen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fullscreen = False
        self.ship_limit = 3

        # Geschosseinstellungen
        self.bullet_width = 2
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.fleet_direction = 1
        self.ship_speed = 1.0
        self.alien_speed = 0.4
        self.bullet_speed = 1.5
        self.alien_points = 50

        self.score_scale = 10

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points += self.score_scale
        self.score_scale *= 2
