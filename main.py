from flask import Flask, jsonify, request

app = Flask(__name__)

drones = [
    {
        'id': 12534,
        'name': 'drone1'
    },
    {
        'id': 17623,
        'name': 'drone2'
    }
]


@app.route("/")
def get_home():
    return 'Home'


@app.route("/drones")
def get_drones():
    return jsonify(drones), 200


@app.route("/drones/<drone_index>")
def get_one_drone(drone_index):
    return jsonify(drones[drone_index]), 200


@app.route("/drones/create_drone", methods=['POST'])
def create_drone():
    data = request.get_json()
    drones.append(data)
    return jsonify(data), 201


'''
GET --> Obtain information
POST --> Create information
PUT --> Update information
DELETE --> Delete information
'''

if __name__ == "__main__":
    app.run(debug=True)
