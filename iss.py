import requests
import time
import json

def fetch_names():
    try:
        response = requests.get('http://api.open-notify.org/astros.json' ,timeout=9)
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
        response = requests.get('http://api.open-notify.org/iss-now.json', headers=headers, timeout=11 )
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
    if json_names is not None:
        for person in json_names['people']:
            name = person['name']
            names.append(name)
        print ("Names Fetched")
    else:
        print ('Fetching names failed, trying again')
        json_names = fetch_names()
    
    results = []
    first_timestamp = 0
    total_time = 0
    i = 0
    print ()
    while i < 5:

        coords = fetch_location()
        if coords is None:
            print ('skipping failled request...')
            continue
        timestamp = coords['timestamp']
        longitude = float(coords['iss_position']['longitude'])
        latitude = float(coords['iss_position']['latitude'])
        if i == 0:
            first_timestamp = timestamp
        
        
        data = {"timestamp":timestamp, 'coords': {'longitude': longitude, "latitude": latitude}}
        results.append(data)
        i +=1
        print (f"Fetching coords {i*20}% complete")
        time.sleep(5)
    
    total_time = timestamp - first_timestamp
    names_dic = {"names": names}
    results.append(names_dic)
    print ()
    print (results)
    print (f'Task complete, coords fetched in {total_time} seconds')    
    
    x = f"{timestamp}.json"
    with open (x,'a') as f:
        json.dump(results, f, indent=4)
    
    print (f"file written to {x}")