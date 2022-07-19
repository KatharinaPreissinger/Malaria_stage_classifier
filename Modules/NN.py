def format_values(name, spath):
    """Formats values and writes them into array
    
    Parameters
    ----------
    name : str
        Name of the txt file
    spath : str
        Name of the directory
    parameter : str
        Name of the parameter
        
    Returns
    -------
    values : ndarray
        1 dimensional array with type float that contains the content of the text file
        
    """
    values = []
    # reads x_data from folder
    data = open(spath + '/' + name,'r')
    row = data.read().split('\n')
    col = row[0].split(' ') 
    nrow = len(row)
    ncol = len(col)
    data.close()
    # writes x_data in array
    v = []
    for cs in row:
        num = cs.split(',')
        for n in num:
            if len(n) == 0:
                continue
            if n[0] == '[' and n[1] == '[' and n[2] == 'a':
                v.append(float(n.replace('[[array([', '')))
            elif n[0] == '[' and n[1] == '[':
                v.append(float(n.replace('[[', '')))
            elif n[0] == '[' and n[1] == 'a':
                v.append(float(n.replace('[array([', '')))
            elif n[0] == '[' and n[-1] == ']':
                continue
            elif n[0] == '[':
                v.append(float(n.replace('[', '')))
            elif n[0] == ' ' and n[1] == '[':
                v = []
                v.append(float(n.replace(' [', '')))
            elif n[0] == ' ' and n[1] == 'a':
                v = []
                n.replace(' ', '')
                v.append(float(n.replace('array([', '')))
            elif n[0] == ' ' and n[1] == 'd':
                continue
            elif n[0] == 'a':
                v.append(float(n.replace('array([', '')))
            elif n[-1] == ']' and n[-2] == ']' and n[-3] == ')' and n[-4] == '8':
                continue
            elif n[-1] == ']' and n[-2] == ']' and n[-3] == ')' and n[-4] == ']':
                n.replace(' ', '')
                v.append(float(n.replace('])]]', '')))
            elif n[-1] == ']' and n[-2] == ']':
                n.replace(' ', '')
                v.append(float(n.replace(']]', '')))
            elif n[-1] == ')' and n[-2] == ']':
                n.replace(' ', '')
                v.append(float(n.replace('])', '')))
                values.append(v)
            elif n[-1] == ']' and n[-2] == ')' and n[-3] == ']':
                v.append(float(n.replace('])]', '')))
            elif n[-1] == ']' and n[-2] == ')':
                if n[-3] == '8':
                    continue
                else:
                    v.append(float(n.replace(')]', '')))
            elif n[-1] == ']':
                v.append(float(n.replace(']', '')))
                values.append(v)
            else:
                try:
                    v.append(float(n))
                except ValueError:
                    continue
    if len(v) > 0:
        values.append(v)
    return values

def format_NN_values(name, spath):
    """Formats values for NN input and writes them into array
    
    Parameters
    ----------
    name : str
        Name of the txt file
    spath : str
        Name of the directory
    parameter : str
        Name of the parameter
        
    Returns
    -------
    values : ndarray
        1 dimensional array with type float that contains the content of the text file
        
    """
    values = []
    # reads x_data from folder
    data = open(spath + '/' + name,'r')
    row = data.read().split('\n')
    col = row[0].split(' ') 
    nrow = len(row)
    ncol = len(col)
    data.close()
    # writes x_data in array
    v = []
    for cs in row:
        num = cs.split(' ')
        for n in num:
            #print(n)
            if len(n) == 0:
                continue
            elif len(n) == 1:
                if n[-1] == ']':
                    values.append(v)
                    v = []
            else:
                try:
                    if n[0] == '[' and n[1] == '[':
                        try:
                            v.append(float(n.replace('[[', '')))
                        except ValueError:
                            continue
                    elif n[0] == '[':
                        v.append(float(n.replace('[', '')))
                    elif n[-1] == ']' and n[-2] == ']':
                        n.replace(' ', '')
                        try:
                            v.append(float(n.replace(']]', '')))
                        except ValueError or IndexError:
                            continue
                    elif n[-1] == ']':
                        if len(n) == 1:
                            values.append(v)
                        else:
                            n.replace(' ', '')
                            v.append(float(n.replace(']', '')))
                            values.append(v)
                        v = []
                    else:
                        try:
                            v.append(float(n))
                        except ValueError:
                            continue
                except IndexError:
                    continue
    if len(v) > 0:
        values.append(v)
    return values

