import time
import socket


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.conn = socket.create_connection((host, port))
        if timeout:
            self.conn.settimeout(timeout)

    def get(self, metric_name):
        data = f'get {metric_name}\n'
        response = self._send_and_receive(data)
        status, data = response.split('\n', maxsplit=1)
        print(response.encode())
        if status != 'ok':
            raise ClientError

        metrics = {}
        data = data.strip()
        if data == '':
            return metrics

        try:
            for line in data.split('\n'):
                metric_name, metric_value, timestamp = line.split()
                if metric_name not in metrics:
                    metrics[metric_name] = []
                metrics[metric_name].append((int(timestamp), float(metric_value)))
        except (IndexError, ValueError):
            raise ClientError

        for metric in metrics.values():
            metric.sort(key=lambda x: x[0])

        return metrics

    def put(self, metric, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        data = f'put {metric} {value} {timestamp}\n'
        response = self._send_and_receive(data)
        if not response == 'ok\n\n':
            raise ClientError

    def _send_and_receive(self, data):
        self.conn.sendall(data.encode())
        return self.conn.recv(1024).decode()


def main():
    c = Client('127.0.0.1', 8888)
    c.put(metric='palm.cpu', value=0.5, timestamp=1150864245)
    c.put(metric='palm.cpu', value=0.6, timestamp=1150864243)
    c.put(metric='palm.cpu', value=0.7, timestamp=1150864246)
    print(c.get('palm.cpu'))
    # print(c.get('palm.cpu1'))


if __name__ == '__main__':
    main()
