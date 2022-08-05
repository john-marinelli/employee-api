import json
from flask import Flask, request, jsonify, make_response
from db import controller

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/employees', methods={"GET"})
def employees():
    return jsonify(controller.get_all_employees())

@app.route('/employees/<employee_id>', methods=["GET", "PATCH", "POST", "DELETE"])
def single_employee(employee_id):
    match request.method:
        case "GET":
            result = controller.get_employee(employee_id)
            return jsonify(result), 200
        case "PATCH":
            if request.args["col"] and request.args["col_val"] and (request.args["col"] != "employeeid"):
                controller.patch_employee(employee_id, request.args["col"], request.args["col_val"])
                return make_response({'message' : "Success"})
            else:
                return make_response({'message' : 'Invalid arguments'})
        case "POST":
            json_body = request.get_json()
            if json_body:
                controller.create_employee(json_body["first_name"], json_body["last_name"], json_body["email"], json_body["address"], json_body["phone"], json_body["employee_id"])
                return make_response({'message' : 'success'})
        case "DELETE":
            controller.delete_employee(employee_id)
            return make_response({'message' : 'Deleted'})

if __name__ == "__main__":
    controller.init_db()
    app.run(debug=True)