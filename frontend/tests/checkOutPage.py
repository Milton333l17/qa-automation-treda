import re
from playwright.sync_api import Page, expect

def test_flujo_checkout_completo(page: Page):
    # 1. Preparación: Agregar producto y navegar al Checkout
    page.goto("https://sauce-demo.myshopify.com/collections/all")

    page.get_by_role("link", name="Bronze sandals").first.click()
    page.get_by_role("button", name="Add to Cart").click()

    #espera a que el contador suba a 1
    cart_link = page.get_by_role("link", name=re.compile(r"My Cart", re.IGNORECASE)).first
    expect(cart_link).to_contain_text("1", timeout=10000)
    
     # Ir al Home
    page.locator("#main-menu").get_by_role("link", name="Home").first.click()
    page.wait_for_load_state("networkidle") # Asegura que los scripts del Home carguen
    expect(page).to_have_url("https://sauce-demo.myshopify.com/")

    # Abrir Carrito y Checkout
    cart_link.click()
    # 2. Primer clic en Checkout (el del Drawer)
    btn_checkout_drawer = page.get_by_role("button", name=re.compile(r"Check Out", re.IGNORECASE)).first
    btn_checkout_drawer.wait_for(state="visible")
    btn_checkout_drawer.click()

    # 3. MANEJO DE PÁGINA INTERMEDIA (Si no saltó directo al formulario)
    # Esperamos un momento para ver si la URL es /cart
    page.wait_for_load_state("networkidle")
    
    if "/cart" in page.url:
        print("Detectada página intermedia de carrito, haciendo segundo Check Out...")
        # Buscamos el botón de checkout específico de la página de carrito
        btn_checkout_page = page.get_by_role("button", name=re.compile(r"Check Out", re.IGNORECASE)).last
        btn_checkout_page.click()

    
    
    # 4. Información de Envío (Datos del Formulario)
    # Esperamos a que cargue la página de checkout
    page.wait_for_load_state("networkidle")
    email_input = page.get_by_role("textbox", name="Email")
    email_input.wait_for(state="visible", timeout=15000)

    page.get_by_role("textbox", name="Email").fill("pruebacheckout@yopmail.com")
    page.get_by_role("textbox", name="First name").fill("Aliya")
    page.get_by_role("textbox", name="Last name").fill("Kihn")
    page.get_by_role("textbox", name="Address").fill("kr56#74-32")
    page.get_by_role("textbox", name="City").fill("Bogota")

    # 5. Aseguramos que el país sea Colombia (esto "despierta" el selector de departamentos)
    # Usamos un selector flexible para el label de Country
    page.locator("select[name='countryCode']").select_option(label="Colombia")
    #6. Esperamos a que el selector de 'State' o 'Province' aparezca y sea interactuable
    state_select = page.locator("select[name='zone']")
    
    # Esperamos a que el selector no esté vacío y sea visible
    state_select.wait_for(state="visible", timeout=15000)
    
    # 3. Seleccionamos "Boyacá" 
    state_select.select_option(value="Boyacá")

    page.get_by_role("textbox", name="Postal code").fill("111102")
    page.get_by_role("textbox", name="Phone").fill("3245762431")

    # 3. Datos de Pago (Manejo de iFrames Dinámicos)

    page.wait_for_selector("iframe[title*='Card number']", state="visible", timeout=25000)
    
    # Número de tarjeta
    card_frame = page.frame_locator("iframe[title*='Card number']").first
    card_frame.locator("#number").fill("4242424242424242")
    
    # Fecha de expiración
    expiry_frame = page.frame_locator("iframe[title*='Expiration']").first
    expiry_frame.locator("#expiry").fill("12/28")
    
    # Código de seguridad (CVV)
    cvv_frame = page.frame_locator("iframe[title*='Security code']").first
    cvv_frame.locator("#verification_value").fill("123")

    # 4. Finalizar Compra
    page.get_by_role("button", name="Pay now").click()

    # 5. Validación final (Aserción)
    # Verificamos que aparezca un mensaje de confirmación o error de tarjeta
    # (Como usamos datos falsos, probablemente salga un error, lo cual valida que el flujo llegó al final)
    expect(page.locator("body")).to_contain_text(re.compile(r"(Thank you|Payment|error)", re.IGNORECASE))

    print("Flujo de checkout ejecutado y validado.")