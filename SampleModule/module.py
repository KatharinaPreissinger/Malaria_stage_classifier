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

class AFMimg():
    """A class that contains the x-, y-, z-values, filename and directory of the raw AFM file
    
    Attributes
    ----------
    xvalues : ndarray
        N dimensional array with type float that contains the x-values of the igor pro height trace data
    yvalues : ndarray
        N dimensional array with type float that contains the y-values of the igor pro height trace data
    zvalues : ndarray
        N dimensional array with type float that contains the z-values of the igor pro height trace data
    filename : str
        String that contains the name of the .txt file
    directory : str
        String that contains the directory of the .txt file
        
    """
    def __init__(self, xvalues, yvalues, zvalues, filename, directory):
        """
        Parameters
        ----------
        xvalues : ndarray
            N dimensional array with type float that contains the x-values of the igor pro height trace data
        yvalues : ndarray
            N dimensional array with type float that contains the y-values of the igor pro height trace data
        zvalues : ndarray
            N dimensional array with type float that contains the z-values of the igor pro height trace data
        filename : str
            String that contains the name of the .txt file
        directory : str
            String that contains the directory of the .txt file
            
        """
        self.xvalues = xvalues
        self.yvalues = yvalues
        self.zvalues = zvalues
        self.filename = filename
        self.directory = [directory]

    def set_directory(self, new_dir):
        """Adds a new directory to the class
        
        Parameters
        ----------
        new_dir : str
           The new directory
           
        """
        self.directory.append(new_dir)
        
    def create_directory(self, directory, name):
        """Creates a new directory
      
        Parameters
        ----------
        directory : str
           The directory of the new folder
        name : str
           The name of the new folder
    
        Returns
        -------
        str
           The directory + name of the new folder
        """
        new_dir = directory[0] + '/' + name
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        return new_dir

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
