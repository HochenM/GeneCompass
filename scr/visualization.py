import matplotlib.pyplot as plt


def plot_prediction_vs_actual(
    y_true,
    y_pred,
    save_path=None
):
    """
    Plot predicted DON values against actual DON values.
    """

    plt.figure(figsize=(8, 6))

    plt.scatter(y_true, y_pred)

    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())

    plt.plot(
        [min_val, max_val],
        [min_val, max_val],
        linestyle="--"
    )

    plt.xlabel("Actual DON")
    plt.ylabel("Predicted DON")
    plt.title("Prediction vs Actual - Best Model")

    plt.tight_layout()

    if save_path:
        plt.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()


def plot_residuals(
    y_true,
    y_pred,
    save_path=None
):
    """
    Plot residuals against predicted values.
    """

    residuals = y_true - y_pred

    plt.figure(figsize=(8, 6))

    plt.scatter(
        y_pred,
        residuals,
        alpha=0.7
    )

    plt.axhline(
        y=0,
        linestyle="--"
    )

    plt.xlabel("Predicted DON")
    plt.ylabel("Residuals")
    plt.title("Residual Plot - Best Model")

    plt.tight_layout()

    if save_path:
        plt.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()


def plot_residual_histogram(
    y_true,
    y_pred,
    save_path=None,
    bins=20
):
    """
    Plot the distribution of residuals.
    """

    residuals = y_true - y_pred

    plt.figure(figsize=(8, 6))

    plt.hist(
        residuals,
        bins=bins,
        edgecolor="black"
    )

    plt.axvline(
        x=0,
        linestyle="--"
    )

    plt.xlabel("Residual")
    plt.ylabel("Frequency")
    plt.title("Residual Distribution - Best Model")

    plt.tight_layout()

    if save_path:
        plt.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()
