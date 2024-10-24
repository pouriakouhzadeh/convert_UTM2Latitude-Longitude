import utm

# UTM coordinates (easting, northing, zone number, zone letter)
utm_coords = [
    (581533, 3644812, 39, 'S'),
    (581533, 3644312, 39, 'S'),
    (581429, 3644312, 39, 'S'),
    (581429, 3644812, 39, 'S')
]

# Convert UTM to lat/lon (setting northern=True as Iran is in the Northern Hemisphere)
lat_lon_coords = [utm.to_latlon(easting, northing, zone_number, northern=True) for easting, northing, zone_number, _ in utm_coords]

# Print the result
for i, (lat, lon) in enumerate(lat_lon_coords, start=1):
    print(f"Point {i}: Latitude = {lat}, Longitude = {lon}")
