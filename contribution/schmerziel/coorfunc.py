from typing import *
import constants


# functions that must be applied to the coord lists

def dilate(origin: tuple, destination: tuple, coords: list, factor: float,
           frames: int):
    pass
    # apply to x1: (x0+(originx-destinationx)/frames)*factor
    # apply to y1: (y0+(originy-destinationy)/frames)*factor


def translate(coords: List[Tuple], x, y) -> Tuple:
    newcoords = []
    for xy in coords:
        newcoords.append((xy[0]+x, xy[1]+y))
    return newcoords


def prepared_coords(func_x, x_o, x_t) -> List:
    return [(x, func_x(x)) for x in range(x_o, x_t+1)]


def find_origin(coords: List) -> Tuple:
    num_coords = len(coords)
    sum_x = 0
    sum_y = 0

    for coord in coords:
        sum_x += coord[0]
        sum_y += coord[1]

    # basically find the "center" of an object from list of coords
    avg_x = sum_x/num_coords
    avg_y = sum_y/num_coords

    res = (int(avg_x), int(avg_y))
    return res


def ease_out(starting_frame: int,
             current_frame: int,
             end_frame: int,
             ease_factor: float) -> int:
    end_bound = end_frame - starting_frame + 1
    linear_percentage = (current_frame - starting_frame + 1) \
                        / end_bound
    processed_percentage = -(linear_percentage ** ease_factor)+1
    return int(processed_percentage * end_bound + starting_frame - 1)


def ease_in(starting_frame: int,
            current_frame: int,
            end_frame: int,
            ease_factor: float) -> int:
    end_bound = end_frame - starting_frame + 1
    linear_percentage = (current_frame-starting_frame+1) \
                        / end_bound
    processed_percentage = linear_percentage**ease_factor
    return int(processed_percentage * end_bound + starting_frame - 1)


def get_frames_ease_out(start: int, end: int, ease_factor) -> Set:
    return {ease_out(start, frame, end, ease_factor)
            for frame in range(start, end+1)}


def get_frames_ease_in(start: int, end: int, ease_factor: float) -> Set:
    return {ease_in(start, frame, end, ease_factor)
            for frame in range(start, end+1)}


def get_frames_ease(start: int, end: int,
                    ease_factor: float, easing_type: int) -> Set:
    if easing_type == constants.EASE_IN:
        return get_frames_ease_in(start, end, ease_factor)
    elif easing_type == constants.EASE_OUT:
        return get_frames_ease_out(start, end, ease_factor)
    else:
        return {0}
