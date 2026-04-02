# QA Automation Challenge - Treda Solutions

##  Descripción

Este repositorio contiene la solución a la prueba técnica de QA Automation, enfocada en validar el flujo de autenticación, gestión de usuarios y proceso de compra en una aplicación web, así como la validación de servicios backend mediante pruebas automatizadas.

Se incluyen:
- Diseño de pruebas (Test Plan y Test Cases)
- Automatización de pruebas frontend
- Automatización de pruebas backend

---

##  Estructura del Proyecto
```text
qa-automation-treda/
├── backend/                
│   ├── tests/
│   │   ├── test_api_users.py  
│   └── reporte_backend_treda_final.html
├── frontend/               
│   ├── test/
│   │   ├── cartPage.py
|   |   ├──    checkOutPage.py
|   |   ├──   test_login_page.py
│   |   ├──reporte_frontend_treda.html
|   └── └──reporte_frontend_cartPage_treda.html
├── test-cases/               
│    └── test-cases.md
│     
├── test-plan/             
│    └── test-plan.md
|  
└── README.md     
```
---

##  Tecnologías Utilizadas

- Python 3.10+
- Pytest
- Playwright
- Pytest-HTML

---

##  Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/Milton333l17/qa-automation-treda.git
cd qa-automation-treda
```
## 3. Instalar dependencias
```bash
pip install pytest playwright pytest-html
playwright install chromium
```
## Ejecución de pruebas
### Frontend
```bash
python -m pytest frontend/tests/nombre.py --headed --slowmo 500 --html=reporte_frontend_treda.html --self-contained-html
```
### Backend
```bash
python -m pytest backend/tests/nombre.py --html=reporte_backend_treda.html --self-contained-html
```
## Reportes
Los reportes se generan en formato HTML y permiten visualizar:

* Resultado de ejecución
* Pruebas exitosas y fallidas
* Detalle de cada caso

## Justificación de herramientas
Se eligió este stack porque:

* Playwright permite automatizar aplicaciones modernas y manejar elementos dinámicos.
* Pytest facilita la organización de pruebas y su ejecución.
* Python permite escribir pruebas claras y fáciles de mantener.
* Pytest-HTML ayuda a generar reportes simples para evidenciar resultados.

## Observaciones
Durante la ejecución se identificaron algunos comportamientos relevantes:

### CAPTCHA en login
No fue posible automatizar completamente el login debido a la presencia de CAPTCHA en la aplicación, lo que bloquea la ejecución automática.

### Persistencia del carrito
Se observó que el carrito mantiene productos incluso al cambiar de usuario, lo que puede indicar que no hay aislamiento de sesión.

### Checkout con iFrames
Los campos de tarjeta de crédito están dentro de iFrames, por lo que fue necesario usar selectores específicos y esperas.

### API
Se utilizaron headers como x-api-key y project_id para consumir correctamente los endpoints.

## Cobertura de pruebas
Se incluyeron:
* Casos positivos (happy path)
* Casos negativos
* Edge cases
* Pruebas frontend (flujo de compra)
* Pruebas backend (GET y POST)

## Propuestas de mejora
Si tuviera más tiempo, me gustaría:

* Organizar mejor el código para hacerlo más mantenible.
* Investigar cómo automatizar el login evitando el CAPTCHA en entorno de pruebas.
* Agregar más escenarios de prueba.
* Automatizar la ejecución de pruebas al subir cambios al repositorio.

## Entregables incluidos
* Test Plan
* Test Cases
* Automatización frontend
* Automatización backend
* Reportes HTML

## Conclusión
El proyecto cubre los flujos principales del sistema mediante pruebas manuales y automatizadas, permitiendo validar el comportamiento del frontend y backend e identificar posibles mejoras.
