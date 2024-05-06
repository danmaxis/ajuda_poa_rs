# Ajuda Poa RS

This project aims to provide a solution for managing and visualizing data related to the needs and resources available in Porto Alegre, RS.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12
- Google Sheets API Key

### Installing

1. Clone the repository
2. Install the dependencies using pip: 
    ```sh
    pip install -r requirements.txt
    ```
3. Set your Google Sheets API Key as an environment variable named GOOGLE_API_KEY.

# Usage
Execute the main script. This script performs the following operations:

- Fetches data from a specified Google Sheets spreadsheet
- Processes the data
- Generates a map visualization

# Features
The main script includes the following features:

- `get_spreadsheet_data`: Fetches data from Google Sheets
- `calculate_gravity`: Calculates gravity of needs
- `parse_needs`: Parses needs and resources from data
- `geocode_addresses`: Geocodes addresses
- `create_map`: Creates a map visualization

# Contributing
Refer to `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

# License
This project is licensed under the NCSA Open Source License. See `LICENSE.md` for more details.