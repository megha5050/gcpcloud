import requests
import pprint
import flask
from flask import request, jsonify
host='0.0.0.0'
port='3000'

master_app=flask.Flask(__name__)



@master_app.route('/', methods=['GET'])
def home_page():
    return '''
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Welcome to My Sample Webpage</title>
</head>

<body>

  <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">

<!--HEADER -->

		<tbody><tr>
		<td align="center">
		<table class="col-800" width="900" border="0" align="center" cellpadding="0" cellspacing="0">
		<tbody><tr>
		<td align="center" valign="top" background="&fm=jpg" bgcolor="#66809b" style="background-size:cover; background-position:top;height=" 400""="">
		<table class="col-600" width="600" height="400" border="0" align="center" cellpadding="0" cellspacing="0">

		<tbody><tr>
		<td height="40"></td>
		</tr>

		<tr>
		<td align="center" style="line-height: 0px;">
		<img style="display:block; line-height:0px; font-size:0px; border:0px;" src="https://cloud.google.com/images/social-icon-google-cloud-1200-630.png" width="300" height="200" alt="logo">
		</td>
		</tr>

		<tr>
		<td align="center" style="font-family: 'Raleway', sans-serif; font-size:37px; color:#ffffff; line-height:24px; font-weight: bold; letter-spacing: 5px;">
	WELCOME <span style="font-family: 'Raleway', sans-serif; font-size:37px; color:#ffffff; line-height:39px; font-weight: 300; letter-spacing: 5px;"> TO MICROSERVICES DEPLOYMENT</span>
		</td>
		</tr>


		<tr>
		<td align="center" style="font-family: 'Lato', sans-serif; font-size:15px; color:#ffffff; line-height:24px; font-weight: 300;">
	Here we will have a demo on How to Deploy MicroServices in Google Cloud Platform and retrive its IP ADDRESS.
		</td>
		</tr>


		<tr>
		<td height="50"></td>
		</tr>
		</tbody></table>
		</td>
		</tr>
		</tbody></table>
		</td>
		</tr>


<!-- END HEADERR -->



		</tbody></table>

</body>
</html>'''


@master_app.route("/getip", methods=["GET"])
def get_my_ip():
    return jsonify({'IP ADDRESS OF THE MACHINE': request.remote_addr}), 200


master_app.run(host,port)
