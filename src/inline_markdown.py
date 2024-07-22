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



# First regex functions (ch 3.4)
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    # r"!\[(.*?)\]\((.*?)\)"
    # print(matches)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    # print(matches)
    return matches


# Split images & links (ch 3.5)
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        matches = extract_markdown_images(node.text)
        print(matches)
        search_string = node.text

        for match in matches:
            match_string = f"![{match[0]}]({match[1]})"
            split_text = search_string.split(match_string)
            
            if split_text[0] != "":
                # Adds text node
                new_nodes.append(TextNode(split_text[0], text_type_text))
            # adds link node
            new_nodes.append(TextNode(match[0], text_type_image, match[1]))
            search_string = split_text[1]
        # adds last text string if it exists
        if search_string:
            new_nodes.append(TextNode(search_string, text_type_text))            

        print(f'New Nodes: {new_nodes}')
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        matches = extract_markdown_links(node.text)
        search_string = node.text

        for match in matches:
            match_string = f"[{match[0]}]({match[1]})"
            split_text = search_string.split(match_string)
            
            if split_text[0] != "":
                # Adds text node
                new_nodes.append(TextNode(split_text[0], text_type_text))
            # adds link node
            new_nodes.append(TextNode(match[0], text_type_link, match[1]))
            search_string = split_text[1]
        # adds last text string if it exists
        if search_string:
            new_nodes.append(TextNode(search_string, text_type_text))            

        print(f'New Nodes: {new_nodes}')
    return new_nodes




# matches = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]

# matches_wo_capture_groups = ['[to boot dev](https://www.boot.dev)', '[to youtube](https://www.youtube.com/@bootdotdev)']


node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    text_type_text,
)

node2 = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )

node_image = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )

# Node image answer:
[
    TextNode("This is text with an ", text_type_text),
    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
]

# LINK NODE EXAMPLE:
# [
#     TextNode("This is text with a ", text_type_text),
#     TextNode("link", text_type_link, "https://boot.dev"),
#     TextNode(" and ", text_type_text),
#     TextNode("another link", text_type_link, "https://blog.boot.dev"),
#     TextNode(" with text that follows", text_type_text),
# ]

# IMAGE NODE EXAMPLE:
[
    TextNode("This is text with an ", text_type_text),
    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
]
# [
#     TextNode(This is text with an !, text, None), 
#     TextNode(image, image, https://i.imgur.com/zjjcJKZ.png),
# ]


# new_nodes = split_nodes_link([node2])
image_nodes = split_nodes_image([node_image])
# print(new_nodes)
# [
#     TextNode("This is text with a link ", text_type_text),
#     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
#     TextNode(" and ", text_type_text),
#     TextNode(
#         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
#     ),
# ]








#########################
# BOOT.DEV SOLUTION for split nodes function
# ########################

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

# node = TextNode("This is text with a `code block` word", text_type_text)
# node2 = TextNode("This is text with a **bold**", text_type_text)
# node3 = TextNode("This is text with an *italic* word", text_type_text)
# node4 = TextNode("This is text with a `code block` word", text_type_text)
# code_nodes = split_nodes_delimiter([node], "`", text_type_code)
# bold_nodes = split_nodes_delimiter([node2], "**", text_type_bold)

# print(f"Code Nodes: {code_nodes}")
# print(f"Bold node: {bold_nodes}")
# for node in new_nodes:
#     print(node)