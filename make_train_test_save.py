# Import modules.

import sklearn.model_selection
import random_mac

# Make a dataset.

data, labels = random_mac.dataset.make(
  2,
  oui_file="./oui.csv",
  cid_file="./cid.csv"
)

# Split the dataset.

training_data, testing_data, training_labels, testing_labels = sklearn.model_selection.train_test_split(data, labels)

# Make, train, and test a classifier.

classifier = random_mac.classifier.make()

classifier = random_mac.classifier.train(
  classifier,
  training_data,
  training_labels
)

score = random_mac.classifier.test(
  classifier,
  testing_data,
  testing_labels
)

print("score = {}%".format(str(int(100 * score))))

# Save the classifier.

random_mac.classifier.save(
  classifier,
  file="./random-mac-classifier.pickled"
)
