def fed_power(x,y):
    """
    Returns x raised to the power of y.

    Parameters
    ----------
    x : int
        base
    y : int
        exponent

    Returns
    -------
    out : int
        the result of x to the power of y
    """

    return x**y

def al_ratio(contour_length, contour_area):
    """Determines ratio of contour length and area
    
    Parameters
    ----------
    contour_length : ndarray
        1 dimensional array with type float that contains length of contours        
    contour_area : ndarray
        1 dimensional array with type float that contains area of contours
    Returns
    -------
    array
        ratio : an array with type float that contains ratio of contour length to area
    
    """
    ratio = []
    i = 0
    for a in contour_area:
        if a == 0:
            ratio.append(0)
        else:
            ratio.append(contour_length[i]/a)
        i += 1
    return ratio

class class_power():
    """A class that performs the power function."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def power(self):
        try:
            return self.x**self.y
        except:
            print('Something went wrong. Make sure x and y are both numbers')
