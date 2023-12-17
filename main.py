from backpropagation import backpropagation

def main():
    data = []
    read_data(data)
    
    print("please set a learningrate: ", end='')
    learning_rate = input()
    backpropagation()
    

def read_data(data):
    import csv
    with open('data.txt', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            data.append(list(row))
    

if __name__ == '__main__':
    main()
