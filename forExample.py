"""Anonymize the names using hash"""
import hashlib


with open("example.csv") as f, open('allAnonymizedNames.csv', 'w') as fout:
    for ex in f:
        list = ex.split(",")
        list[0] = hashlib.md5(list[0].encode()).hexdigest()
        fout.write(','.join(list))

