import re
from playwright.sync_api import Page, expect

def test_agregar_productos_y_validar_en_home(page: Page):
    # 1. Navegar directamente al catálogo
    page.goto("https://sauce-demo.myshopify.com/collections/all")
    
    #   Agregar producto 1
    page.get_by_role("link", name="Black heels").first.click()
    page.get_by_role("button", name="Add to Cart").click()
    
    # Esperamos que el contador suba a 1
    cart_link = page.get_by_role("link", name=re.compile(r"My Cart", re.IGNORECASE)).first
    expect(cart_link).to_contain_text("1", timeout=10000)
    
    # Agregar producto 2
    page.get_by_role("link", name="Catalog").first.click()
    page.get_by_role("link", name="Bronze sandals").first.click()
    page.get_by_role("button", name="Add to Cart").click()
    
    # Esperamos que el contador suba a 2
    expect(cart_link).to_contain_text("2", timeout=10000)

    
    # 2. Ir al Home y ESPERAR 
    page.locator("#main-menu").get_by_role("link", name="Home").first.click()
    page.wait_for_load_state("networkidle") # Asegura que los scripts del Home carguen
    expect(page).to_have_url("https://sauce-demo.myshopify.com/")

    # 3. Forzar el clic en el carrito desde el Home
    
    final_cart_icon = page.get_by_role("link", name=re.compile(r"My Cart", re.IGNORECASE)).first
    final_cart_icon.wait_for(state="visible")
    final_cart_icon.click()

    # Validamos que el Drawer aparezca (buscando el texto que solo sale cuando se abre)
    expect(page.get_by_text("My Cart (2)").first).to_be_visible(timeout=10000)
    
    print("Prueba exitosa: Navegó al Home y desplegó el Drawer con 2 productos.")

    #python -m pytest tests/cartPage.py --headed --slowmo 1000
    
    #python -m pytest tests/cartPage.py --headed --slowmo 500 --html=reporte_frontend_treda.html --self-contained-html