cache = {}

def get_page(url):
    if url in cache:
        return cache[url]
    
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


def get_data_from_server(url):
    url = "got data."
    return url


print(get_page("https://www.google.com/"))
print(get_page("https://www.google.com/"))
