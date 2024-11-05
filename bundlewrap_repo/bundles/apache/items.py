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

pkg_apt = {
    "apache2": {
        "installed": True,  # default
        "needs": ["action:upgrade packages"],
    },
}
#Uses files/template.html.j2 as the Apache2 index.html
files = {
    "/var/www/html/index.html": {
        "mode": "0644",
        "owner": "www-data",
        "group": "www-data",
        "content_type": "jinja2",
        "encoding": "utf-8",
        "source": "template.html.j2",
        "needs": ["pkg_apt:apache2"],
        "triggers": ["svc_systemd:apache2.service"]
    },
}
# Starts
svc_systemd = {
    "apache2.service": {
        "enabled": True,  # default
        "running": True,  # default
        "triggered": True
    },

}