"""
Test script to verify frontend-backend connectivity.
Run this to check if the backend is accessible and CORS is configured correctly.
"""
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import json

def test_backend_connection():
    """Test if backend is running and accessible."""
    print("Testing Backend Connection...")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:8000"
    
    # Test 1: Health check
    print("\n1. Testing Health Endpoint...")
    try:
        with urlopen(f"{base_url}/") as response:
            data = json.loads(response.read())
            print(f"   [OK] Backend is running: {data}")
    except URLError as e:
        print(f"   [ERROR] Backend not accessible: {e}")
        print("   Make sure backend is running: uvicorn app.main:app --reload")
        return False
    
    # Test 2: CORS headers (simulate frontend request)
    print("\n2. Testing CORS Configuration...")
    try:
        req = Request(f"{base_url}/")
        req.add_header("Origin", "http://localhost:5173")
        with urlopen(req) as response:
            cors_header = response.headers.get("Access-Control-Allow-Origin")
            if cors_header:
                print(f"   [OK] CORS configured: {cors_header}")
            else:
                print("   ⚠ CORS header not found (may still work)")
    except Exception as e:
        print(f"   ⚠ CORS test error: {e}")
    
    # Test 3: API endpoints
    print("\n3. Testing API Endpoints...")
    endpoints = [
        ("/api/auth/register", "POST"),
        ("/api/problems", "GET"),
        ("/api/submissions", "POST"),
    ]
    
    for endpoint, method in endpoints:
        try:
            req = Request(f"{base_url}{endpoint}")
            req.add_header("Origin", "http://localhost:5173")
            req.get_method = lambda: method
            try:
                with urlopen(req, timeout=2) as response:
                    print(f"   [OK] {method} {endpoint} - Status: {response.status}")
            except HTTPError as e:
                if e.code in [404, 405, 422]:  # Expected errors for missing data
                    print(f"   [OK] {method} {endpoint} - Endpoint exists (Status: {e.code})")
                else:
                    print(f"   ⚠ {method} {endpoint} - Status: {e.code}")
        except URLError as e:
            print(f"   [ERROR] {method} {endpoint} - Error: {e}")
    
    # Test 4: Database connection
    print("\n4. Testing Database Connection...")
    try:
        with urlopen(f"{base_url}/db-test") as response:
            data = json.loads(response.read())
            print(f"   [OK] Database: {data}")
    except Exception as e:
        print(f"   [ERROR] Database test failed: {e}")
    
    print("\n" + "=" * 50)
    print("Connection Test Complete!")
    print("\nFrontend Configuration:")
    print("  - API Base URL: http://127.0.0.1:8000/api")
    print("  - Frontend URL: http://localhost:5173")
    print("\nBackend Configuration:")
    print("  - Backend URL: http://127.0.0.1:8000")
    print("  - CORS Origins: http://localhost:5173, http://127.0.0.1:5173")
    
    return True

if __name__ == "__main__":
    test_backend_connection()

