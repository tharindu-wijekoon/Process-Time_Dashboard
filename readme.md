# Process Time Dashboard
This is a Streamlit web application that allows users to visualize and analyze process times in relation to different home and host entities, products, and process time categories. The app takes in a CSV file and provides interactive filters to help analyze the data and visualize the results in bar charts and tables.

## Features
- CSV Upload: Users can upload a CSV file containing process time data.
- Data Filtering: Users can filter the data based on home and host entities, products, and process time categories.
- Interactive Dashboard: Visualize process times in a bar chart with dynamic updates based on user-selected filters.
- Multi-level Table: A table with hierarchical column headers (Host, Process Time, Product) is displayed for detailed insights.
- Streamlit Widgets: Use selectboxes and multi-select widgets for easy data filtering.

## Requirements
To run the Streamlit app, you need to have the following libraries installed:
- Streamlit
- Pandas
- NumPy

You can install them using pip:
```
pip install streamlit pandas numpy
```

## Running the Streamlit App
1. Clone the repository:

```
git clone https://github.com/tharindu-wijekoon/Process-Time_Dashboard.git
```

2. Navigate to the project directory:
```
cd Process-Time_Dashboard
```

3. Install the required libraries (if you haven't done so already):
```
pip install -r requirements.txt
```

4. Run the Streamlit app:
```
cd './Streamlit App'
streamlit run main.py
```

This will open the app in your default browser, or you can access it locally at http://localhost:8501.

## How the Dashboard Works
1. Upload a CSV File: The first step in using the dashboard is to upload a CSV file containing the relevant data (**'Process-time.csv'** file from AIESEC Data files). *If not uploaded, the programe will load the Process-time.csv file for November 2024 which is provided.*

2. Home and Host Entity Selection: Select a Home Entity and Host Entity from the dropdown menus.

3. Product and Process Time: You can filter the data further by selecting one or more Products and Process Time categories. *Vizualisations will not return untill you select at least one Product and Process Time category.*

4. Interactive Table: After filtering, the app will display a table with multi-level column headers, providing a detailed view of the process times across different combinations of Home, Host, and Product.

5. Bar Chart: A bar chart will visualize the selected data, with process times displayed for different Home and Host entities, allowing you to easily compare across categories.

## Example Usage
- CSV File: The app expects the CSV file to be in the standard format of **Process-time.csv** in AIESEC Data files.

- Data Filtering: You can use the dropdowns to filter data based on:

    - Home Entity: Choose a specific home location or entity.
    - Host Entity: Choose a host location or entity.
    - Product: Choose the product or category.
    - Process Time: Select different process time categories.
- Visualizing Data: Once you’ve applied filters, the table and bar chart will automatically update to reflect your selected values.

## Troubleshooting
If you encounter issues while running the app:

- Missing dependencies: Make sure all the required libraries are installed by running pip install -r requirements.txt.

- CSV Format Issues: Ensure that the CSV file contains the necessary columns (Home MC, Host MC, Product, Process Time, etc.) in the correct format.

- Streamlit Error: If you run into an error while running the app, check the terminal logs for any specific error messages. If necessary, restart the app by running streamlit run main.py again.