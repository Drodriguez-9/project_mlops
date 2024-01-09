import logging
from processor import DataProcessor
import argparse


def main(input_filepath: str, output_filepath: str):
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
    preprocessor.write_data(output_filepath)


if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Data processing for UCI Adult dataset.")
    # Add arguments for input and output file paths
    parser.add_argument("input_filepath", type=str, help="The path to the raw data")
    parser.add_argument("output_filepath", type=str, help="The path to save the processed data")
    # Parse the arguments
    args = parser.parse_args()
    # Run the main function with the provided arguments
    main(args.input_filepath, args.output_filepath)
