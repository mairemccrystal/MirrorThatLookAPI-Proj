import csv
import cv2
#import image

with open('garments.csv') as csvfile:
    reader = csv.DictReader(csvfile)




 # Creating the menu
    print('---- MENU -----')
    print('--PRESS 1 FOR TOP LAYER --')
    print('--PRESS 2 FOR BOTTOM LAYER --')
    print('--PRESS 3 FOR SHOES --')
    print('--PRESS 4 TO CLOSE THE PROGRAM --')


    menu_action = input('')


    if menu_action == '1':
        countTop = 0
        print('Enter a colour: ')
        topColour = input('')

        for column in reader:
                if column['Garment Layer'] == 'Top' and column['Colour']==topColour:
                    topID = column['ID']
                    print(topID)
                    countTop = countTop+1

                    #TO OUTPUT THE IMAGES OF ALL TOPS
                    topIDread = str(topID)
                    imgStore = ('data/' + topIDread+'.jpeg')
                    img = cv2.imread(imgStore)
                    cv2.imshow('image', img)
                    cv2.waitKey(1000)


        print(countTop)




    elif menu_action == '2':
            countBottom = 0
            print('Enter a colour: ')
            bottomColour = input('')

            for column in reader:
                if column['Garment Layer'] == 'Bottom' and column['Colour'] == bottomColour :
                    bottomID = column['ID']
                    print(bottomID)
                    countBottom = countBottom + 1

                    # TO OUTPUT THE IMAGES OF ALL BOTTOMS
                    bottomIDread = str(bottomID)
                    imgStore = ('data/' + bottomIDread + '.jpeg')
                    img = cv2.imread(imgStore)
                    cv2.imshow('image', img)
                    cv2.waitKey(1000)

            print(countBottom)



    elif menu_action == '3':
        countShoes = 0
        print('Enter a colour for the shoe:')
        shoeColourSearch = input('')

        for column in reader:
            if column['Garment Layer'] == 'Shoe' and column['Colour'] == shoeColourSearch:
                shoeID = column['ID']
                print(shoeID)
                countShoes = countShoes + 1

                # TO OUTPUT THE IMAGES OF ALL SHOES
                shoesIDread = str(shoeID)
                imgStore = ('data/' + shoesIDread + '.jpeg')
                img = cv2.imread(imgStore)
                cv2.imshow('image', img)
                cv2.waitKey(1000)
        print(countShoes)





