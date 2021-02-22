
class Button:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def check_press(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2
