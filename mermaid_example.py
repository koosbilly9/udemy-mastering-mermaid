import base64
from IPython.display import display, Image
import matplotlib.pyplot as plt


def draw_mermaid(graph):
    graphbytes = graph.encode("utf8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    display(Image(url="https://mermaid.ink/img/" + base64_string))

if __name__ == '__main__':
    draw_mermaid("""
    graph LR:
        A--> B & C & D;
        B--> A & E;
    """)