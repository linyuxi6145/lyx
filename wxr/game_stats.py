class GameStats:
    """跟踪外星入侵的统计数据"""
    
    def __init__(self, ai_game):
        """初始化统计数据"""
        self.settings = ai_game.settings
        self.reset_stats()

        #处于活跃状态时开始游戏
        self.game_active = False

        # 高分不应重置
        self.high_score = 0
        
    def reset_stats(self):
        """初始化游戏期间可能更改的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1