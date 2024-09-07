class Polygon:
    def __init__(self, sides):
        self.sisi = sides

    def perimeter(self):
        perimeter = sum(self.sisi)

        return perimeter


class Quadrilateral(Polygon):
    def info(self):
        print("Hello, ini adalah Quadrilateral.")


class Pentagon(Polygon):
    def info(self):
        print("Hello, ini adalah Pentagon.")


quad_obj = Quadrilateral([3, 6, 7, 9])
penta_obj = Pentagon([2, 4, 6, 8, 10])

quad_perimeter = quad_obj.perimeter()
penta_perimeter = penta_obj.perimeter()

# Keliling objek
print(f"Keliling segiempat adalah {quad_perimeter}")
quad_obj.info()
print(f"Keliling Pentagon adalah {penta_perimeter}")
penta_obj.info()
