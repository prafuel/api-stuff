import webapp2
import os 
import urllib 
import json   
from google.appengine.ext.webapp import template 

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(_file_), "index.html")
        context = {}
        self.response.out.write(template.render(path, context))    
            
                          
    def post(self): 
        pincode = self.request.get("zipCode")
        url = "https://api.postalpincode.in/pincode/"  + pincode
        # response = urllib.urlopen(url)                   
        # if response.getcode() == 200: 
        # data = json.loads(response.read()) 
        # if data and isinstance(data, list) and 'PostOffice' in data[0]: /
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        post_office = data[0]['PostOffice'][0]['State']                 
        name = data[0]['PostOffice'][0]['Name']                 
        block = data[0]['PostOffice'][0]['Block']                 
        district = data[0]['PostOffice'][0]['District'] 
                 
        template_values = { 
            "post_office": post_office,  
            "name": name, 
            "block": block, 
            "district": district 
        }                                  
        path = os.path.join(os.path.dirname(_file_), "results.html")
        self.response.out.write(template.render(path, template_values))
        
app = webapp2.WSGIApplication([('/',MainPage)], debug=True)   
                      
        #              else: 
        #         self.response.out.write("Invalid data received from API")         else: 
        #     self.response.out.write("Error fetching data from API")