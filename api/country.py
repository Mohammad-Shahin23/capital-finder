from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):

        s = self.path
        
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        country = dic.get("country")
        capital = dic.get("capital")
        

        if country:
            
            url = "https://restcountries.com/v3.1/name/"
            res = requests.get(url+country)
            data = res.json()
            try:
                result = data[0]["capital"][0]
                massage = "The capetal of " + country + " is " + result 
            except: 
                massage = " You entered unvalid country "
        

        if capital:
            url = "https://restcountries.com/v3.1/capital/"
            
            res = requests.get(url+capital)
            data = res.json()
            try:
                result = data[0]["name"]["common"]
                massage = "The capetal of " + capital + " is " + result 
            except: 
                massage = " You entered unvalid capital "
        
       
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(massage.encode('utf-8'))
        return