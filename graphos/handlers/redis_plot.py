""" Redis Plot Data Handler """

from .base_plot import BasePlotDataHandler


class RedisPlotDataHandler(BasePlotDataHandler):

    server_address = ''
    x_list_name = ''

    def __init__(self, server_address, x_list_name, *args, **kwargs):
        self.server_address = model_name
        self.x_list_name = field_name
        super(RedisPlotDataHandler, self).__init__(
            server_address, x_list_name, *args, **kwargs)

    def get_data_instance(self):
        try:
            import redis
        except ImportError, e:
            logging.error("redis -redis server \
                binding for Python is not installed. \
                            Try pip install redis")

        from redis import ConnectionError
        r_inst = redis.Redis(server_address)
        r_inst.ping()

        return r_inst

    def get_data(self):

        data = super(RedisPlotDataHandler, self).get_data()

        data.update({
            'server_address': self.server_address,
            'x_list_name': self.x_list_name,
        })

        return data

    def get_template(self):

        template = 'graphos/redis_template.html'

        return template
