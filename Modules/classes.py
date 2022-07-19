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
        new_dir : str
           The directory and name of the new folder

        """
        new_dir = directory[0] + '/' + name
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        return new_dir
    
class contAFMimg(AFMimg):
    """A class which inherits from AFMimg and contains the contour and the rectangles covering the 
    objects in the image
    
    Attributes
    ----------    
    rect_del : ndarray
        1 dimensional array with type rectangle that contains rectangles around contours
    rect2_del : ndarray
        1 dimensional array with type int, rectangle that contains rectangles around clicked coordinates
    rect_exp : ndarray
        1 dimensional array with type rectangle that contains the not selected expanded rectangles
    cnt_all : ndarray
        1 dimensional array with type contours that were not selected manually
    cnt_del : ndarray
        1 dimensional array with type contours that contains all not selected contours in the loop
    img_cnt : image
        N dimensional array with type int that contains all not selected contours
    img_gr : ndarray
        N dimensional array with type float that contains a greyscale image of the original image
    img_rgb : ndarray
        N dimensional array with type float that contains img_gr as rgb image with detected contours
    coord : ndarray
        N dimensional array with type float that contains the coordinates of points inside manually
        selected rectangles/contours
    cdrawn : ndarray
        1 dimensional array with type int, int, float, float that contains the index of a rectangle with
        corresponding contour, the x- and y-coordinate of the contour
        
    """
    
    def __init__(self, xvalues, yvalues, zvalues, filename, directory, propAFMimg,
                 rect_del, rect2_del, rect_exp, cnt_all, cnt_del, img_cnt, img_gr, img_rgb, coord, cdrawn):
        """
        Parameters
        ----------
        rect_del : ndarray
            1 dimensional array with type rectangle that contains rectangles around contours
        rect2_del : ndarray
            1 dimensional array with type int, rectangle that contains rectangles around clicked coordinates
        rect_exp : ndarray
            1 dimensional array with type rectangle that contains the not selected expanded rectangles
        cnt_all : ndarray
            1 dimensional array with type contours that were not selected manually
        cnt_del : ndarray
            1 dimensional array with type contours that contains all not selected contours in the loop
        img_cnt : image
            N dimensional array with type int that contains all not selected contours
        img_gr : ndarray
            N dimensional array with type float that contains a greyscale image of the original image
        img_rgb : ndarray
            N dimensional array with type float that contains img_gr as rgb image with detected contours
        coord : ndarray
            N dimensional array with type float that contains the coordinates of points inside manually
            selected rectangles/contours
        cdrawn : ndarray
            1 dimensional array with type int, int, float, float that contains the index of a rectangle with
            corresponding contour, the x- and y-coordinate of the contour
            
        """
        super().__init__(xvalues, yvalues, zvalues, filename, directory)
        self.propAFMimg = propAFMimg
        self.rect_del = rect_del
        self.rect2_del = rect2_del
        self.rect_exp = rect_exp
        self.cnt_all = cnt_all
        self.cnt_del = cnt_del
        self.img_cnt = img_cnt
        self.img_gr = img_gr
        self.img_rgb = img_rgb
        self.coord = coord
        self.cdrawn = cdrawn    
        
class propAFMimg(AFMimg):
    """A class which inherits from AFMimg and contains size, threshold value and the expansion factor of the rectangles covering the objects in the image
    
    Attributes
    ----------    
    imgh : float
        The height of the image in µm
    imgw : float
        The width of the image in µm
    imgrh : int
        The resolution of the yvalues
    imgrw : int
        The resolution of the xvalues
    thr : int
        Manually chosen threshold value for grayscale images
    
    """
    def __init__(self, xvalues, yvalues, zvalues, filename, directory, imgh, imgw, imgrh, imgrw, thr):
        """
        Parameters
        ---------
        imgh : float
            The height of the image in µm
        imgw : float
            The width of the image in µm
        imgrh : int
            The resolution of the yvalues
        imgrw : int
            The resolution of the xvalues
        thr : int
            Manually chosen threshold value for grayscale images
        thr_arr : ndarray
            1 dimensional array with type int that contains all manually selected threshold values
        smin : float
            The minimum size of a rectangle
        smax : float
            The maximum size of a rectangle
    
        """
        super().__init__(xvalues, yvalues, zvalues, filename, directory)
        self.imgh = imgh
        self.imgw = imgw
        self.imgrh = imgrh
        self.imgrw = imgrw
        self.thr = thr
                
class LMimg():
    """A class that contains the x-, y-, z-values, filename and directory of the raw LM file
    
    Attributes
    ----------
    orig : ndarray
        N dimensional array with type int that contains the colour values of the LM image
    values : ndarray
        N dimensional array with type int that contains the greyscale values of the LM image
    val_enh : ndarray
        N dimensional array with type int that contains the enhanced LM image
    filename : str
        String that contains the name of the .txt file
    directory : str
        String that contains the directory of the .txt file
        
    """
    def __init__(self, orig, values, val_enh, filename, directory):
        """
        Parameters
        ----------
        orig : ndarray
            N dimensional array with type int that contains the colour values of the LM image
        values : ndarray
            N dimensional array with type int that contains the greyscale values of the LM image
        val_enh : ndarray
            N dimensional array with type int that contains the enhanced LM image
        filename : str
            String that contains the name of the .txt file
        directory : str
            String that contains the directory of the .txt file
            
        """
        self.orig = orig
        self.values = values
        self.val_enh = val_enh
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
        new_dir : str
           The directory and name of the new folder

        """
        new_dir = directory[0] + '/' + name
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        return new_dir

