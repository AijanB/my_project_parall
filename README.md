# Parallelepiped Analyzer

## Overview
This Python project reads parallelepiped dimensions from a JSON file, calculates various geometric properties, and stores the results in separate JSON files. Additionally, it computes and saves the average values of these characteristics.

## Features
- Reads input data from `parallelepipeds.json`
- Computes:
  - Diagonal length
  - Volume
  - Surface area
  - Angles (alpha, beta, gamma)
  - Radius and volume of the described sphere
- Saves the calculated properties into `characteristics.json`
- Computes average values and saves them in `statistics.json`
- Displays results in a structured JSON format

## Installation & Usage
### Prerequisites
Ensure you have Python installed (preferably Python 3). If you don't have Python installed, download it from [python.org](https://www.python.org/).

### Running the Script
1. Clone this repository or download the script files.
2. Ensure you have `parallelepipeds.json` formatted correctly in the same directory.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the script:
   ```sh
   python calculations.py
   ```
5. The script will generate two JSON files:
   - `characteristics.json` with detailed calculations
   - `statistics.json` with average values
6. The results will also be printed in the terminal.

## File Structure
```
my_project/
│── calculations.py          # Main script for processing parallelepiped data
│── parallelepipeds.json     # Input file with dimensions
│── characteristics.json     # Output file with detailed calculations
│── statistics.json          # Output file with average values
│── README.md                # Project documentation
```
