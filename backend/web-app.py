from http.server import HTTPServer, BaseHTTPRequestHandler

HOSTNAME = "localhost"
PORT = 8080

# Класс-обработчик входящих запросов
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # 2. Отправляем заголовки (headers)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        # 3. Отправляем тело ответа
        self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))

# Инициализация сервера
webServer = HTTPServer((HOSTNAME, PORT), MyHandler)
print(f"Сервер запущен: http://{HOSTNAME}:{PORT}")

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    print("Работа сервера прервана")

webServer.server_close()
print("Сервер остановлен...")