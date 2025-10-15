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

MERMAID_CLASS_DIAGRAM="""
---
+ String Owner ( + = Public/ -:Private / #:Protected /~:only access by self and packages that inherit it
---
classDiagram
    class BankAccount {
        -String owner
        -BigDecimal balance
        +withdrawal() bool
        +deposit() int
        
        method_abstact_1()*
        method_static_1() String$
    
    }
    class Person
        Person: -String name
        Person: -Int age
        Person: #List~string~ siblings
        Person: +walk( Int distance)
        Person: +talk() List~string~
     
        
        BankAccount--Person
"""

MERMAID_CLASS_DIAGRAM_2="""
---
title: Animal Relationship
---
classDiagram
    %% directions LR/TB(default)/RL/BT
    %% Cardinality /Multiplicity 1:1, 1:many, many:1 done before link ex "0" o-- "1"
    direction TB
    
    Animal <|-- Mammal : Inheritance
    Animal <|-- Reptile : Inheritance
    
    Mammal "0" o-- "*" Dog : Aggregation
    Mammal "1" *-- "*" Dolphin : Composition
    
    Reptile "1" *-- "0-N" Platypus : Composition
    
    class Animal{
        - age: int
        + makeSound(): void
    }
    
    class Mammal {
        <<Abstract>>
        # furColor: String
        - giveBirth(): void
    }
    
    class Reptile {
        << Interface>>
        # scaleType: string
        + layEggs(): void
    }
    
    class Dog {
        << Good Boy>>
        # breed: string
        + bark(): void
    }


    class Dolphin
        <<wtf>> Dolphin
        Dolphin: + swim() void


namespace WeirdFamily {   
    class Platypus {
        # poisonous: boolean
        + swim() void
        
    }
       
}

link Platypus "birds.html" "goto birds detail"

click Animal call emitEvent("callback_animal", "Animal")
click Dog call emitEvent("callback_dog", "Good Boy")



"""

# ---
# State Diagram machine state diagram
# Models a state a system can be in and what event tiggers transistion between states.
# Components
# States: boxes/circles = distinct condition th system can be in
#     Initial State = circle
#     Final State = circle with dot inside
# Activities: operations a system perform while in a particular state
#
# Events: occurrences that trigger transistion
#
# Transistions: arrows show move from one state to next TRIGGERED by events
# Actions: operations performed when transistion occur
#
# ---
MERMAID_STATE_DIAGRAM="""
---
title: Car Design states
---
stateDiagram-v2
    Design: Label Design
    Produce: Plant 99
    direction LR
    [*]-->Design
    Design --> Produce
    Produce --> Deliver : Do not F Up
    Deliver --> [*]
    
    note right of Design
        blajvk
        blah blah
    end note
    
    note left of Deliver: 7 Days
"""

MERMAID_STATE_DIAGRAM_COMPOSITE = """
stateDiagram-v2
    [*] --> state1
    state state1 {
        [*] --> state2
        state state2 {
            [*] --> state3
            state3 --> [*]
        }
        state2 --> [*]
    }
    state1 --> [*]
    
    state state3{
     state22
     state23
     state24
     
     state22 --> [*]
     state23 --> [*]
     state24 --> [*]
    }
    
    direction LR
"""

MERMAID_STATE_DIAGRAM_CHOICE = """
stateDiagram-v2
    state special_primer <<choice>>
    state primer_entrance <<fork>>
    state join_color_booth <<join>>
    
    %% define css class
    classDef body_in_white fill:white
    classDef primed font-style:italic
    classDef no_primer fill:#F00, color:white
    
    %% Apply css list nodes space class
    class rk, Yes, No body_in_white
    class hangonparts, Yes rk_primer primed
    class  magic_juice, Yes no_primer
    
    
    [*]--> rk
    rk --> primer_entrance
    primer_entrance --> hangonparts
    primer_entrance --> rk_primer
    
    hangonparts --> join_color_booth
    rk_primer --> join_color_booth
    
    join_color_booth --> spray_booth
    
    
    
    state rk_primer {
        special_primer --> Yes: sowu = 204
        special_primer --> No : sowu != 204
        Yes --> magic_juice
        magic_juice -->[*]
        No --> [*]
    }
    
    direction LR
"""




def handle_mermaid_click(e: GenericEventArguments):
    """
    This Python function is called from JavaScript via the emitEvent.
    The event object `e` contains the arguments passed from JavaScript.
    """
    node_id = e.args
    ui.notify(f"You clicked node: {node_id}")

def handle_animal_click(e: GenericEventArguments):
    ui.notify(f"animal clicked")

def handle_dog_click(e: GenericEventArguments):
    ui.notify(f"dog clicked {e.args}")


# --- Register the event handler ---
# The event name 'node_clicked' must match the one used in emitEvent()
ui.on('node_clicked', handle_mermaid_click)
ui.on('callback_animal', handle_animal_click)
ui.on('callback_dog', handle_dog_click)

with ui.row():
    toggle_mermaid_diagram = ui.toggle({
        MERMAID_CLASS_DIAGRAM:"Class diagram",
        MERMAID_CLASS_DIAGRAM_2: "Class diagram with callback" ,
        MERMAID_SEQUENCE_DIAGRAM_3: "Seq OnlineShop",
        MERMAID_SEQUENCE_DIAGRAM_2: "Seq DB",
        MERMAID_SEQUENCE_DIAGRAM: "Seq Diagram",
        MERMAID_FLOWCHART_LINE_STYLE: "Line style",
        MERMAID_OIDC: 'C4 Oidc', MERMAID_FLOWCHART: 'Flowchart',
        MERMAID_SUB_GRAPH: 'Sub graph',
        MERMAID_STATE_DIAGRAM: 'State diagram',
        MERMAID_STATE_DIAGRAM_COMPOSITE: 'State diagram composite',
        MERMAID_STATE_DIAGRAM_CHOICE: 'State diagram choice',},
        value=MERMAID_STATE_DIAGRAM_CHOICE)

    text_mermaid = ui.codemirror(language='Python'
                                 ).classes('h-80'
                                           ).bind_value_from(toggle_mermaid_diagram, "value")

    ui.mermaid('', config={'securityLevel': 'loose'}
               ).bind_content_from(text_mermaid, "value"
                                   ).classes("size-200")

ui.run()