class contLMimg(LMimg):
    """A class which inherits from LMimg and contains the contour and the rectangles covering the 
    objects in the image
    
    Attributes
    ----------    
    rect_del : ndarray
        1 dimensional array with type rectangle that contains rectangles around contours
    rect2_del : ndarray
        1 dimensional array with type int, rectangle that contains rectangles around clicked coordinates
    rect_exp : ndarray
        1 dimensional array with type rectangle that contains the not selected expanded rectangles
    cnt_all : ndarray
        1 dimensional array with type contours that were not selected manually
    cnt_del : ndarray
        1 dimensional array with type contours that contains all not selected contours in the loop
    img_cnt : image
        N dimensional array with type int that contains all not selected contours
    img_gr : ndarray
        N dimensional array with type float that contains a greyscale image of the original image
    img_rgb : ndarray
        N dimensional array with type float that contains img_gr as rgb image with detected contours
    coord : ndarray
        N dimensional array with type float that contains the coordinates of points inside manually
        selected rectangles/contours
    cdrawn : ndarray
        1 dimensional array with type int, int, float, float that contains the index of a rectangle with
        corresponding contour, the x- and y-coordinate of the contour

    """
    
    def __init__(self, orig, values, val_enh, filename, directory, propLMimg,
                 rect_del, rect2_del, rect_exp, cnt_all, cnt_del, img_cnt, img_gr, img_rgb, coord, cdrawn):
        """
        Parameters
        ----------
        rect_del : ndarray
            1 dimensional array with type rectangle that contains rectangles around contours
        rect2_del : ndarray
            1 dimensional array with type int, rectangle that contains rectangles around clicked coordinates
        rect_exp : ndarray
            1 dimensional array with type rectangle that contains the not selected expanded rectangles
        cnt_all : ndarray
            1 dimensional array with type contours that were not selected manually
        cnt_del : ndarray
            1 dimensional array with type contours that contains all not selected contours in the loop
        img_cnt : image
            N dimensional array with type int that contains all not selected contours
        img_gr : ndarray
            N dimensional array with type float that contains a greyscale image of the original image
        img_rgb : ndarray
            N dimensional array with type float that contains img_gr as rgb image with detected contours
        coord : ndarray
            N dimensional array with type float that contains the coordinates of points inside manually
            selected rectangles/contours
        cdrawn : ndarray
            1 dimensional array with type int, int, float, float that contains the index of a rectangle with
            corresponding contour, the x- and y-coordinate of the contour
            
        """
        super().__init__(orig, values, val_enh, filename, directory)
        self.propLMimg = propLMimg
        self.rect_del = rect_del
        self.rect2_del = rect2_del
        self.rect_exp = rect_exp
        self.cnt_all = cnt_all
        self.cnt_del = cnt_del
        self.img_cnt = img_cnt
        self.img_gr = img_gr
        self.img_rgb = img_rgb
        self.coord = coord
        
