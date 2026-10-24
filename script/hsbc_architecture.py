from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS
from diagrams.aws.database import Aurora
from diagrams.aws.security import IAM
from diagrams.onprem.client import User

with Diagram("HSBC Switzerland - Databricks Architecture", show=False, direction="TB"):
    
    with Cluster("Swiss Operational Hubs"):
        geneva = User("Geneva HQ\n(Private Banking)")
        zurich = User("Zurich Office\n(Corporate Banking)")

    with Cluster("Cloud Infrastructure & Databricks Lakehouse"):
        
        with Cluster("Governance & Security Layer"):
            unity = IAM("Unity Catalog\n(FINMA Compliance / RBAC)")
            
        with Cluster("Compute Layer"):
            collab = ECS("Shared Databricks Workspaces\n(Cross-Office Collaboration)")
            
        with Cluster("Storage Layer"):
            delta = Aurora("Delta Lake\n(Unified Client & Market Data)")

    # Connections & Data Flow
    geneva >> Edge(label="Encrypted TLS", color="blue") >> collab
    zurich >> Edge(label="Encrypted TLS", color="blue") >> collab
    
    collab >> Edge(label="Read / Write", color="darkgreen") >> delta
    unity >> Edge(label="Governance & Masking", color="red") >> collab
    unity >> Edge(label="Access Control", color="red") >> delta
