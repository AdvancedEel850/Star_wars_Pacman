
"""This creates every pellet, or dot on the game board. This class uses encapsulation, 
as the x and y list for this class are not used anywhere else in the program. Please ignore how long the
list are, as there are many pellets."""

import arcade

class Dots:

    def __init__(self) -> None:
        self.dots = arcade.SpriteList()
        self._x_list = [40, 63, 86, 109, 132, 155, 178, 201, 224, 247, 270, 340, 363, 386, 409, 432, 455, 478, 501, 524, 547, 570, 40, 40, 40, 40, 40, 40, 40, 40, 570, 570, 570, 570, 570, 570, 570, 570, 65, 88, 111, 134, 157, 180, 203, 226, 249, 272, 295, 318, 341, 364, 387, 410, 433, 456, 479, 502, 525, 548, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 145, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 271, 271, 271, 271, 271, 271, 271, 271, 271, 271, 271, 271, 271, 340, 340, 340, 340, 340, 340, 340, 340, 340, 340, 340, 340, 340, 66, 89, 112, 205, 228, 251, 274, 335, 358, 381, 404, 544, 521, 498, 205, 205, 404, 404, 210, 233, 256, 279, 302, 325, 348, 371, 394, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 394, 394, 394, 394, 394, 394, 394, 394, 394, 394, 394, 394, 167, 190, 420, 443, 40, 63, 86, 109, 131, 154, 177, 200, 223, 246, 363, 386, 409, 432, 455, 478, 501, 524, 547, 570, 40, 40, 40, 570, 570, 570, 63, 86, 178, 201, 224, 247, 365, 388, 411, 434, 520, 543, 86, 86, 86, 520, 520, 520, 40, 63, 115, 240, 370, 495, 570, 547, 40, 63, 86, 109, 132, 155, 178, 201, 224, 247, 293, 316, 362, 385, 408, 431, 454, 477, 500, 523, 545, 568, 40, 40, 570, 570, 233, 256, 279, 302, 325, 348, 371]
        self._y_list = [736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 736, 713, 690, 667, 644, 621, 598, 575, 552, 713, 690, 667, 644, 621, 598, 575, 552, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 636, 110, 133, 156, 179, 202, 225, 271, 294, 317, 340, 363, 386, 409, 432, 455, 478, 501, 524, 547, 570, 593, 616, 662, 685, 708, 110, 133, 156, 179, 202, 225, 271, 294, 317, 340, 363, 386, 409, 432, 455, 478, 501, 524, 547, 570, 593, 616, 662, 685, 708, 662, 685, 708, 534, 511, 260, 237, 214, 191, 110, 87, 64, 41, 662, 685, 708, 534, 511, 260, 237, 214, 191, 110, 87, 64, 41, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 586, 609, 586, 609, 485, 485, 485, 485, 485, 485, 485, 485, 485, 110, 133, 156, 283, 306, 329, 352, 375, 398, 421, 445, 468, 110, 133, 156, 283, 306, 329, 352, 375, 398, 421, 445, 468, 410, 410, 410, 410, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 232, 209, 186, 232, 209, 186, 186, 186, 186, 186, 186, 186, 186, 186, 186, 186, 186, 186, 161, 136, 111, 161, 136, 111, 111, 111, 111, 111, 111, 111, 111, 111, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 64, 87, 64, 87, 335, 335, 335, 335, 335, 335, 335]

    def _setup(self):

        for i in range(0, len(self._x_list)):
            self.dot = arcade.Sprite("Images/blaster.png")
            self.dot.center_x = self._x_list[i]
            self.dot.center_y = self._y_list[i]
            self.dots.append(self.dot)

        return self.dots


#  615 255