class propLMimg(LMimg):
    """A class which inherits from LMimg and contains size, threshold value of the LM image
    
    Attributes
    ----------    
    imgh : float
        The height of the image in µm
    imgw : float
        The width of the image in µm
    imgrh : int
        The resolution of the yvalues
    imgrw : int
        The resolution of the xvalues
    thr : int
        Manually chosen threshold value for grayscale images

    """
    def __init__(self, orig, values, val_enh, filename, directory, imgh, imgw, imgrh, imgrw, thr):
        """
        Parameters
        ---------
        imgh : float
            The height of the image in µm
        imgw : float
            The width of the image in µm
        imgrh : int
            The resolution of the yvalues
        imgrw : int
            The resolution of the xvalues
        thr : int
            Manually chosen threshold value for grayscale images
    
        """
        super().__init__(orig, values, val_enh, filename, directory)
        self.imgh = imgh
        self.imgw = imgw
        self.imgrh = imgrh
        self.imgrw = imgrw
        self.thr = thr
        
class Cell():
    """A class that contains the geometric properties of a cell
    
    Attributes
    ----------
    img : ndarray
        N x N x N dimensional array that contains the extracted cell images
    gfimg : ndarray
        N x N x N dimensional array that contains the gaussian filtered images
    zcut2: ndarray
        N x 2 dimensional array with type float that contains two extracted cuts
    label: ndarray
        N dimensional array with type str that contains the labels of the images
    cntCell : ndarray
        N x N X (1, 1) dimensional array with type (int, int) that contains the contour of the cells
    centre : ndarray
        N x (1, 1) dimensional array with type (float, float) that contains the centre of the cell
    mcentre : ndarray
        N x (1, 1) dimensional array with type (float, float) that contains the centre of mass of the cell
    radius : ndarray
        N dimensional array with type float that contains the radius of the detected circle
    rectChange : ndarray
        N x (1, 1, 1, 1, 1, 1, 1) dimensional array with type float that contains the bounding coordinates of
        the bounding rectangle around a cell
    offset : ndarray
        N x (1, 1) dimensional array with type float that contains the x and y offset of the cropped image
    
    """
    def __init__(self, img, gfimg, zcut2, label, cntCell, centre, mcentre, radius, rectChange, offset):
        self.img = img
        self.gfimg = gfimg
        self.zcut2 = zcut2
        self.label = label
        self.cntCell = cntCell
        self.centre = centre
        self.mcentre = mcentre
        self.radius = radius
        self.rectChange = rectChange
        self.offset = offset
        
    def calc_cellCnt(self, circle_found, img_hc, directory):
        """Calculates the coordinates of the cell contour
        
        Parameters
        ----------
        circle_found : ndarray
            N x (1, 1, 1) dimensional array with type float that contains the centre and the
            radius of the detected circle
        img_hc : ndarray
            N x N dimensional array that contains the normalised zvalues
            
        """
        i = 0
        for circ in circle_found:
            # Calculates the cell contour
            cntOCell = []
            # Calculates coordinates of cell contour
            xc = circ[0]
            yc = circ[1]
            rad = circ[2]
            # Cuts the cell out of the original image img_hc
            x0 = xc - rad * 1
            y0 = yc - rad * 1
            x1 = xc + rad * 1
            y1 = yc + rad * 1
            self.offset.append((x0, y0))
            self.radius.append(rad)
            if len(np.asarray(img_hc).shape) > 2:
                img_hc = np.asarray(cv2.cvtColor(np.asarray(img_hc), cv2.COLOR_RGB2GRAY))
            else:
                img_hc = np.asarray(img_hc)
            img_crop = np.asarray(img_hc)[int(y0):int(y0+(y1-y0)), int(x0):int(x0+(x1-x0))]
            self.img.append(img_crop)
            # enhances cropped image
            from PIL import Image, ImageEnhance
            img_cPIL = Image.fromarray(np.uint8((img_crop)*255))
            enh = ImageEnhance.Contrast(img_cPIL)
            img_enh = enh.enhance(3)
            # determines Gaussian filtered image
            gf = scipy.ndimage.filters.gaussian_filter(np.asarray(img_enh), (1,1), mode='constant')
            self.gfimg.append(gf)
            # finds coordinates of circle contour
            img_circ = np.zeros((img_crop.shape[0], img_crop.shape[1]), np.uint8)
            cv2.circle(img_circ,(xc-x0,yc-y0),rad,255)
            points = np.transpose(np.where(img_circ==255))
            # arranges coordinates in the right order
            arr_clock = []
            arr_cclock = []
            num = 0
            for num in range(0, len(points)):
                if num == 0:
                    continue
                    #arr_clock.append(points[num])
                elif num == 1:
                    arr_cclock.append(points[num])
                    y = points[num][1]
                else:
                    if abs(arr_cclock[-1][1] - points[num][1]) > 10:
                        arr_clock.append(points[num])
                    else:
                        arr_cclock.append(points[num])
            try:
                points_new = np.concatenate((arr_clock, arr_cclock[::-1]))
            except ValueError:
                continue
            #points_new = arr_cclock
            coord = []
            for p in points_new:
                coord.append([p[1], p[0]])
            cntOCell.append((np.asarray(coord).astype(np.int32)))

            # Draws contour on empty image to get closed contour
            new_img = np.zeros((img_crop.shape[0], img_crop.shape[1]), np.uint8)*255
            new_img = cv2.drawContours(new_img, cntOCell, -1, (255,0,0), thickness=1)

            cntCell = []
            points = np.transpose(np.where(new_img==255))
            # arranges coordinates in the right order
            arr_clock = []
            arr_cclock = []
            num = 0
            for num in range(0, len(points)):
                if num == 0:
                    continue
                    #arr_clock.append(points[num])
                elif num == 1:
                    arr_cclock.append(points[num])
                    y = points[num][1]
                else:
                    if abs(arr_cclock[-1][1] - points[num][1]) > 10:
                        arr_clock.append(points[num])
                    else:
                        arr_cclock.append(points[num])           
            points_new = np.concatenate((arr_clock, arr_cclock[::-1]))
            coord = []
            for p in points_new:
                coord.append([p[1], p[0]])
            self.cntCell.append((np.asarray(coord).astype(np.int32)))
            i += 1
        
    def calc_geomP(self):
        """Calculates the coordinates inside the cell, its centre, and its centre of mass
        
        """
        for i in range(0, len(self.cntCell)):
            coord_in = find_coordborder([self.cntCell[i]], self.img[i])
            # Determines the z-value of all points inside a contour
            pin = points_incell(coord_in, self.img[i])
            # Determines the geometric centre of a contour (cell)
            scentre, all_coord = geometric_centre(coord_in)
            # Determines the centre of mass inside a rectangle weighted by the corresponding z-values.
            smcentre = centre_of_mass(all_coord, self.gfimg[i])
            self.centre.append(scentre)
            self.mcentre.append(smcentre)
        
    def extract_cut(self, circle_found, imgh, imgw, imgrh, imgrw):
        """Extracts cut from cell image
        
        Parameters
        ----------
        circle_found : ndarray
            N x (1, 1, 1) dimensional array with type float that contains the centre and the
            radius of the detected circle
        imgh : float
            The height of the image in µm
        imgw : float
            The width of the image in µm
        imgrh : int
            The resolution of the yvalues
        imgrw : int
            The resolution of the xvalues
        
        """
        for i in range(0, len(self.mcentre)):
            xrs, yrs, xls, yls, xprs, yprs, xpls, ypls = calc_straight(circle_found, self.mcentre[i], self.centre[i],
                                                                       imgh, imgrh, imgw, imgrw)

            # Finds contour points on the parallel straight
            crmatch = match_coord(xrs, yrs, self.cntCell[i])
            clmatch = match_coord(xls, yls, self.cntCell[i])
            # Finds contour points on the perpendicular straight
            cprmatch = match_coord(xprs, yprs, self.cntCell[i])
            cplmatch = match_coord(xpls, ypls, self.cntCell[i])
            csort = sort_coord(crmatch, clmatch)
            cpsort = sort_coord(cprmatch, cplmatch) 

            # Calculates x-, y- and z-values of both straights
            cxpara, cypara, zipar, cxp, cyp, zp, z2cs = calc_asymcut(self.img[i], csort, 'para', imgh, imgrh, imgw,
                                                                     imgrw, self.centre[i])
            cxp, cyp, zp, cxperp, cyperp, ziperp, z2 = calc_asymcut(self.img[i], cpsort, 'perp', imgh, imgrh, imgw,
                                                                    imgrw, self.centre[i])

            for i in range(0, len(cxperp)):
                z2cs[i][1] = ziperp[i]
            self.zcut2.append(z2cs)
    
class ToolTip(object):
    """Class that defines a window upon hovering mouse event
    
    """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        """Shows a window, when hovering above an icon
        
        """
        self.tooltipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1) # window without border and no normal means of closing
        tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx(), self.widget.winfo_rooty()))
        label = tk.Label(tw, text = self.text, background = "#ffffe0", relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        """Hides a window, when previously shown by hovering above an icon
        
        """
        tw = self.tooltipwindow
        try:
            tw.destroy()
        except AttributeError:
            self.tooltipwindow = None
        self.tooltipwindow = None
