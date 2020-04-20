import math 
import numpy as np

print("imported steg")

def get_binary_significant_digits(binary_num):
    significant_digits = bin(math.floor(int(binary_num, 2) / 16))[2:].zfill(4).ljust(8, "0")
    return significant_digits 

# rename to something more mathically descriptive
def get_binary_insignificant_digits(binary_num):
    insignificant_digits = bin(math.floor(int(binary_num, 2) % 16))[2:].zfill(4).ljust(8, "0")
    return insignificant_digits 

def get_binary_pixel_insignificant_digits(binary_pixel):
    insignificant_digits = [get_binary_insignificant_digits(x) for x in binary_pixel]
    return insignificant_digits

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
    print("HELLO")
    #convert visible image to binary array
    visible_image_array_binary = np.apply_along_axis(convert_pixel_decimal_to_binary, 1, visible_image_array) 
    
    #remove insignificant digits from visible image binary array
    visible_image_array_significant_binary = np.apply_along_axis(get_binary_pixel_significant_digits, 1, visible_image_array_binary)
    print("visible_image_array_significant_binary")
    print(visible_image_array_significant_binary)
    
    #convert the visible image back from binary to decimal [[255,255,255]]
    visible_image_array_decimal = np.apply_along_axis(convert_pixel_binary_to_decimal, 1, visible_image_array_significant_binary)
    print("visible_image_array_decimal")
    print(visible_image_array_decimal)
    
    #convert invisible image to binary array [[128,0,0]] -> [[10000000,00000000,00000000]]
    invisible_image_array_binary = np.apply_along_axis(convert_pixel_decimal_to_binary, 1, invisible_image_array)  
    
    #move significant digits of invisible image to be the insignificant digits [[1000,0000,0000]]
    invisible_image_array_binary_insignificant = np.apply_along_axis(convert_binary_pixel_significant_to_insignificant, 1, invisible_image_array_binary) 
    print("invisible_image_array_binary_insignificant")
    print(invisible_image_array_binary_insignificant)

    
    #convert modified invisible binary array to decimal [[8,0,0]]
    invisible_image_array_decimal = np.apply_along_axis(convert_pixel_binary_to_decimal, 1, invisible_image_array_binary_insignificant)
    print("invisible_image_array_decimal")
    print(invisible_image_array_decimal)
    
   
    #add the two arrays together [263,255,255]
    combined_image_array = visible_image_array_decimal + invisible_image_array_decimal
    print("combined_image_array")
    print(combined_image_array)
    
    return combined_image_array 

def extract_image(combined_image_array):
    image_array_binary = np.apply_along_axis(convert_pixel_decimal_to_binary, 1, combined_image_array)
    print("image_array_binary")
    print(image_array_binary)
    
    image_array_binary_insignificant = np.apply_along_axis(get_binary_pixel_insignificant_digits, 1, image_array_binary)
    print("image_array_binary_insignificant")
    print(image_array_binary_insignificant)
    
    image_array_decimal = np.apply_along_axis(convert_pixel_binary_to_decimal, 1, image_array_binary_insignificant) 
    print("image_array_decimal")
    print(image_array_decimal)
    
    return image_array_decimal

    
