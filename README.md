# README

## Project Overview

This project focuses on analyzing parallelepipeds and their related geometric properties. The program performs a series of calculations on the dimensions of parallelepipeds, including:

- Diagonal
- Volume
- Surface Area
- Angles (α, β, γ)
- Radius and Volume of the Described Sphere

The results of these calculations are organized into two primary output files:
- **characteristics.json**: Contains detailed geometric information for each parallelepiped.
- **statistics.json**: Provides average values for each geometric property across all parallelepipeds.

**Important**: The outputs such as `statistics.json` and `characteristics.json` are **not** added to GitHub as they are generated dynamically by the code based on input data.

## Project Structure

```
/project-root
│
├── /outputs
│   ├── characteristics.json    # Stores detailed geometric properties for each parallelepiped
│   └── statistics.json        # Stores average statistics for all parallelepipeds
│
├── /utils
│   └── /functions.py          # Contains the functions used for calculating the properties
│
├── parallelepipeds.json       # Input data file containing dimensions (a, b, c) of various parallelepipeds
├── main.py                  # Main script to perform the calculations and generate outputs
└── README.md                  # Project documentation (this file)
```

## Key Functions

- **`get_diag(a, b, c)`**: Returns the diagonal of the parallelepiped.
- **`get_volume(a, b, c)`**: Calculates the volume of the parallelepiped.
- **`get_surface(a, b, c)`**: Computes the surface area of the parallelepiped.
- **`get_alpha(a, b, c)`**: Calculates the angle α between the `a` dimension and the diagonal.
- **`get_beta(a, b, c)`**: Calculates the angle β between the `b` dimension and the diagonal.
- **`get_gamma(a, b, c)`**: Calculates the angle γ between the `c` dimension and the diagonal.
- **`get_sphr_radius(a, b, c)`**: Determines the radius of the sphere that circumscribes the parallelepiped.
- **`get_sphr_volume(a, b, c)`**: Calculates the volume of the sphere described by the parallelepiped.

## How It Works

1. **Loading Data**:
   - The `parallelepipeds.json` file is read to extract the dimensions (`a`, `b`, `c`) for each parallelepiped.

2. **Calculations**:
   - For each parallelepiped, the various geometric properties are calculated using the functions defined in `functions.py`.

3. **Generating Outputs**:
   - The calculated properties are saved to the `characteristics.json` file.
   - Average statistics for all parallelepipeds are calculated and stored in `statistics.json`.

4. **Displaying Results**:
   - The program outputs the results in JSON format, both in the terminal and saved as files (`characteristics.json` and `statistics.json`).

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**:
    If there are any dependencies (such as specific Python libraries), install them by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script**:
    Execute the main script to generate the outputs:
    ```bash
    python script.py
    ```

4. **Check the Output**:
    After running the script, the `characteristics.json` and `statistics.json` files will be generated in the `/outputs` directory.
