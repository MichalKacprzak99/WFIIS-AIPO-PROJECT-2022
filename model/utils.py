def rectangle_overlap(r1, r2):
    # (startX, startY, endX, endY)
    # if rectangle has area 0, no overlap
    if r1[0] == r1[2] or r1[3] == r1[1] or r2[2] == r2[0] or r2[3] == r2[1]:
        return False

    # If one rectangle is on left side of other
    if r1[0] > r2[2] or r2[0] > r1[2]:
        return False

    # If one rectangle is above other
    if r1[1] > r2[3] or r2[1] > r1[3]:
        return False

    return True


def expand_rectangle_whit_rect(to_be_expanded, rect):
    ret = (min(to_be_expanded[0], rect[0]),
           min(to_be_expanded[1], rect[1]),
           max(to_be_expanded[2], rect[2]),
           max(to_be_expanded[3], rect[3]))
    return ret


def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except:
            return None
    return dct
