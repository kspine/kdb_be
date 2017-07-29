

class Error(Exception):
    pass


class SvcError(Error):
    pass


class ParamError(Error):
    pass


class OraError(Error):
    pass


class DipDbError(Error):
    pass


class NetError(Error):
    pass


class CheckPrivilegeFailed(Error):
    pass


"""
query and stop
"""


class DataflowNotExistOrNotLoad(Error):
    pass


class DipError(Error):
    pass


"""
create
"""


class ConnectDip(DipError):
    pass


class MaxLimitError(DipError):
    pass


def handle_exception(e):
    def _gen_res(code, msg):
        return {'error_code': code, 'error_msg': msg}

    try:
        raise e
    except NetError as e:
        return _gen_res('00000', str(e))
    except OraError as e:
        return _gen_res('00000', str(e))
    except DipDbError as e:
        return _gen_res('00000', str(e))
    except CheckPrivilegeFailed as e:
        return _gen_res('00000', str(e))
    except DipError as e:
        return _gen_res('00000', str(e))
    except DataflowNotExistOrNotLoad as e:
        return _gen_res('00000', str(e))
    except MaxLimitError as e:
        return _gen_res('00000', str(e))
    except Exception as e:
        return _gen_res('00000', str(e))


if __name__ == '__main__':
    try:
        raise DipError
    except Exception as e:
        print(e)
