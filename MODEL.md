graph TD
    subgraph "The Baobab (Architectural Core)"
        A[B.S. Information Science Roots] --> B(PADI Technical Standard v1.1)
        B --> C{Technical Sovereignty}
        C --> D[Zenodo DOI: 10.5281/zenodo.18894084]
        C --> E[MIT License: Copyright Gitandu]
    end

    subgraph "The Nairobi Bureau (Reasoning Layer)"
        D --> F[PADI Validator v2.0]
        E --> F
        G[padi.shacl Shapes] --> F
        H[padi.ttl Taxonomy] --> F
    end

    subgraph "The Nano (Execution Layer)"
        F --> I[AI Worker / Junior Engineer]
        I --> J[Vibe Coding Implementation]
        J --> K[Validated Legal Tech Output]
    end

    subgraph "The Protocol (Control Loop)"
        L[AGENTS.md] --> I
        I -- "Perceive-Reason" --> F
        F -- "Validated" --> K
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#00f,stroke:#fff,color:#fff
    style F fill:#00ff00,stroke:#333,stroke-width:4px
    style I fill:#fff2cc,stroke:#d6b656
