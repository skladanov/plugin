# src/helloworld_plugin/processor.py

class HelloWorldProcessor:
    """
    Обработчик кастомного шага 'hello_world'.
    Вызывается ядром TestY во время прогона автотеста.
    """
    
    def process(self, context, params):
        """
        Основная точка входа исполнения.
        
        :param context: Контекст выполнения от ядра TMS (может содержать ID задачи).
        :param params: Словарь параметров из формы шага в интерфейсе TestY.
                       Например, если вы добавили поле "name" в настройках шага,
                       оно придет здесь как params['name'].
        :return: dict Результат согласно спецификации API шагов TestY.
        """
        
        # Получаем параметр name, если пользователь заполнил его в шаге
        name = params.get('name', 'Guest')
        
        message = f"Hello, {name}! This is your custom plugin."
        
        return {
            "status": "passed",
            "output": message,
            "attachments": []
        }