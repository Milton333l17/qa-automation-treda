import re
from playwright.sync_api import Page, expect

def test_login_fallido_shopify(page: Page) -> None:
    # 1. Navegar al sitio
    page.goto("https://sauce-demo.myshopify.com/")
    
    # 2. Entrar a la sección de Login 
    page.get_by_role("link", name="Log In").click()
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("pepito.pere@hotmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("1234567")
    
    # 3. ACCIÓN: Hacer clic en el botón de Sign In
    page.get_by_role("button", name="Sign In").click()

    # 4. VALIDACIÓN (Aserción):
    # En Shopify, los errores suelen aparecer en un contenedor con clase 'errors'
    error_message = page.get_by_text("Incorrect email or password")
    
    # Verificamos que sea visible
    expect(error_message).to_be_visible(timeout=10000)
    
    print("\nPrueba de Front OK: El sistema detectó correctamente las credenciales falsas.")