def read_images(path):
    """Reads text files of characteristic cuts and labels them according to their category
    
    Parameters
    ----------
    path : str
        The name of the folder that contains the characteristic cuts
        
    Returns
    -------
    carr_form : ndarray
        N x (N x N) dimensional array with type float that contains N times two characteristic cross-sections with 50 data points
    label_form : ndarray
        1 dimensional array with type int that contains the labels of N cells
    
    """
    # Opens the conten of the folder
    stages = os.listdir(path)
    # parameters for the NN
    batch_size = 2 # minibatches
    IMSIZE = (50,50) # all images in dataset will be rescaled to this dimensions
    IMAGE_WIDTH = IMSIZE[0]
    IMAGE_HEIGHT = IMSIZE[1]
    IMAGE_CHANNELS = 1 # RGB color
    # Reads the cuts from the folder
    # stage: Healthy = 0, Ring = 1, Trophozoite = 2, Schizont = 3
    carr = []
    label = []
    for stage in stages:
        if (stage == 'Healthy' or stage == 'Ring' or stage == 'Trophozoite' or stage == 'Schizont'):
            dpath = path + '/' + stage
            arrs = os.listdir(dpath)
            for arr in arrs:
                cs = format_values(arr, dpath) 
                if stage == 'Healthy':
                    if len(cs) > 2:
                        cs.pop(-1)
                    cs_new = []
                    if cs[0][0] > 300:
                        continue
                    carr.append(cs)
                    label.append(0)
                elif stage == 'Ring':
                    if len(cs) > 2:
                        cs.pop(-1)
                    cs_new = []
                    if cs[0][0] > 300:
                        continue
                    carr.append(cs)
                    label.append(1)
                elif stage == 'Trophozoite':
                    if len(cs) > 2:
                        cs.pop(-1)
                    cs_new = []
                    if cs[0][0] > 300:
                        continue
                    carr.append(cs)
                    label.append(2)
                else:
                    if len(cs) > 2:
                        cs.pop(-1)
                    cs_new = []
                    if cs[0][0] > 300:
                        continue
                    carr.append(cs)
                    label.append(3)
    
    # Normalises the values of the cuts to range from 0 to 1
    carr_norm = []
    for car in carr:
        ca_new = []
        for ca in car:
            xmax = max(ca)
            xmin = min(ca)
            if xmax - xmin == 0:
                c_new = np.asarray(ca)
            else:
                c_new = (np.asarray(ca) - xmin) / (xmax - xmin)
            ca_new.append(c_new)
        carr_norm.append(ca_new)
    carr_form = np.asarray(carr_norm)
    label_form = np.asarray(label)
    return carr_form, label_form

def train_model(model, carr_form, label_form, cut_train, label_train, directory, mname, tlabel):
    """Trains NN model on a combination of old and new data
    
    Parameters
    ----------
    model : Sequential
        The pre-trained neural network
    carr_form : ndarray
        N x 2 x 50 array with type float that contains N times two characteristic cross-sections with 50 data points
    label_form : ndarray
        N x 1 array with type int that contains the labels of N cells
    directory : str
        The name of the network folder
    mname : str
        The name of the new network
    tlabel : tkinter Label
        Displays the progres of the calculation
        
    Returns
    -------
    model : tf.keras.Sequential
        Sequential class that contains the trained new keras model
        
    """
    # Formats the input data and target labels
    cut_new = carr_form.reshape(carr_form.shape[0], carr_form.shape[2], carr_form.shape[1])
    label_new = to_categorical(label_form, num_classes=4)
    # Formats the old data
    cut_train = np.asarray(cut_train)
    cut_old = cut_train.reshape(cut_train.shape[0], cut_train.shape[2], cut_train.shape[1])
    label_old = to_categorical(label_train, num_classes=4)
    # Updates model with a smaller learning rate
    opt = RMSprop(learning_rate=0.0001)
    tlabel.config(text="Please wait, network is training... 30%")
    # Compiles the model
    model.compile(optimizer=opt, loss='categorical_crossentropy')
    # Creates a composite dataset of old and new data
    cut, label = np.vstack((cut_old, cut_new)), np.vstack((label_old, label_new))
    tlabel.config(text="Please wait, network is training... 60%")
    # Fits the model on new data
    model.fit(cut, label, epochs=20, batch_size=20, shuffle=True, verbose = 2)
    tlabel.config(text="Please wait, network is training... 90%")
    # Saves the new model
    model.save(directory + '/' + mname + '.h5')
    return model
