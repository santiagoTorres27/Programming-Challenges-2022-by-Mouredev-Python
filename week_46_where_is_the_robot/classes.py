class Robot:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._face_direction = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def face_direction(self):
        return self._face_direction

    @face_direction.setter
    def face_direction(self, value):
        self._face_direction = value

    def rotate(self):
        self.face_direction = self.face_direction + 90
        if self.face_direction >= 360:
            self._face_direction = 0

    def move(self, value):
        if self.face_direction == 0:
            self.y += value
        elif self.face_direction == 90:
            self.x -= value
        elif self.face_direction == 180:
            self._y -= value
        elif self.face_direction == 270:
            self._x += value
        self.rotate()

    def __str__(self):
        return f"X: {self._x}, Y: {self._y}"
