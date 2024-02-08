import argparse

import wandb
from sklearn import datasets
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Define sweep config
sweep_configuration = {
    "method": "random",
    "name": "sweep",
    "metric": {"goal": "maximize", "name": "accuracy"},
    "parameters": {
        "n_neighbors": {"min": 2, "max": 20},  # uniform sample value from 2 to 20
        "weights": {"values": ["uniform", "distance"]},
        "p": {"values": [1, 2, 3]},
    },
}


def main():
    run = wandb.init(project="iris-sweep")

    n_neighbors = run.config.n_neighbors
    weights = run.config.weights
    p = run.config.p

    # Load dataset
    df = datasets.load_iris()
    X = df.data
    y = df.target

    # Split into train and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    # Instantiate the model
    model = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights, p=p)

    # Get metrics
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    accuracy = cross_val_score(model, X_train, y_train, cv=kfold, scoring="accuracy").mean()
    f1_macro = cross_val_score(model, X_train, y_train, cv=kfold, scoring="f1_macro").mean()
    neg_log_loss = cross_val_score(model, X_train, y_train, cv=kfold, scoring="neg_log_loss").mean()

    # Log the results
    wandb.log({"accuracy": accuracy, "f1_macro": f1_macro, "neg_log_loss": neg_log_loss})


if __name__ == "__main__":
    sweep_id = wandb.sweep(sweep=sweep_configuration, project="iris-sweep")
    wandb.agent(sweep_id, function=main, count=10)
