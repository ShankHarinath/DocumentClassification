# Document Classification

##Techniques:

* SVM (RBF Kernel) - 73.0193501278 %
* Linear SVM with Stocastic Gradient Descent
  - 80-20 split:
    - Accuracy: 99.1967871486 %
    - Precision/class: (0.99595551,  0.97634691)
    - Recall/class: (0.99094567,  0.98934754)
    - F1 Score/class: (0.99344428,  0.98280423)
  
  - 5-fold cross validation: [99.379335523913837, 99.233296823658268, 99.379108838568297, 98.940832724616512, 96.018991964937905]
  
Loss function: Hinge loss

# Edge case 2 handled!

#Information Retreival:
Symptoms, causes, prognosis, prevention and treatment information for a given document will be extracted, if exists.

# Execution Procedure:

`python driver.py` will run both classification adn the informtaion retreival.
Informtaion retreival happens for an individual file. We need to pass the entire file path in the 'driver.py' file.

