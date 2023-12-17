def parse_pipeline_name(name: str) -> str:
    name = name.split('.')[0]
    name = name.replace('_', ' ')
    return name
