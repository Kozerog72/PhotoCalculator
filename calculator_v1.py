# Calculator-1: to determine the size of the object on the camera matrix in the analyzed image.

"""
Note:
Full-frame cameras have a sensor size of 36 x 24 mm (width / height).
Frame sizes have the following meanings:
HD = 1280 x 720 pixels
Full HD = 1920 x 1080 pixels
This calculator - determines the size of the object on the camera matrix in the analyzed image.
"""


def object_size():
    global i, m, o, e, c, r
    size_by = 'Width'
    size_opt = input('Now "size_by = Width". Enter "s" to change "size_by = Height" or other key to continue: ')
    while size_opt == 's':
        if size_by == 'Height':
            size_by = 'Width'
            size_opt = input('Now "size_by = Width". Enter "s" to change "size_by = Height" or other key to continue: ')
        else:
            size_by = 'Height'
            size_opt = input(
                'Now "size_by = Height". Enter "s", to change "size_by = Width" or other key to continue: ')
    if size_by == 'Width':
        i = 'Enter width_size of the image in "pixels": '
        m = 'Enter width_size of the camera matrix in "mm": '
        o = 'Enter the measured width_size of the object in the image in "pixels": '
        r = 'Result:  '
        e = 'Error'
        c = 'Enter "c" to continue or other key to finish: '
    if size_by == 'Height':
        i = 'Enter height_size of the image in "pixels": '
        m = 'Enter height_size of the camera matrix in "mm": '
        o = 'Enter the measured height_size of the object in the image in "pixels": '
        r = 'Result'
        e = 'Error'
        c = 'Enter "c" to continue or other key to finish: '
    next = 'c'
    while next == 'c':
        i_num = float(input(i))
        m_num = float(input(m))
        o_num = float(input(o))
        if o_num == None:
            print(e, "ERROR")
        else:
            r = o_num * m_num / i_num
            print(r)
        next = input(c)
    print("Object_size result is: ", r, "mm")


object_size()

# Calculator-2: to calculate distance to object.

"""
The formula for determining the distance to an object based on the characteristics of the camera, lens, and captured photograph.
d = f * (H + h) / H
f = Lens focal length - "millimeter"
h = True size of the object - "meter"
H = Object size on the camera matrix - "millimeter"
"""


def object_distance():
    global f, h, H, e, c, d
    distance_by = 'Width'
    distance_opt = input('Now "size_by = Width". Enter "s" to change "size_by = Height" or other key to continue:  ')
    while distance_opt == 's':
        if distance_by == 'Height':
            distance_by = 'Width'
            distance_opt = input(
                'Now "size_by = Width". Enter "s" to change "size_by = Height" or other key to continue:  ')
        else:
            distance_by = 'Height'
            distance_opt = input(
                'Now "size_by = Height". Enter "s", to change "size_by = Width" or other key to continue:  ')
    if distance_by == 'Width':
        f = 'Enter lens focal length - "millimeter": '
        h = 'Enter true size of the object - "meter": '
        H = 'Enter object size on the camera matrix - "millimeter": '
        d = 'Result '
        e = 'Error'
        c = 'Enter "c" to continue or other key to finish: '
    if distance_by == 'Height':
        f = 'Enter lens focal length - "millimeter": '
        h = 'Enter true size of the object - "meter": '
        H = 'Enter object size on the camera matrix - "millimeter": '
        d = 'Result '
        e = 'Error'
        c = 'Enter "c" to continue or other key to finish: '
    next = 'c'
    while next == 'c':
        f_num = float(input(f))
        h_num = float(input(h))
        H_num = float(input(H))
        if H_num == None:
            print(e, "ERROR")
        else:
            d = f_num / 1000 * (H_num / 1000 + h_num) / (H_num / 1000)
            print(d)
        next = input(c)
    print("Object_distance result is: ", d / 1000, "km")


object_distance()
