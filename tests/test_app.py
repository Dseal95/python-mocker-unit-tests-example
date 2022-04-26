from modules.app import run_app
import pandas as pd

import pytest


def create_synthetic_test_data():
    """Generate fake test data."""
    df = pd.DataFrame(
        data=list(zip([1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3])),
        columns=["A", "B", "C"],
    )

    return df


def test_e2e_app_run(mocker):
    """Test e2e app run locally."""
    # mock get_data_from_cloud_database() & write_processed_data_back_to_cloud_database()
    mocker.patch(
        "modules.app.get_data_from_cloud_database",
        return_value=create_synthetic_test_data(),
    )
    mocker.patch(
        "modules.app.write_processed_data_back_to_cloud_database", return_value=None
    )

    # run run_app() function to test e2e
    actual = run_app()

    desired = pd.DataFrame(
        data=list(zip([-1, -1, -1, -1, -1], [2, 2, 2, 2, 2], [-3, -3, -3, -3, -3])),
        columns=["A", "B", "C"],
    )

    assert actual.equals(desired)
