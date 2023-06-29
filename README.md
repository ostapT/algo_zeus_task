# Cryptocurrency Market Data Visualization

This project is a simple web application that collects and visualizes cryptocurrency market data using the Binance API and Plotly library. It provides candlestick charts and a pie chart representing market capitalizations of selected cryptocurrencies.

## Installation

1. Clone the repository:

```shell
git clone https://github.com/ostapT/algo_zeus_task.git
```

2. Navigate to the project directory:
```shell
cd algo_zeus_task
```
3. Set virtual environment:
```shell
python3 -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (MacOS | Linux)
```
4. Install dependencies:
```shell
pip install -r requirements.txt
```

# Usage
1. Set up your Binance API credentials by creating a .env like .env.sample file in the project directory with the following content:
```angular2html
API_KEY=your-api-key
API_SECRET=your-api-secret
```
2. Run the Flask web application:
```shell
python app.py
```

Open your web browser and go to http://localhost:5000 to access the application.

Choose the interval (1h, 1d, or 4h) and enter the symbol of the cryptocurrency you want to visualize.

Click the "Submit" button to display the candlestick chart and market cap pie chart.

## Candlestick chart:
Available on http://localhost:5000
![Candlestick.png](static%2FCandlestick.png)
## Market caps pie chart:
Available on http://localhost:5000/piechart
![PieChart.png](static%2FPieChart.png)

# Database Implementation
To implement a relational database in this project, you can follow these steps:

- Create a new database for the project.

- Modify the necessary code in app.py to establish a connection with the database.

- Determine the structure of your database tables based on the data you want to store. For example, you can create a table for each cryptocurrency symbol, with columns for the different data fields like Open Time, Open Price, High Price, Low Price, Close Price, etc.

- Modify the data collection code in collect_data() function to store the data directly into the database tables using SQL queries, instead of saving them to CSV files.

- Update the visualization code to fetch data from the database tables instead of reading from CSV files. Use appropriate SQL queries to retrieve the required data for generating the candlestick and pie charts.

# Scheduled Data Collection

To schedule the script for data collection at specific intervals, you can use tools like cron (on Unix-based systems) or Task Scheduler (on Windows).
