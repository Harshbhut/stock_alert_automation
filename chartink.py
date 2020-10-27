import requests_html
import pyppdf.patch_pyppeteer

final_data = []
session = requests_html.HTMLSession()
r = session.get('https://chartink.com/dashboard/28268')
r.html.render(sleep=3)

base1 = '/html/body/div/div/div[3]/div/div/div[2]/div[2]/div/div[13]/div/div[2]/div[3]/div/div/div[2]/table' #DS2-1
base2 = '/html/body/div/div/div[3]/div/div/div[2]/div[2]/div/div[6]/div/div[2]/div[3]/div/div/div[2]/table' #DS2-2
base3= '/html/body/div/div/div[3]/div/div/div[2]/div[2]/div/div[5]/div/div[2]/div[3]/div/div/div[2]/table' #Ds2-3


links = [base1,base2,base3]

def get_data():
    for i in links:
        items = r.html.xpath(i,first = True)
        for item in items.find('tr'):
            data = [head.text for head in item.find("td")]
            if 'No data for table' in data:
                continue
            else:
                final_data.append(data)
                
    res = list(filter(None,final_data))
    print("Data Downloaded Succesfully...Going Ahead Now...\n")
    return res


