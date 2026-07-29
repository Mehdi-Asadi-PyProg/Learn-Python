#!/usr/bin/env python3
"""
================================================================================
  PYTHON CONSOLE PROGRAMMING TUTORIAL
  From Beginner to Advanced
================================================================================

  This single file is a complete, self-contained tutorial for writing
  professional command-line (console) applications in Python.

  Topics covered (in order):
    1.  Introduction & shebang
    2.  print() and basic output
    3.  input() and basic input
    4.  sys.argv – raw command-line arguments
    5.  getopt (legacy, brief overview)
    6.  argparse – the modern standard
         - positional arguments
         - optional arguments / flags
         - short & long options
         - type conversion
         - default values
         - required options
         - choices / restricted values
         - action types (store_true, count, append…)
         - mutually exclusive groups
         - subparsers (sub-commands)
         - argument groups & help customization
    7.  Richer terminal output (colors, progress bars – optional libraries)
    8.  Reading from stdin / piping
    9.  Exit codes & sys.exit()
   10.  Configuration files + argparse (best practice)
   11.  Logging instead of print for real apps
   12.  Packaging a console app (entry points)
   13.  Best practices & checklist

  How to use this file:
    • Read it top-to-bottom.
    • Run individual sections by uncommenting the `if __name__ == "__main__":`
      blocks or by calling the demo functions.
    • Experiment: change values, break things, fix them.

  Requirements: Python 3.8+ (standard library only for core parts).
  Optional extras (mentioned but not required): rich, colorama, tqdm.

================================================================================
"""

# ---------------------------------------------------------------------------
# 1. SHEBANG & MODULE DOCSTRING
# ---------------------------------------------------------------------------
# The line at the very top (`#!/usr/bin/env python3`) is the "shebang".
# On Unix-like systems it tells the OS which interpreter to use when the
# file is executed directly:  ./console_programming_tutorial.py
# On Windows it is ignored; you run the script with `python script.py`.

import sys
import argparse
import logging
from pathlib import Path
from typing import List, Optional


# ---------------------------------------------------------------------------
# 2. BASIC OUTPUT – print()
# ---------------------------------------------------------------------------
def section_print():
    """Demonstrate basic and slightly advanced use of print()."""
    print("=" * 60)
    print("SECTION 2: print()")
    print("=" * 60)

    # Simple output
    print("Hello, console world!")

    # Multiple values (separated by space by default)
    name = "Alice"
    age = 30
    print("Name:", name, "Age:", age)

    # Custom separator and end
    print("one", "two", "three", sep=" | ", end=" <-- done\n")

    # Formatted strings (f-strings – preferred in modern Python)
    print(f"{name} is {age} years old.")

    # Writing to stderr (useful for error messages)
    print("This is an error message", file=sys.stderr)

    # Flush immediately (important when piping or in long-running loops)
    print("Flushed line", flush=True)


# ---------------------------------------------------------------------------
# 3. BASIC INPUT – input()
# ---------------------------------------------------------------------------
def section_input():
    """Demonstrate reading user input interactively."""
    print("\n" + "=" * 60)
    print("SECTION 3: input()")
    print("=" * 60)

    # Basic prompt
    # Uncomment the next lines to try interactively:
    # user_name = input("Enter your name: ")
    # print(f"Hello, {user_name}!")

    # Always strip whitespace and consider validation
    # raw = input("Enter a number: ").strip()
    # try:
    #     number = int(raw)
    # except ValueError:
    #     print("That was not a valid integer.", file=sys.stderr)
    #     sys.exit(1)

    print("(Interactive input examples are commented out so the file can run non-interactively.)")


