from .stats import parse_args
from time import sleep
# import os


def main():
    # os.system('clear')
    args = parse_args()
    while True:
        args.func(args)
        if args.refresh == 0:
            break
        else:
            try:
                sleep(args.refresh)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()
