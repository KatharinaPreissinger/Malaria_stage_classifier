def calc_asymcut(values, coord, ori, imgh, imgrh, imgw, imgrw, centre):
    """Determines the cross-section along the most asymmetric cut through the z_values and shifts
    the origin to the geometric centre
    Parameters
    ----------
    values : ndarray
        N dimensional array with type float that contains the grayscale values of the original image
    coord : ndarray
        1 dimensional array with type (float, float), (float, float) that contains
        the x- and y-coordinate left of a point and the x- and y-coordinate right of a point
    ori : str
        Orientation of the straight: parallel, perpendicular
    imgh : int
        The height of the image
    imgrh : int
        The resolution of the image in y-direction
    imgw : int
        The width of the image
    imgrw : int
        The resolution of the imag in x-direction
    centre : ndarray
        N dimensional array with type float, float that contains the x- and y-coordinates of the geometric
        cetnre
        
    Returns
    -------
    cxpara : ndarray
        1 dimensional array with type float that contains the x-coordinates of the asymmetric cut
    cypara : ndarray
        1 dimensional array with type float that contains the y-coordinates of the asymmetric cut
    zpara : ndarray
        1 dimensional array with type float that contains the z-coordinates of the asymmetric cut
    cxperp : ndarray
        1 dimensional array with type float that contains the x-coordinates of the perpendicular
        asymmetric cut
    cyperp : ndarray
        1 dimensional array with type float that contains the y-coordinates of the perpendicular
        asymmetric cut
    ziperp : ndarray
        1 dimensional array with type float that contains the z-coordinates of the perpendicular
        asymmetric cut
    zipar : ndarray
        1 dimensional array with type float that contains the z-coordinates of the asymmetric cut
    cut : ndarray
        1 dimensional array with type float that contains the points of the asymmetric cut in µm
    pcut : ndarray
        1 dimensional array with type float that contains the points of the perpendicular asymmetric
        cut in µm
    x2cs : ndarray
        2 dimensional array with type float that contains the x-coordinates of the asymmetric parallel
        and perpendicular cut
    y2cs : ndarray
        2 dimensional array with type float that contains the y-coordinates of the asymmetric parallel
        and perpendicular cut
    z2cs : ndarray
        2 dimensional array with type float that contains the z-coordinates of the asymmetric parallel
        and perpendicular cut
    cut2 : ndarray
        2 dimensional array with type float that contains the points of the parallel and perpendicular
        asymmetric
        cut in µm
    """
    cxpara = []
    cypara = []
    zipar = []
    x2cs = []
    y2cs = []
    z2cs = []
    cxperp = []
    cyperp = []
    ziperp = []
    cut = []
    cut2 = []
    pcut = []
    # Determines the cross-section of the cut
    xparan = []
    yparan = []
    i = 0
    for c in coord:
        xs = c[1][0]
        xe = c[0][0]
        ys = c[1][1]
        ye = c[0][1]
        # Calculates the length of the cut
        cut_num = int(math.sqrt(math.pow((xe - xs), 2) + math.pow((ye - ys), 2)))
        cut_num = 50
        # Makes points with distance of approximately 1 pixel
        x,y = np.linspace(xs, xe, cut_num), np.linspace(ys, ye, cut_num)
        if ori == 'para':
            cxpara.append(x)
            cypara.append(y)
            map_coord = scipy.ndimage.map_coordinates(values, np.vstack((y, x)))
            zipar.append(map_coord)
            x2cs.append([x, 0])
            y2cs.append([y, 0])
            z2cs.append([map_coord, 0])
        else:
            cxperp.append(x)
            cyperp.append(y)
            map_coord = scipy.ndimage.map_coordinates(values, np.vstack((y, x)))
            ziperp.append(map_coord)

        # Shifts the origin to the geometric centre
        xnorm = np.linspace(xs-centre[i][0], xe-centre[i][0], cut_num)
        ynorm = np.linspace(ys-centre[i][1], ye-centre[i][1], cut_num)
        xparan.append(xnorm)
        yparan.append(ynorm)
        # Calculates the distance of the start and end point to the centre in pixel and the length of
        # the cut through the object in µm
        cut_arr = []
        if len(xnorm) == 0:
            continue
        else:
            distance_lcentre = math.sqrt((xnorm[0] * imgw / imgrw) ** 2
                                         + (ynorm[0] * imgh / imgrh) ** 2)
            distance_rcentre = math.sqrt((xnorm[-1] * imgw / imgrw) ** 2
                                         + (ynorm[-1] * imgh / imgrh) ** 2)                
            # Calculates points of cut in µm
            cut_arr = np.linspace(-distance_lcentre, distance_rcentre, cut_num)
            if ori == 'para':
                cut.append(cut_arr)
                cut2.append([cut_arr, 0])
            else:
                pcut.append(cut_arr)
        i += 1
    return cxpara, cypara, zipar, cxperp, cyperp, ziperp, z2cs

