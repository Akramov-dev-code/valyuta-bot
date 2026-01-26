# mainga tegmang


def get_all_currency() -> list:
    with open("currency.txt", "r") as file:
        natija = []
        data =  file.read()
        currencies_str = data.split("\n")
        for currency in currencies_str:
            if currency:
                natija.append(currency.split(","))

    return natija