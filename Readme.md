# Kaggle Heart Failure Machine Learning Example

This repo will contain work for the [Kaggle Heart Failure Dataset](https://www.kaggle.com/fedesoriano/heart-failure-prediction)

This repo will show how to quickly create a Scikit-Learn Pipeline and ColumnTransformers to train a model and save the pickle file.

## Setup

This repo uses `pip-tools`

`pip install pip-tools`

Create a file called `requirements.in` and put high level packages there.

`pip-compile` will create the `requirements.txt` file with all of the dependencies.

Then use your standard, `pip install -r requirements.txt` or you can execute `pip-sync`.

To update the env after adding/removing from requirements.in:  `pip-compile;pip-sync`

Example
```text
# create requirements.in
# put name of package
scikit-learn
pandas


pip-compile ./requirements.in

pip-compile --upgrade-package scikit-learn

pip-sync
```

