from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path


DATA_PATH = Path(__file__).with_name("classical_catalog_data.json")


def build_catalog() -> dict[str, list[dict[str, object]]]:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    authors = deepcopy(payload["authors"])
    works = deepcopy(payload["works"])
    authors_by_key = {author["key"]: author for author in authors}
    for work_entry in works:
        author = authors_by_key[work_entry["author_key"]]
        work_entry["author"] = author["name"]
        work_entry["subtitle"] = author["name"]
        work_entry["search_tags"] = ", ".join(work_entry["tags"])
    return {"authors": authors, "works": works}
