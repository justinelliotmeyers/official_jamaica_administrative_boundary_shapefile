#Run this script from inside the same directory
import geopandas as gpd

# Read the Shapefile
shp_file = gpd.read_file('jamaica_communities_PIOJ_UPDATE.shp')

# Ensure the GeoDataFrame is in the WGS 84 CRS
shp_file = shp_file.to_crs("EPSG:4326")

# Convert to GeoJSON
shp_file.to_file('jamaica_communities_PIOJ_UPDATE.geojson', driver='GeoJSON')
