#!/usr/bin/env python3
#
# Udacian activity to practice http get and post 
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs



memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
    	# Submit the form
        #how long is the message
        length = int(self.headers.get('Content-length', 0))
        # Read the correct amount of data from the request.
        body = self.rfile.read(length).decode()
        params = parse_qs(body)

        message =''

        student_name= params["name"][0]
        city_name = params["city"][0]
        enrolment_name = params["enrollment"][0]
        nanodegree_name = params["nanodegree"][0]
        status_code = params["status"][0]
        #student_object = Udacian(params["name"][0],params["city"][0],params["enrollment"][0],params["nanodegree"][0],params["status"][0])
        message = "student " + student_name + " is enrolled in " + city_name + " studing " + enrolment_name + " in " + nanodegree_name + " and hi is " + status_code

        # Escape HTML tags in the message so users can't break world+dog.
        #message = message.replace("<", "&lt;")

        #Store it in memory.
        #memory.append(message)

        # 1. Send a 303 redirect back to the root page.
        self.send_response(200)

        self.send_header('location', '/')
        self.end_headers()
        self.wfile.write(form.format(message).encode())


    def do_GET(self):
        #get the info and display it
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # 2. Put the response together out of the form and the stored messages.
        #known = "\n".join("{} : {}".format(key, memory[key])
                             # for key in sorted(memory.keys()))
        self.wfile.write(form.format('').encode())



if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
