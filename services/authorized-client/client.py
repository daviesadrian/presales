#!/usr/bin/env python3
"""Authorized Client - calls the protected API with proper credentials."""

from google.auth import default
from google.auth.transport.requests import Request
import requests
import sys

def call_protected_api(api_url):
    """Call protected API as an authorized service account."""

    try:
        # Get the default credentials (service account)
        credentials, project = default()

        # Refresh to get a valid token
        credentials.refresh(Request())

        # Get the access token
        token = credentials.token

        print(f"[Authorized Client] Using service account: {credentials.service_account_email}")
        print(f"[Authorized Client] Calling: {api_url}")

        # Call the protected API with the token
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(api_url, headers=headers)

        print(f"[Authorized Client] Status: {response.status_code}")
        print(f"[Authorized Client] Response: {response.json()}")

        return response.status_code == 200

    except Exception as e:
        print(f"[Authorized Client] Error: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py <api_url>")
        print("Example: python client.py https://protected-api-xxx.run.app/api/secret")
        sys.exit(1)

    api_url = sys.argv[1]
    success = call_protected_api(api_url)
    sys.exit(0 if success else 1)
