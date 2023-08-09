from extract_data import ExtractData
from transform_data import TransformData
from load_data import LoadData

if __name__ == "__main__":
    username = "tarcisio-marinho"
    url_base = "https://api.github.com/users"
    url_endpoint = url_base + '/' + username

    data_extraction = ExtractData(
        username='tarcisio-marinho', 
        url=url_endpoint)
    events = data_extraction.get_received_events_json()

    data_transform = TransformData(
        json_data=events, 
        date_start='2023-08-01', 
        date_end='2023-08-31')
    events_filtered = data_transform.filter_created_at()
    events_flatted = data_transform.spark_flatten(events_filtered)

    data_load = LoadData(
        spark_df=events_flatted)
    data_load.write_csv('events_flatted')
    data_load.save_json('events', events)
    