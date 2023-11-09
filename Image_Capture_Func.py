from pywinauto import WindowSpecification

import Constants as cons


#  Calculate coordinates from the zero position in the main frame
#  to the selected element
def cal_element_coordinate(left, top, right, bottom):
    ele_coord = {'l': 0,
                 't': 0,
                 'r': 0,
                 'b': 0}
    coordinate_array = cons.Dig_zero_Coordinate
    ele_coord['l'] = left - coordinate_array[0]
    ele_coord['t'] = top - coordinate_array[1]
    ele_coord['r'] = right - coordinate_array[0]
    ele_coord['b'] = bottom - coordinate_array[1]

    return ele_coord


# Capture selected Area or Element
def area_capture_with_coordinate(dia: WindowSpecification, title: str, coordinate: [int]):
    coord = cal_element_coordinate(coordinate[0], coordinate[1],
                                   coordinate[2], coordinate[3])
    img = dia.capture_as_image()
    (img.crop([coord['l'], coord['t'], coord['r'], coord['b']])
     .save(fr'Capture\{title}_crop.png'))
