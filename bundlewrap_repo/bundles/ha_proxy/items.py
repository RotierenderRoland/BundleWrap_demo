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
    "haproxy": {
        "installed": True,  # default
        "needs": ["action:upgrade packages"],
    },
}

files = {
    "/etc/haproxy/haproxy.cfg": {
        "mode": "0644",
        "owner": "root",
        "group": "root",
        "content_type": "jinja2",
        "encoding": "utf-8",
        "source": "proxy.conf.j2",
        "needs": ["pkg_apt:haproxy"],
        "triggers": ["svc_systemd:haproxy.service"],
    },
}


# Restarts the haproxy.service
svc_systemd = {
    "haproxy.service": {
        "enabled": True,  # default
        "running": True,  # default
        "triggered": True
    },
}