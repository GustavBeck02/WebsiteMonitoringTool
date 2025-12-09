import sqlite3
import pandas as pd
from typing import Dict, Any


def calculate_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """Calculate monitoring statistics from a DataFrame."""
    if df.empty:
        return {}

    total_checks = len(df)
    successful_checks = len(df[df['status_code'] == 200])
    availability = (successful_checks / total_checks) * 100 if total_checks > 0 else 0

    return {
        "total_checks": total_checks,
        "availability": availability,
        "avg_response_time": df['response_time_ms'].mean(),
        "max_response_time": df['response_time_ms'].max(),
        "min_response_time": df['response_time_ms'].min(),
        "start_time": df['timestamp'].min(),
        "end_time": df['timestamp'].max(),
    }


def print_analysis(url: str, stats: Dict[str, Any]):
    """Print the analysis results for a specific URL."""
    
    print("\n" + "-" * 50)
    print(f"Website Monitoring Analysis for '{url}':")
    print(f"\nTime Range:          {stats['start_time']} to {stats['end_time']}")
    print(f"Total Checks:        {stats['total_checks']}")
    print(f"Availability:        {stats['availability']:.2f}%")
    print(f"\nAverage Response Time: {stats['avg_response_time']:.2f} ms")
    print(f"Max Response Time:     {stats['max_response_time']:.2f} ms")
    print(f"Min Response Time:     {stats['min_response_time']:.2f} ms")


def analyze_data(db_path: str):
    """Analyze the monitoring data stored in the SQLite database."""
    try:
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query("SELECT * FROM checks", conn)

        if df.empty:
            print("No data available for analysis.")
            return

        if "url" not in df.columns:
            print("No 'url' column found in the database.")
            return

        # Group by URL to provide separate analysis for each monitored website
        for url, group_df in df.groupby('url'):
            stats = calculate_statistics(group_df)
            if stats:
                print_analysis(url, stats)

    except Exception as e:
        print(f"Error analyzing data: {e}")


if __name__ == "__main__":
    db_path = "monitoring.db"
    analyze_data(db_path)