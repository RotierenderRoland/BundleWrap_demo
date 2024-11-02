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
    # Installation of Apache2 Webserver
    "apache2": {
        "pkg_apt": {
            "name": "apache2",
            "state": "present",
            "needs": ["action:upgrade packages"],
        },
    },
}