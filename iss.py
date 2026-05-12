import requests
import time
import json

def fetch_names():
    try:
        response = requests.get('http://api.open-notify.org/astros.json' ,timeout=15)
        response.raise_for_status()
        names = response.json()
        return names
    
    except requests.exceptions.HTTPError as e:
        print ('HTTP error occured:', e)
    except requests.exceptions.RequestException as e:
        print (' a request error occured:', e)

def fetch_location():
    headers = {
    "X-API-KEY": "ABC123STUDENT",
    "Content-Type": "application/json"
    }

    try:
        response = requests.get('http://api.open-notify.org/iss-now.json', headers=headers, timeout=16 )
        response.raise_for_status()
        coords = response.json()
        
        return coords
    
    except requests.exceptions.HTTPError as e:
        print (' HTTP error occured',e)
    except requests.exceptions.RequestException as e:
        print (" request error  occured ", e)

    
if __name__ == '__main__':
    json_names = fetch_names()
    names = []
    for person in json_names['people']:
        name = person['name']
        names.append(name)
    
    results = []
    i = 0
    while i < 5:

        coords = fetch_location()
        if coords is None:
            print ('skipping failled request...')
            continue
        timestamp = coords['timestamp']
        longitude = coords['iss_position']['longitude']
        latitude = coords['iss_position']['latitude']

        data = {"timestamp":timestamp, 'coords': {'longitude': longitude, "latitude": latitude}}
        results.append(data)
        i +=1
        print (i)
        time.sleep(5)


    names_dic = {"names": names}
    results.append(names_dic)
    print (results)
    
    
    x = f"{timestamp}.json"
    with open (x,'a') as f:
        json.dump(results, f, indent=4)