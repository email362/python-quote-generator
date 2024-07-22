# import requests

# url = "http://api.forismatic.com/api/1.0/"
# params = {
#     "method": "getQuote",
#     "format": "json",
#     "lang": "en"
# }


# print("Quote Text: " + quote["quoteText"])
# print("Author: " + quote["quoteAuthor"])

# def getQuote():
#     response = requests.get(url, params=params)
#     quote = response.json()
#     return quote

# for i in range(4):
#     x = getQuote()
#     print(x)

import dearpygui.dearpygui as dpg
import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return data['content'], data['author']
    else:
        return "Failed to retrieve quote", ""

def update_quote():
    quote, author = get_random_quote()
    dpg.set_value("quote_text", quote)
    dpg.set_value("quote_author", f"- {author}")

# Create the GUI
dpg.create_context()

with dpg.window(label="Random Quote Generator", width=600, height=300):
    dpg.add_text("Quote:")
    dpg.add_text("", tag="quote_text", wrap=480)
    dpg.add_text("", tag="quote_author")
    dpg.add_button(label="Random Quote", callback=update_quote)

# Initialize with a quote
update_quote()

dpg.create_viewport(title="Random Quote Generator", width=600, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
