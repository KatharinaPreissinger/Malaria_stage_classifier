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

def draw_cont(img, contour, name, directory):
    """Draws contours and returns image
    
    Parameters
    ----------
    img : ndarray
        N dimensional array with type int that contains the image to process
    contour : contours
        Contours that contains list of coordinates of detected contours
    name : str
        The name of the returned image
    directory : str
        The directory where the image is saved
        
    Returns
    -------
    image
        an image that contains the selected contours
    
    """
    new_img = np.zeros((img.shape[0], img.shape[1],3), np.uint8)*255
    new_img = cv2.drawContours(new_img, contour, -1, (255,0,0), thickness=1)
    fig, (ax1) = plt.subplots(1,figsize=(5,5))
    plt.xticks([]),plt.yticks([])
    ax1.imshow(new_img)
    plt.close()
    return new_img

def filter_cont(contour, index):
    """Selects contours by index
    
    Parameters
    ----------
    contour : contours
        Contours that contains list of coordinates of detected contours
    index : ndarray
        1 dimensional array with type int that contains index of selected contours
        
    Returns
    -------
    array
        an array with type contours that contains selected contours
    
    """
    cnt = []
    for ind in index:
            cnt.append(contour[ind])
    return cnt

def filter_df(ind, c_length, c_area, c_ratio):
    """Writes new DataFrame with selected data
    
    Parameters
    ----------
    ind : ndarray
        1 dimensional array with type int that contains the index of data selected from other DataFrame
    c_length : ndarray
        1 dimensional array with type float that contains the length of selected contours
    c_area : ndarray
        1 dimensional array with type float that contains the area of selected contour
    c_ratio : ndarray
        1 dimensional array with type float that contains the ratio of contour length and area
        
    Returns
    -------
    DataFrame, array, array, array
        DataFrame (df) : a DataFrame that contains properties of selected contours
        array (length) : an array with type float that contains the length of each selected contour
        array (area) : an array with type float that contains the area of each selected contour
        array (ratio) : an array with type float that contains the length/area ratio of each selected contour
    
    """
    length = []
    area = []
    ratio = []
    i = 0
    for i in range(0, len(ind)):
        length.append(c_length[ind[i]])
        area.append(c_area[ind[i]])
        ratio.append(c_ratio[ind[i]])
        i += 1
    df = write_df(length, area, ratio)
    return df, length, area, ratio

def filter_values(df, column, min_val, max_val):
    """Filters column in DataFrame by values
    
    Parameters
    ----------
    df : DataFrame
        DataFrame that contains contour properties
    column : string
        The name of the column
    min_val : float
        The minimum value of the data
    max_val : float
        The maximum value of the data
        
    Returns
    -------
    array
        an array with type int that describes values, which fulfill conditions
    
    """
    df_new = df[column].between(min_val, max_val)
    ind = []
    i = 0
    for index in df_new:
        if index == True:
            ind.append(i)
        i += 1
    return ind

def find_cont(img):
    """Detects contours and draws them in RGB image
    
    Parameters
    ----------
    img : ndarray
        N dimensional array with type int that contains the image to process
    
    Returns
    -------
    image, contours
        image: an image that contains the detected contours
        contours: a list of coordinates of contours that were detected in the image
    
    """
    contour, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    canvas = np.ones((img.shape[0], img.shape[1],3), np.uint8)*255
    canvas = cv2.drawContours(canvas, contour, -1, (255,0,0), thickness=1)
    fig, (ax1) = plt.subplots(1,figsize=(5,5))
    plt.xticks([]),plt.yticks([])
    ax1.imshow(canvas)
    plt.close()
    return canvas, contour

