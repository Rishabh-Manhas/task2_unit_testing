import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):
    def test_website_loading(self):
        url = "https://atgworld"
        print("Attempting to connect to:", url)
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Website loaded successfully!")
            self.assertTrue(True)  # Pass the test
        else:
            print("Failed to load website!")
            self.assertTrue(False, f"Website failed to load with status code: {response.status_code}")

if __name__ == "__main__":
    unittest.main()
