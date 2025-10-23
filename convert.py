def simplify_dot(input_path: str, output_path: str):
    edges: dict[str, list[str]] = {}

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = "".join([i for i in line if i not in "\t\n;"]).split(" -> ")
            if parts[0] not in edges:
                edges[parts[0]] = []
            edges[parts[0]].append(parts[1])

    with open(output_path, 'w', encoding='utf-8') as f:
        for src, targets in sorted(edges.items()):
            parts = [f"\"{t}\"" for t in targets]
            target_str = "{ " + f"{" ".join(targets)}" + " }" if len(targets) > 1 else targets[0]
            print(target_str)
            f.write(f"{src} -> {target_str}\n")

simplify_dot("line.dot", "simp.dot")
