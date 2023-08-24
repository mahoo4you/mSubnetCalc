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

one_bits = "1"
zero_bits = "0"
max_bit = 32
min_bit = 1


def subnet_calc(number):
    # k= 2^m
    # m = log₂(k)
    k = math.log2(int(number))
    return int(k)


def get_bits(bits_to_shift):
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


def netmask_bit_to_dez(bit):
    net_okt_dez = 0
    if bit == 8:
        net_okt_dez = 255
    elif bit != 8:
        net_okt_dez = 0
        if bit == 7:
            net_okt_dez = 254
        elif bit != 7:
            net_okt_dez = 0
            if bit == 6:
                net_okt_dez = 252
            elif bit != 6:
                net_okt_dez = 0
                if bit == 5:
                    net_okt_dez = 248
                elif bit != 5:
                    net_okt_dez = 0
                    if bit == 4:
                        net_okt_dez = 240
                    elif bit != 4:
                        net_okt_dez = 0
                        if bit == 3:
                            net_okt_dez = 224
                        elif bit != 3:
                            net_okt_dez = 0
                            if bit == 2:
                                net_okt_dez = 192
                            elif bit != 2:
                                net_okt_dez = 0
                                if bit == 1:
                                    net_okt_dez = 128
                                elif bit != 1:
                                    net_okt_dez = 0
    return net_okt_dez


def welcome(name):
    print(format(name))


if __name__ == '__main__':
    welcome('IPv4 Subnetting-:')

byte1 = int(input("First Octet: "))
byte2 = int(input("Second Octet: "))
byte3 = int(input("Third Octet: "))
byte4 = int(input("Fourth Octet: "))
input_suffix = int(input("Suffix: "))
number_of_subnets = int(input("How many subnets: "))
bits_to_shift = subnet_calc(int(number_of_subnets))
new_suffix = input_suffix + bits_to_shift

for i in range(1, new_suffix + min_bit):
    one_bit_result = i * one_bits
    bit = max_bit - new_suffix
    for x in range(bit + min_bit):
        zero_bit_result = x * zero_bits
    netmask_str = one_bit_result + zero_bit_result

netmask_okt1 = netmask_str[:8]
netmask_list = [netmask_okt1]
netmask_okt2 = netmask_str[8:16]
netmask_list.append(netmask_okt2)
netmask_okt3 = netmask_str[16:24]
netmask_list.append(netmask_okt3)
netmask_okt4 = netmask_str[24:32]
netmask_list.append(netmask_okt4)

for i in range(1):
    bit = netmask_okt1.count("1")
    netmask_byte1 = netmask_bit_to_dez(bit)
    bit_add1 = get_bits(bit)
    bit = netmask_okt2.count("1")
    bit_add2 = get_bits(bit)
    netmask_byte2 = netmask_bit_to_dez(bit)
    bit = netmask_okt3.count("1")
    bit_add3 = get_bits(bit)
    netmask_byte3 = netmask_bit_to_dez(bit)
    bit = netmask_okt4.count("1")
    bit_add4 = get_bits(bit)
    netmask_byte4 = netmask_bit_to_dez(bit)

netadress_byte1 = int(netmask_byte1) & int(byte1)
netadress_byte2 = int(netmask_byte2) & int(byte2)
netadress_byte3 = int(netmask_byte3) & int(byte3)
netadress_byte4 = int(netmask_byte4) & int(byte4)

if new_suffix == 8 or new_suffix < 8:
    for b1 in range(netadress_byte1, 255, bit_add1):
        print(
            str(b1) + "." + str(netadress_byte2) + "." + str(netadress_byte3) + "." + str(netadress_byte4) + "/" + str(
                new_suffix))
elif new_suffix == 9 or new_suffix < 17:
    for b2 in range(netadress_byte2, 255, bit_add2):
        print(
            str(netadress_byte1) + "." + str(b2) + "." + str(netadress_byte3) + "." + str(netadress_byte4) + "/" + str(
                new_suffix))
elif new_suffix == 17 or new_suffix < 25:
    for b3 in range(netadress_byte3, 255, bit_add3):
        print(
            str(netadress_byte1) + "." + str(netadress_byte2) + "." + str(b3) + "." + str(netadress_byte4) + "/" + str(
                new_suffix))
elif new_suffix == 25 or new_suffix < 33:
    for b4 in range(netadress_byte4, 255, bit_add4):
        print(
            str(netadress_byte1) + "." + str(netadress_byte2) + "." + str(netadress_byte3) + "." + str(b4) + "/" + str(
                new_suffix))
