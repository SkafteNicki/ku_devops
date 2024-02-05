import argparse

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier

models = {
    "LogisticRegression": LogisticRegression(solver="liblinear", multi_class="ovr"),
    "LinearDiscriminantAnalysis": LinearDiscriminantAnalysis(),
    "KNeighborsClassifier": KNeighborsClassifier(),
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="LogisticRegression", type=str)
    args = parser.parse_args()

    # Load dataset
    df = datasets.load_iris()
    X = df.data
    y = df.target

    # Split into train and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    # Instantiate the model
    model = models[args.model]

    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)

    # Get metrics
    accuracy = cross_val_score(model, X_train, y_train, cv=kfold, scoring="accuracy").mean()
    f1_macro = cross_val_score(model, X_train, y_train, cv=kfold, scoring="f1_macro").mean()
    neg_log_loss = cross_val_score(model, X_train, y_train, cv=kfold, scoring="neg_log_loss").mean()
