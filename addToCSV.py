#THIS CLASS DETECTS THE MAIN COLOUR IN IMAGES IN A GIVEN RANGE
#IT WILL THEN LABEL THE COLORS AND ADD TO THE CSV
#THIS IS FOR LABELLING THE COLORS - ATM ONLY 1 COLOR WANT TO WORK ON MULTIPLE
# && WANT TO EVENTUALLY ADD SHAPE DETECTION


import csv
import cv2
import colorDetection
#import image
import webcolors

from colorthief import ColorThief


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


with open('garments.csv', 'w', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Garment Layer", "Colour"])
    for i in range(1, 300):
        #print(i);
        IDread = str(i)
        imgStore = ('data/' + IDread + '.jpeg')

        color_thief = ColorThief(imgStore)
        domcol = (color_thief.get_color(quality=1))
        requested_colour = ((domcol))
        actual_name, closest_name = get_colour_name(requested_colour)
       # print("Closest colour name:", closest_name)
        writer.writerow([i, "Garment Layer", closest_name])
        print(i)

# row_count = sum(1 for row in reader)
   # insertAt = row_count + 1
   # print(row_count)
   # print(insertAt)



