import csv
import math
import operator


def load_data_set(filename):
    with open(filename, newline='') as iris:
        data_reader = csv.reader(iris, delimiter=',')
        return list(data_reader)


def get_classes(training_set, classes):
    for instance in training_set:
        if instance[len(instance)-1] not in classes:
            classes.append(instance[len(instance)-1])


def find_euclidean_distance(sample, training_set, attributes, distances):
    dist = 0
    for ctr in range(len(training_set)):
        for x in range(attributes):
            dist += (float(training_set[ctr][x]) - sample[x]) ** 2
        distances.append((training_set[ctr], math.sqrt(dist)))
        dist = 0
    distances.sort(key=operator.itemgetter(1))


def find_neighbors(distances, neighbors, k):
    for ctr in range(k):
        neighbors.append(distances[ctr])


def find_response(neighbors, classes):
    votes = [0, 0, 0]

    for instance in neighbors:
        neighbor = instance.__getitem__(0)
        for ctr in range(len(classes)):
            if neighbor[len(neighbor)-1] == classes[ctr]:
                votes[ctr] += 1;
    return max(enumerate(votes), key=operator.itemgetter(1))


def main():
    k = 3
    # training_set = list()
    neighbors = list()
    distances = list()
    classes = list()
    file = 'iris-dataset.csv'
    attributes = 4

    # load the Iris data set
    training_set = load_data_set(file)

    # generate response classes from data set
    get_classes(training_set, classes)

    # test data
    test_instance = [5.4, 3.2, 1.5, 0.3]

    # calculate distance from each instance in training data
    find_euclidean_distance(test_instance, training_set, attributes, distances)

    # find k nearest neighbors
    find_neighbors(distances, neighbors, k)

    # get the class with maximum votes
    index, value = find_response(neighbors, classes)
    print('The predicted class is : ' + classes[index])
    print('Number of votes : ' + str(value) + ' out of ' + str(k))


if __name__ == '__main__':
    main()
