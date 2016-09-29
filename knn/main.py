import csv
import math
import operator


def load_data_set(filename):
    with open(filename, newline='') as iris:
        data_reader = csv.reader(iris, delimiter=',')
        return list(data_reader)


def string_to_float(data_set):
    new_set = []
    for data in data_set:
        new_set.append([float(x) for x in data[0:len(data)-1]] + [data[len(data)-1]])
    return new_set


def get_classes(training_set):
    return list(set([c[-1] for c in training_set]))


def find_euclidean_distance(sample, training_set, attributes):
    distances = []
    dist = 0
    for data in training_set:
        for x in range(attributes):
            dist += (data[x] - sample[x]) ** 2
        distances.append((data, math.sqrt(dist)))
        dist = 0
    distances.sort(key=operator.itemgetter(1))
    return distances


def find_neighbors(distances, k):
    return distances[0:k]


def find_response(neighbors, classes):
    votes = [0] * len(classes)

    for instance, _ in neighbors:
        for ctr, c in enumerate(classes):
            if instance[-1] == c:
                votes[ctr] += 1

    return max(enumerate(votes), key=operator.itemgetter(1))


def main():
    try:
        # get value of k
        k = int(input('Enter the value of k : '))

        # load the training data set
        training_file = input('Enter name of training data file : ')
        training_set = load_data_set(training_file)

        # convert string data to float
        training_set = string_to_float(training_set)

        # generate response classes from data set
        classes = get_classes(training_set)

        # load test data set
        test_file = input('Enter name of test data file : ')
        test_set = load_data_set(test_file)

        n = len(test_set)
        # convert string data to float
        test_set = string_to_float(test_set)

        for ctr in range(n):
            # calculate distance from each instance in training data
            distances = find_euclidean_distance(test_set[ctr], training_set, len(classes))

            # find k nearest neighbors
            neighbors = find_neighbors(distances, k)

            # get the class with maximum votes
            index, value = find_response(neighbors, classes)

            print('The predicted class for sample ' + str(ctr + 1) + ' is : ' + classes[index])
            print('Number of votes : ' + str(value) + ' out of ' + str(k))

    except ValueError:
        print('Input is not a number')


if __name__ == '__main__':
    main()
