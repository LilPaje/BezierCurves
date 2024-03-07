def lerp(p0: float, p1: float, t: float) -> float:
    if not 0 <= t <= 1:
        raise ValueError("Parameter t must be between 0 and 1")

    return (1 - t) * p0 + t * p1


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def lerp(self, other: "Vector2", t: float) -> "Vector2":
        if not 0 <= t <= 1:
            raise ValueError("Parameter t must be between 0 and 1")

        x = lerp(self.x, other.x, t)
        y = lerp(self.y, other.y, t)
        return Vector2(x, y)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"


class Line2:
    def __init__(self, start: Vector2, end: Vector2):
        self.start = start
        self.end = end

    def lerp(self, t: float) -> Vector2:
        return self.start.lerp(self.end, t)

    def __repr__(self):
        return f"Line2({self.start}, {self.end})"


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def lerp(self, other: "Vector3", t: float) -> "Vector3":
        if not 0 <= t <= 1:
            raise ValueError("Parameter t must be between 0 and 1")

        x = lerp(self.x, other.x, t)
        y = lerp(self.y, other.y, t)
        z = lerp(self.z, other.z, t)
        return Vector3(x, y, z)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"


class Line3:
    def __init__(self, start: Vector3, end: Vector3):
        self.start = start
        self.end = end

    def lerp(self, t: float) -> Vector3:
        return self.start.lerp(self.end, t)

    def __repr__(self):
        return f"Line3({self.start}, {self.end})"
