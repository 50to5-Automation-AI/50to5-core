import json
import logging
from initialization_agent import InitializationAgent
from quality_control_agent import QualityControlAgent

def load_config(config_file: str) -> Dict[str, Any]:
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def create_initialization_agent(config: Dict[str, Any]) -> InitializationAgent:
    logger = logging.getLogger(config["logger_name"])
    logging.basicConfig(level=logging.INFO)
    
    return InitializationAgent(
        name=config["name"],
        system_message=config["system_message"],
        redis_config=config["redis_config"],
        logger=logger,
        db_config=config["db_config"]
    )

def create_quality_control_agent(config: Dict[str, Any]) -> QualityControlAgent:
    return QualityControlAgent(
        name=config["name"],
        description=config["description"],
        db_config=config["db_config"]
    )

def main():
    config = load_config('config.json')

    init_agent_config = config["initialization_agent"]
    qc_agent_config = config["quality_control_agent"]

    initialization_agent = create_initialization_agent(init_agent_config)
    quality_control_agent = create_quality_control_agent(qc_agent_config)

    initialization_agent.initialize_environment()
    quality_control_agent.monitor_state()

if __name__ == "__main__":
    main()
