#!/usr/bin/python3

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

print(f"Current list:\n\t{vendors}")

print(f"The sorted list:\n\t{sorted(vendors)}")

print(f"The original list has not changed:\n\t{vendors}")

sortedvendors = sorted(vendors)

print(f"New variable sortedvendors:\n\t{sortedvendors}")

baksortvendors = sorted(vendors,reverse=True)

print(f"New variable baksortvendors:\n\t{baksortvendors}")

vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', 'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']

print(f"New variable vendorsdeux:\n\t{vendorsdeux}")
print(f"Sorted vendorsdeux:\n\t{sorted(vendorsdeux}")

