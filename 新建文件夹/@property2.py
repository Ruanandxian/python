class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('defult')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, m):
        self._height = m

    @property
    def resolution(self):
        return self._width + self._height
