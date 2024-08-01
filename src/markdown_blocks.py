
text_block = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

def markdown_to_blocks(markdown):
    answer = []
    strings = markdown.split("\n\n")
    for item in strings:
        if item != "":
            answer.append(item.strip())
    return answer


markdown_to_blocks(text_block)


def block_to_block_type(text_block):
    ...