# priceScraper
please help me I "borrowed" this code (only differece is that the amazon link was itallian ) and it gives this error

File "main.py", line 49, in <module>
    check_price()
  File "main.py", line 21, in check_price
    title = soup.find(id="productTitle").get_text()
AttributeError: 'NoneType' object has no attribute 'get_text'
