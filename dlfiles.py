'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


from urllib import request
my_url = '' 

def downloaddata(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_loc = r'goog.csv'
    fx = open(dest_loc, "w")
    for line in lines:
        fx.write(line + "\n")
        fx.close()
downloaddata(my_url)
    
