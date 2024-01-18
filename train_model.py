import pandas as pd
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import joblib

x = pd.read_csv("x.csv", sep="\t")
y = pd.read_csv("y.csv", sep="\t")

# save mode of each feature in order to assign these values as default at the patient to be filled in the form
x.mode().to_csv("x_mode.csv", sep="\t", index=False)

# Evaluate using Cross Validation
num_folds = 5
seed = 42

kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
kfold.get_n_splits(x)
print(kfold)

# Create the parameter grid based on the results of random search
param_grid = {
    'n_estimators': [10, 20, 30],
    'max_depth': [3, 4, 5],
    'min_samples_leaf': [4, 3, 2],
    'min_samples_split': [5, 4, 3],
    'max_features': ["sqrt", "log2"],
    'bootstrap': [False],
    'random_state': [42]
}
# Create a based model
rf = RandomForestClassifier()
# Instantiate the grid search model
model_grid = GridSearchCV(estimator=rf, param_grid=param_grid,
                          cv=kfold, n_jobs=-1)
model_grid.fit(x, y)

model = model_grid.best_estimator_

# Save the model using joblib
joblib.dump(model, "rf_tbd_other_Dec12_23.joblib")
