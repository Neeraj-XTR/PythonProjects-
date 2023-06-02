# # Created a simple route using flask
# from flask import Flask,request,jsonify
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "HOME"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# # Creating a more complex route towards the api
# # GET route
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
#
# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "Neeraj",
#         "email": "xyz@ex.com"
#     }
#
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra
#
#     return jsonify(user_data), 200
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


# # POST Request
