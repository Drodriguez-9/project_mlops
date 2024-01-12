import logging
from processor import DataProcessor
import argparse


def main(input_filepath: str, output_train_filepath: str, output_test_filepath: str):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")
    preprocessor = DataProcessor()

    logger.info("reading data")
    preprocessor.read_data(input_filepath)

    logger.info("processing data")
    preprocessor.process_data()

    logger.info("saving processed data")
    preprocessor.write_data(output_train_filepath, output_test_filepath)


if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Data processing for UCI Adult dataset.")
    # Add arguments for input and output file paths
    parser.add_argument("input_filepath", type=str, help="The path to the raw data")
    parser.add_argument("output_train_filepath", type=str, help="The path to save the training processed data")
    parser.add_argument("output_test_filepath", type=str, help="The path to save the test processed data")
    # Parse the arguments
    args = parser.parse_args()
    # Run the main function with the provided arguments
    main(args.input_filepath, args.output_train_filepath, args.output_test_filepath)
