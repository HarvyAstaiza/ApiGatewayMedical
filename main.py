from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests
import re

from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
Cors = CORS(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Cambiar por el que seconveniente
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/validar'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60 * 60 * 24)
        access_token = create_access_token(identity=user, expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running..."
    return jsonify(json)

@app.route("/pacientes", methods=['GET'])
def getPacientes():
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/pacientes'
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)

@app.route("/pacientes/<string:id>", methods=['GET'])
def getPaciente(id):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/pacientes/'+id
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)


@app.route("/pacientes", methods=['POST'])
def crearPacientes():
    data=request.get_json()
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/pacientes'
    response=requests.post(url, headers=headers, json=data)
    json=response.json()
    return jsonify(json)


@app.route("/pacientes/<string:id>", methods=['PUT'])
def modificarPacientes(id):
    data=request.get_json()
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/pacientes/'+id
    response=requests.put(url, headers=headers, json=data)
    json=response.json()
    return jsonify(json)


@app.route("/pacientes/<string:id>", methods=['DELETE'])
def eliminarPacientes(id):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/pacientes/'+id
    response=requests.delete(url, headers=headers)
    json=response.json()
    return jsonify(json)


# evaluador
@app.route("/evaluadores", methods=['GET'])
def getEvaluadores():
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/evaluadores'
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)


@app.route("/evaluadores/<string:id>", methods=['GET'])
def getEvaluador(id):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/evaluadores/'+id
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)


@app.route("/evaluadores", methods=['POST'])
def crearEvaluadores():
    data=request.get_json()
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/evaluadores'
    response=requests.post(url, headers=headers, json=data)
    json=response.json()
    return jsonify(json)


@app.route("/evaluadores/<string:id>", methods=['PUT'])
def modificarEvaluadores(id):
    data=request.get_json()
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/evaluadores/'+id
    response=requests.put(url, headers=headers, json=data)
    json=response.json()
    return jsonify(json)


@app.route("/evaluadores/<string:id>", methods=['DELETE'])
def eliminarEvaluador(id):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/evaluadores/'+id
    response=requests.delete(url, headers=headers)
    json=response.json()
    return jsonify(json)


# Diagnostico
@app.route("/diagnosticos", methods=['GET'])
def getDiagnosticos():
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/diagnosticos'
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)


@app.route("/diagnosticos/<string:id>", methods=['GET'])
def getDiagnostico(id):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/diagnosticos/'+id
    response=requests.get(url, headers=headers)
    json=response.json()
    return jsonify(json)


@app.route("/diagnosticos", methods=['POST'])
def crearDiagnosticos():
    data=request.get_json()
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/diagnosticos'
    response=requests.post(url, headers=headers, json=data)
    json=response.json()
    return jsonify(json)


@app.route("/diagnosticos/<string:id>", methods=['PUT'])
def modificarDiagnosticos(id):
    data=request.get_json()
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/diagnosticos/'+id
    response=requests.put(url, headers=headers, json=data)
    json=response.json()
    return jsonify(json)


@app.route("/diagnosticos/<string:id>", methods=['DELETE'])
def eliminarDiagnosticos(id):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/diagnosticos/'+id
    response=requests.delete(url, headers=headers)
    json=response.json()
    return jsonify(json)


@app.route("/diagnosticos/<string:id>/paciente/<string:id_paciente>", methods=['PUT'])
def asignarDiagnosticoPaciente(id, id_paciente):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/diagnosticos/'+id+'/paciente/'+id_paciente
    response=requests.put(url, headers=headers)
    json=response.json()
    return jsonify(json)

@app.route("/diagnosticos/<string:id>/evaluador/<string:id_evaluador>", methods=['PUT'])
def asignarDiagnosticoEvaluador(id, id_evaluador):
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-medical"]+'/diagnosticos/'+id+'/evaluador/'+id_evaluador
    response=requests.put(url, headers=headers)
    json=response.json()
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
        return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] +
          ":" + str(dataConfig["port"]))
serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
app.run()
