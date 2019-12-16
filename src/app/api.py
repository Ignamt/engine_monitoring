"""API que expone los métodos del servicio para monitoreo."""
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



