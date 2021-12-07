import arcade

class Dots:

    def __init__(self) -> None:
        self.dots = arcade.SpriteList()
        self._x_list = [40, 63, 86, 109, 132, 155, 178, 201, 224, 247, 270, 340, 363, 386, 409, 432, 455, 478, 501, 524, 547, 570, 40, 40, 40, 40, 40, 40, 40, 40, 570, 570, 570, 570, 570, 570, 570, 570, 65, 88, 111, 134, 157, 180, 203, 226, 249, 272, 295, 318, 341, 364, 387, 410, 433, 456, 479, 502, 525, 548, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145]
        self._y_list = [736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 713, 690, 667, 644, 621, 598, 575, 552, 713, 690, 667, 644, 621, 598, 575, 552, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 110, 133, 156, 179, 202, 225, 248, 271, 294, 317, 340, 363, 386, 409, 432, 455, 478, 501, 524, 547, 570, 593, 616, 662, 685, 708]

    def _setup(self):

        for i in range(0, len(self._x_list)):
            self.dot = arcade.Sprite("Images/blaster.png")
            self.dot.center_x = self._x_list[i]
            self.dot.center_y = self._y_list[i]
            self.dots.append(self.dot)

        return self.dots


        # 340 570
        # 560 746
        #  145 713 to 145 110