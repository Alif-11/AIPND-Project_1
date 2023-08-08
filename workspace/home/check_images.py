#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#                                                                          
# PROGRAMMER: Alif Abdullah
# DATE CREATED: 7/8/2023                                
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Calculate program execution time by taking start time
    start_time = time()
    
    # The function takes 3 command line arguments from the user:
    # - the path to the directory of pet images, as --dir (ex pet_images/)
    # - the name of model architecture to be used, as --arch (ex vgg)
    # - the path to the text file with recognized dog names as --dogfile (ex dognames.txt)
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)

    # The function takes the pet images directory. Using the filenames in the directory,
    # it creates and returns a dictionary whose keys are the filenames in the directory that was passed in,
    # and whose values are a list with one element: 
    # - (index 0) the animal breed that is contained within each of the filenames
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results    
    check_creating_pet_image_labels(results)

    # The function modifies the dictionary returned in the last function, adding to the values list
    # - (index 1) the label the classifier categorized the image as
    # - (index 2) the integer 1 if there is a match between the labels in indices 0 and 1, and 0 otherwise
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results    
    check_classifying_images(results)    

    # The function adjust_results4_isadog is defined in the file adjust_results4_isadog.py
    # The function modifies the dictionary returned in the last function, adding to the values list
    # - (index 3) 1 if the pet image is of an actual dog, 0 otherwise
    # - (index 4) 1 if the classifier categorizes the image as a dog, 0 otherwise
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    # The function returns a dictionary with summary statistics about the performance of the current executed model.
    # The keys are the statistic names, and the values are the actual statistics.
    # They will be listed in this format - (key : description of significance of value)
    # ('n_images' : number of images)
    # ('n_dogs_img': number of images that are dogs)
    # ('n_notdogs_img' : number of images that are not dogs)
    # ('n_match': number of matches between the actual breed and classifier label)
    # ('n_correct_dogs' : number of images of dogs the classifier thought was a dog)
    # ('n_correct_notdogs' : number of images of not dogs the classifer thought was not a dog)
    # ('n_correct_breed' : number of dogs that the classifier correctly labelled with the right breed)
    # ('pct_match' : 'n_match' over 'n_images')
    # ('pct_correct_dogs' : 'n_correct_dogs' over 'n_dogs_img')
    # ('pct_correct_notdogs' : 'n_correct_notdogs' over 'n_notdogs_img')
    # ('pct_correct_breed' : 'n_correct_breed' over 'n_dogs_img')
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    # Prints a list of summary statistics that offer insight into the accuracy and efficiency of the models
    # Displays the model name, number of images, number of dogs and not dogs, every percentage statistic from the last dictionary
    # as well as two error statistics:
    # - Misclassified dogs: the images with a dog that the classifier thought had no dog, and vice versa
    # - Misclassified breeds: the images where the classifier thought an image of a dog was a dog, but gave an incorrect label for the breed
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Calculate program execution time by taking end time
    end_time = time()
    
    # Print overall runtime in seconds in the hh:mm:ss format
    tot_time = end_time - start_time#calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
