import random_mac
import sklearn.model_selection
import mac_attrs
import pytest

# This fixture approximates `oui.csv`, a file needed by the classifier.

@pytest.fixture
def oui_file(tmp_path):
  # Create a temporary subdirectory if one does not already exist.
  subdirectory = tmp_path.joinpath("subdirectory")

  try:
    subdirectory.mkdir()
  except FileExistsError:
    pass

  # Create a temporary file in the subdirectory.
  file = subdirectory.joinpath("oui.csv")
  file.write_text("Assignment,\na0b1c2,\n")

  # Yield the file.
  yield file

# This fixture approximates `cid.csv`, a file needed by the classifier.

@pytest.fixture
def cid_file(tmp_path):
  # Create a temporary subdirectory if one does not already exist.
  subdirectory = tmp_path.joinpath("subdirectory")

  try:
    subdirectory.mkdir()
  except FileExistsError:
    pass

  # Create a temporary file in the subdirectory.
  file = subdirectory.joinpath("cid.csv")
  file.write_text("Assignment,\n0a1b2c,\n")

  # Yield the file.
  yield file

# This fixture represents the classifier used by the app.

@pytest.fixture
def classifier(oui_file, cid_file):
  data, labels = random_mac.dataset.make(
    1, 
    oui_file=oui_file, 
    cid_file=cid_file
  )
  
  training_data, testing_data, training_labels, testing_labels = sklearn.model_selection.train_test_split(data, labels)

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

  return classifier

# This fixture represents the path to the pickled classifer.

@pytest.fixture
def pickle(tmp_path, classifier):
  # Create a temporary subdirectory if one does not already exist.
  subdirectory = tmp_path.joinpath("subdirectory")

  try:
    subdirectory.mkdir()
  except FileExistsError:
    pass

  # Create a path to a pickle file in the subdirectory.
  file = subdirectory.joinpath("test-classifier.pickled")

  # Save (pickle) a classifier.
  random_mac.classifier.save(classifier, file)

  # Yield the path.
  yield file

# This fixture represents an instance of the app.

@pytest.fixture
def app(pickle):
  yield mac_attrs.make_app(file=pickle)

# This fixture represents a web client.

@pytest.fixture
def client(app):
  return app.test_client()
