## %WinDir%\System32\Drivers\Etc

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import time

class S(BaseHTTPRequestHandler):
    def _set_response_1(self):
        self.send_response(200)
        self.send_header('Date', 'Thu, 24 Dec 2020 02:16:38 GMT')############################
        self.send_header('Content-type', 'text/html;charset=utf-8')
        self.send_header('Transfer-Encoding', 'chunked')
        self.send_header('Connection', 'keep-alive')
        self.send_header('Set-Cookie', '__cfduid=daccc159500fb72cd65897aede651b4961608776197; expires=Sat, 23-Jan-21 02:16:37 GMT; path=/; domain=.aomeitech.com; HttpOnly; SameSite=Lax')#########
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'x-requested-with,content-type')
        self.send_header('Expires', 'Thu, 19 Nov 1981 08:52:00 GMT')##########################
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Set-Cookie', 'security_session_verify=7e3b15274031bee5163044dc2c60f85c; expires=Sun, 27-Dec-20 10:16:38 GMT; path=/; HttpOnly')
        self.send_header('Set-Cookie', 'security_session_verify=7e3b15274031bee5163044dc2c60f85c; expires=Sun, 27-Dec-20 10:16:38 GMT; path=/; HttpOnly')
        self.send_header('Set-Cookie', 'PHPSESSID=ucn201mhllhj3r42c3t9m6d26a; path=/')
        self.send_header('Set-Cookie', 'security_session_verify=7e3b15274031bee5163044dc2c60f85c; expires=Sun, 27-Dec-20 10:16:38 GMT; path=/; HttpOnly')
        self.send_header('Vary', 'Accept-Encoding')
##        self.send_header('CF-Cache-Status', 'DYNAMIC')
##        self.send_header('cf-request-id', '073421be0000001a663f9b8000000001')############################
##        self.send_header('Report-To', '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report?s=N99kceVanVEEzfS%2BX4NhdN6%2BGIGeIqco7MIMTU7ApalNCW6Q%2BMmB1Nalay5ApOkH8q3tDHICy79MxjSrS4CzENatO4nrjods9DUMohmym2JrJQ%3D%3D"}],"group":"cf-nel","max_age":604800}')
##        self.send_header('NEL', '{"report_to":"cf-nel","max_age":604800}')
##        self.send_header('Server', 'cloudflare')
##        self.send_header('CF-RAY', '6066d24338131a66-SIN')
        self.end_headers()
        ##a
        ##a608776198
        ##0

    def _set_response_2(self):
        self.send_response(200)
        self.send_header('Date', 'Thu, 24 Dec 2020 02:16:39 GMT')############################
        self.send_header('Content-type', 'text/html;charset=utf-8')
        self.send_header('Transfer-Encoding', 'chunked')
        self.send_header('Connection', 'keep-alive')
        self.send_header('Set-Cookie', '__cfduid=d8cce26958697be809243a0bfb463d40a1608776198; expires=Sat, 23-Jan-21 02:16:38 GMT; path=/; domain=.aomeitech.com; HttpOnly; SameSite=Lax')#########
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'x-requested-with,content-type')
        self.send_header('Expires', 'Thu, 19 Nov 1981 08:52:00 GMT')##########################
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Set-Cookie', 'security_session_verify=7e3b15274031bee5163044dc2c60f85c; expires=Sun, 27-Dec-20 10:16:39 GMT; path=/; HttpOnly')
        self.send_header('Set-Cookie', 'security_session_verify=7e3b15274031bee5163044dc2c60f85c; expires=Sun, 27-Dec-20 10:16:39 GMT; path=/; HttpOnly')
        self.send_header('Set-Cookie', 'PHPSESSID=ucn201mhllhj3r42c3t9m6d26a; path=/')
        self.send_header('Set-Cookie', 'security_session_verify=7e3b15274031bee5163044dc2c60f85c; expires=Sun, 27-Dec-20 10:16:39 GMT; path=/; HttpOnly')
        self.send_header('Vary', 'Accept-Encoding')

    def do_GET(self):
        logging.info("\nGET requests,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        if "/php/sn/recv?client=TOK" == str(self.path):
            self.request_version(HTTP/1.0)
            self._set_response_1()
            self.wfile.write("a\na608776198\n0".encode('utf-8'))
##            self.wfile.write("40\nXk0AKCwxVGgCfAUwYj6tYGUtYjO9Yj6yY8FxYiFyQTwyYAUxWGByWGUEfAHzY6==\n0".encode("utf-8"))
            
        if "/php/sn/recvtestV1?client=" in str(self.path):
            self._set_response_2()
            self.wfile.write("40\nXk0AKCwxVGgCfAUwYj6tYGUtYjO9Yj6yY8FxYiFyQTwyYAUxWGByWGUEfAHzY6==\n0".encode("utf-8"))

def run(server_class=HTTPServer, handler_class=S, port=80):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
