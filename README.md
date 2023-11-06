# Exchange Rate Calculator

This is a simple Python application that calculates exchange rates for the Georgian Lari (GEL) against other selected currencies by default. You can choose another currency for exchange in `cfg.py` file. The application is built with [Streamlit](https://streamlit.io/) and fetches exchange rate data from a public API. Please note, that exchange rates are not real-time and are updated once a day. So they may differ from the actual exchange rates.

## Try it out
Applications is available [here](http://206.189.54.224:8888/). It runs on DigitalOcean droplet.

## Getting Started

### Prerequisites

Before you can run this application, make sure you have the following prerequisites installed:

- Python 3.x
- [Streamlit](https://streamlit.io/) (used for the web application)
- [Fire](https://github.com/google/python-fire) (used for the command-line interface)
- [streamlit-keyup](https://github.com/blackary/streamlit-keyup) (used for keyboard events)

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

### Usage
1. Run the application using the following command. It will run application on port 8888.

```bash
streamlit run app.py --server.port 8888
```

2. If you want to manually update the exchange rate data, you can use the command-line interface. Run the following command:

```bash
python rates.py
```

3. You can schedule the rates.py script to run daily using a cron job to keep your exchange rate data up to date. For example, to run the script once a day at a specific time, you can add the following line to your crontab:

```bash
0 0 * * * /usr/bin/python3 /path/to/rates.py
```

### Configuration
You can configure the application by editing the cfg.py file. You can change the base currency, target currencies, and the API endpoint for fetching exchange rate data.

- `CURRENCY` - The base currency for exchange. Default is `GEL`.
- `CURRENCIES` - Contains a list of target currencies for exchange. Default is `{'GEL': ['USD', 'RUB', 'KZT', 'EUR']}`.


### Acknowledgments
Exchange rate data is fetched from [fawazahmed0/currency-api](https://github.com/fawazahmed0/currency-api).


## Feedback and Contribution
If you encounter any issues, have feature suggestions, or would like to contribute to the development of this extension, please visit the [GitHub repository](https://github.com/yaroslavpoltoran/gel_rate_site) and create an issue or pull request.

## Contact the Project Maintainer

If you have any questions or feedback, don't hesitate to reach out to the project maintainer:

**Yaroslav Poltoran**

- **Telegram**: [https://t.me/yaroslavpoltoran](https://t.me/yaroslavpoltoran)

Feel free to connect and get in touch with me. Your feedback is highly appreciated!