class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f" {key}={value}"
        return result
    
    def __repr__(self) -> str:
        return f"HTML Node Object: tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"