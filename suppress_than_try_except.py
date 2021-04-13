from contextlib import suppress

def raise_value_error():
    print('raise value error')
    raise ValueError()

def raise_os_error():
    print('raise os error')
    raise OSError()

class SuppressTest:
    """
    suppress is
    1) convinient
    2) better readability
    than try catch

    stop_propage_with_suppress is equivalent to
    try:
        raise_value_error()
        try:
            raise_os_error()
        except OSError:
            pass
    except ValueError:
        pass
    """
    @staticmethod
    def stop_propagage_with_suppress():
        with suppress(ValueError):
            raise_value_error()
            with suppress(OSError):
                raise_os_error()

    @staticmethod
    def test_return_err():
        with suppress(ValueError) as err:
            raise_value_error()
            # exit this context and dont pass error
        print(err) # None

        with suppress(ValueError) as err:
            raise_os_error()
            # exit this context and pass error
            raise_value_error()
        print(err) # OSError

        with suppress(ValueError) as err:
            raise_value_error()
            # exit this context and dont pass error
            raise_os_error()
        print(err) # None


if __name__ == "__main__":
    SuppressTest.stop_propagage_with_suppress()
    SuppressTest.test_return_err()