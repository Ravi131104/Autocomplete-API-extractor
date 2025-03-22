import requests
import time
import json

API_BASE = "http://35.200.185.69:8000/{version}/autocomplete?query={query}"
VERSIONS = ["v1", "v2", "v3"]  # API versions to check
QUERY_CHARS = "abcdefghijklmnopqrstuvwxyz"  # Starting queries
OUTPUT_FILE = "autocomplete_results.json"

def fetch_names(version, query, request_counter):
    """Fetch names from the autocomplete API for a specific version and query."""
    url = API_BASE.format(version=version, query=query)
    
    while True:
        try:
            response = requests.get(url)
            request_counter[version] += 1  # Increment request count
            
            if response.status_code == 200:
                data = response.json()
                print(f"[{version}] Response for '{query}': {data}")  # Debugging output
                return data.get("results", [])  # Extract names from "results" key
            
            elif response.status_code == 429:
                print(f"[{version}] Rate limited! Retrying in 2 seconds...")
                time.sleep(2)
            
            else:
                print(f"[{version}] Error {response.status_code}: {response.text}")
                return []
        
        except requests.exceptions.RequestException as e:
            print(f"[{version}] Request failed: {e}")
            return []

def extract_all_names():
    """Extract names for all API versions and store them in JSON format."""
    results = {version: {"names": [], "requests_made": 0, "records_found": 0} for version in VERSIONS}
    request_counter = {version: 0 for version in VERSIONS}  # Track requests
    
    for version in VERSIONS:
        print(f"Fetching results for {version}...")
        all_names = set()  # Use a set to avoid duplicates
        
        for char in QUERY_CHARS:
            names = fetch_names(version, char, request_counter)
            print(f"[{version}] Query '{char}' returned {len(names)} names")  # Debugging print
            all_names.update(names)
        
        results[version]["names"] = list(all_names)
        results[version]["requests_made"] = request_counter[version]  # Store request count
        results[version]["records_found"] = len(all_names)  # Store total records found
        print(f"[{version}] Total unique records found: {results[version]['records_found']}")  # Debugging print
    
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=4)
    
    print(f"\n✅ Extraction complete! Results saved in {OUTPUT_FILE}")
