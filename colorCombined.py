# # THIS CLASS ALLOWS ME TO ENTER AN OPTION FOR GARMENT
# # AND THEN ADD A COLOUR AND IT WILL GIVE ALL GARMENTS OF THAT COLOUR
# # IN 5 I JUST USE TO SEE THE VALUES FROM THE ADD TO CSV OPTION
#
# import csv
# import cv2
# import colorDetection
# #import image
# import sys
# import numpy as np
# import io
# import webcolors
#
# from colorthief import ColorThief
# with open('garments.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#
#
# #CODE FROM https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green-with-python
#     def closest_colour(requested_colour):
#         min_colours = {}
#         for key, name in webcolors.css3_hex_to_names.items():
#             r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#             rd = (r_c - requested_colour[0]) ** 2
#             gd = (g_c - requested_colour[1]) ** 2
#             bd = (b_c - requested_colour[2]) ** 2
#             min_colours[(rd + gd + bd)] = name
#         return min_colours[min(min_colours.keys())]
#
#
#     def get_colour_name(requ1ested_colour):
#         try:
#             closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
#         except ValueError:
#             closest_name = closest_colour(requested_colour)
#             actual_name = None
#         return actual_name, closest_name
#
#
#
#
#
#
#  # Creating the menu
#     print('---- MENU -----')
#     print('--PRESS 1 FOR TOP LAYER --')
#     print('--PRESS 2 FOR BOTTOM LAYER --')
#     print('--PRESS 3 FOR SHOES --')
#     print('--PRESS 4 TO CLOSE THE PROGRAM --')
#     print('--PRESS 5 TO SELECT ALL BY COLOUR --')
#
#
#     menu_action = input('')
#
#
#     if menu_action == '1':
#         countTop = 0
#         print('Enter a colour: ')
#         topColour = input('')
#
#         for column in reader:
#                 if column['Garment Layer'] == 'Top' and column['Colour']==topColour:
#                     topID = column['ID']
#                     print(topID)
#                     countTop = countTop+1
#
#                     #TO OUTPUT THE IMAGES OF ALL TOPS
#                     topIDread = str(topID)
#                     imgStore = ('data/' + topIDread+'.jpeg')
#
#                     color_thief = ColorThief(imgStore)
#                     domcol = (color_thief.get_color(quality=1))
#                     requested_colour = ((domcol))
#                     actual_name, closest_name = get_colour_name(requested_colour)
#                     print("Closest colour name:", closest_name)
#
#
#                     img = cv2.imread(imgStore)
#                     cv2.imshow('image', img)
#                     cv2.waitKey(1000)
#
#                     #Color of the item
#
#
#
#
#
#
#         print(countTop)
#
#
#     elif menu_action == '2':
#             countBottom = 0
#             print('Enter a colour: ')
#             bottomColour = input('')
#
#             for column in reader:
#                 if column['Garment Layer'] == 'Bottom' and column['Colour'] == bottomColour :
#                     bottomID = column['ID']
#                     print(bottomID)
#                     countBottom = countBottom + 1
#
#                     # TO OUTPUT THE IMAGES OF ALL BOTTOMS
#                     bottomIDread = str(bottomID)
#                     imgStore = ('data/' + bottomIDread + '.jpeg')
#                     img = cv2.imread(imgStore)
#
#                     color_thief = ColorThief(imgStore)
#                     domcol = (color_thief.get_color(quality=1))
#                     requested_colour = ((domcol))
#                     actual_name, closest_name = get_colour_name(requested_colour)
#                     print("Closest colour name:", closest_name)
#
#                     cv2.imshow('image', img)
#                     cv2.waitKey(1000)
#
#             print(countBottom)
#
#
#
#     elif menu_action == '3':
#         countShoes = 0
#         print('Enter a colour for the shoe:')
#         shoeColourSearch = input('')
#
#         for column in reader:
#             if column['Garment Layer'] == 'Shoe' and column['Colour'] == shoeColourSearch:
#                 shoeID = column['ID']
#                 print(shoeID)
#                 countShoes = countShoes + 1
#
#                 # TO OUTPUT THE IMAGES OF ALL SHOES
#                 shoesIDread = str(shoeID)
#                 imgStore = ('data/' + shoesIDread + '.jpeg')
#                 img = cv2.imread(imgStore)
#
#                 color_thief = ColorThief(imgStore)
#                 domcol = (color_thief.get_color(quality=1))
#                 requested_colour = ((domcol))
#                 actual_name, closest_name = get_colour_name(requested_colour)
#                 print("Closest colour name:", closest_name)
#
#                 cv2.imshow('image', img)
#                 cv2.waitKey(1000)
#         print(countShoes)
#
#     elif menu_action == '5':
#             countAll = 0
#             print('Enter a colour: ')
#             allColour = input('')
#
#             for column in reader:
#                 if column['Garment Layer'] == 'Garment Layer' and column['Colour'] == allColour:
#                     allID = column['ID']
#                     print(allID)
#                     countAll = countAll + 1
#
#                     # TO OUTPUT THE IMAGES OF ALL BOTTOMS
#                     allIDread = str(allID)
#                     imgStore = ('data/' + allIDread + '.jpeg')
#                     img = cv2.imread(imgStore)
#
#                     color_thief = ColorThief(imgStore)
#                     domcol = (color_thief.get_color(quality=1))
#                     requested_colour = ((domcol))
#                     actual_name, closest_name = get_colour_name(requested_colour)
#                     print("Closest colour name:", closest_name)
#
#                     cv2.imshow('image', img)
#                     cv2.waitKey(1000)
#
#             print(countAll)
