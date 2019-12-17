"""API que expone los métodos del servicio para monitoreo."""
import os
import subprocess

from flask import Flask, jsonify, redirect, url_for, request
from monitoring.monitor import predict_CTF


def instance_api():
    """Crea una instancia del objeto WSGI de la API.

    Usamos esta función para poder usar el objeto con pytest y gunicorn.
    """
    api = Flask("api")

    @api.route("/")
    def index():
        return redirect(url_for("alive"))

    @api.route("/alive")
    def alive():
        return jsonify({"alive": True})

    @api.route("/predict", methods=["GET"])
    def predict():
        output = predict_CTF()
        return jsonify(output)

    @api.route("/data/upload", methods=["POST"])
    def upload_data():
        if request.files:
            version = 1
            data_file_path = os.sep.join([os.environ.get("DATA_PATH", "./src/monitoring/data"), "data_to_predict"])
            while os.path.exists(f"{data_file_path}_{version}.csv"):
                version += 1

            curr_data_file = data_file_path + ".csv"
            versioned_data_path = f"{data_file_path}_{version}.csv"

            if os.path.exists(curr_data_file):
                subprocess.run(["mv", curr_data_file, versioned_data_path])

            file = request["files"].get("csv")
            file.save(curr_data_file)
            return jsonify(message="Data saved successfully.", success=True)

        else:
            return jsonify({"message": "No data file was received.", "success": False})
    # @api.errorhandler(Exception)
    # def handle_exceptions(error):
    #     print(error)
    #     return jsonify({"success": False})

    # @api.route("/monitor", methods=["POST"])
    # def monitor():
    #     return jsonify(message="hi")

    return api


if __name__ == "__main__":
    api = instance_api()
    api.run(host="0.0.0.0", port="8080", debug=True, use_reloader=True)



