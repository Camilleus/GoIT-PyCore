# import requests
# from datetime import datetime

# response = requests.get(
#     "http://api.nbp.pl/api/exchangerates/tables/a?format=json")

# if response.ok == True:
#     data = response.json()[0]
#     table = data['table']
#     no = data["no"]
#     effectiveDate = data["effectiveDate"]
#     print(f"Exchange rates for {effectiveDate}: \n",
#           "table:", table, "\n number:", no)

#     rates = data["rates"]
#     for rate in rates:
#         currency = rate["currency"]
#         code = rate["code"]
#         mid = rate["mid"]
#         print(currency, " code:", code, "value:", mid)


import aiohttp
from datetime import datetime, timedelta
import asyncio
import sys


async def fetch_data_from_nbp_api(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.ok:
                    return await response.json()
                else:
                    print(
                        f"Error fetching data. HTTP Status: {response.status}")
    except aiohttp.ClientError as ce:
        print(f"AIOHTTP ClientError: {ce}")
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None


def process_exchange_rate_data(date_data):
    rates = {}
    for rate in date_data['rates']:
        if rate['code'] in ['USD', 'EUR']:
            rates[rate['code']] = {
                'sale': rate['ask'], 'purchase': rate['bid']}
    return {date_data['effectiveDate']: rates}


async def fetch_exchange_rates_for_date(start_date, end_date):
    try:
        base_url = f"http://api.nbp.pl/api/exchangerates/tables/C/{start_date}/{end_date}/?format=json"
        data = await fetch_data_from_nbp_api(base_url)
        if data:
            results = []
            for date_data in data:
                results.append(process_exchange_rate_data(date_data))
            return results
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
    return None


async def fetch_exchange_rates(start_date, end_date):
    return await fetch_exchange_rates_for_date(start_date, end_date)


async def main():
    if len(sys.argv) != 2:
        print("Usage: python NBPExchangeRates.py <number_of_days>")
        return

    days_ago = int(sys.argv[1])
    today = datetime.now()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")

    results = await fetch_exchange_rates(start_date, end_date)
    if results:
        print(results)
    else:
        print("Failed to fetch exchange rates.")

if __name__ == "__main__":
    asyncio.run(main())
