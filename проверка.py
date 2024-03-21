def one_hot_encode(labels, num_classes=None):
    if num_classes is None:
        num_classes = max(labels) + 1

    one_hot_labels = []
    for label in labels:
        one_hot = [0] * num_classes
        one_hot[label] = 1
        one_hot_labels.append(one_hot)

    return one_hot_labels

vector = [0, 2, 3, 0]
encoded_vector = one_hot_encode(vector)
print(encoded_vector)