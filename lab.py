import requests
print(requests.__version__)
text=requests.get("https://raw.githubusercontent.com/KennyUA/cmput404/master/lab.py")
print(text.text)