def calc_straight(circle_found, mcentre, centre, imgh, imgrh, imgw, imrw):
    """Determines the straight betweeen the centre of mass and the geometric centre and the values
    of the points on the straight within a range of 50 pixels (much larger than cell diameter)
    around the geometric centre.
    Calculates the perpendicular straight and the values of the points on the straight.
    
    Parameters
    ----------
    circle_found : ndarray
        1 dimensional array with type float, float, float that contains the x- and y-coordinate of the 
        centre and the radius of the bounding circle
    mcentre : ndarray
        N dimensional array with type float, float that contains the x- and y-coordinates of the
        centre of mass weighted by the corresponding z-values
    centre : ndarray
        N dimensional array with type float, float that contains the x- and y-coordinates of the
        geometric centre
    imgh : int
        The height of the image
    imgrh : int
        The resolution of the image in y-direction
    imgw : int
        The width of the image
    imgrw : int
        The resolution of the imag in x-direction
        
    Returns
    -------
    xrs : ndarray
        1 dimensional array with type float that contains all x coordinates on the straight right of the
        geometric centre within a range of 50 pixels
    yrs : ndarray
        1 dimensional array with type float that contains all y coordinates on the straight right of the
        geometric centre within a range of 50 pixels
    xls : ndarray
        1 dimensional array with type float that contains all x coordinates on the straight left of the
        geometric centre within a range of 50 pixels
    yls : ndarray
        1 dimensional array with type float that contains all y coordinates on the straight left of the
        geometric centre within a range of 50 pixels
    xprs : ndarray
        1 dimensional array with type float that contains all x coordinates on the perpendicular straight
        right of the geometric centre within a range of 50 pixels
    yprs : ndarray
        1 dimensional array with type float that contains all y coordinates on the perpendicular straight
        right of the geometric centre within a range of 50 pixels
    xpls : ndarray
        1 dimensional array with type float that contains all x coordinates on the perpendicular straight
        left of the geometric centre within a range of 50 pixels
    ypls : ndarray
        1 dimensional array with type float that contains all y coordinates on the perpendicular straight
        left of the geometric centre within a range of 50 pixels
 
    """
    stra = []
    pstra = []
    xrs = []
    yrs = []
    xls = []
    yls = []
    xprs = []
    yprs = []
    xpls = []
    ypls = []
    i = 0
    for c in centre:
        # Determines the distance between the centre of mass and the geometric centre
        xc, yc = c
        xm, ym = mcentre[i]
        rad = circle_found[0][2]
        if xc - xm == 0:
            m = 0
            t = 0
            straight_len = 0
            x_add = 0
            x_rend = 0
            y_rend = 0
            x_lend = 0
            y_lend = 0
            # Calculates the perpendicular straight
            n = 0
            x_padd = 0
            t_p = 0
            x_prend = 0
            y_prend = 0
            x_plend = 0
            y_plend = 0
        else:
            m = (yc - ym) / (xc - xm)    
            t = yc - m * xc
            straight_len = rad * imgrh / imgh
            x_add = straight_len / math.sqrt(1 + m ** 2)
            x_rend = xc + x_add
            y_rend = x_rend * m + t
            x_lend = xc - x_add
            y_lend = x_lend * m + t
            # Calculates the perpendicular straight
            n = -1 / m
            x_padd = straight_len / math.sqrt(1 + n ** 2)
            t_p = yc-n * xc 
            x_prend = xc + x_padd
            y_prend = x_prend * n + t_p
            x_plend = xc - x_padd
            y_plend = x_plend * n + t_p

        # Determines the number of pixels between xc, yc and both sides of the centre x_rend, y_rend,
        # x_lend, y_lend
        num = int(math.sqrt(math.pow((x_rend - xc), 2) + math.pow((y_rend - yc), 2)))
        x,y = np.linspace(xc, x_rend, num), np.linspace(yc, y_rend, num)
        xrs.append(x)
        yrs.append(y)
        num = int(math.sqrt(math.pow((xc - x_lend), 2) + math.pow((yc - y_lend), 2)))
        x,y = np.linspace(x_lend, xc, num), np.linspace(y_lend, yc, num)
        xls.append(x)
        yls.append(y)
        stra.append((xc, yc, x_rend, y_rend, x_lend, y_lend, xm, ym))

        # Determines the number of pixels between xc, yc and and both sides of the centre x_prend, 
        # y_prend, x_plend, y_plend
        nump = int(math.sqrt(math.pow((x_prend - xc), 2) + math.pow((y_prend - yc), 2)))
        xp,yp = np.linspace(xc, x_prend, nump), np.linspace(yc, y_prend, nump)
        xprs.append(xp)
        yprs.append(yp)
        nump = int(math.sqrt(math.pow((xc - x_plend), 2) + math.pow((yc - y_plend), 2)))
        xp,yp = np.linspace(x_plend, xc, nump), np.linspace(y_plend, yc, nump)
        xpls.append(xp)
        ypls.append(yp)
        pstra.append((xc, yc, x_prend, y_prend, x_plend, y_plend))
        i += 1
    return xrs, yrs, xls, yls, xprs, yprs, xpls, ypls

