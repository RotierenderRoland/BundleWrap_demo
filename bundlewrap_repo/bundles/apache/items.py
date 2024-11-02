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
#Uses files/template.html.j2 as the Apache2 index.html
files = {
    "/var/www/html/index.html": {
        "mode": "0644",
        "owner": "www-data",
        "group": "www-data",
        "content_type": "jinja2",
        "encoding": "utf-8",
        "source": "template.html.j2",
        "needs": ["item:apache2"],
        "triggers": ["svc_systemd:apache2.service"]
    },
}
# Restarts the apache2.service
svc_systemd = {
    "apache2.service": {
        "enabled": True,  # default
        "running": True,  # default
        "restart": True,
    },

}