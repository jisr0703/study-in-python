import string
import re


TEST_CASE0 = '172.2.10.1'
TEST_CASE1 = '172.2.0.1'
TEST_CASE2 = '172.2.10.01'
TEST_CASE3 = '172.2.1110.01'
TEST_CASE4 = '172..1110.01'
TEST_CASE5 = '2022:0bc3:0000:0000:853e:0777:1234:0'
TEST_CASE6 = '2022:0bc3:0000::853e:0777:1234:0'
TEST_CASE7 = '2022:0bc3:0000::4853e:0777:1234:0'
TEST_CASE8 = '2022:0bg3:0000::4853e:0777:1234:0'
TEST_CASE9 = '2022:0bg3:0000::4853e:0777:1234:0:1239'
TEST_CASE10 = '2022:0bc3:0000:0000:e853e:0777:1234:0'
TEST_CASE11 = '2022:0bc3:0000:0000:853E:0777:1234:0'


def protocol_inspection_idea1(ip: str) -> str:
    if ip.count('.') == 3:
        if IPv4_inspection(ip):
            return 'IPv4'

    if ip.count(':') == 7:
        if IPv6_inspection(ip):
            return 'IPv6'

    return 'Neither'


def IPv4_inspection(ipv4: str) -> bool:
    ip_nums = ipv4.split('.')

    if len(ip_nums) != 4:
        return False

    for i in ip_nums:
        if len(i) == 0 or (i[0] == '0' and len(i) != 1) or not i.isdigit() or (0 > int(i) or int(i) > 255):
            return False

    return True


def IPv6_inspection(ipv6: str) -> bool:
    ip_nums = ipv6.split(':')

    if len(ip_nums) != 8:
        return False

    for i in ip_nums:
        if len(i) == 0 or not all(j in string.hexdigits for j in i) or (int(i, 16) < 0 or int(i, 16) > int('ffff', 16)):
            return False

    return True


def protocol_inspection_idea2(ip: str) -> str:
    ipv4_num_pattern = '(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'
    ipv4 = re.compile(r'^({p}\.){{3}}{p}$'.format(p=ipv4_num_pattern))

    if ipv4.match(ip):
        return 'IPv4'

    ipv6_num_pattern = '([0-9a-f]{1,4})'
    ipv6 = re.compile(r'^({p}\:){{7}}{p}$'.format(p=ipv6_num_pattern), re.IGNORECASE)

    if ipv6.match(ip):
        return 'IPv6'

    return 'Neither'


print(protocol_inspection_idea1(TEST_CASE0))
print(protocol_inspection_idea1(TEST_CASE1))
print(protocol_inspection_idea1(TEST_CASE2))
print(protocol_inspection_idea1(TEST_CASE3))
print(protocol_inspection_idea1(TEST_CASE4))
print(protocol_inspection_idea1(TEST_CASE5))
print(protocol_inspection_idea1(TEST_CASE6))
print(protocol_inspection_idea1(TEST_CASE7))
print(protocol_inspection_idea1(TEST_CASE8))
print(protocol_inspection_idea1(TEST_CASE9))
print(protocol_inspection_idea1(TEST_CASE10))
print(protocol_inspection_idea1(TEST_CASE11))
print('-----')
print(protocol_inspection_idea2(TEST_CASE0))
print(protocol_inspection_idea2(TEST_CASE1))
print(protocol_inspection_idea2(TEST_CASE2))
print(protocol_inspection_idea2(TEST_CASE3))
print(protocol_inspection_idea2(TEST_CASE4))
print(protocol_inspection_idea2(TEST_CASE5))
print(protocol_inspection_idea2(TEST_CASE6))
print(protocol_inspection_idea2(TEST_CASE7))
print(protocol_inspection_idea2(TEST_CASE8))
print(protocol_inspection_idea2(TEST_CASE9))
print(protocol_inspection_idea2(TEST_CASE10))
print(protocol_inspection_idea2(TEST_CASE11))
