"""命令行随机密码生成器。

示例：
    py -3 password_generator.py
    py -3 password_generator.py --length 20 --no-symbols
"""

from __future__ import annotations

import argparse
import random
import string
import sys


def build_alphabet(use_symbols: bool) -> str:
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += "!@#$%^&*?-_"
    return alphabet


def generate_password(length: int, use_symbols: bool) -> str:
    if length < 4:
        raise ValueError("长度至少 4")

    pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if use_symbols:
        pools.append("!@#$%^&*?-_")

    # 每类至少取 1 个，避免弱密码
    chars = [random.choice(pool) for pool in pools]
    alphabet = build_alphabet(use_symbols)
    chars.extend(random.choice(alphabet) for _ in range(length - len(chars)))
    random.shuffle(chars)
    return "".join(chars)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成随机密码（只打印，不保存）")
    parser.add_argument("--length", type=int, default=12, help="密码长度，默认 12，至少 4")
    parser.add_argument("--no-symbols", action="store_true", help="不使用符号")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        password = generate_password(args.length, use_symbols=not args.no_symbols)
    except ValueError as exc:
        print("错误:", exc, file=sys.stderr)
        return 1
    print(password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
