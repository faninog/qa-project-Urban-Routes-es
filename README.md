# **Pruebas automatizadas para comprobar la funcionalidad de Urban Routes** 🔍

Este proyecto contiene la automatización de pruebas para solicitar un taxi en la aplicación ***Urban Routes*** por medio de python, apoyado de las librerías pytest y selenium. Este código se creó por medio de la aplicación ***pycharm***.

---

## **Objetivo.**

El objetivo principal es comprobar por medio de la automatización en python, los casos de prueba para todos los pasos que debe seguir el usuario para poder pedir un taxi e identificar que los **botones**, **campos de texto**, **código de tarjeta**, **botón inteligente** y las **esperas** para cambiar de ventanas, funcionen adecuadamente.

---

## **Condiciones requeridas**🧭:
- Es necesario instalar las librerías de ***pytest***, y ***selenium Webdriver*** para así poder correr las pruebas.
- Se debe actualizar la URL del servidor en el archivo ***data.py*** en la constante ***urban_routes_url***.


## **Lista de archivos requeridos**📖:

-  **data.py** (Este se encuentra dentro de la carpeta **data**. Este archivo contiene todas las constantes para poder trabajar con el servidor de Urban Routes y las constantes para llenar los espacios requeridos para asignar un taxi). 
-  **retrieve_code.py** (Este se encuentra dentro de la carpeta **utils**. Este archivo contiene el código necesario para poder obtener el código de mensaje de texto posterior a ingresar el número de teléfono válido).
-  **urban_routes_page.py** (Este se encuentra en la carpeta **pages**. Este archivo contiene todos los localizadores y métodos necesarios para poder correr todos los casos de prueba).
-  **test_urban_routes.py** (Este se encuentra en la carpeta **tests**). Este archivo contiene todas las pruebas para interactuar con el servidor de urban routes.

- **README.md**

## **Casos de prueba**.🧐

|№	| Nombre de la prueba	|Descripción:|
|---|-------------|---|
1	|test_1_set_route|	Configuración de las direcciones desde (from), y hasta (to).
2	|test_2_select_comfort_tariff|	Es la encargada de seleccionar la tarifa Comfort.
3	|test_3_add_phone_number|	Es la encargada de Rellenar el número de teléfono, e incluir el código por mensaje de texto.
4	|test_4_add_payment_method|	Es la encargada de verificar que se agregue un método de pago.
5	|Stest_5_add_driver_message|	Es la encargada de verificar que se pueda incluir un mensaje para el conductor asignado.
6	|test_6_add_blanket_tissues|	Es el encargado de verificar que se puedan solicitar manta y pañuelos.
7|	test_7_add_two_icecream|	Es la encargada de verificar que el usuario pueda pedir dos helados.
8|	test_8_modal_look_taxi|	Es el encargado de verificar que al seguir todos los pasos para solicitar un taxi, el botón inteligente (smart_button) se active y pueda iniciar la búsqueda de un conductor.
9|	test_9_wait_info_driver_modal|	Es el encargado que, después de un tiempo de espera para la asignación del conductor, pueda salir los datos  y el tiempo de llegada del mismo.


## **Ejecución de pruebas**❌✅:

- Utilice el archivo ***test_urban_routes.py*** para ejecutar todas las pruebas. Éstas están enumeradas del 1 al 9 en orden ascendente "test_n_": 


    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

- Todas las pruebas tienen cada una las comprobaciones necesarias para verificar que los campos y su interacción con el usuario sea la adecuada.
