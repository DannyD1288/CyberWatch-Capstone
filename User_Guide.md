# CyberWatch User Guide

## Start the application
1. Install Python 3.11 or later.
2. Open the `cyberwatch` folder in a terminal.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python app.py`.
5. Visit `http://127.0.0.1:5000`.

## Analyze a sample log
1. Under **Upload security logs**, select `sample_data/sample_log.csv`.
2. Click **Analyze logs**.
3. Review the event counts and any generated security alerts.
4. Use the alert status dropdown to display Open or Resolved alerts.
5. Click **Resolve** on an open alert when you have finished reviewing it.
6. Use the search box and outcome dropdown in **Recent authentication events** to narrow results.

## Expected sample behavior
The sample has seven events: six failed and one successful. Six failures share IP `192.0.2.10` within 50 seconds and should generate one alert on a fresh database. If the alert is already resolved, the Open alerts metric can be zero.

## Reset local demonstration data
Stop the application, delete the local `cyberwatch.db` file, and restart. This clears imported data; do not do this if you need to retain previous demonstration results.

## Troubleshooting
- **No chart:** check internet connectivity for the Chart.js CDN; tables still work.
- **Upload rejected:** check CSV header names, timestamp format, IP addresses, and result values.
- **Port in use:** stop other programs using port 5000.
