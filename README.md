# AIPND-Project_1
This repo hosts my work for the first project of the Artificial Intelligence Programming with Python Nanodegree Program. This project revolved around using a pre-tained image classifier to classify images of animals into dogs and not dogs, as well as to identify the breed of dog in the picture. We tested three CNN models - vgg, alexnet, and resnet.

This project took around 10 hours to complete. All the auxiliary python programs that will be mentioned below were ran in the driver file check_images.py.

## My work revolved around:
* Recording the time it took for the entire program to execute, using the time module.
* Handling user inputs ((string) the path image directory where the user's dog images are stored, (string) the name of the CNN model used, (string) the list of valid dog breed names to be used in checking if an identified photo is a dog breed. I also provided default values in case the user decided not to provide their own values. This was done using the **argparse** module in the **get_input_args.py** file.
* Read in a directory of pet image files and converted their names into a list of strings using the **listdir* module, then created a dictionary where the file names were the keys and a list containing one element - the associated labels for the pet breeds - was the values. I processed the filenames to convert them into pet labels within the **get_pet_labels.py** file. I returned this dictionary to the main check_images.py file.
* Used the predefined classifier method that came with the project to run the specified model on each image in the specified image directory. I then stored the label the model classified each image, as well as whether there was a match between the associated labels derived from the file name and the classifier label, within the dictionary from the last bullet point. This was done in the **classify_images.py** file.
