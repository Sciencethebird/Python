
acquaintance = {'Yahan': 'My junior high crush', 'Heng Li':'my religious brother', 'Robert':'My college roommate'}
print(acquaintance)

print("Use key to dereference: ", acquaintance['Yahan'])

print("\nValues in dictionary")
for k in acquaintance:
    print(k)

print()
# keys / values
print('{:8}'.format('keys'), acquaintance.keys())
print('{:8}'.format('values') ,acquaintance.values())
print()

# items()
for k, v in acquaintance.items():
    print("Key: {0:8}, Value: {1}".format(k,v))