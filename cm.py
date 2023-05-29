import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Actual and predicted sections for a single person
actual_sections = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
predicted_sections = ['A', 'B', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'C']

# Define the list of all possible sections
all_sections = ['A', 'B', 'C']

# Calculate the confusion matrix
confusion_mat = confusion_matrix(actual_sections, predicted_sections, labels=all_sections)

# Plot the confusion matrix
plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.colorbar()
tick_marks = np.arange(len(all_sections))
plt.xticks(tick_marks, all_sections, rotation=45)
plt.yticks(tick_marks, all_sections)
plt.xlabel("Predicted Section")
plt.ylabel("Actual Section")

# Add labels to each cell
thresh = confusion_mat.max() / 2.0
for i in range(len(all_sections)):
    for j in range(len(all_sections)):
        plt.text(j, i, format(confusion_mat[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if confusion_mat[i, j] > thresh else "black")

plt.tight_layout()
plt.show()
