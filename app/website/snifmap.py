import plotly.express as px
import json
import os

__name__ = "snifmap"
__version__ = "1.0.0"

def get_data(filename: str) -> dict:
    try:
        with open(filename) as f:
            raw = json.load(f)
            data = dict(
                lat = [item["latitude"] for item in raw],
                lon = [item["longitude"] for item in raw],
                id = range(1, len(raw) + 1),
                speed = [ms_to_kmh(item["gpsSpeed"]) for item in raw]
            )
            print("Downloaded data from json file 1/2")
            return data
    except:
        raise ("Error during fetch data from json file")
    
def ms_to_kmh(speed: float) -> float:
    result = speed * 3.6
    result = round(result, 2)
    return result

def get_map(filename: str) -> str:
    # Create data dict
    fetch = get_data(filename)
    data = dict(
        lon = fetch["lon"],
        lat = fetch["lat"],
        id = fetch["id"],
        speed = fetch["speed"]
    )
    
    # Create figure map
    fig = px.scatter_mapbox(data_frame=data, lat="lat", lon="lon", hover_name="id", zoom=3, color="speed")

    # Connect all points
    fig.update_traces(mode="lines+markers")
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "l": 0, "t": 0, "b": 0})

    #save map to src folder
    try:
        html_filename = "map.html"
        html_path = os.path.join("src", html_filename)
        fig.write_html(html_path)
        print(f"Map saved to {html_path} 2/2")
        return html_path
    except:
        raise ("Error during save map")