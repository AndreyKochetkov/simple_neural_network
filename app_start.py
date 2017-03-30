import sys

# Import datasets, classifiers and performance metrics
from sklearn import datasets, metrics
from sklearn.neural_network import MLPClassifier

# The digits dataset
from input import MatrixInput
from utils import create_parser




def main():
    """
        Main function. Enter point of application
    """
    parser = create_parser()
    namespace = parser.parse_args()  # get arguments from parser

    learning_rate = namespace.lr

    data_set = datasets.load_digits()
    full_amount = len(data_set.images)
    train_amount = full_amount // 2
    if learning_rate < 0 or learning_rate > 1:
        print("Learning rate must be in interval from 0 to 1 \nYou value is: {}".format(learning_rate))
        sys.exit()

    if train_amount < 1:
        print("Train amount must be greater than 1 \nYou value is: {}".format(train_amount))
        sys.exit()

    # To apply a classifier on this data, we need to flatten the image, to
    # turn the data in a (samples, feature) matrix:
    data = data_set.images.reshape((full_amount, -1))

    # Create a classifier: a support vector classifier
    classifier = MLPClassifier(solver='sgd', activation='logistic', hidden_layer_sizes=(64,),
                               learning_rate='constant', learning_rate_init=learning_rate, verbose=True)

    # We learn the digits on the first half of the digits
    classifier.fit(data[:train_amount], data_set.target[:train_amount])

    # Now predict the value of the digit on the second half:
    expected = data_set.target[train_amount:]
    predicted = classifier.predict(data[train_amount:])

    print("Classification report for classifier %s:\n%s\n"
          % (classifier, metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

    def classify(matrix):
        return classifier.predict(matrix)

    matrix_input = MatrixInput()
    matrix_input.show(classify)


if __name__ == '__main__':
    main()
