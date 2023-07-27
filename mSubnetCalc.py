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
one_bits = "1"
zero_bits = "0"
max_bit = 32
min_bit = 1


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


print("IPv4 Subnet Calculator\n")
ipv4_okt1 = input("First Octet: ")
ipv4_okt2 = input("Second Octet: ")
ipv4_okt3 = input("Third Octet: ")
ipv4_okt4 = input("Fourth Octet: ")
input_suffix = input("Suffix: ")
int_suffix = int(input_suffix)
for i in range(1, int_suffix + min_bit):
    one_bit_result = i * one_bits
    bit = max_bit - int_suffix
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

print("netmask: ", netmask_list)
for i in range(1):
    bit = netmask_okt1.count("1")
    netmask_byte1 = netmask_bit_to_dez(bit)
    bit = netmask_okt2.count("1")
    netmask_byte2 = netmask_bit_to_dez(bit)
    bit = netmask_okt3.count("1")
    netmask_byte3 = netmask_bit_to_dez(bit)
    bit = netmask_okt4.count("1")
    netmask_byte4 = netmask_bit_to_dez(bit)
    print("netmask decimal:",
          str(netmask_byte1) + "." + str(netmask_byte2) + "." + str(netmask_byte3) + "." + str(netmask_byte4))
ipv4_list = [bin(int(ipv4_okt1)), bin(int(ipv4_okt2)), bin(int(ipv4_okt3)), bin(int(ipv4_okt4))]
print("IPv4: ", ipv4_list)
print("IPv4 decimal:",
      ipv4_okt1 + "." + ipv4_okt2 + '.' + ipv4_okt3 + '.' + ipv4_okt4 + "/" + str(int_suffix))

netadress_byte1 = int(netmask_byte1) & int(ipv4_okt1)
netadress_byte2 = int(netmask_byte2) & int(ipv4_okt2)
netadress_byte3 = int(netmask_byte3) & int(ipv4_okt3)
netadress_byte4 = int(netmask_byte4) & int(ipv4_okt4)

if int_suffix == 8 or int_suffix < 8:
    res_byte1 = 255 - netmask_byte1
    last_ip_byte1 = netadress_byte1 + res_byte1

    res_byte2 = 255 - netmask_byte2
    last_ip_byte2 = netadress_byte2 + res_byte2

    res_byte3 = 255 - netmask_byte3
    last_ip_byte3 = netadress_byte3 + res_byte3

    res_byte4 = 255 - netmask_byte4
    last_ip_byte4 = netadress_byte4 + res_byte4

elif int_suffix == 9 or int_suffix < 17:
    res_byte1 = 255 - netmask_byte1
    last_ip_byte1 = netadress_byte1 + res_byte1

    res_byte2 = 255 - netmask_byte2
    last_ip_byte2 = netadress_byte2 + res_byte2

    res_byte3 = 255 - netmask_byte3
    last_ip_byte3 = netadress_byte3 + res_byte3

    res_byte4 = 255 - netmask_byte4
    last_ip_byte4 = netadress_byte4 + res_byte4

elif int_suffix == 17 or int_suffix < 25:
    res_byte1 = 255 - netmask_byte1
    last_ip_byte1 = netadress_byte1 + res_byte1

    res_byte2 = 255 - netmask_byte2
    last_ip_byte2 = netadress_byte2 + res_byte2

    res_byte3 = 255 - netmask_byte3
    last_ip_byte3 = netadress_byte3 + res_byte3

    res_byte4 = 255 - netmask_byte4
    last_ip_byte4 = netadress_byte4 + res_byte4

elif int_suffix == 25 or int_suffix < 33:
    res_byte1 = 255 - netmask_byte1
    last_ip_byte1 = netadress_byte1 + res_byte1

    res_byte2 = 255 - netmask_byte2
    last_ip_byte2 = netadress_byte2 + res_byte2

    res_byte3 = 255 - netmask_byte3
    last_ip_byte3 = netadress_byte3 + res_byte3

    res_byte4 = 255 - netmask_byte4
    last_ip_byte4 = netadress_byte4 + res_byte4
calc_hosts = 32 - int_suffix
total_hosts = (2 ** calc_hosts) - 2

print("Netadress: " +
      str(netadress_byte1) + "." + str(netadress_byte2) + "." + str(netadress_byte3) + "." + str(netadress_byte4))
first_ip_byte4 = int(netadress_byte4 + 1)
print("First IP: " + str(netadress_byte1) + "." + str(netadress_byte2) + "." + str(netadress_byte3) + "." + str(
    first_ip_byte4))
print("Last IP: ", str(last_ip_byte1) + "." + str(last_ip_byte2) + "." + str(last_ip_byte3) + "." + str(
    last_ip_byte4 - 1))
print("Broadcast: ", str(last_ip_byte1) + "." + str(last_ip_byte2) + "." + str(last_ip_byte3) + "." + str(
    last_ip_byte4))
print("Total Hosts: ", total_hosts)
