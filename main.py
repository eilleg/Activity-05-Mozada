import cv2
import numpy as np

def menu():
    filepath = "gelgel.jpg"

    img = cv2.imread(filepath)

    p = """
        Please Select Action:
        1 - Show a Pixel Value
        2 - Set a Pixel Value
        3 - Set Image Dimension
        4 - Set Image Total Pixel Count
        5 - Print Data Type of Loaded Image """

    print(p)
    input1= int(input("Input Here: "))

    if input1 == 1:
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        pxBlue = img[x,y,0]
        pxGreen = img[x,y,1]
        pxRed = img[x,y,2]
        print("Pixel Value")
        print("Blue: ", pxBlue)
        print("Green: ", pxGreen)
        print("Red: ", pxRed)
        

    elif input1 == 2:
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        pxBlue = img[x,y,0]
        pxGreen = img[x,y,1]
        pxRed = img[x,y,2]
        print("Set Value for each channel")
        b = int(input(" Enter value for blue: "))
        g = int(input(" Enter value for green: "))
        r = int(input(" Enter value for red: "))
        pxBlue1 = img.itemset((x,y,0),b)
        pxGreen1 = img.itemset((x,y,1),g)
        pxRed1 = img.itemset((x,y,2),r)
        print("Value Before \nBlue: ", pxBlue, "\nGreen: ", pxGreen, "\nRed: ", pxRed)
        print("Value Now \nBlue: ", pxBlue1, "\nGreen: ", pxGreen1, "\nRed: ", pxRed1)
        

    elif input1 == 3:
        print("Set Image Dimension")
        xstart = int(input("Enter starting row:"))
        xend = int(input("Enter ending row:"))
        ystart = int(input("Enter starting column:"))
        yend = int(input("Enter ending column:"))
        a,b,c = img.shape
        if xstart <= a:
            
            if xend <= a:
                
                if ystart <= b:
                    
                    if yend <= b:
                        print("Dimension set is within the bounderies")
                    else:
                        print(" Dimension set is out of bounderies")
                        
                else:
                        print(" Dimension set is out of bounderies")

            else:
                        print(" Dimension set is out of bounderies")

        else:
                        print(" Dimension set is out of bounderies")
                        

    elif input1 == 4:
        pxcount = int(input("Set desired pixel count: "))
        if img.size < pxcount:
            print("Original Pixel count:", img.size)
            print("Set Pixel count: ", pxcount)
            print("Original Pixel count is less than Set Pixel count")
        elif img.size < pxcount:
            print("Original Pixel count:", img.size)
            print("Set Pixel count: ", pxcount)
            print("Original Pixel count is more than Set Pixel count")
        else:
            print("Original Pixel count:", img.size)
            print("Set Pixel count: ", pxcount)
            print("Original Pixel count is equal to Set Pixel count")


    elif input1 == 5:
        print(img.dtype)


    else:
        print("Please choose between 1 to 5 only")
        menu()
        
            
