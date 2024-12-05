'''
-----------------------------------------------
This is an module for testing the viability of
a CLI for the Boundary Plotter toolset
-----------------------------------------------
'''

import os
import argparse
from pyfiglet import figlet_format as pf #this is unecessary, but it makes me happy. . .
from angles import decimal_degree_to_quad_bearing,decimal_degree_to_azimuth,parse_bearing,Angle

def parse_bearing_command(args):
    result = parse_bearing(args.bearing)
    print(f"   >>>Decimal Degrees: {result}")

def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(
        prog=__name__
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: parse_bearing
    parser_parse = subparsers.add_parser("parse_bearing",aliases=["-pb","bearing","pb"],help="Parse a bearing string into decimal degrees.")
    parser_parse.add_argument("bearing", type=str, nargs="?", help="The bearing string to parse (e.g., 'N32°10'32\"E').")
    parser_parse.set_defaults(func=parse_bearing_command)

    # Command: decimal_degree_to_azimuth
    parser_azimuth = subparsers.add_parser(
        "decimal_degree_to_azimuth", help="Convert decimal degrees into an azimuth bearing."
    )
    parser_azimuth.add_argument("decimal_degree", type=float, nargs="?", help="The decimal degree to convert.")
    parser_azimuth.set_defaults(func=decimal_degree_to_azimuth)

    # Command: decimal_degree_to_quad_bearing
    parser_quad = subparsers.add_parser(
        "decimal_degree_to_quad_bearing", help="Convert decimal degrees into a quadrant bearing."
    )
    parser_quad.add_argument("decimal_degree", type=float, nargs="?", help="The decimal degree to convert.")
    parser_quad.set_defaults(func=decimal_degree_to_quad_bearing)

    # Start interactive mode
    print(pf(font="dos_rebel",text='angles'))
    print("Welcome to the Survey Bearing Conversion Tool CLI!")
    print("Type 'help' to see available commands or 'exit' to quit.\n")

    while True:
        try:
            user_input = input(">> ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            if not user_input:
                continue
            args = parser.parse_args(user_input.split())
            if hasattr(args, "func"):
                if any(value is None for value in vars(args).values() if value != args.command):
                    # Prompt for missing arguments
                    for key, value in vars(args).items():
                        if value is None and key != "command":
                            args.__dict__[key] = input(f"Enter value for '{key}': ")
                args.func(args)
            else:
                parser.print_help()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            continue

class _help():

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir,"cli_help.md")
        self._text: str = open(file=file_path, mode='r').read()
    
    def __repr__(self):
        return self._text        

if __name__ == "__main__":
    main()
    