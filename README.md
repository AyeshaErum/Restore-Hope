# Restore-Hope
# RestoreSync - Matching Algorithm and Admin Dashboard

RestoreSync is a real-time disaster response system that matches aid requests from Internally Displaced Person (IDP) camps with available resources from NGOs. The system utilizes a Python-based matching algorithm, a live MongoDB database connection, and an admin dashboard to streamline humanitarian aid delivery.

## Project Overview

1. **Matching Algorithm**: 
   - Logs aid requests from IDP camps and connects to the MongoDB database to retrieve live NGO inventory data.
   - The algorithm filters NGOs based on the resources they can provide and their proximity to the aid request location.
   - Matches the most suitable NGO to fulfill the aid request.

2. **Python Script**:
   - The matching algorithm is implemented in Python, which fetches data from the MongoDB database, applies filtering logic, and updates the database with the best NGO match.

3. **Admin Dashboard**:
   - An intuitive dashboard for admins to validate matches made by the algorithm.
   - Displays real-time data such as color-coded maps, graphical analytics, and automated alerts to assist admins in tracking the status of aid requests.

## Features

- **Matching Algorithm**: Efficiently matches aid requests to NGOs based on available resources and proximity.
- **Real-time Data**: Continuously updated information, including maps and analytics, to track aid delivery.
- **Admin Dashboard**: Allows for validation and manual adjustment of algorithmic matches.

## Setup and Installation

### Prerequisites
- Python 3.x
- MongoDB database
- Libraries: `Flask`, `PyMongo`, `requests`, `pandas`, etc.

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/RestoreSync.git
   cd RestoreSync
