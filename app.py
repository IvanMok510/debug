import http.server
import socketserver
import threading
import time

# Basic HTML content with elements for Selenium testing
HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>Selenium Test Page</title>
</head>
<body>
    <h1>Test Page</h1>
    <button id="click-me">Click Me</button>
    <input id="text-input" type="text" placeholder="Enter text">
    <div id="dynamic-content" style="display:none;">Dynamic Text</div>
    <iframe id="test-iframe" srcdoc="<p>Iframe Content</p>"></iframe>
    <a href="javascript:window.open('http://localhost:8000/popup');">Open Popup</a>
    <button onclick="alert('Alert!');">Trigger Alert</button>
    
    <script>
        // Simulate dynamic content
        setTimeout(() => {
            document.getElementById('dynamic-content').style.display = 'block';
        }, 2000);
    </script>
</body>
</html>
"""

POPUP_CONTENT = """
<!DOCTYPE html>
<html>
<body>
    <h1>Popup Window</h1>
</body>
</html>
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode())
        elif self.path == '/popup':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(POPUP_CONTENT.encode())
        else:
            self.send_error(404)

def run_server():
    with socketserver.TCPServer(("", 8000), Handler) as httpd:
        print("Serving at http://localhost:8000")
        httpd.serve_forever()

# Run the server in a background thread
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# Give the server a moment to start
time.sleep(1)

print("Server is running. You can now run Selenium tests against http://localhost:8000")

# Keep the main thread alive by joining the server thread (blocks until Ctrl+C)
server_thread.join()
