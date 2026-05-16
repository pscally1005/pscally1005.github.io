#!/usr/bin/env python3
"""CLI used by GitHub Actions to update the mailing list."""

from __future__ import annotations

import argparse
import sys

from subscribers import subscribe, unsubscribe_by_email, unsubscribe_by_token


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    sub_add = sub.add_parser("subscribe")
    sub_add.add_argument("--email", required=True)

    sub_rm = sub.add_parser("unsubscribe")
    group = sub_rm.add_mutually_exclusive_group(required=True)
    group.add_argument("--token")
    group.add_argument("--email")

    sub_ls = sub.add_parser("list")

    args = parser.parse_args()

    try:
        if args.command == "subscribe":
            message, _created = subscribe(args.email)
            print(message)
        elif args.command == "unsubscribe":
            if args.token:
                print(unsubscribe_by_token(args.token))
            else:
                print(unsubscribe_by_email(args.email))
        elif args.command == "list":
            from subscribers import load_subscribers

            for row in load_subscribers():
                print(row["email"])
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
