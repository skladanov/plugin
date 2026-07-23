from testy.plugins.hooks import TestyPluginConfig, hookimpl, URLS_SENTINEL
from .views import IndexView


class HelloWorldConfig(TestyPluginConfig):
    package_name = 'helloworld_plugin'
    verbose_name = 'Demo: Hello World Page'
    description = 'Adds a simple static page to the navigation'
    version = '0.1.0'

    # Базовый путь: http://127.0.0.1/plugins/helloworld/
    plugin_base_url = 'helloworld'

    author = 'Your Name'

    # Указываем путь к нашему файлу urls.py
    urls_module = 'helloworld_plugin.urls'


@hookimpl
def config():
    return HelloWorldConfig