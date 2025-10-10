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

MERMAID_SEQUENCE_DIAGRAM = """
---
Sequence Diagram
Benefits
1) Understanding system behavior
2) Communication espcially between technical and non technical stakeholders
3) Design and Doc
4) Id issues and possible improvements
5) Testing and Validation - used to dev test / use cases
6) During sys main shows stakeholders
7) Prototyping and planning
8) Training and on boarding

-- Default
participant is default
syncronys by default
% comment
Lines
- , -- , > , >> solid arrowsyncronys
) Async communication
x end communication

---
sequenceDiagram
    Actor Manager
    participant Alice as sup1
    note right of James: Text Bob move it
    note over Alice, James: howzit <br/> Bro
    
    Manager-->>Alice: Call a meeting
    Alice ->> James: Hi James, its Alice
    James -) Alice: Hello Alice
    Alice ->> Bob: Are you there Bob
    Bob -x Alice: On my way    
    create actor caller1
    Alice -) caller1: Hi 
    caller1 ->> Alice: Hi Dear, lunch orders
    Bob -x Alice: Have to drop out
    destroy Bob
    Alice --x Bob: Bye
    Manager -->> Alice : Everyone ready?
    Alice -->> Manager: Finishing food orders now
    Manager --) Alice: Fish
    Alice ->> James: Food ?
    James -) Alice: Beef
    Alice ->> caller1: 1 fish 1 beef
    caller1 ->> Alice: done
    destroy caller1
    Alice -x caller1: thanks
    
    
    
"""

MERMAID_SEQUENCE_DIAGRAM_2 = """
sequenceDiagram
    loop Till successfull every 3 mins
        critical Establish connection to DB
            Server->>Database: Give me data
            activate Database
            Database-->>Server: here we go
            deactivate Database
            
        option Network Timeout
            Server --> Server: Log network error
        
        option Server Timeout
            Server --> Server: Server error
         
        break on crit error    
            Server --> Server: Log invalid credentials
        end
            
        end
    end
"""

MERMAID_SEQUENCE_DIAGRAM_3 = """
sequenceDiagram
    autonumber
    box rgb(255,5,5,0.7) Front end 😁
    participant User
    participant App as "Shopping App"
    end
    
    box cyan the Backend 👖
    participant Gateway as "Payment Gateway"
    participant Bank
    end
    
    User->>App: Select item and checkout
    activate App
    App ->> Gateway: initiate payment request
    activate Gateway
    
    
    
    % Alternative use +/- to activate deactivate
    Gateway->>+Bank: Process payment
    
    create actor Teller
    par Bank to Teller
        Bank--)+Teller: check balance
            
            rect rgb(0,255,0,0.7)
                alt is balance enough?    
                    Teller --)Bank: Balance ok 👍
                else balance to low
                    Teller --)Bank: Balance Nok 👎
                end
                
                opt
                   Teller --)Bank: No such account 😳
                   Teller --)Bank: Account froze 🥶
                   Teller --)Bank: Suspicious transaction 🚨     
                end
            end
    and Bank to Gateway
        rect yellow
            Bank --) Gateway: Play tune 🎶
        end
        
    end
    
    Teller--)-Bank: bye
        
    destroy Teller
    Bank--xTeller: Thanks
    
    
    
    Bank->>-Gateway: Payment approved
    
    
    Gateway->>App: Payment successful
    deactivate Gateway
    App--xUser: Order confirmation
    deactivate App
    
    
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
    toggle_mermaid_diagram = ui.toggle({
        MERMAID_SEQUENCE_DIAGRAM_3: "Seq OnlineShop",
        MERMAID_SEQUENCE_DIAGRAM_2: "Seq DB",
        MERMAID_SEQUENCE_DIAGRAM: "Seq Diagram",
        MERMAID_FLOWCHART_LINE_STYLE: "Line style",
        MERMAID_OIDC: 'C4 Oidc', MERMAID_FLOWCHART: 'Flowchart',
        MERMAID_SUB_GRAPH: 'Sub graph'},
        value=MERMAID_SEQUENCE_DIAGRAM_3)

    text_mermaid = ui.codemirror(language='Python'
                                 ).classes('h-80'
                                           ).bind_value_from(toggle_mermaid_diagram, "value")

    ui.mermaid('', config={'securityLevel': 'loose'}
               ).bind_content_from(text_mermaid, "value"
                                   ).classes("size-200")

ui.run()
