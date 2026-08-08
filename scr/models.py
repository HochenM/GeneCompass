from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
import xgboost as xgb


def create_linear_model():
    """Create a Linear Regression model."""
    return LinearRegression()


def create_lasso_model():
    """Create a Lasso regression model using SGD."""
    return SGDRegressor(
        penalty="l1",
        alpha=0.0001,
        learning_rate="constant",
        eta0=1e-5,
        random_state=42
    )


def create_ridge_model():
    """Create a Ridge regression model using SGD."""
    return SGDRegressor(
        penalty="l2",
        alpha=0.0001,
        learning_rate="constant",
        eta0=1e-5,
        random_state=42
    )


def create_random_forest_model():
    """Create a Random Forest regression model."""
    return RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )


def create_xgboost_model():
    """Create an XGBoost regression model."""
    return xgb.XGBRegressor(
        n_estimators=100,
        max_depth=6,
        random_state=42,
        n_jobs=-1
    )


def create_mlp_model():
    """Create an MLP regression model."""
    return MLPRegressor(
        hidden_layer_sizes=(100, 50),
        activation="relu",
        solver="adam",
        max_iter=500,
        random_state=42
    )


def get_models():
    """
    Return all regression models used in GeneCompass.
    """

    return {
        "Linear": create_linear_model(),
        "Lasso": create_lasso_model(),
        "Ridge": create_ridge_model(),
        "Random Forest": create_random_forest_model(),
        "XGBoost": create_xgboost_model(),
        "MLP": create_mlp_model()
    }
