# UCD Census Data Processing Script

This Python script is designed to clean and process census data from the `ucd_census.csv` file. It performs data deduplication, parsing, and normalization, and then outputs a cleaned version of the data into a new CSV file.

## Features

- **Deduplication**: Removes duplicate entries from specified columns.
- **Data Parsing**: Parses participant attributes and dates into a more structured format.
- **Data Normalization**: Explodes columns to normalize the data for easier analysis.
- **CSV Output**: Exports the cleaned data into `cleaned_ucd_census.csv`.

## Dependencies

The script relies on the following Python libraries:

- `pandas`
- `numpy`
- `datetime`

You can install these dependencies using `pip`:

```bash
pip install pandas numpy
```

## Usage

1. Ensure that your input data file, ucd_census.csv, is in the same directory as the script.

2. Run the script using Python:
```bash
python main.py
```

3. The script will generate a cleaned CSV file named cleaned_ucd_census.csv in the same directory.

## File Structure

- `main.py`: The main script that processes the data.
- `ucd_census.csv`: The input file containing the raw census data.
- `cleaned_ucd_census.csv`: The output file containing the cleaned data.

## License

- This project is licensed under the MIT License. [See here](https://opensource.org/licenses/MIT) for more details.

## Author

Renato Perez