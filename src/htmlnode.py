class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    def __repr__(self) -> str:
        return f"HTML Node Object: tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, children=None, props=props)
        # if self.value == None:
        #     raise ValueError("Leaf nodes must have a value")

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None) -> None:
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have a tag")
        if self.children == None:
            raise ValueError("Parent node must have children")
        
        def recursive_children(children, counter=0):
            if counter == len(self.children):
                return ""
            children_string = children[counter].to_html()
            return children_string + recursive_children(children, counter + 1)
        
        children_html = recursive_children(self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"