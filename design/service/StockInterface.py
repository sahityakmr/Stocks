import logging as log


class StockInterface:

    @staticmethod
    def api_1(request_obj):
        log.info("Received request")
        pass

    @staticmethod
    def api_2(self, request_obj):
        log.info("Received request")
        pass

    @staticmethod
    def api_3(self, request_obj):
        log.info("Received request")
        pass

    @staticmethod
    def api_4(self, request_obj):
        log.info("Received request")
        pass

    @staticmethod
    def api_5(self, request_obj):
        log.info("Received request")
        pass


stock_interface = StockInterface()


def serve_request(request):
    # based on req_type route the request using switch
    return stock_interface.api_1(request)
