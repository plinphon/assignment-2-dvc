"""Tests for load_data module."""

import numpy as np
import pandas as pd

from src.load_data import get_features


class TestGetFeatures:
    """Test cases for the get_features function."""

    def test_get_features_column_renaming(self) -> None:
        """Test that column names are properly renamed."""
        # Create test DataFrame with iris-like column names
        test_data = pd.DataFrame(
            {
                "sepal length (cm)": [5.1, 4.9, 4.7],
                "sepal width (cm)": [3.5, 3.0, 3.2],
                "petal length (cm)": [1.4, 1.4, 1.3],
                "petal width (cm)": [0.2, 0.2, 0.2],
                "target": [0, 0, 0],
            }
        )

        result = get_features(test_data)

        # Check that column names are properly renamed
        expected_columns = [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "target",
        ]

        assert list(result.columns) == expected_columns

    def test_get_features_preserves_data(self) -> None:
        """Test that data values are preserved during transformation."""
        test_data = pd.DataFrame(
            {
                "sepal length (cm)": [5.1, 4.9, 4.7],
                "sepal width (cm)": [3.5, 3.0, 3.2],
                "petal length (cm)": [1.4, 1.4, 1.3],
                "petal width (cm)": [0.2, 0.2, 0.2],
                "target": [0, 0, 0],
            }
        )

        result = get_features(test_data)

        # Check that data values are preserved
        assert result["sepal_length"].tolist() == [5.1, 4.9, 4.7]
        assert result["sepal_width"].tolist() == [3.5, 3.0, 3.2]
        assert result["petal_length"].tolist() == [1.4, 1.4, 1.3]
        assert result["petal_width"].tolist() == [0.2, 0.2, 0.2]
        assert result["target"].tolist() == [0, 0, 0]

    def test_get_features_returns_copy(self) -> None:
        """Test that function returns a copy, not modifying original."""
        test_data = pd.DataFrame(
            {
                "sepal length (cm)": [5.1, 4.9],
                "sepal width (cm)": [3.5, 3.0],
                "target": [0, 1],
            }
        )

        original_columns = test_data.columns.tolist()
        result = get_features(test_data)

        # Original DataFrame should be unchanged
        assert test_data.columns.tolist() == original_columns
        # Result should have different columns
        assert result.columns.tolist() != original_columns

    def test_get_features_empty_dataframe(self) -> None:
        """Test function behavior with empty DataFrame."""
        test_data = pd.DataFrame()
        result = get_features(test_data)

        assert result.empty
        assert isinstance(result, pd.DataFrame)

    def test_get_features_single_row(self) -> None:
        """Test function with single row DataFrame."""
        test_data = pd.DataFrame(
            {"sepal length (cm)": [5.1], "sepal width (cm)": [3.5], "target": [0]}
        )

        result = get_features(test_data)

        assert len(result) == 1
        assert list(result.columns) == ["sepal_length", "sepal_width", "target"]
        assert result["sepal_length"].iloc[0] == 5.1

    def test_get_features_no_cm_columns(self) -> None:
        """Test function with columns that don't contain '(cm)'."""
        test_data = pd.DataFrame(
            {"feature one": [1, 2, 3], "feature two": [4, 5, 6], "target": [0, 1, 0]}
        )

        result = get_features(test_data)

        # Columns should still be processed (spaces replaced with underscores)
        expected_columns = ["feature_one", "feature_two", "target"]
        assert list(result.columns) == expected_columns

    def test_get_features_mixed_column_types(self) -> None:
        """Test function with mixed data types."""
        test_data = pd.DataFrame(
            {
                "sepal length (cm)": [5.1, 4.9, 4.7],
                "sepal width (cm)": [3.5, 3.0, 3.2],
                "target": [0, 1, 2],
                "species": ["setosa", "versicolor", "virginica"],
            }
        )

        result = get_features(test_data)

        # Check that all data types are preserved
        assert result["sepal_length"].dtype == np.float64
        assert result["target"].dtype == np.int64
        assert result["species"].dtype == object

    def test_get_features_with_nan_values(self) -> None:
        """Test function behavior with NaN values."""
        test_data = pd.DataFrame(
            {
                "sepal length (cm)": [5.1, np.nan, 4.7],
                "sepal width (cm)": [3.5, 3.0, np.nan],
                "target": [0, 1, 2],
            }
        )

        result = get_features(test_data)

        # NaN values should be preserved
        assert pd.isna(result["sepal_length"].iloc[1])
        assert pd.isna(result["sepal_width"].iloc[2])
        assert not pd.isna(result["target"].iloc[0])

    def test_get_features_preserves_index(self) -> None:
        """Test that DataFrame index is preserved."""
        test_data = pd.DataFrame(
            {"sepal length (cm)": [5.1, 4.9, 4.7], "target": [0, 1, 2]},
            index=[10, 20, 30],
        )

        result = get_features(test_data)

        assert result.index.tolist() == [10, 20, 30]