def centre_of_mass(all_coord, img):
    """Determines the centre of mass inside a rectangle weighted by the corresponding z-values
    
    Parameters
    ----------
    all_coord : ndarray
        1 dimensional array with type float, float that contains all x- and y-coordinates inside a rectangle
    img : ndarray
        N dimensional array with type float that contains the z_values of the data
        
    Returns
    -------
    array
        an array with type float, float that contains the x- and y-coordinates of the centre of mass weighted by the corresponding
        z-values
    
    """
    centre_mass = []
    mass_coord = []
    mass_height = []
    for all_c in all_coord:
        mass_c = []
        mass_h = []
        for c in all_c:
            x = c[0]
            y = c[1]
            h = img[y][x]
            x_mass = h*x
            y_mass = h*y
            mass_h.append(h)
            mass_c.append((x_mass,y_mass))
        mass_height.append(mass_h)
        mass_coord.append(mass_c)

    i = 0
    for mass_c in mass_coord:
        """sumh = np.asarray(mass_height[i]).astype(np.int64).sum()
        sumx = np.asarray(([m[0] for m in mass_c])).astype(np.int64).sum()
        print(sumx, sumh)
        sumh = np.asarray(mass_height[i]).sum()
        sumx = np.asarray(([m[0] for m in mass_c])).sum()
        print(sumx, sumh)
        """
        sumh = sum(mass_height[i])
        sumx = sum(([m[0] for m in mass_c]))
        x_mcentre = sumx/sumh
        sumy = sum(([m[1] for m in mass_c]))
        y_mcentre = sumy/sumh
        centre_mass.append((x_mcentre,y_mcentre))
        i += 1
    return centre_mass

