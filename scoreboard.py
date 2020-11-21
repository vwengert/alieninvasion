import pygame.font

class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into rendered image."""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(
            score_str,
            True,
            self.text_color,
            self.settings.bg_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the highscore into rendered image."""
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score_str,
            True,
            self.text_color,
            self.settings.bg_color
        )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.high_score_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check for new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)