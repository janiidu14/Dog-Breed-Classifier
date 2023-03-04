#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Janidu Rathnayaka
# DATE CREATED: 24/11/2022                                 
# REVISED DATE: 06/02/2023

# Imports python modules
from os import listdir

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
    
    # Retrieve the filenames from folder pet_images/
    filename_list = listdir(image_dir)
    
    # Creates empty dictionary named results_dic
    results_dic = dict()
        
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for files in filename_list:
        word_array = files.lower().split("_")[:-1]
        
        dog_name = ""
        for word in word_array:
            dog_name += word + " "
            
               
        dog_name = dog_name.strip();
        # Check if label is only alphabetic characters 
        if dog_name not in results_dic:
            results_dic[files] = [dog_name]
        else:
            print("** Warning: Key=", files, 
                  "already exists in results_dic with value =", 
                  dog_name)
            
    # Return the results_dic dictionary 
    return results_dic