def find_contour_img(img, img_thr, directory):
    """Finds contours, filters them by manually chosen values and returns filtered contours
    
    Parameters
    ----------
    img : image
        N dimensional array with type int that contains the original image
    img_thr : image
        N dimensional array with type int that contains the thresholded image
    directory : str
        The directory where the image is saved
        
    Returns
    -------
    image, array
        image (img_ab) : an array with type int that contains filtered contours
        array (c_a) : an array with type contours that contains selected contours
    
    """
    # Finds contours in image
    cnt_img, cnt = find_cont(img_thr)

    # Calculates properties of contours and writes to pandas DataFrame
    c_length, c_area = get_contarea(cnt)
    c_ratio = al_ratio(c_length, c_area)  
    df = write_df(c_length, c_area, c_ratio)

    # Filters data for selected values
    ind_c = filter_values(df, "length/area", 0, 0.5)
    df_cr, length_cr, area_cr, ratio_cr = filter_df(ind_c, c_length, c_area, c_ratio)
    c_cr = filter_cont(cnt, ind_c)
    ind_l = filter_values(df_cr, "contour length", 1, 160000)
    df_l, length_l, area_l, ratio_l = filter_df(ind_l, length_cr, area_cr, ratio_cr)
    c_l = filter_cont(c_cr, ind_l)
    ind_a = filter_values(df_l, "contour area", 500, 1000000)
    df_a, length_a, area_a, ratio_a = filter_df(ind_a, length_l, area_l, ratio_l)
    c_a = filter_cont(c_l, ind_a)
    img_a = draw_cont(img, c_a, 'areas', directory)

    return c_a

def find_extrema(img):
    """Finds index of max and min value in image
    
    Parameters
    ----------
    img : image
        N dimensional array with type float that contains the z_values of the data
        
    Returns
    -------
    int, int
        int (z_min) : min value in array
        int (z_max) : max value in array
    
    """   
    ind_min = np.argmin(img) # index of flattened array
    ind_max = np.argmax(img)
    img_fl = img.flatten()
    z_min = img_fl[ind_min]
    z_max = img_fl[ind_max]
    return z_min, z_max

def get_contarea(contour):
    """Determines area that is surrounded by contour and its length
    
    Parameters
    ----------
    contour : contours
        Contours that contains list of coordinates of detected contours
        
    Returns
    -------
    array, array
        array (length) : an array with type float that contains length of contours
        array (area) : an array with type float that contains area of contours
    
    """
    length = []
    area = []
    for line in contour:
        length.append(len(line))
        area.append(cv2.contourArea(line))
    return length, area

def normalise_zvalues(img):
    """Returns normalised grayscale image
    
    Parameters
    ----------
    img : image
        N dimensional array with type float that contains the z_values of the data

    Returns
    -------
    array
        an array with type int that contains grayscale values of the image
        
    """       
    # Calculates grayscale image from height trace values
    img_min, img_max = find_extrema(img)
    imggr = np.zeros((img.shape[0], img.shape[1]))
    i = 0
    for line in img:
        j = 0
        for h in line:
            grayv = round((h+abs(img_min))/(img_max-img_min)*255)
            imggr[i][j] = grayv
            j += 1
        i += 1
    return imggr

def RGB_2_bin(img, value):
    """Converts RGB image to grayscale image
    
    Parameters
    ----------
    img : image
    
    value : int
        The value, which determines if the point is True or False
    
    Returns
    -------
    image
        a binary image
        
    """    
    img_new = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8) 
    x = 0
    for x in range(0, img.shape[0]):
        y = 0
        for y in range(0, img.shape[1]):
            if img[x][y] == value:
                img_new[x][y] = True
            else:
                img_new[x][y] = False
            y += 1
        x += 1
    return img_new

def write_df(c_length, c_area, ratio):
    """Writes data in pandas data frame
    
    Parameters
    ----------
    c_length : ndarray
        1 dimensional array with type float that contains list of contour lengths
    c_area : ndarray
        1 dimensional array with type float that contains list of contour areas
    ratio : ndarray
        1 dimensional array with type float that contains ratio of contour length to area
        
    Returns
    -------
    DataFrame
        df : a DataFrame that contains contour length, area and ratio length/area
    
    """
    df = pd.DataFrame({"contour length": c_length, "contour area": c_area, "length/area": ratio})
    return df
