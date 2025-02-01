import csv
from pymongo import MongoClient
from geopy.distance import geodesic  # To calculate the geographical distance between two coordinates

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['RestoreSync']

# Function to calculate distance between two coordinates
def calculate_distance(request_location, ngo_location):
    return geodesic(request_location, ngo_location).kilometers

# Function to match requests with the nearest NGOs
def match_requests_with_ngos(requests, ngos_inventory):
    matches = []

    for request in requests:
        matched_ngos = []
        request_location = tuple(request['location']['coordinates'])  # Ensure tuple format (lat, long)

        for ngo in ngos_inventory:
            # Ignore the _id field and extract actual NGO data
            for ngo_name, data in ngo.items():
                if ngo_name == "_id":  # Skip the ObjectId field
                    continue

                if 'resources' in data and 'location' in data:
                    resources_match = all(
                        resource in data['resources'] and data['resources'][resource] >= quantity
                        for resource, quantity in request['resources'].items()
                    )

                    if resources_match:
                        ngo_location = tuple(data['location']['coordinates'])  # Ensure tuple format (lat, long)
                        distance = calculate_distance(request_location, ngo_location)
                        matched_ngos.append({'ngo_name': ngo_name, 'distance': distance})

        # Sort by distance and select the closest NGO
        best_match = min(matched_ngos, key=lambda x: x['distance'], default={'ngo_name': None})['ngo_name']
        matches.append({'request_id': request['request_id'], 'best_match': best_match})

    return matches

# Function to save results as CSV
def save_matches_to_csv(matches, filename='matches.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['request_id', 'best_match'])
        writer.writeheader()
        writer.writerows(matches)

# Fetch requests from MongoDB
requests = list(db.requests.find({}, {"_id": 0}))  # Exclude _id for cleaner data

# Fetch NGOs inventory from MongoDB
ngos_inventory = list(db.ngos.find())  # Keep _id but filter it inside processing

# Debugging: Print the data structure
print("Requests:", requests)
print("NGOs:", ngos_inventory)

# Process matching
matches = match_requests_with_ngos(requests, ngos_inventory)

# Save results
save_matches_to_csv(matches)

print("Matching completed. Results saved in matches.csv.")