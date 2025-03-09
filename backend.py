import http.server
import socketserver
import os
import cgi
import base64
import json
from test import recognize_image  # Import your image recognition function

# Create an uploads directory if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data (file upload)
        content_type, params = cgi.parse_header(self.headers.get('Content-Type'))
        if content_type == 'multipart/form-data':
            # Use the FieldStorage class from cgi to parse the form data
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
            file_item = form['file']  # This retrieves the file item from the form

            if file_item is not None and file_item.filename:
                # Save the uploaded file to the "uploads" folder
                file_name = os.path.basename(file_item.filename)
                file_path = os.path.join('uploads', file_name)

                # Open the file and save its content
                with open(file_path, 'wb') as f:
                    f.write(file_item.file.read())

                # Call the Python script to recognize the image
                processed_image_path = recognize_image(file_name)
                with open(processed_image_path, "rb") as img_file:
                    encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                # Return the recognition result as JSON
                response = {
                    "image": encoded_string
                }
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Bad request: No file uploaded.")

    def do_GET(self):
        # Serve static files (like the HTML file) from the current directory
        return super().do_GET()

# Start the server
PORT = 8000
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
