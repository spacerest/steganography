from steg import *
import cv2
import numpy as np
from PIL import Image
import pytest

IMG_DIR = './test/'

def test_compare_empty_images():
    img_array_1= np.zeros((1,1,3), np.uint8)
    img_array_2 = np.zeros((1,1,3), np.uint8)
    assert np.array_equal(img_array_1, img_array_2)

def test_compare_same_images():
    img1 = Image.open(IMG_DIR + 'test1.jpg')
    img2 = Image.open(IMG_DIR + 'test2.jpg')
    img_array_1 = np.asarray(img1)
    img_array_2 = np.asarray(img2)
    assert np.array_equal(img_array_1, img_array_2)

def test_converts_zero_from_binary_to_decimal():
    decimal = convert_binary_to_decimal('0')
    assert decimal == 0

def test_converts_zero_from_decimal_to_binary():
    binary = convert_decimal_to_binary(0)
    assert binary == '00000000'

def test_gets_byte_significant_digits():
    byte = '10100101'
    result = get_binary_significant_digits(byte)
    assert result == '10100000'

def test_gets_signficant_digits_of_binary_pixel_values():
    binary_pixel = ['11111110', '10101001', '00110010']
    result = get_binary_pixel_significant_digits(binary_pixel)
    assert np.array_equal(result, ['11110000', '10100000', '00110000'])

def test_converts_binary_pixel_to_decimal_pixel():
    binary_pixel= ['11111110', '10101001', '00110010']
    decimal_pixel_expected = [0+2+4+8+16+32+64+128, 1+0+0+8+0+32+0+128, 0+2+0+0+16+32+0+0]
    decimal_pixel = convert_pixel_binary_to_decimal(binary_pixel)
    assert np.array_equal(decimal_pixel, decimal_pixel_expected)

def test_converts_decimal_pixel_to_binary_pixel():
    decimal_pixel = [2, 8, 16]
    binary_pixel = convert_pixel_decimal_to_binary(decimal_pixel)
    assert np.array_equal(binary_pixel, ['00000010', '00001000', '00010000'])

def test_convert_invisible_significant_digits_to_insignificant_digits():
    significant_digits = '01010000'
    result = convert_binary_significant_to_insignificant(significant_digits)
    assert result == '0101'

def test_combines_one_pixel_images():
    img_array_1 = np.zeros((1,1,3), np.uint8)
    #00000000
    img_array_1[0,0] = [0,0,0]
    img_array_2 = np.zeros((1,1,3), np.uint8)
    #0100000
    img_array_2[0,0] = [128,128,128]
    #00000100 = 4
    result_img_array = combine_image_arrays(img_array_1, img_array_2)
    img_array_expected = np.zeros((1,1,3), np.uint8)
    img_array_expected[0,0] = [8,8,8]
    assert np.array_equal(result_img_array, img_array_expected)



    


# todo: delete this
#def test_raise_error_odd_num_bits():
#    with pytest.raises(ValueError):
#        original_num = '111'
#        result = get_sig_dig(original_num)
#

