#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

import random


def get_random_string(length):
    # result_str store the string generated by this code
    sample_letters = 'adcdefghijklmnopkrstuvxwyzADCDEFGHIJKLMNOPKRSTUVXWYZ1234567890'
    result_str = ''.join((random.choice(sample_letters) for i in range(length)))
    return result_str




