import requests
from rich import print

def mock_req():
    for i in range(10000):
        resp = requests.get(f"http://localhost:5000/call/{i}")
        print(resp.status_code,i)


if __name__ == "__main__":
    mock_req()
