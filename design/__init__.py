from design.service import RequestBaker as baker, StockInterface as manger, CalculatorCommandLineInterface as cli


def drive():
    input_map = cli.get_cli_request()
    api_req = baker.bake(input_map)
    manger.serve_request(api_req)


if __name__ == '__main__':
    drive()
