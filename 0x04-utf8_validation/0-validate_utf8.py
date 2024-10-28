#!/usr/bin/python3
""" Determines if a given data set represents a valid UTF-8 encoding. """
from itertools import takewhile


def int_to_bytes(nums):
    """ Helper function that converts ints to bits """
    bytes = 0
    mask = 1 << 7
    while mask & nums:
        bytes += 1
        mask = mask >> 1
    return bytes


def validUTF8(data):
    """ Initialize a variable to keep track of the
    number of bytes expected.
    """
    num_bytes = 0

    """ Iterate through each integer in the data """
    for i in range(len(data)):
        """ Check if the most significant bit (MSB)
         is 0 (single-byte character) """
        # If single byte char, then valid..
        if num_bytes == 0:
            num_bytes = int_to_bytes(data[i])
            if num_bytes == 0:
                continue

        # At this point, byte is a multi-byte char
            if num_bytes == 1 or num_bytes > 4:
                """ UTF-8 can be 1 to 4 bytes long """
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        num_bytes -= 1
    return num_bytes == 0
