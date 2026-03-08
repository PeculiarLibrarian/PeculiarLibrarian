# Installation: pip install fastmcp pyshacl rdflib
from fastmcp import FastMCP
from pyshacl import validate
import rdflib
import os

# Initialize the Embassy Receptionist
mcp = FastMCP("PADI_Embassy_Authority")

# Path to your SHACL shapes
SHACL_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "shapes", "handshake.ttl")

@mcp.tool()
def validate_agent_handshake(agent_id: str, credential: str, protocol_version: str = "2.0") -> str:
    """
    Validates a visiting agent's credentials against the PADI v2.0 SHACL Authority.
    """
    # Create the RDF Data Graph
    g = rdflib.Graph()
    ns = rdflib.Namespace("https://padi-standard.org/ns/authority#")
    agent_uri = rdflib.URIRef(f"https://padi-standard.org/agents/{agent_id}")
    
    g.add((agent_uri, rdflib.RDF.type, ns.Agent))
    g.add((agent_uri, ns.hasCredential, rdflib.Literal(credential)))
    g.add((agent_uri, ns.protocolVersion, rdflib.Literal(protocol_version)))

    # Run the SHACL validation bridge
    conforms, results_graph, results_text = validate(
        data_graph=g,
        shacl_graph=SHACL_PATH,
        inference='rdfs'
    )

    if conforms:
        return f"✅ [ACCESS GRANTED]: Agent '{agent_id}' validated via PADI v2.0 SHACL."
    else:
        return f"❌ [ACCESS DENIED]: Architectural Non-Compliance.\n{results_text}"

if __name__ == "__main__":
    mcp.run()
