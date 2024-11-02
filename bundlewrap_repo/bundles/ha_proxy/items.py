#Update the System 
actions = {
    'update repositories': {
        'command': "apt update",
        'expected_return_code': 0,
    },
        'upgrade packages': {
        'command': "apt upgrade -y",
        'expected_return_code': 0,
        'needs': ['action:update repositories'],
    }
}

items = {
    # Installation of HA-Proxy Loadbalancer
    "haproxy": {
        "pkg_apt": {
            "name": "haproxy",
            "state": "present",
            "needs": ["action:upgrade packages"],
        },
    },
}