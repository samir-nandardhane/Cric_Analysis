# Cricket Match Outcome Extractor & Cricket Data Processor

This repository contains two Python scripts: `ipl_parser.py` for extracting cricket match outcomes and `cricket_data_processor.py` for processing cricket match data.

# Cricket Match Outcome Extractor

## Overview

The purpose of the `ipl_parser.py` script is to retrieve details about cricket match results from an Cricinfo website. This script employs regular expressions to analyze the data and gather important information like the bowler, batsman, delivery outcome, and accompanying commentary for each event.

## Example
```
batter_bowler
Deshpande to Karthik<!-- -->, <span>OUT</span>
Smith to Johnson<!-- -->, <span>OUT</span>
```

Running the script will extract the following outcomes:

```
| b        | c        | d    |
|----------|----------|------|
| Deshpande| Karthik  | OUT  |
| Smith    | Johnson  | OUT  |
```


Sure, here's a sample README file content you can use for your GitHub repository based on the `cricket_data_processor.py` module:

---

# Cricket Data Processor

## Overview

The Cricket Data Processor is a Python module designed to process cricket match data and perform various data transformations and cleanups. This module is particularly useful for analyzing cricket match statistics, player performances, and generating structured datasets for further analysis.

The module includes functionalities to:

- Extract bowler, batter, and outcome details from match data
- Clean and preprocess run data
- Retrieve player details such as batting style and bowling style
- Sort and organize match data by innings, over, and ball

## Usage

To use the Cricket Data Processor module, import the `CricketDataProcessor` class from the `cricket_data_processor.py` file and create an instance of the class with your cricket match data DataFrame. Here's an example of how to use the module:

```python
import pandas as pd
from cricket_data_processor import CricketDataProcessor

# Load your cricket match data into a DataFrame (mydata)
mydata = pd.read_csv('path_to_your_data.csv')

# Create an instance of CricketDataProcessor
data_processor = CricketDataProcessor(mydata)

# Process the cricket data
processed_data = data_processor.process_cricket_data()

# Use the processed_data DataFrame for further analysis or export
print(processed_data.head())
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


