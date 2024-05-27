class Shoe:
    def __init__(self, brand, size, material):
        self._brand = brand
        self.size = size
        self._material = material

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("Size must be a positive number")
        self._size = size

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material
