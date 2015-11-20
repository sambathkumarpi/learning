import csv

fname = raw_input("give the file name: ")
# read the test data file
with open(fname, "r") as fin:
    reader = csv.reader(fin)
    # create a dictionary of ids:frequency pairs
    ids_freq = {} 
    for row in reader:
        print(row)  # test
        ids, name = row 
        ids_freq[ids] = ids_freq.get(ids, 0) + 1

print('-'*70)

# refresh reader object
with open(fname, "r") as fin:
    reader = csv.reader(fin)
    # make a list of all rows that have duplicate ids's
    duplicate_ids = []
    for row in reader:
        ids, name = row
        # add row to list if ids frequency is above 1
        if ids_freq[ids] > 1:
            duplicate_ids.append(row)


# show results
import pprint
pprint.pprint(ids_freq)
print('-'*70)
pprint.pprint(sorted(duplicate_ids))



