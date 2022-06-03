import pygame.font
 
class Button:
 
    def __init__(self, ai_game, msg):
        """I初始化子弹状态"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #设置按钮的尺寸和特性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #构建按钮的rect对象并将其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #按钮对象只需要准备一次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将消息转换为渲染图像，并将文本置于按钮中央"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #绘制空白按钮，然后绘制消息
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)