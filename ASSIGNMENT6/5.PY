class Image:
    def __init__(self,image_width,image_height,color_code):
        self.__image_width=image_width
        self.__image_height=image_height
        self.__color_code=color_code
    @property
    def image_width(self):
        return self.__image_width
    @property
    def image_height(self):
        return self.__image_height
    @property
    def color_code(self):
        return self.__color_code
    @image_width.setter
    def image_width(self,image_width):
        self.__image_width=image_width
    @image_height.setter
    def image_height(self,image_height):
        self.__image_height=image_height
    @image_width.setter
    def color_code(self,color_code):
        self.__color_code=color_code
    def __str__(self):
        return f"Image Width{self.image_width} and Image Height{self.image_height}and Colour code{self.color_code}"
i=Image(400,589,"red")
i.image_width=456
i.image_height=487
i.colour_code='red'
print(i.__str__())




        
        