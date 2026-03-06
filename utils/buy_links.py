def get_buy_links(medicine_name):

    query = medicine_name.replace(" ", "%20")

    links = {
        "1mg": f"https://www.1mg.com/search/all?name={query}",
        "pharmeasy": f"https://pharmeasy.in/search/all?name={query}",
        "netmeds": f"https://www.netmeds.com/catalogsearch/result?q={query}"
    }

    return links