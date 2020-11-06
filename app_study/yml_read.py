import yaml


def caps_yml_read():
    with open('../configs/caps.yml') as f:
        capsconfig = yaml.safe_load(f)
        caps = capsconfig['desirecaps']
        ip = capsconfig['server']['ip']
        port = capsconfig['server']['port']
        f.close()
    return (caps,ip,port)

caps_yml_read()