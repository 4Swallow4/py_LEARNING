"""命令行待办本，数据保存在 数据样例/todo.json。

示例：
    py -3 todo.py list
    py -3 todo.py add "把第 8 章跑完"
    py -3 todo.py done 4
    py -3 todo.py remove 1
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_STORE = ROOT / "数据样例" / "todo.json"


def load_todos(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON 损坏：{path}") from exc
    if not isinstance(data, list):
        raise ValueError("待办文件必须是列表")
    return data


def save_todos(path: Path, todos: list[dict[str, Any]]) -> None:
    path.write_text(
        json.dumps(todos, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def next_id(todos: list[dict[str, Any]]) -> int:
    if not todos:
        return 1
    return max(int(item["id"]) for item in todos) + 1


def cmd_list(todos: list[dict[str, Any]], show_all: bool) -> None:
    visible = todos if show_all else [t for t in todos if not t.get("done")]
    if not visible:
        print("没有待办。" if show_all else "没有未完成的待办。用 list --all 看全部。")
        return
    for item in visible:
        mark = "x" if item.get("done") else " "
        print(f"[{mark}] {item['id']}. {item['text']}")


def cmd_add(todos: list[dict[str, Any]], text: str) -> None:
    text = text.strip()
    if not text:
        raise ValueError("待办内容不能为空")
    todos.append({"id": next_id(todos), "text": text, "done": False})
    print("已添加:", text)


def find_item(todos: list[dict[str, Any]], item_id: int) -> dict[str, Any]:
    for item in todos:
        if int(item["id"]) == item_id:
            return item
    raise ValueError(f"没有 id={item_id} 的待办")


def cmd_done(todos: list[dict[str, Any]], item_id: int) -> None:
    item = find_item(todos, item_id)
    item["done"] = True
    print("已完成:", item["text"])


def cmd_remove(todos: list[dict[str, Any]], item_id: int) -> None:
    item = find_item(todos, item_id)
    todos.remove(item)
    print("已删除:", item["text"])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="超小的命令行待办本")
    parser.add_argument(
        "--store",
        type=Path,
        default=DEFAULT_STORE,
        help="JSON 存储路径",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="列出待办")
    p_list.add_argument("--all", action="store_true", help="包含已完成")

    p_add = sub.add_parser("add", help="新增")
    p_add.add_argument("text", help="待办内容")

    p_done = sub.add_parser("done", help="标记完成")
    p_done.add_argument("id", type=int)

    p_remove = sub.add_parser("remove", help="删除")
    p_remove.add_argument("id", type=int)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store: Path = args.store
    try:
        todos = load_todos(store)
        if args.command == "list":
            cmd_list(todos, show_all=args.all)
            return 0
        if args.command == "add":
            cmd_add(todos, args.text)
        elif args.command == "done":
            cmd_done(todos, args.id)
        elif args.command == "remove":
            cmd_remove(todos, args.id)
        else:
            parser.error(f"未知命令 {args.command}")
        save_todos(store, todos)
    except (OSError, ValueError) as exc:
        print("错误:", exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
