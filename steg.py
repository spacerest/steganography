import math 
import numpy as np

def get_binary_significant_digits(binary_num):
    significant_digits = bin(math.floor(int(binary_num, 2) / 16))[2:].zfill(4).ljust(8, "0")
    return significant_digits 

def convert_binary_to_decimal(binary_number):
    return int(binary_number,2)

def convert_decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:].zfill(8) 

def get_binary_pixel_significant_digits(binary_pixel):
    significant_digits = [get_binary_significant_digits(x) for x in binary_pixel]
    return significant_digits

def convert_binary_significant_to_insignificant(binary_number):
    return binary_number[:4]

def convert_binary_pixel_significant_to_insignificant(binary_pixel):
    return [convert_binary_significant_to_insignificant(x) for x in binary_pixel]
    
def convert_pixel_binary_to_decimal(binary_pixel):
    return [convert_binary_to_decimal(x) for x in binary_pixel]

def convert_pixel_decimal_to_binary(decimal_pixel):
    return [convert_decimal_to_binary(x) for x in decimal_pixel]

def combine_image_arrays(visible_image_array, invisible_image_array):
    visible_image_array_binary = np.apply_along_axis(convert_pixel_decimal_to_binary, 1, visible_image_array)  
    invisible_image_array_binary = np.apply_along_axis(convert_pixel_decimal_to_binary, 1, invisible_image_array)  
    invisible_image_array_binary_insignificant = np.apply_along_axis(convert_binary_pixel_significant_to_insignificant, 1, invisible_image_array_binary) 
    invisible_image_array_decimal = np.apply_along_axis(convert_pixel_binary_to_decimal, 1, invisible_image_array_binary_insignificant)
    visible_image_array_decimal = np.apply_along_axis(convert_pixel_binary_to_decimal, 1, visible_image_array_binary)
    combined_image_array = visible_image_array_decimal + invisible_image_array_decimal
    return combined_image_array 
