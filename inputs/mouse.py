class Mouse():
    
    def __init__(self, button, start_pos, direction):
        self.button = button
        self.start_pos = start_pos
        self.direction = direction

    def reset(self):
        self.button = None
        self.start_pos = None
        self.direction = [0, 0]