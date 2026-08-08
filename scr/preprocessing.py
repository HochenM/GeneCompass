import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(path):
    """Load the processed genomic dataset."""
    df = pd.read_csv(path)
    return df


def prepare_features_target(df):
    """
    Separate target, genotype identifiers, and SNP features.

    Returns
    -------
    X : pandas.DataFrame
        SNP feature matrix.
    y : pandas.Series
        DON target.
    genotypes : pandas.DataFrame
        Genotype identifiers.
    """

    y = df["DON"]
    genotypes = df[["Genotype"]].copy()

    X = df.drop(columns=["DON", "Genotype"]).copy()
    X = X.astype("float32")

    return X, y, genotypes


def split_data(X, y, test_size=0.2, random_state=42):
    """Split data into training and test sets."""

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def scale_data(X_train, X_test):
    """
    Standardize training and test features.

    The scaler is fitted only on training data.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler
