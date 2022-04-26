import pandas as pd


def get_data_from_cloud_database(key):
    """Connect to an api's database and retreive data."""
    if key is None:
        raise ConnectionError("Cannot connect to database.")


def do_some_calculation(data: pd.DataFrame, column: str):
    """Return the inputted data with the specified column's values multiplied by -1 (signs flipped).

    Args:
        data (pd.DataFrame): Input data.
        column (str): column in data to be multiplied by -1.

    Returns:
        pd.DataFrame: DataFrame with a reversed sign column.
    """
    # flip the sign of an entire numerical column of data.
    data[column] = -1 * data[column]

    return data


def write_processed_data_back_to_cloud_database():
    """Connect to an api's database and retreive data."""
    raise ConnectionError("Cannot write data back to database.")


def run_app():
    """Run app."""

    df = get_data_from_cloud_database(key=None)
    df = do_some_calculation(data=df, column="A")
    df = do_some_calculation(data=df, column="C")

    write_processed_data_back_to_cloud_database()

    return df
