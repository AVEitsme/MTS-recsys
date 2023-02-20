import pandas as pd


class DatasetProcessor:
    @staticmethod
    def split_train_test(source: pd.DataFrame, date_feature: str, days_count: int) -> list[pd.DataFrame]:
        """Split source data on train ( < max date - days count) & test (> max date - days count) by date feature.

        Args:
            source (pd.DataFrame): Source dataframe.
            date_feature (str): Name of date feature.
            days_count (int): Count of days.

        Returns:
            list[pd.DataFrame]: Returns list of train & test.
        """

        test_indexes = source[
            (source[date_feature] > source[date_feature].max() - pd.tseries.offsets.DateOffset(days = days_count))
            & (source[date_feature] < source[date_feature].max())
        ].index
        return [
            source[~source.index.isin(test_indexes)],
            source[source.index.isin(test_indexes)]
        ]
