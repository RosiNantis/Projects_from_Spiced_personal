import requests

def hello_world():
    return requests.get('http://flask_py:5000').text

if __name__ == "__main__":
    print(hello_world())