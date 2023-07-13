import argparse

from db2ndb.main import gather_transformers, transform


def run(argv=None):
    parser = argparse.ArgumentParser("db2ndb")
    parser.add_argument("file")
    parser.add_argument(
        "-w",
        "--write",
        action="store_true",
        help="Write back modified files.",
    )
    parser.add_argument(
        "--disable",
        action="append",
        metavar="TRANSFORMATION",
        help="Disable a transformation.",
        dest="disabled_transformations",
    )

    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return exc.code

    with open(args.file) as f:
        transformers = gather_transformers(args.disabled_transformations)
        out = transform(f.read(), transformers)

    if args.write:
        with open(args.file, "w") as f:
            f.write(out)
    else:
        print(out)

    return 0
