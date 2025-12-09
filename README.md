# WebsiteMonitoringTool

A simple, Python-based monitoring tool to track website availability, log performance data, and analyze historical uptime data.

## Features

-   **Status Checks:** Periodically checks if a website is online and records the HTTP status code.
-   **Performance Logging:** Measures and stores the response time for each check.
-   **Data Persistence:** Saves all monitoring data to a local SQLite database (`monitoring.db`).
-   **Configurable:** The target URL and check interval can be easily configured via a `config.json` file.
-   **Data Analysis:** Provides a summary of the collected data, including availability percentage, and average, minimum, and maximum response times.
-   **Testing:** Includes a test suite to ensure the monitoring logic functions correctly.

## Requirements

-   Python 3.x
-   Required packages are listed in `requirements.txt`.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/GustavBeck02/WebsiteMonitoringTool
    cd WebsiteMonitoringTool
    ```
2.  Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    ```
    Then, activate it:
    - On **Windows**: `.\venv\Scripts\activate`
    - On **macOS/Linux**: `source venv/bin/activate`

3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Configuration

Before the first run, a `config.json` file is needed in the root directory. It is created automatically with default values on the first run if missing.

**Example `config.json`:**
```json
{
    "url": "https://www.google.com",
    "interval_seconds": 5
}
```

### 2. Start the Monitor

To start monitoring the website specified in the configuration:
```bash
python monitor.py
```
The script will print status updates to the console and save data to `monitoring.db`. Press `CTRL+C` to stop.

### 3. Analyze Collected Data

To analyze the collected data:
```bash
python analyze.py
```

### 4. Run Tests

To verify that the tool is working as expected:
```bash
python test_runner.py
```
