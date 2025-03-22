# Autocomplete API Extractor

## 📌 Project Overview
This project extracts all possible names from an **undocumented autocomplete API** across three versions: **v1, v2, and v3**.  
The API endpoints used are:  

_(where `{version}` is `v1`, `v2`, or `v3`)_  

Since there is no official documentation, we **explored** and **reverse-engineered** the API to handle rate limits, query strategies, and response patterns.

---

## 🔍 Approach to Discovering API Behavior

1. **Exploration:** Started by testing basic queries (`a`, `b`, `c`, etc.) for **v1, v2, and v3**.
2. **Response Analysis:** Printed full API responses to understand the structure and key fields.
3. **Debugging v2 & v3:** If v2 and v3 didn’t return expected results, we tested alternative endpoints and query parameters.
4. **Rate Limits:** Detected `429 Too Many Requests` responses and implemented automatic retry mechanisms.
5. **Efficient Querying:** Used recursive querying to explore all possible names.

---

## 🛠 Handling Constraints & Limitations

### ✅ **Rate Limiting**
- The API enforces rate limits (returns `429` if too many requests are made).
- **Solution:** Implemented **exponential backoff** to retry requests efficiently.

### ✅ **API Errors & Unknown Behavior**
- Some versions (`v2` & `v3`) returned unexpected responses.
- **Solution:** Logged full API responses for debugging.
- Tested alternative endpoints (`/v1/autocomplete?query=a&version=2`).

### ✅ **Efficient Data Extraction**
- Minimized redundant queries by caching results.
- Stored extracted names in a JSON file for easy access.

---

## 🏗 Code Structure

- **`autocomplete_extractor.py`** → Queries **v1, v2, and v3**, handles rate limits, and saves results.
- **`autocomplete_results.json`** → Stores extracted names from all versions.
- **`README.md`** → Documentation of approach and findings.

---

## 🚀 Running the Script

### 1️⃣ Install Dependencies
Ensure you have Python installed, then install `requests`:


### 2️⃣ Run the Extractor

### 3️⃣ View Extracted Data
After execution, the results are saved in **`autocomplete_results.json`**:


---

## 📊 Results Summary

### 🔹 Unique Names Extracted
### 🔹 API Requests Made
### 🔹 API Records Count

---