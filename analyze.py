import sqlite3
import pandas as pd



def analyze_data(db_path: str):
    """Analyze the monitoring data stored in the SQLite database."""
    try:
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query("SELECT * FROM checks", conn)
            
            if df.empty:
                print("No data available for analysis.")
                return
            
            # Calculate statistics
            total_checks = len(df)
            successful_checks = len(df[df['status_code'] == 200])
            availability = (successful_checks / total_checks) * 100
            failed_checks = total_checks - successful_checks
            avg_response_time = df['response_time_ms'].mean()
            max_response_time = df['response_time_ms'].max()
            min_response_time = df['response_time_ms'].min()
            
            # Print analysis results
            print(f"\n\nWebsite Monitoring Analysis for:")

            print(f"\nTime Range:    {df['timestamp'].min()} to {df['timestamp'].max()}")

            print(f"\nTotal Checks: {total_checks}")
            #print(f"Successful Checks: {successful_checks}")
            #print(f"Failed Checks: {failed_checks}")
            print(f"Availability: {availability:.2f}%")

            print(f"\nAverage Response Time: {avg_response_time:.2f} ms")
            print(f"Max Response Time: {max_response_time:.2f} ms")
            print(f"Min Response Time: {min_response_time:.2f} ms")

            
    
    except Exception as e:
        print(f"Error analyzing data: {e}")



if __name__ == "__main__":
    db_path = "monitoring.db"
    analyze_data(db_path)