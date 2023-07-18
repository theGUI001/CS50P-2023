# Py Finance

#### Video Demo:  <https://www.youtube.com/watch?v=v_XkPWSYqug&ab_channel=theGUI001>

#### Description

Py Finance is an application that shows the main information about Shares and FIIs of the Brazilian stock exchange (B3).

With the application you can see the current market price of an asset as well as its maximum and minimum value, market capitalization, average daily trading volume, in addition to viewing a candlestick chart with opening, closing, maximum and minimum values, in addition to trading volume per day for the last 3 months. All this updated every 15 minutes thanks to the [brapi](https://brapi.dev/) API


All available tickers can be viewed at the following [address](https://brapi.dev/api/available) (Recommended to have the [JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh) extension installed)

The application relies heavily on the brapi API, so be understandable if the application doesn't work due to API downtimes, also remember to be reasonable about the number of requests you send to the API. For more details about the api, how it works, among others, see the [brapi website](https://brapi.dev/)

> **Warning**
> Para o pleno funcionamento o programa precisa de algumas bibliotecas instaladas, todas estão listadas no arquivo requirements.txt e podem ser instaladas com:
> ```sh
> pip install -r requirements.txt
> ```

How to use the app:

1. Clone the repo
```sh
git clone "https://github.com/CS50P-2023/"
```

2. cd into final project folder:
```sh
cd "CS50P 2023/final_project"
```

3. Install requirements:
```sh
pip install -r requirements.txt
```

4. Run the app with:
```sh
python project.py
```

Do you want to modify or add some function? see how to run the tests

1. cd into final_project folder
```sh
cd "CS50P 2023/final_project"
```

2. Run pytest
```sh
pytest test_project.py
```

>**Warning**
> Remember you need to have pytest installed