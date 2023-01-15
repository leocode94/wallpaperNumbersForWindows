# Import the required modules
import os
import random
# Assign the target directory
directory = 'C:/Users/Leonardo/Pictures/Wallpapers'
# Iterate over the files in that directory
for filename in os.scandir(directory):
    # Creates a random number
    randomNumber = random.randrange(1000000000, 9999999999)
    # Transform the filename in a string
    file = str(filename)
    # Name of path for Windows
    windowsPath = 'C:/Users/Leonardo/Pictures/Wallpapers/'
    # Check the type of the extensions
    if file.endswith(".jpg'>"):
        os.rename(filename, windowsPath + str(randomNumber) + ".jpg")
    elif file.endswith(".png'>"):
        os.rename(filename, windowsPath + str(randomNumber) + ".png")
    elif file.endswith(".jpeg'>"):
        os.rename(filename, windowsPath + str(randomNumber) + ".jpeg")
    elif file.endswith(".tif'>"):
        os.rename(filename, windowsPath + str(randomNumber) + ".tif")
    elif file.endswith(".jfif'>"):
        os.rename(filename, windowsPath + str(randomNumber) + ".jfif")
    elif file.endswith(".JPG'>"):
        os.rename(filename, windowsPath + str(randomNumber) + ".jpg")
print("All files on ", directory, " have been renamed!")