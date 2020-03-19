import csv
import cv2
import colorDetection
#import image

with open('garments.csv') as csvfile:
    reader = csv.DictReader(csvfile)




 # Creating the menu

print('Enter a colour: ')
theID = input('')
imgStore = ('data/' + theID+'.jpeg')
img = cv2.imread(imgStore)
cv2.imshow('image', img)
cv2.waitKey(10000)








# topColour = input('')
#
# for column in reader:
#     if column['Garment Layer'] == 'Top' and column['Colour']==topColour:
#         topID = column['ID']
#         print(topID)
#
#         topIDread = str(topID)
#         imgStore = ('data/' + topIDread+'.jpeg')
#         img = cv2.imread(imgStore)
#         cv2.imshow('image', img)
#         cv2.waitKey(1000)

