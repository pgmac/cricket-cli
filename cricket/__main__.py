from .stats import parse_args


def main():
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
