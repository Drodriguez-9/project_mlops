import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


class DataProcessor:
    """
    Class for reading, processing, and writing data from the UCI
    `Adult` dataset.
    """

    def __init__(self):
        self.data = None

    def read_data(self, raw_data_path: str):
        """Read raw data into DataProcessor."""
        self.data = pd.read_csv(raw_data_path, header=None, na_values="?")
        # Define the column names
        column_names = [
            "age",
            "workclass",
            "fnlwgt",
            "education",
            "education-num",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital-gain",
            "capital-loss",
            "hours-per-week",
            "native-country",
            "income",
        ]
        self.data.columns = column_names

    def process_data(self, stable=True):
        """Process raw data into useful files for model."""
        # Drop rows with missing values
        self.data = self.data.dropna()

        # label encode the target variable to have the classes 0 and 1
        self.data.assign(
            income=LabelEncoder().fit_transform(self.data["income"]),
        )
        # Identify categorical and numerical columns
        cat_ix = self.data.select_dtypes(include=["object", "bool"]).columns
        num_ix = self.data.select_dtypes(include=["int64", "float64"]).columns

        # Label encode the target variable 'income'
        self.data["income"] = LabelEncoder().fit_transform(self.data["income"])

        # Label encode categorical columns
        for col in cat_ix:
            self.data[col] = LabelEncoder().fit_transform(self.data[col])

        # Initialize the ColumnTransformer with StandardScaler
        ct = ColumnTransformer(
            [("n", StandardScaler(), num_ix)], remainder="passthrough"
        )  # 'passthrough' leaves the already encoded categorical columns untouched

        # Apply the ColumnTransformer to the dataset to standarize
        self.data[num_ix] = ct.fit_transform(self.data[num_ix])

    def write_data(self, processed_data_path: str):
        """Write processed data to directory."""
        self.data.to_csv(processed_data_path, index=False)
