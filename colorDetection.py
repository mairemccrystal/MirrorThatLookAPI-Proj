
import sys
import numpy as np
import io
import webcolors

from colorthief import ColorThief


from colorthief import ColorThief

color_thief = ColorThief('data/20.jpeg')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)

domcol = (color_thief.get_color(quality=1))
# build a color palette
palette = color_thief.get_palette(color_count=6)

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

requested_colour = ((domcol))
actual_name, closest_name = get_colour_name(requested_colour)

print("Closest colour name:", closest_name)

print(domcol)
#colname = webcolors.rgb_to_name((domcol))
#print(colname)



