from nicegui import ui

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

MERMAID_FLOWCHART="""
flowchart TB
    A-->B
    B-->C
    C-->D
    C-->D
"""

toggle_mermaid_diagram = ui.toggle({MERMAID_OIDC:'C4 Oidc', MERMAID_FLOWCHART:'Flowchart '}, value=MERMAID_OIDC)

text_mermaid = ui.codemirror(language='Python'
                             ).classes('h-80'
                           ).bind_value_from(toggle_mermaid_diagram, "value")



ui.mermaid(''
           ).bind_content_from(text_mermaid, "value"
                               ).classes("size-full")

ui.run()
