import argparse
import wandb
import seaborn as sns

from sklearn.model_selection import cross_val_score
from sklearn import datasets
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

models = {
    'LogisticRegression': LogisticRegression(solver='liblinear', multi_class='ovr'),
    'LinearDiscriminantAnalysis': LinearDiscriminantAnalysis(),
    'KNeighborsClassifier': KNeighborsClassifier(),
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default='LogisticRegression', type=str)
    args = parser.parse_args()

    run = wandb.init(project='iris', config={'model': args.model})

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
    accuracy = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy').mean()
    f1_macro = cross_val_score(model, X_train, y_train, cv=kfold, scoring='f1_macro').mean()
    neg_log_loss = cross_val_score(model, X_train, y_train, cv=kfold, scoring='neg_log_loss').mean()

    # Log the results
    wandb.log({'accuracy': accuracy,
                'f1_macro': f1_macro,
                'neg_log_loss': neg_log_loss})


    # Plot the training points
    fig = sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=df.target_names[y],
        alpha=1.0,
        edgecolor="black",
    )
    wandb.log({'data_scatter': wandb.Image(fig)})

    # Train single model on all data
    model = models[args.model]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_probas = model.predict_proba(X_test)

    # Try out scikit-learn integration
    labels = df.feature_names
    wandb.sklearn.plot_class_proportions(y_train, y_test, labels)
    wandb.sklearn.plot_learning_curve(model, X_train, y_train)
    wandb.sklearn.plot_roc(y_test, y_probas, labels)
    wandb.sklearn.plot_precision_recall(y_test, y_probas, labels)
    wandb.sklearn.plot_confusion_matrix(y_test, y_pred, labels)