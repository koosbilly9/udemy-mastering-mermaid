from nicegui import ui
from nicegui.events import GenericEventArguments

MERMAID_OIDC = """
C4Context
    title OIDC Enterprise Authentication (Context View)
    
    Person(user, "Employee", "A user attempting to access an enterprise application.")
    
    Enterprise_Boundary(enterprise, "Enterprise Systems") {
        System(client_app, "Enterprise Application", "An internal web application (e.g., HR Portal, CRM) that requires user authentication.")
        System(idp, "Identity Provider (IdP)", "The enterprise's central identity provider (e.g., Okta, Azure AD, Keycloak) that stores user identities.")
    }
    
    Rel(user, client_app, "1. Uses")
    Rel(client_app, idp, "2. Authenticates users via OIDC")
"""

MERMAID_FLOWCHART = """
--- 
Fowchart or graph
 - TD, LR ,DT ,RL eg flochart TD
 
all text support markdown and html tags
 

Nodes like A,B
 - case sesitive A, a is 2 nodes
 - Add description A[Start] a[Exit to Start], add emoji , add markdown `` 
 -- shape [], ([]), [//], [()] = database
Edges Like Arrow -->
 - 3 chars
 - --- solid line
 - --> arrow
 - <-> , --o, o--o, -.-.>, ==>, -.-, --Text here -->, -->|text here|
 - ~~~ invisible line
---
flowchart 
    A(["**Start** 🛫"]) 
    a[Exit to Start];b[continue to new start]
    
    A-."(1-r)<sup>P</sup>".-> B & E & F 
    A ~~~ G["Secret Agent 1 ㊙ 🕵"]
    G ~~~~~|"look under the ⛰"| H["Secret Agent2 ㊙ 🕵"]
    A --> P1["Police lev1 👮"]
    A -..-> P2["Police lev2 🚔"]
    A -....-> P4["Police lev4 🚨"]
    F["$(1-R)^P$"]
    B-->C["**FV**: Future Val PVx(1-R)<sup>P</sup>"]
    C-.->D{stop or go}
    D -.?.-> a & b
    a[Stop ↩
        loop back to the start 🛫] --> A
    b[/"Go ⤵"/] --> A1
    
    A1 --text here--> B1["1:Alternative() function call"]
    B1 ==> C1
    B1 <-->|One Way?| C1
    C1 o--o D1
    
"""

MERMAID_SUB_GRAPH = """
---
Subgraph (flowchart)

must have "end"

---
graph LR
    subgraph one[Single]
    A1
    click A1 call emitEvent("node_clicked", "stop clicking me!!") "Tooltip"
    
    
    end
    
    subgraph Multi
        subgraph two[Double inverse]
        direction RL
        B1[(oracle)]-->B2
        click B1 "https://www.github.com" "tooltip" _blank
        
        end
        
        subgraph three[Triple]
        direction TB
        C1 --> C2 & C3
        
        end
    end
    
    one-->Multi
    two-->three
"""

MERMAID_FLOWCHART_LINE_STYLE = """
%%{
    init:{
        'workflow':{
            'curve': 'step'
        }
    }
}%%
flowchart TB
    A([Start])-->B[/Input x/]
    B --> C{"x>5?"}
    C -..->|yes|D([stop])
    C -->|No|F[/print x/]
    F-->G[x =x + 1]
    G:::colorC -->C
    
    linkStyle 1,3 stroke-width:6px, stroke:#00ff00
    linkStyle 4 stroke-width:6px, stroke:#ff0000
    
    style B color:#ffffff, font-size:18pt, fill:#00aaff
    
    classDef default font-size:15pt, stroke-widht:3-x
    
    classDef colorC color:#ff00fF
    
    class A,D colorC 
"""


def handle_mermaid_click(e: GenericEventArguments):
    """
    This Python function is called from JavaScript via the emitEvent.
    The event object `e` contains the arguments passed from JavaScript.
    """
    node_id = e.args
    ui.notify(f"You clicked node: {node_id}")


# --- Register the event handler ---
# The event name 'node_clicked' must match the one used in emitEvent()
ui.on('node_clicked', handle_mermaid_click)

with ui.row():
    toggle_mermaid_diagram = ui.toggle({MERMAID_FLOWCHART_LINE_STYLE: "Line style",
                                        MERMAID_OIDC: 'C4 Oidc', MERMAID_FLOWCHART: 'Flowchart',
                                        MERMAID_SUB_GRAPH: 'Sub graph'},
                                       value=MERMAID_FLOWCHART_LINE_STYLE)

    text_mermaid = ui.codemirror(language='Python'
                                 ).classes('h-80'
                                           ).bind_value_from(toggle_mermaid_diagram, "value")

    ui.mermaid('', config={'securityLevel': 'loose'}
               ).bind_content_from(text_mermaid, "value"
                                   ).classes("size-200")

ui.run()
