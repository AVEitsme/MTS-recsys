import pandas as pd


class DatasetProcessor:
    @staticmethod
    def split_train_test(source: pd.DataFrame, date_feature: str, months_count: int) -> list[pd.DataFrame]:
        """Split source data on train ( < max date - months count) & test (> max date - months count) by date feature.

        Args:
            source (pd.DataFrame): Source dataframe.
            date_feature (str): Name of date feature.
            months_count (int): Count of months.

        Returns:
            list[pd.DataFrame]: Returns list of train & test.
        """

        test_indexes = source[
            (source[date_feature] > source[date_feature].max() - pd.tseries.offsets.DateOffset(months = months_count))
            & (source[date_feature] < source[date_feature].max())
        ].index
        return [
            source[~source.index.isin(test_indexes)],
            source[source.index.isin(test_indexes)]
        ]
