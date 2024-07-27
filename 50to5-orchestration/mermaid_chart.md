graph TD
    subgraph Initialization
        InitializationAgent["InitializationAgent"]
    end

    subgraph Quality Control
        QualityControlAgent["QualityControlAgent"]
    end

    subgraph Monitoring
        MonitoringAgent["MonitoringAgent"]
    end

    subgraph Executive
        DecisionAgent["DecisionAgent"]
        TaskGenerator["TaskGenerator"]
        DiscriminatorAgent["DiscriminatorAgent"]
    end

    subgraph Departments
        EngineeringAgent["EngineeringAgent"]
        MarketingAgent["MarketingAgent"]
    end

    InitializationAgent -->|Allocates session UUID and initializes environment| QualityControlAgent
    InitializationAgent -->|Allocates session UUID and initializes environment| MonitoringAgent

    QualityControlAgent -->|Monitors system state| InitializationAgent
    QualityControlAgent -->|Logs task data| MonitoringAgent

    MonitoringAgent -->|Sends performance reports| QualityControlAgent
    MonitoringAgent -->|Sends performance reports| InitializationAgent

    DecisionAgent -->|Allocates tasks| TaskGenerator
    DecisionAgent -->|Allocates tasks| DiscriminatorAgent

    TaskGenerator -->|Generates tasks| DecisionAgent
    TaskGenerator -->|Generates tasks| DiscriminatorAgent

    DiscriminatorAgent -->|Critiques tasks| TaskGenerator
    DiscriminatorAgent -->|Critiques tasks| DecisionAgent

    DecisionAgent -->|Sends tasks| EngineeringAgent
    DecisionAgent -->|Sends tasks| MarketingAgent
