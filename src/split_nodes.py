from textnode import TextNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []    
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        
        else:
            chunks = node.text.split(delimiter)

            if len(chunks) % 2 == 0:    
                raise Exception("Invalid markdown syntax - missing opening or closing delimiter.")

            for i in range(len(chunks)):
                if chunks[i] == '':
                    continue

                if i % 2 == 0:
                    new_nodes.append(TextNode(chunks[i], text_type_text))
                else:
                    new_nodes.append(TextNode(chunks[i], text_type))

    return new_nodes



#########################
# BOOT.DEV SOLUTION
########################

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for old_node in old_nodes:
#         if old_node.text_type != text_type_text:
#             new_nodes.append(old_node)
#             continue
#         split_nodes = []
#         sections = old_node.text.split(delimiter)
#         # print(f"TEXT: {old_node.text}")
#         # print(f"SECTIONS: {sections}")
#         if len(sections) % 2 == 0:
#             raise ValueError("Invalid markdown, formatted section not closed")
#         for i in range(len(sections)):
#             if sections[i] == "":
#                 continue
#             if i % 2 == 0:
#                 split_nodes.append(TextNode(sections[i], text_type_text))
#             else:
#                 split_nodes.append(TextNode(sections[i], text_type))
#         new_nodes.extend(split_nodes)
#         # print(f"SPLIT NODES: {split_nodes}")
#         # print(f"NEW NODES: {new_nodes}")
#     return new_nodes


# NEW NODES: [TextNode(bold, bold, None), TextNode( and , text, None), TextNode(italic, italic, None)]
# NEW NODES: [TextNode(, text, None), TextNode(bold, bold, None), TextNode( and , text, None), TextNode(italic, italic, None), TextNode(, text, None)]

node = TextNode("This is text with a `code block` word", text_type_text)
node2 = TextNode("This is text with a **bold**", text_type_text)
node3 = TextNode("This is text with an *italic* word", text_type_text)
node4 = TextNode("This is text with a `code block` word", text_type_text)
# code_nodes = split_nodes_delimiter([node], "`", text_type_code)
# bold_nodes = split_nodes_delimiter([node2], "**", text_type_bold)

# print(f"Code Nodes: {code_nodes}")
# print(f"Bold node: {bold_nodes}")
# for node in new_nodes:
#     print(node)