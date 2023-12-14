#!/bin/bash

def main():
    data = []
    read_data()

def read_data(data):
    import csv
    with open('app1.data', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            data.append(list(map(float, row)))
    length_d = len(data)

if __name__ == '__main__':
    main()
