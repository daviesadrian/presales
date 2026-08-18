#!/usr/bin/env python3
"""Unauthorized Client - tries to call protected API without proper credentials."""

import requests
import sys

def call_protected_api_unauthorized(api_url):
    """Try to call protected API without authorization."""

    try:
        print(f"[Unauthorized Client] Attempting to call: {api_url}")
        print(f"[Unauthorized Client] No credentials provided")

        # Call without any authorization header
        response = requests.get(api_url)

        print(f"[Unauthorized Client] Status: {response.status_code}")
        print(f"[Unauthorized Client] Response: {response.json()}")

        if response.status_code == 403:
            print("[Unauthorized Client] ✗ ACCESS DENIED (as expected)")
            return True  # Expected behavior
        else:
            print("[Unauthorized Client] ✓ Got access (unexpected!)")
            return False

    except Exception as e:
        print(f"[Unauthorized Client] Error: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py <api_url>")
        print("Example: python client.py https://protected-api-xxx.run.app/api/secret")
        sys.exit(1)

    api_url = sys.argv[1]
    success = call_protected_api_unauthorized(api_url)
    sys.exit(0 if success else 1)
