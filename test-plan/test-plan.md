# Test Plan - QA Automation Challenge

## 1. Objective
El objetivo de este plan de pruebas es validar la calidad y la funcionalidad de la aplicación web SauceDemo y la API ReqRes mediante la identificación de defectos, la garantía del correcto funcionamiento de los flujos de usuario críticos (como el inicio de sesión, la selección de productos y el proceso de compra) y la verificación de la fiabilidad de los puntos finales de la API.
## 2. Scope
### In Scope

Las siguientes funcionalidades se probarán como parte de este plan de pruebas:

**Interfaz de usuario (SauceDemo):**
- Funcionalidad de inicio de sesión de usuario
- Listado y selección de productos
- Operaciones del carrito de compra (agregar/eliminar productos)
- Proceso de pago

**Backend (API ReqRes):**
- Solicitudes GET (recuperación de datos de usuario)
- Solicitudes POST (creación de nuevos usuarios)
- Validación de respuesta (códigos de estado y estructura de datos)

### Out of Scope

Las siguientes áreas no están incluidas:

- Pruebas de rendimiento (pruebas de carga y estrés)
- Pruebas de seguridad (pruebas de penetración, análisis de vulnerabilidades)
- Pruebas de compatibilidad en múltiples dispositivos o navegadores
- Validación de la base de datos (integridad interna de los datos)
## 3. Test Strategy
El enfoque de pruebas combinará técnicas manuales y automatizadas para garantizar una validación integral del sistema.

Las pruebas manuales se utilizarán para diseñar y validar casos de prueba, centrándose en la experiencia del usuario, el comportamiento funcional y los casos límite.

Las pruebas automatizadas se implementarán para validar flujos de usuario críticos y la funcionalidad de la API:

- La automatización del frontend se realizará con Playwright para simular interacciones de usuario como el inicio de sesión, la selección de productos y el proceso de compra.

- Las pruebas del backend se llevarán a cabo mediante la automatización de la API para validar los endpoints, incluyendo la verificación de solicitudes y respuestas, los códigos de estado y la integridad de los datos.

El proceso de pruebas se centrará en validar los resultados esperados, identificar defectos y garantizar que las funcionalidades críticas se comporten de forma consistente en diferentes escenarios.
## 4. Test Types
Se realizarán los siguientes tipos de pruebas:

- **Functional Testing:** 

Para verificar que la aplicación se comporta según los requisitos esperados, incluyendo el inicio de sesión, la selección de productos, las operaciones del carrito y el proceso de pago.

- **UI Testing:**

Para validar que los elementos de la interfaz de usuario se muestren correctamente y que las interacciones funcionen como se espera.

- **API Testing:**  

Para verificar la corrección de los puntos finales del backend, incluyendo el manejo de solicitudes, la estructura de respuesta y los códigos de estado.

- **Negative Testing:**

Para asegurar que el sistema maneja correctamente las entradas no válidas, como credenciales de inicio de sesión incorrectas o campos obligatorios faltantes.

- **Edge Case Testing:**  

Para validar el comportamiento del sistema en condiciones inusuales o extremas, como entradas vacías, valores de datos grandes o acciones inesperadas del usuario.
