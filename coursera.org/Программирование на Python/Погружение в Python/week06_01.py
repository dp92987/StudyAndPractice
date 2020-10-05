import asyncio

metrics = {}


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        validated_data = self.parse_and_validate(data)
        if validated_data:
            action, params = validated_data
            if action == 'get':
                status = 'ok'
                resp = self.get(params)
            else:
                status = 'ok'
                resp = self.put(params)
        else:
            status = 'error'
            resp = '\nwrong command'
        return f'{status}{resp}\n\n'

    @staticmethod
    def parse_and_validate(data):
        data_list = data.split(maxsplit=1)
        if len(data_list) > 1:
            action = data_list[0]
            params = data_list[1].split()
            if action == 'get' and len(params) == 1:
                return action, params
            elif action == 'put' and len(params) == 3:
                try:
                    params[1] = float(params[1])
                    params[2] = int(params[2])
                    return action, params
                except ValueError:
                    pass

    @staticmethod
    def get(params):
        param = params[0]
        result = '\n'
        if param == '*':
            for metric_name, metric_values in metrics.items():
                for metric_value in metric_values:
                    result = f'{result}{metric_name} {metric_value[0]} {metric_value[1]}\n'
        else:
            metric_values = metrics.get(param, [])
            for metric_value in metric_values:
                result = f'{result}{param} {metric_value[0]} {metric_value[1]}\n'
        return result[:-1]

    @staticmethod
    def put(params):
        param, value, timestamp = params
        metrics.setdefault(param, [])
        for metric in metrics[param]:
            if metric[1] == timestamp:
                metrics[param].remove(metric)
        metrics[param].append((value, timestamp))
        return ''


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8888)