def find_coordborder(cnt_drawn, img):
    """Finds points inside cell contour and returns their coordinates
    
    Parameters
    ----------
    cnt_drawn : ndarray
        1 dimensional array with type int, int, float, float that contains the index of a rectangle
        with corresponding contour,
        the y- and x-coordinate of the contour
    img : ndarray
        N dimensional array with type float that contains the z_values of the data
    
    Returns
    -------
    array
        an array with type float, float, float that contains the y-coordinate, the minimum and
        maximum x-coordinate of the points
        inside a contour
        
    """    
    img_coord = []
    for cnt in cnt_drawn:
        cnt_minx = min(cnt, key = lambda c: c[0])
        cnt_miny = min(cnt, key = lambda c: c[1])
        cnt_maxx = max(cnt, key = lambda c: c[0])
        cnt_maxy = max(cnt, key = lambda c: c[1])
        x_min = cnt_minx[0]
        x_max = cnt_maxx[0]
        y_min = cnt_miny[1]
        y_max = cnt_maxy[1]

        icoord = []
        y = y_min + 1
        for y in range(y_min + 1,y_max):
            coord = []
            for c in cnt:
                x_cnt = c[0]
                y_cnt = c[1]
                if y_cnt == y:
                    coord.append((x_cnt, y_cnt))
            if len(coord) > 0:
                x_imgmin = min(coord, key = lambda co: co[0])
                x_imgmax = max(coord, key = lambda co: co[0])
                icoord.append((y, x_imgmin[0], x_imgmax[0]))
        img_coord.append(icoord) 
    return img_coord 

def geometric_centre(img_coord):
    """Determines the geometric centre of a contour (cell)
    
    Parameters
    ----------
    img_coord : ndarray
        1 dimensional array with type float, float, float that contains the y-coordinate, the minimum and maximum x-coordinate
        
    Returns
    -------
    array, array
        array (centre) : an array with type float, float that contains the x- and y-coordinate of the centre of a rectangle
        array (all_coord) : an array with type float, float that contains all x- and y-coordinates inside a rectangle
    
    """
    all_coord = []
    for coord in img_coord:
        all_c = []
        for co in coord:
            y = co[0]
            x_min = co[1]
            x_max = co[2]
            x = x_min
            for x in range(x_min, x_max + 1):
                all_c.append((x, y))
        all_coord.append(all_c)
    # Sums over all coords
    centre = []
    for all_c in all_coord:
        sumx = sum([co[0] for co in all_c])
        numx = len(all_c)
        x_centre = sumx/numx
        sumy = sum([co[1] for co in all_c])
        numy = len(all_c)
        y_centre = sumy/numy
        centre.append((x_centre, y_centre))
    return centre, all_coord

def match_coord(x_straight, y_straight, cntCell):
    """Finds contour points on the straight and sorts the coordinates by distance of the point from
    the geometric centre
    
    Parameters
    ----------
    x_straight : ndarray
        1 dimensional array with type float that contains all x coordinates on the straight within a
        range of 50 pixels
    y_straight : ndarray
        1 dimensional array with type float that contains all x coordinates on the straight within a
        range of 50 pixels
    cnt_drawn : ndarray
        1 dimensional array with type int, int, float, float that contains the index of a rectangle
        with corresponding contour,
        the y- and x-coordinate of the contour
        
    Returns
    -------
    array, array
        array (match_coord) : an array with type float, float, float that contains the x-coordinate,
        the y-coordinate and
        the distance of the point from the geometric centre
        array (sort_coord) : an array with type float, float that contains the x- and y-coordinate of a point
        
    """
    coord_match = []
    i = 0
    for xstr in x_straight:
        coord_m = []
        j = 0
        for x in xstr:
            xdo = int(math.floor(x))
            xup = int(math.ceil(x))
            ydo = int(math.floor(y_straight[i][j]))
            yup = int(math.ceil(y_straight[i][j]))
            #print(xdo, xup, ydo, yup)
            for coord in cntCell:
                xcnt = int(coord[0])
                ycnt = int(coord[1])
                if xcnt == xdo and ycnt == ydo:
                    if len(coord_m) == 0:
                        coord_m.append((x, y_straight[i][j]))
                    elif coord_m[-1] == (x, y_straight[i][j]):
                        continue
                    else:
                        coord_m.append((x, y_straight[i][j]))
                elif xcnt == xup and ycnt == yup:
                    if len(coord_m) == 0:
                        coord_m.append((x, y_straight[i][j]))
                    elif coord_m[-1] == (x, y_straight[i][j]):
                        continue
                    else:
                        coord_m.append((x, y_straight[i][j]))
                elif xcnt == xup and ycnt == ydo:
                    if len(coord_m) == 0:
                        coord_m.append((x, y_straight[i][j]))
                    elif coord_m[-1] == (x, y_straight[i][j]):
                        continue
                    else:
                        coord_m.append((x, y_straight[i][j]))
                elif xcnt == xdo and ycnt == yup:
                    if len(coord_m) == 0:
                        coord_m.append((x, y_straight[i][j]))
                    elif coord_m[-1] == (x, y_straight[i][j]):
                        continue
                    else:
                        coord_m.append((x, y_straight[i][j]))
            j += 1
        coord_match.append(coord_m)
        i += 1
    return coord_match