# ---------------------------------------------------------------------------
# 4. sys.argv – THE RAW ARGUMENT LIST
# ---------------------------------------------------------------------------
def section_sys_argv():
    """Show how to access command-line arguments the hard way."""
    print("\n" + "=" * 60)
    print("SECTION 4: sys.argv")
    print("=" * 60)

    print(f"sys.argv          = {sys.argv}")
    print(f"Script name       = {sys.argv[0]}")
    print(f"Number of args    = {len(sys.argv) - 1}")

    if len(sys.argv) > 1:
        print("Arguments received:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"  [{i}] {arg}")
    else:
        print("No extra arguments were supplied.")
        print("Try running:  python console_programming_tutorial.py hello world 42")

    # Classic manual parsing (fragile – avoid in real code)
    # if len(sys.argv) != 3:
    #     print("Usage: script.py <name> <age>")
    #     sys.exit(1)
    # name = sys.argv[1]
    # age  = int(sys.argv[2])


# ---------------------------------------------------------------------------
# 5. getopt – LEGACY MODULE (brief mention only)
# ---------------------------------------------------------------------------
def section_getopt():
    """Very short note about the older getopt module."""
    print("\n" + "=" * 60)
    print("SECTION 5: getopt (legacy)")
    print("=" * 60)
    print(
        "The getopt module (inspired by C's getopt) exists but is rarely used\n"
        "in new Python code. Prefer argparse (or click / typer for bigger apps).\n"
        "We skip practical examples here."
    )


# ---------------------------------------------------------------------------
# 6. argparse – THE STANDARD WAY
# ---------------------------------------------------------------------------

# ---- 6.1 Minimal example -------------------------------------------------
def demo_minimal_argparse():
    """
    Smallest useful argparse program.
    Run:  python console_programming_tutorial.py minimal Alice
    """
    parser = argparse.ArgumentParser(description="Minimal greeter")
    parser.add_argument("name", help="Person to greet")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


# ---- 6.2 Positional + optional arguments ---------------------------------
def demo_basic_argparse():
    """
    Demonstrates positional arguments, optional flags, types, defaults.
    Examples:
      python console_programming_tutorial.py basic Alice
      python console_programming_tutorial.py basic Alice --age 28
      python console_programming_tutorial.py basic Alice -a 28 --verbose
      python console_programming_tutorial.py basic --help
    """
    parser = argparse.ArgumentParser(
        prog="greeter",
        description="A friendly command-line greeter",
        epilog="Thanks for trying the tutorial!",
    )

    # Positional argument (required by default)
    parser.add_argument("name", help="Name of the person to greet")

    # Optional argument with short and long form
    parser.add_argument(
        "-a", "--age",
        type=int,                 # automatic conversion + validation
        default=None,
        help="Age of the person (optional)",
    )

    # Boolean flag (store_true)
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    # Another common pattern: count how many times a flag appears
    parser.add_argument(
        "-q", "--quiet",
        action="count",
        default=0,
        help="Reduce output (can be repeated: -qq)",
    )

    args = parser.parse_args()

    # Use the parsed values
    greeting = f"Hello, {args.name}"
    if args.age is not None:
        greeting += f" (age {args.age})"
    greeting += "!"

    if args.verbose:
        print(f"[verbose] Parsed arguments: {args}")
    if args.quiet == 0:
        print(greeting)
    elif args.quiet == 1:
        print(f"Hi {args.name}")
    else:
        pass  # completely silent


# ---- 6.3 Choices, required options, append action ------------------------
def demo_advanced_options():
    """
    Shows restricted choices, required flags, and collecting multiple values.
    Examples:
      python console_programming_tutorial.py options --color red file1.txt
      python console_programming_tutorial.py options --color blue -i a -i b out.txt
    """
    parser = argparse.ArgumentParser(description="Advanced options demo")

    parser.add_argument("output", help="Output filename")

    parser.add_argument(
        "--color",
        choices=["red", "green", "blue"],
        required=True,
        help="Text color (required)",
    )

    parser.add_argument(
        "-i", "--include",
        action="append",          # can be repeated; builds a list
        default=[],
        help="Include pattern (repeatable)",
    )

    parser.add_argument(
        "--mode",
        choices=["fast", "safe"],
        default="safe",
        help="Processing mode (default: safe)",
    )

    args = parser.parse_args()
    print(f"Output   : {args.output}")
    print(f"Color    : {args.color}")
    print(f"Includes : {args.include}")
    print(f"Mode     : {args.mode}")


# ---- 6.4 Mutually exclusive groups ---------------------------------------
def demo_mutex_group():
    """
    Only one of the options in a mutually exclusive group may be given.
    Example:
      python console_programming_tutorial.py mutex --json
      python console_programming_tutorial.py mutex --xml
      # both together → error
    """
    parser = argparse.ArgumentParser(description="Mutually exclusive group demo")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--json", action="store_true", help="Output JSON")
    group.add_argument("--xml",  action="store_true", help="Output XML")
    group.add_argument("--csv",  action="store_true", help="Output CSV")

    args = parser.parse_args()
    if args.json:
        print('{"status": "ok"}')
    elif args.xml:
        print("<status>ok</status>")
    else:
        print("status,ok")


# ---- 6.5 Subparsers (sub-commands) – the power feature -------------------
def demo_subparsers():
    """
    Many real CLIs (git, docker, pip…) use sub-commands.
    Examples:
      python console_programming_tutorial.py subcmd init --force
      python console_programming_tutorial.py subcmd build --target release
      python console_programming_tutorial.py subcmd --help
      python console_programming_tutorial.py subcmd init --help
    """
    parser = argparse.ArgumentParser(prog="mytool", description="Tool with sub-commands")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # ---- init sub-command ----
    parser_init = subparsers.add_parser("init", help="Initialize a new project")
    parser_init.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser_init.add_argument("--name", default="project", help="Project name")

    # ---- build sub-command ----
    parser_build = subparsers.add_parser("build", help="Build the project")
    parser_build.add_argument(
        "--target",
        choices=["debug", "release"],
        default="debug",
        help="Build target",
    )
    parser_build.add_argument("-j", "--jobs", type=int, default=1, help="Parallel jobs")

    # ---- clean sub-command ----
    parser_clean = subparsers.add_parser("clean", help="Remove build artifacts")
    parser_clean.add_argument("--all", action="store_true", help="Also remove caches")

    args = parser.parse_args()

    if args.command == "init":
        print(f"Initializing project '{args.name}' (force={args.force})")
    elif args.command == "build":
        print(f"Building target={args.target} with {args.jobs} job(s)")
    elif args.command == "clean":
        print(f"Cleaning (all={args.all})")


# ---- 6.6 Argument groups & custom help formatting ------------------------
def demo_argument_groups():
    """
    Logical grouping improves --help readability for complex tools.
    """
    parser = argparse.ArgumentParser(
        description="Demo of argument groups",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # shows defaults in help
    )

    # Positional
    parser.add_argument("infile", help="Input file")

    # Group 1
    input_group = parser.add_argument_group("Input options")
    input_group.add_argument("--encoding", default="utf-8", help="File encoding")
    input_group.add_argument("--skip-header", action="store_true", help="Skip first line")

    # Group 2
    output_group = parser.add_argument_group("Output options")
    output_group.add_argument("-o", "--output", default="out.txt", help="Output file")
    output_group.add_argument("--overwrite", action="store_true", help="Overwrite existing")

    args = parser.parse_args()
    print(args)


# ---- 6.7 Custom type / validation functions ------------------------------
def positive_int(value: str) -> int:
    """Custom type that only accepts positive integers."""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue


def demo_custom_type():
    """
    Example:
      python console_programming_tutorial.py custom --count 5
      python console_programming_tutorial.py custom --count -3   # error
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=positive_int, required=True)
    args = parser.parse_args()
    print(f"Count = {args.count}")


# ---------------------------------------------------------------------------
# 7. RICHER TERMINAL OUTPUT (optional libraries)
# ---------------------------------------------------------------------------
def section_rich_output():
    """
    Mention popular libraries that make console apps beautiful.
    They are NOT part of the standard library.
    """
    print("\n" + "=" * 60)
    print("SECTION 7: Richer terminal output")
    print("=" * 60)
    print(
        """
Popular third-party libraries:

  • colorama / rich          – colored text, tables, markdown, panels
  • tqdm / rich.progress     – progress bars
  • click / typer            – higher-level CLI frameworks (built on argparse ideas)
  • prompt_toolkit           – advanced interactive prompts & auto-completion

Example with the standard library only (ANSI escape codes):
"""
    )
    # Simple ANSI colors (work on most modern terminals)
    RED    = "\033[31m"
    GREEN  = "\033[32m"
    YELLOW = "\033[33m"
    RESET  = "\033[0m"
    print(f"{GREEN}Success{RESET}  |  {YELLOW}Warning{RESET}  |  {RED}Error{RESET}")


# ---------------------------------------------------------------------------
# 8. READING FROM STDIN / PIPING
# ---------------------------------------------------------------------------
def section_stdin():
    """
    Real console tools often accept data from pipes.
    Example usage:
      echo "hello world" | python console_programming_tutorial.py stdin
      cat file.txt | python console_programming_tutorial.py stdin
    """
    print("\n" + "=" * 60)
    print("SECTION 8: Reading from stdin")
    print("=" * 60)

    if sys.stdin.isatty():
        print("No piped input detected (stdin is a terminal).")
        print("Try:  echo 'hello' | python console_programming_tutorial.py stdin")
    else:
        data = sys.stdin.read()
        print(f"Received {len(data)} characters from stdin:")
        print(data[:200] + ("…" if len(data) > 200 else ""))


# ---------------------------------------------------------------------------
# 9. EXIT CODES
# ---------------------------------------------------------------------------
def section_exit_codes():
    """
    Convention:
      0   → success
      1   → general error
      2   → misuse of shell builtins / invalid arguments (argparse uses this)
      130 → terminated by Ctrl-C (SIGINT)
    """
    print("\n" + "=" * 60)
    print("SECTION 9: Exit codes")
    print("=" * 60)
    print("Use sys.exit(code) or raise SystemExit(code).")
    print("argparse automatically exits with code 2 on usage errors.")


# ---------------------------------------------------------------------------
# 10. COMBINING ARGPARSE WITH CONFIG FILES (common pattern)
# ---------------------------------------------------------------------------
def demo_config_and_args():
    """
    Typical pattern in real applications:
      1. Define defaults
      2. Load config file (if present)
      3. Let command-line arguments override everything
    """
    print("\n" + "=" * 60)
    print("SECTION 10: Config file + argparse pattern")
    print("=" * 60)

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, help="Path to config file")
    parser.add_argument("--host", default=None)
    parser.add_argument("--port", type=int, default=None)
    args = parser.parse_args([])          # empty for demo; normally parse_args()

    # Simulated config
    config = {"host": "localhost", "port": 8080}
    if args.config and args.config.exists():
        # In real code you would load JSON/YAML/TOML here
        pass

    # Command-line wins
    host = args.host or config["host"]
    port = args.port or config["port"]
    print(f"Final host={host}, port={port}")


# ---------------------------------------------------------------------------
# 11. LOGGING INSTEAD OF PRINT
# ---------------------------------------------------------------------------
def section_logging():
    """
    For any non-trivial program prefer the logging module.
    """
    print("\n" + "=" * 60)
    print("SECTION 11: logging")
    print("=" * 60)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )
    log = logging.getLogger("demo")

    log.debug("This appears only if level is DEBUG")
    log.info("Application started")
    log.warning("Something looks suspicious")
    log.error("An error occurred")
    # log.exception("…")  # includes traceback when used inside except block


# ---------------------------------------------------------------------------
# 12. PACKAGING A CONSOLE APPLICATION
# ---------------------------------------------------------------------------
def section_packaging():
    """
    How to turn your script into an installable command.
    """
    print("\n" + "=" * 60)
    print("SECTION 12: Packaging (entry points)")
    print("=" * 60)
    print(
        """
In pyproject.toml (modern) or setup.cfg / setup.py:

  [project.scripts]
  mygreeter = "mypackage.cli:main"

Then after `pip install .` the user can simply type:

  mygreeter Alice --age 30

The function `main()` usually looks like:

  def main(argv: Optional[List[str]] = None) -> int:
      parser = build_parser()
      args = parser.parse_args(argv)
      … do work …
      return 0

  if __name__ == "__main__":
      sys.exit(main())
"""
    )


# ---------------------------------------------------------------------------
# 13. BEST PRACTICES CHECKLIST
# ---------------------------------------------------------------------------
def section_best_practices():
    print("\n" + "=" * 60)
    print("SECTION 13: Best practices checklist")
    print("=" * 60)
    print(
        """
✓  Always provide a clear description and helpful --help text
✓  Use type= and choices= for automatic validation
✓  Prefer subparsers over a giant list of flags when the tool has modes
✓  Return meaningful exit codes
✓  Write errors to stderr, normal output to stdout (so piping works)
✓  Make the program usable both interactively and in scripts/pipelines
✓  Add a --version flag (action="version", version="%(prog)s 1.0")
✓  Keep the main() function small; put logic in other functions/modules
✓  Document the expected environment (Python version, optional deps)
✓  Consider click or typer once the CLI grows beyond ~15 options
"""
    )


# ---------------------------------------------------------------------------
# MAIN DISPATCHER
# ---------------------------------------------------------------------------
def build_main_parser() -> argparse.ArgumentParser:
    """Top-level parser that selects which demo / section to run."""
    parser = argparse.ArgumentParser(
        description="Python Console Programming Tutorial – interactive demos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available demos
---------------
  print, input, argv, getopt, minimal, basic, options,
  mutex, subcmd, groups, custom, rich, stdin, exit,
  config, logging, packaging, practices, all
        """,
    )
    parser.add_argument(
        "demo",
        nargs="?",
        default="all",
        help="Which section/demo to run (default: all)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available demos and exit",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    # We need a two-stage parse because the demos themselves also use argparse.
    # First we only look at the very first argument to decide which demo.
    if argv is None:
        argv = sys.argv[1:]

    if not argv or argv[0] in ("-h", "--help"):
        build_main_parser().print_help()
        return 0

    if argv[0] == "--list":
        print("Available demos: print, input, argv, getopt, minimal, basic,")
        print("  options, mutex, subcmd, groups, custom, rich, stdin, exit,")
        print("  config, logging, packaging, practices, all")
        return 0

    demo = argv[0]
    remaining = argv[1:]

    # Temporarily replace sys.argv so the demo parsers see only their own args
    original_argv = sys.argv
    sys.argv = [original_argv[0]] + remaining

    try:
        if demo == "print":
            section_print()
        elif demo == "input":
            section_input()
        elif demo == "argv":
            section_sys_argv()
        elif demo == "getopt":
            section_getopt()
        elif demo == "minimal":
            demo_minimal_argparse()
        elif demo == "basic":
            demo_basic_argparse()
        elif demo == "options":
            demo_advanced_options()
        elif demo == "mutex":
            demo_mutex_group()
        elif demo == "subcmd":
            demo_subparsers()
        elif demo == "groups":
            demo_argument_groups()
        elif demo == "custom":
            demo_custom_type()
        elif demo == "rich":
            section_rich_output()
        elif demo == "stdin":
            section_stdin()
        elif demo == "exit":
            section_exit_codes()
        elif demo == "config":
            demo_config_and_args()
        elif demo == "logging":
            section_logging()
        elif demo == "packaging":
            section_packaging()
        elif demo == "practices":
            section_best_practices()
        elif demo == "all":
            section_print()
            section_input()
            section_sys_argv()
            section_getopt()
            section_rich_output()
            section_stdin()
            section_exit_codes()
            demo_config_and_args()
            section_logging()
            section_packaging()
            section_best_practices()
            print("\n" + "=" * 60)
            print("Argparse demos are interactive – run them individually:")
            print("  python console_programming_tutorial.py basic --help")
            print("  python console_programming_tutorial.py subcmd init --force")
            print("  python console_programming_tutorial.py options --color red out.txt")
            print("=" * 60)
        else:
            print(f"Unknown demo: {demo}", file=sys.stderr)
            print("Use --list to see available demos.", file=sys.stderr)
            return 1
    finally:
        sys.argv = original_argv

    return 0


"""
# Show help
python console_programming_tutorial.py --help

# List all demos
python console_programming_tutorial.py --list

# Run the non-interactive overview
python console_programming_tutorial.py all

# Try specific demos
python console_programming_tutorial.py basic Alice --age 28 -v
python console_programming_tutorial.py subcmd init --force --name myapp
python console_programming_tutorial.py options --color red -i a -i b out.txt
python console_programming_tutorial.py mutex --json
python console_programming_tutorial.py custom --count 5

"""



if __name__ == "__main__":
    sys.exit(main())
