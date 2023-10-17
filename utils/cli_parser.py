import argparse
import sys

from utils.consumer import consume_from_kafka
from utils.producer import produce_to_kafka


class CliParser:
    def __init__(self):
        self.command_map = {
            "consume": consume_from_kafka,
            "produce": produce_to_kafka,
        }

    def parse_command_args(self, args):
        """
        If deployment_functions.py is called from the CLI, act as the entrypoint to
        CLI-enabled functions, defined under the command_map.

        e.g.:
        `python3 -m utils.cli_parser --command deploy --args migrations`
        `python3 -m utils.cli_parser --command manual_deploy --args path/to/file`
        """

        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument(
            "--command", "-c", choices=list(self.command_map.keys())
        )
        arg_parser.add_argument("--args", "-a", nargs="+")

        arg_parser.add_argument("--mode", "-m", nargs="?")

        return arg_parser.parse_args(args)


def run(args):
    parser = CliParser()
    parser_args = parser.parse_command_args(args)

    if parser_args.args:
        if parser_args.mode:
            return parser.command_map[parser_args.command](
                *parser_args.args, parser_args.mode
            )
        else:
            return parser.command_map[parser_args.command](*parser_args.args)
    else:
        return parser.command_map[parser_args.command]()


if __name__ == "__main__":  # pragma: no cover
  
    run(sys.argv[1:])