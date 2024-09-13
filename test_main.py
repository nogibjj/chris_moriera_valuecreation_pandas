from main import (
    dataset_import,
    data_modeling,
    calculate_mean,
    calculate_median_value_creation,
    calculate_std_value_creation,
    plot_value_creation_by_industry,
)
import os


def test_import():
    df = dataset_import()
    assert not df.empty, "Dataset import failed: DataFrame is empty"
    assert (
        "Valuation" in df.columns and "Funding" in df.columns
    ), "Missing essential columns in imported data"
    print("test_import passed.")


def test_modeling():
    df_raw = dataset_import()
    df = data_modeling(df_raw)
    assert not df.empty, "Data modeling failed: DataFrame is empty"
    assert (
        "value_creation" in df.columns
    ), "value_creation column missing after modeling"
    assert (
        df["value_creation"] >= -1e12
    ).all(), "Some value_creation values seem unexpectedly low"
    print("test_modeling passed.")


def test_mean():
    df_raw = dataset_import()
    df = data_modeling(df_raw)
    mean_value = calculate_mean(df)
    assert isinstance(mean_value, float), "Mean value creation is not a float"
    print("test_mean passed.")


def test_median():
    df_raw = dataset_import()
    df = data_modeling(df_raw)
    median_value = calculate_median_value_creation(df)
    assert isinstance(median_value, float), "Median value creation is not a float"
    print("test_median passed.")


def test_stddev():
    df_raw = dataset_import()
    df = data_modeling(df_raw)
    std_value = calculate_std_value_creation(df)
    assert isinstance(std_value, float), "Standard deviation is not a float"
    assert std_value >= 0, "Standard deviation should not be negative"
    print("test_stddev passed.")


def test_plot():
    df_raw = dataset_import()
    df = data_modeling(df_raw)
    save_dir = r"C:/Users/chris/Downloads/IDS706/chris_moriera_valuecreation_pandas/"
    try:
        plot_value_creation_by_industry(df, save_dir)
        assert os.path.exists(
            os.path.join(save_dir, "value_creation_boxplot.png")
        ), "Plot not saved successfully"
        print("test_plot passed.")
    except Exception as e:
        assert False, f"Plotting failed with error: {str(e)}"


if __name__ == "__main__":
    test_import()
    test_mean()
    test_median()
    test_modeling()
    test_stddev()
    test_plot()
    print("All tests complete & passed!")
