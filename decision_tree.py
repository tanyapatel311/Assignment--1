#-------------------------------------------------------------------------
# AUTHOR: Tanya Patel
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

# encode the original categorical training features into numbers and add to the 4D array X.
age_map = {"Young": 0, "Prepresbyopic": 1, "Presbyopic": 2}
spectacle_map = {"Myope": 0, "Hypermetrope": 1}
astig_map = {"No": 0, "Yes": 1}
tear_map = {"Reduced": 0, "Normal": 1}
class_map = {"No": 0, "Yes": 1}
# X = 

# encode the original categorical training classes into numbers and add to the vector Y.
for row in db:
    age, spec, astig, tear, label = row[0], row[1], row[2], row[3], row[4]
    x_row = [age_map[age], spectacle_map[spec], astig_map[astig], tear_map[tear]]
    X.append(x_row)
    Y.append(class_map[label])
# Y =

# fitting the decision tree to the data using entropy as your impurity measure
clf = tree.DecisionTreeClassifier(criterion="entropy", random_state=0)
clf = clf.fit(X, Y)
#clf =

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()