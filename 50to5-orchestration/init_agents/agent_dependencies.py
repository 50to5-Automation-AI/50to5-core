agents = {
    "InitializationAgent": {
        "description": "Initializes the environment and allocates the session UUID.",
        "dependencies": ["QualityControlAgent", "MonitoringAgent"]
    },
    "QualityControlAgent": {
        "description": "Ensures the quality control and state management of the system.",
        "dependencies": ["InitializationAgent", "MonitoringAgent"]
    },
    "MonitoringAgent": {
        "description": "Monitors task performance, logs data, and sends reports.",
        "dependencies": ["InitializationAgent", "QualityControlAgent"]
    },
    "DecisionAgent": {
        "description": "Makes high-level decisions and allocates tasks.",
        "dependencies": ["TaskGenerator", "DiscriminatorAgent"]
    },
    "TaskGenerator": {
        "description": "Generates tasks based on executive goals.",
        "dependencies": ["DiscriminatorAgent"]
    },
    "DiscriminatorAgent": {
        "description": "Critiques tasks and improves their quality.",
        "dependencies": ["TaskGenerator"]
    },
    "EngineeringAgent": {
        "description": "Handles engineering-specific tasks.",
        "dependencies": []
    },
    "MarketingAgent": {
        "description": "Handles marketing-specific tasks.",
        "dependencies": []
    }
}
