import singer
import pandas as pd
import simplejson as json

LOGGER = singer.get_logger()

schema = {
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'date_utc': {'type': 'string', 'format': 'date-time'},
    }
}

def main():
    url = 'https://api.spacexdata.com/v4/launches'
    df = pd.read_json(url)
    records = df.to_dict(orient='records')
    
    # Use simplejson to handle out-of-range float values
    records_json = json.dumps(records, ignore_nan=True)
    records = json.loads(records_json)
    
    singer.write_schema('launches', schema, 'id')
    singer.write_records('launches', records)

if __name__ == '__main__':
    main()
