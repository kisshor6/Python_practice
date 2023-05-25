def getNumberList(filename):

    f = open(filename, 'r')
    line = f.readline()
    numbers = line.split(',')  # split the numbers separated by comma
    numberList = []  # holds the integer value
    for i in numbers:
        numberList.append(int(i))

    return numberList


def getAverage(numbers):

    sum = 0  # stores the sum of the numbers in the list
    count = 0  # keeps the count of numbers in the list
    for i in numbers:
        sum = sum + i
        count = count + 1

    average = sum/count  # calculate the average
    return average


def main():
    filename = input("Enter filename : ")
    # get the numbers from the file
    numbers = getNumberList(filename)
    # get the average from the numbers list
    average = getAverage(numbers)
    # display the average
    print("The average is:", average)


main()
