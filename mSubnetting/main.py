"""
Matthias Holl <2023>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""
import math


def subnet_calc(number):
    # k= 2^m
    # m = log₂(k)
    k = math.log2(int(number))
    return int(k)


def bits_to_add(bits_to_shift):
    if bits_to_shift == 1:
        bit = 128
        return bit

    if bits_to_shift == 2:
        bit = 64
        return bit

    if bits_to_shift == 3:
        bit = 32
        return bit

    if bits_to_shift == 4:
        bit = 16
        return bit

    if bits_to_shift == 5:
        bit = 8
        return bit

    if bits_to_shift == 6:
        bit = 4
        return bit

    if bits_to_shift == 7:
        bit = 2
        return bit

    if bits_to_shift == 8:
        bit = 1
        return bit


def welcome(name):
    print("\033[1;31m{}\033[0m".format(name))


if __name__ == '__main__':
    welcome('mSubnetting -IPv4 Subnetting-:')

byte1 = int(input("First Octet: "))
byte2 = int(input("Second Octet: "))
byte3 = int(input("Third Octet: "))
byte4 = int(input("Fourth Octet: "))
input_suffix = int(input("Suffix: "))
number_of_subnets = int(input("How many subnets: "))
bits_to_shift = subnet_calc(int(number_of_subnets))
new_suffix = input_suffix + bits_to_shift
bit = bits_to_add(bits_to_shift)

if new_suffix == 8 or new_suffix < 8:
    for b1 in range(byte1, 255, bit):
        print(
            str(b1) + "." + str(byte2) + "." + str(byte3) + "." + str(byte4) + "/" + str(new_suffix))
elif new_suffix == 9 or new_suffix < 17:
    for b2 in range(byte2, 255, bit):
        print(
            str(byte1) + "." + str(b2) + "." + str(byte3) + "." + str(byte4) + "/" + str(new_suffix))
elif new_suffix == 17 or new_suffix < 25:
    for b3 in range(byte3, 255, bit):
        print(
            str(byte1) + "." + str(byte2) + "." + str(b3) + "." + str(byte4) + "/" + str(new_suffix))
elif new_suffix == 25 or new_suffix < 33:
    for b4 in range(byte4, 255, bit):
        print(
            str(byte1) + "." + str(byte2) + "." + str(byte3) + "." + str(b4) + "/" + str(new_suffix))
