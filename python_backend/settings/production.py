
ALLOWED_HOSTS = [
    #"http://127.0.0.1"
    'localhost', '127.0.0.1', 'safehomecam.com','originweb-backend-django'
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'https://safehomecam.com',
    'http://192.168.27.123:8081',
    
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