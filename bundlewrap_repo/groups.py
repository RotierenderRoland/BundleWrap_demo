groups = {
    'apache-webserver': {
        'bundles': ["bundle1", "bundle2"],
        'member_patterns': [r"webserver-\d+"],
        'os': 'linux',
    },
    'loadbalancer': {
        'bundles': ["bundle1", "bundle2"],
        'member_patterns': [r"loadbalancer-\d+"],
        'os': 'linux',
    },
}