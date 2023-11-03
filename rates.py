from typing import Dict, List, Any
import logging
import json
import requests

import cfg as cfg


def save_dict_to_json(data: Dict[str, Any], path: str) -> None:
    with open(path, "w") as fp:
        json.dump(data, fp, sort_keys=False, indent=4, ensure_ascii=False)
    logging.info("Dict saved to json", extra={"path": path})


def get_rates(
    currencies: Dict[str, List[str]] = cfg.CURRENCIES, api_url: str = cfg.API_URL
) -> Dict[str, Dict[str, float]]:
    rates = {}
    for from_currency, currencies_list in currencies.items():
        rates[from_currency] = {}
        for to_currency in currencies_list:
            url = api_url.format(from_=from_currency.lower(), to=to_currency.lower())
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                rates[from_currency][to_currency] = data[to_currency.lower()]
            else:
                logging.info(
                    "Error: Failed to retrieve data. "
                    f"Currencies: {from_currency}/{to_currency}. "
                    f"Status code: {response.status_code}"
                )
    return rates


def save_rates(
    currencies: Dict[str, List[str]] = cfg.CURRENCIES, api_url: str = cfg.API_URL, path: str = cfg.RATES_MAP_PATH
) -> None:
    rates = get_rates(currencies=currencies, api_url=api_url)
    save_dict_to_json(data=rates, path=path)


def load_rates(path=cfg.RATES_MAP_PATH):
    with open(path) as json_file:
        rates = json.load(json_file)
    return rates


if __name__ == "__main__":
    import fire

    fire.Fire(save_rates)
