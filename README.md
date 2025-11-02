# Flights Analytics Dashboard
This project analyzes flight booking data using SQL, Python, and Streamlit to create an interactive dashboard. Users can explore airline-wise view availability, and switch between “Check Flights” and “Analytics” modes using visual charts for insights.

# Features
* **Interactive Dashboard:** Built with Streamlit for a fast, responsive user interface.
* **Dual Modes:** Switch between **"Check Flights"** (real-time availability/status) and **"Analytics"**(historical tends and insights).
* **SQL-Driven Backend:** Efficient data retrieval and aggregation handled by modular SQL query (via 'crud.py' and 'dbhelper.py').
* **Visualizations:** Utilizes interactive charts to present insights into flight frequency, popular routes, and time-based availability.
  
## Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| *Frontend/App* | Streamlit | Interactive web application and dashboard framework. |
| *Backend/Logic* | Python | Core programming language. |
| *Database* | SQL  | Data storage, retrieval, and analytical querying. |
| *Visualization*  | Plotly | Creating the interactive bar and line charts. |

---

##  Getting Started

### Prerequisites

To run this project locally, you need the following installed:

* Python (3.7+)
* The required Python packages (listed in requirements.txt).

### Installation

1.  *Clone the repository:*
    bash
    git clone [https://github.com/YourUsername/flights-analytics-dashboard.git](https://github.com/YourUsername/flights-analytics-dashboard.git)
    cd flights-analytics-dashboard
    

2.  *Set up a Virtual Environment (Recommended):*
    bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate   # On Windows

3. *Install dependencies:*
   pip install -r requirements.txt
    
5. *Database setup*

This project connects to a MySQL database to execute the analytical queries defined in crud.py.

1.  *Set up your MySQL Server:* Ensure you have a running MySQL instance and the necessary user credentials.
2.  *Import Data:* Import your flight data (likely from flights_cleaned.csv) into the designated MySQL table.
3.  *Configure Credentials:* The database connection details must be configured within your project, typically in a file like dbhelper.py or through environment variables.
    * *Recommended Method:* Set the following connection parameters as *environment variables* (e.g., in a .env file or directly in your terminal) which are then read by dbhelper.py:
        * DB_HOST (e.g., localhost or an IP address)
        * DB_USER
        * DB_PASSWORD
        * DB_NAME (The name of your flight database)
   
 

### Running the Dashboard

Start the application by running the Streamlit command in your terminal:

```bash
streamlit run app.py
The dashboard will automatically open in your web browser, typically at http://localhost:8501.

# Project Structure

app.py: The main Streamlit application file.

crud.py: Contains functions for running Create, Read, Update, Delete (CRUD) operations on the database.

dbhelper.py: Contains the logic for connecting to MySQL using credentials loaded from the .env file.

requirements.txt: Lists all Python package dependencies.


