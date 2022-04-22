# DEiA 2
 InnoSportsLab Project

## Data Source

The data is extracted using [Overpass
Turbo](https://overpass-turbo.eu/) utility which uses OSM API to
provicde `geojson` information. A sample query can be found below:

```json
[out:json][timeout:25];
// gather results
(
  area["ISO3166-1"="NL"][admin_level=2];
  (
    node["leisure"="fitness_station"](area);
  );
);
// print results
out body;
>;
out skel qt;
```
