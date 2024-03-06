def lerp(p0: float, p1: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * p0 + t * p1

def curve(vector1, vector2):
    lerpA = [0,0]
    lerpB = [0,0]
    lerpPonto = list
    for i in range(0, 11, 1):
        lerpA[0] = (lerp(vector1[0][0], vector1[0][1], i/10))
        lerpA[1] = (lerp(vector1[1][0], vector1[1][1], i/10))

        lerpB[0] = (lerp(vector2[0][0], vector2[0][1], i/10))
        lerpB[1] = (lerp(vector2[1][0], vector2[1][1], i/10))

        lerpPonto.append([lerp(lerpA[0], lerpA[1], i/10)])
        lerpPonto.append([lerp(lerpB[0], lerpB[1], i/10)])

    return lerpPonto