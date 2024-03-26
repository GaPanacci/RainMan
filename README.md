# RainMan

## Overview
RainMan is a Python-based tool designed to predict rain events by analyzing meteorological data. Utilizing parameters such as temperature, relative humidity, dew point temperature (DPT), vapor pressure deficit (VPD), and absolute humidity, RainMan estimates the likelihood of rainfall within a given period. The tool processes data collected from a SwitchBot Indoor/Outdoor Thermo-Hygrometer, stored in a CSV file, to provide timely rain alerts.

## Features
- Calculation of rainfall chance based on key meteorological parameters.
- Rainfall prediction through analysis of increasing trends in humidity and temperature data over a specified period.
- Summarization of consecutive rain alerts into start-end ranges for easy interpretation.

## Data Requirements
The CSV data file should be structured with the following columns in order: Date, Temperature (°C), Relative Humidity (%), DPT (°C), VPD (kPa), and Absolute Humidity (g/m³).

## Installation
1. Ensure that Python 3.x is installed on your system.
2. Install `pandas` library using pip:

## Usage
1. Modify the `file_path` variable in the script to point to the location of your CSV data file.
2. Run the script:

### Functionality
- **Rain Alert:** When the calculated chance of rainfall exceeds a predefined threshold and shows a consistent increase over a specified period, RainMan will print an alert with the start and end times of the predicted rain event.
- **No Rain Detected:** If conditions for rain are not met, the tool will indicate that no significant chance of rain is detected.

## Caveats
- The effectiveness of rain predictions depends on the accuracy and granularity of the input data.
- The tool currently requires manual modification of the data file path in the script.

## Contribution
Contributions, suggestions, and feedback are welcome to improve the RainMan project. Feel free to fork the repository and submit pull requests.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Disclaimer
This tool is provided as-is, with no guarantees of accuracy or reliability. Users should use their judgment and consider additional sources of information when making decisions based on RainMan's predictions.