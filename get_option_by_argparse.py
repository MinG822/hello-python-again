import argparse

SMART = "smart"
DULL = "dull"

def get_test_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="square the given number")
    parser.add_argument("mode", help=f"set mode: {SMART} or {DULL}")
    parser.add_argument("--verbose", "-v", action = "store_true", help="tmi")
    return parser


def parse_args(parser):
    # TODO check
    # parser is isinstance(parser, (argparse.ArgumentParser,)) -> False
    if parser and type(parser) == argparse.ArgumentParser:
        args = parser.parse_args()
        mode = args.mode
        operand = args.square
        is_verbose = args.verbose
        if is_verbose:
            print("Yeah~ I got args! Now we will see")
        return mode, operand, is_verbose
    else:
        raise ValueError()


def square_by_option(mode, operand, is_verbose):
    # TODO check
    # SMART_TYPE = Literal["smart", "dull"] , type(mode) == SMART_TYPE -> FALSE
    if is_verbose:
        print(f"I will gonna be square {operand}")
    if mode == SMART:
        print(f"Mmm it is {operand ** 2} !!")
    elif mode == DULL:
        print(f"Well.. is it {operand * 2} ??")
    else:
        raise ValueError()


if __name__ == "__main__":
    square_by_option(*parse_args(get_test_parser()))