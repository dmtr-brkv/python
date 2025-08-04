from smartphone import Smartphone

catalog = [Smartphone ('samsung', 'A51', '+78805553535'),
           Smartphone ('samsung', 'A52', '+78805553536'),
           Smartphone ('samsung', 'A53', '+78805553537'),
           Smartphone ('samsung', 'A54', '+78805553538'),
           Smartphone ('samsung', 'A55', '+78805553539')]

for Smartphone in catalog:
    print(f"{Smartphone.marka} - {Smartphone.model} - {Smartphone.number}")
