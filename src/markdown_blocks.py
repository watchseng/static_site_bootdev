def markdown_to_blocks(markdown):
    clean_block_list = []
    block_list = markdown.split('\n\n')
    for block in block_list:
        if not block == "":
            clean_block_list.append(block.strip())
    return clean_block_list
