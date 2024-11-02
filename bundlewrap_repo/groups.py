groups = {
    'apache-webserver': {
        'bundles': ["apache"],
        'member_patterns': [r"webserver-\d+"],
        'os': 'linux',
    },
    'loadbalancer': {
        'bundles': ["ha_proxy"],
        'member_patterns': [r"loadbalancer-\d+"],
        'os': 'linux',
    },
}