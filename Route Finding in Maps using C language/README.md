# Route Finding in Maps using C Language

This project aims to develop an efficient implementation of Dijkstra's algorithm for route-finding from Vancouver to New York City using the C language. This involves using the Nominatim API to collect and process map data from OpenStreetMap (OSM), focusing on preselected midpoints (Denver, Oklahoma City, Kansas City, and Riverton) for reference. The algorithm will assume symmetrical distances between points and will not account for real-time traffic conditions or road closures, ensuring a simplified yet effective route optimization process.

## Features

- **Efficient Route-Finding**: Implements Dijkstra's algorithm for optimal route calculation.
- **Alternative Route- Finding**: Implements alternative algorithm to calculate the optimal route and compare it with the Dijkstra's algorithm
- **JSON Parsing**: Uses cJSON library to handle JSON data from OpenStreetMap.
- **Preselected Midpoints**: Focuses on predefined midpoints for route optimization.

## Getting Started

### Prerequisites

- C Compiler (e.g., gcc)
- CMake
- Git
- cJSON Library

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/thisissophiawang/portfolio.git
   cd "Route Finding in Maps using C language"

2. **Clone and Install cJSON**:
cJSON is a JSON parsing library in C. Clone it from GitHub and install it:
 ```bash
git clone https://github.com/DaveGamble/cJSON.git
cd cJSON
mkdir build
cd build
cmake ..
make
sudo make install

### Running the Application
1. Run the executable:
 ```bash
./vancouver
./oklahoma_city
./kansas_city
./riverton
./denver
./new_york





