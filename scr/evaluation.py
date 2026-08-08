import numpy as np

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

from sklearn.model_selection import cross_val_score


def evaluate_model(y_true, y_pred):
    """
    Calculate regression evaluation metrics.

    Returns
    -------
    dict
        MSE, RMSE, MAE, and R2.
    """

    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    return {
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "R2": r2
    }


def cross_validate_model(model, X, y, cv=5, scoring="r2"):
    """
    Perform k-fold cross-validation.

    Returns
    -------
    dict
        Individual scores, mean score, and standard deviation.
    """

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring=scoring
    )

    return {
        "scores": scores,
        "mean": scores.mean(),
        "std": scores.std()
    }


def compare_models(results):
    """
    Convert model evaluation results into a DataFrame.

    Parameters
    ----------
    results : list of dictionaries
        Model names and evaluation metrics.
    """

    import pandas as pd

    return pd.DataFrame(results)
