
from monitor import check_website, init_db
import time
import sqlite3
import os

DB_PATH = "test_monitoring.db"


def run_tests():
    """Runs a series of test scenarios to verify the monitoring logic."""
    
    # Use a separate database for testing 
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    # Ensure the database and table exist before running tests
    init_db(DB_PATH)
    
    # define test cases with different expected outcomes
    test_scenarios = [
        {"url": "https://www.google.com", "expected_code": 200, "description": "Standard case (200 OK)"},
        {"url": "https://www.google.com/non-existent-page", "expected_code": 404, "description": "Client error (404 Not Found)"},
        {"url": "https://domain-does-not-exist-12345.com", "expected_code": 0, "description": "Connection error"}
    ]

    print("Starting tests...")
    print("-" * 30)
    
    all_tests_passed = True

    for scenario in test_scenarios:
        url = scenario["url"]
        expected_code = scenario["expected_code"]
        print(f"Testing: {scenario['description']} for URL: {url}")
        
        # Run the website check
        check_website(url, db_path=DB_PATH)
        
        # Verify the result from the database
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.execute("SELECT status_code FROM checks WHERE url = ? ORDER BY timestamp DESC LIMIT 1", (url,))
            result = cursor.fetchone()
            actual_code = result[0] if result else -1

        if actual_code == expected_code:
            print(f"PASSED: Expected status {expected_code}, got {actual_code}.\n")
        else:
            print(f"FAILED: Expected status {expected_code}, but got {actual_code}!\n")
            all_tests_passed = False
        

    print("=" * 30)
    if all_tests_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
    
    # Clean up the test database
    os.remove(DB_PATH)


if __name__ == "__main__":
    run_tests()