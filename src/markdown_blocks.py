def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks = markdown.split("\n\n")
    final_blocks = []
    for block in raw_blocks:
        if block == "":
            continue
        block = block.strip()
        final_blocks.append(block)
    return final_blocks
