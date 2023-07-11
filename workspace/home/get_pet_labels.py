#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Alif Abdullah
# DATE CREATED: 7/8/2023                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # remove the .jpg file extension from each file. .jpg takes up 4 characters. accomplished by [:-4]
    # realized that I could further split the strings by splitting them by the character "_", which is what I did. accomplished by .split("_")
    # then realized that the end of each list contained an irrelevant number. got rid of it using [:-1] at the end of the list element expression. i handle hidden files by only adding files to my list if they dont start with the character .
    file_names = listdir(image_dir)
    pet_labels = [file[:-4].split("_")[:-1] for file in file_names if file[0]!="."]
    for index in range(len(pet_labels)):
        # go through every element of pet_labels. each element is a list, so take the first element and modify it
        pet_labels[index][0] = pet_labels[index][0].lower()
        
        #join together the elements of fragmented pet name lists into one pet name string
        pet_labels[index] = (" ".join(pet_labels[index])).strip()
    results_dic = dict()
    for k,v in zip(file_names, pet_labels):
        results_dic[k] = [v]
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
