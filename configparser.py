def to_dict(config: configparser.ConfigParser) -> Dict[str, Dict[str, str]]:
    """
    function converts a ConfigParser structure into a nested dict
    Each section name is a first level key in the the dict, and the key values of the section
    becomes the dict in the second level
    {
        'section_name': {
            'key': 'value'
        }
    }
    :param config:  the ConfigParser with the file already loaded
    :return: a nested dict
    """
    return {section_name: dict(config[section_name]) for section_name in config.sections()}

  
path_own_dir = pathlib.Path(__file__).parent.resolve()
path_conf_file = path_own_dir / 'config.ini'
assert path_conf_file.is_file()
config = configparser.ConfigParser()
config.read(path_conf_file)
to_dict(config)