def points_incell(img_coord, img):
    """Determines the z-value of all points inside a contour
    
    Parameters
    ----------
    img_coord : ndarray
        1 dimensional array with type float, float, float that contains the y-coordinate, the minimum
        and maximum x-coordinate
        of the points inside a contour
    img : ndarray
        N dimensional array with type float that contains the z_values of the data
        
    Returns
    -------
    array
        an array with type float that contains all z-values inside a contour
    
    """
    points_inside = []
    for coord in img_coord:
        points_in = []
        for co in coord:
            y = co[0]
            x_min = co[1]
            x_max = co[2]
            x = x_min+1
            p = []
            for x in range(x_min + 1, x_max):
                try:
                    p.append(img[y][x])
                except IndexError:
                    continue
            points_in.append(p)
        points_inside.append(points_in)
    return points_inside

def sort_coord(coord_rmatch, coord_lmatch):
    """Sorts the matching coordinates by distance between left point and right point
    
    Parameters
    ----------
    coord_rmatch : ndarray
        2 dimensional array with type float, float that contains the x-coordinate and the y-coordinate right
        of the centre
    coord_lmatch : ndarray
        2 dimensional array with type float, float that contains the x-coordinate and the y-coordinate left
        of the centre
        
    Returns
    -------
    array
        an array with type (float, float), (float, float) that contains the x- and y-coordinates of the
        points intersecting with the straight of highest asymmetry left and right of the centre of the
        object
        
    """
    distance = []
    i = 0
    for i in range(0, len(coord_rmatch)):
        j = 0
        dist = []
        for j in range(0, len(coord_rmatch[i])):
            k = 0
            for coord in coord_lmatch[i]: 
                xr = coord_rmatch[i][j][0]
                yr = coord_rmatch[i][j][1]
                xl = coord[0]
                yl = coord[1]
                dis = math.sqrt(abs(xr - xl) ** 2 + abs(yr - yl) ** 2)
                dist.append((dis, i, j, k)) # distance, object, coordinates right, coordinates left
                k += 1
        distance.append(dist)

    # Sorts coordinates by distance between points left and right of the centre
    coord_sort = []
    for coord in distance:
        try:
            len_max = max(coord)[0]
            for c in coord:
                if c[0] == len_max:
                    if len(coord_sort) == 0:
                        coord_sort.append((coord_rmatch[c[1]][c[2]], coord_lmatch[c[1]][c[3]]))
                    else:
                        if coord_sort[-1][0][0] == coord_lmatch[c[1]][c[3]][0]:
                            continue
                        else:
                            coord_sort.append((coord_rmatch[c[1]][c[2]], coord_lmatch[c[1]][c[3]])) 
        except ValueError:
            for c in coord:
                if len(coord_sort) == 0:
                    coord_sort.append((coord_rmatch[c[1]][c[2]], coord_lmatch[c[1]][c[3]]))
                else:
                    if coord_sort[-1][0][0] == coord_lmatch[c[1]][c[3]][0]:
                        j += 1
                        continue
                    else:
                        coord_sort.append((coord_rmatch[c[1]][c[2]], coord_lmatch[c[1]][c[3]]))
    return coord_sort
