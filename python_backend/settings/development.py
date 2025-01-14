CORS_ALLOW_ALL_ORIGINS = True

CORS_ORIGIN_WHITELIST = [
    "*"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Origin_Database',  # 你要连接的数据库名称
        'USER': 'originadmin',  # 数据库用户名
        'PASSWORD': 'Origin*Admin_240926',  # 数据库密码
        'HOST': '149.28.170.19',  # 数据库主机，默认为'localhost'
        'PORT': '8600',  # 数据库端口，默认为'3306',
        'OPTIONS': {
            'init_command': "SET time_zone='+08:00'",
        },
    }
}
