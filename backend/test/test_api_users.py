import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:
    # Coneccion CURL
    request_context = playwright.request.new_context(
        base_url="https://reqres.in",
        extra_http_headers={
            "x-api-key": "pub_4a14087498039432124b2ece2732ec714ddefdc47867b72156f261737527e562",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )
    yield request_context
    request_context.dispose()

# --- GET: Consultar usuario ---
def test_get_specific_user(api_context: APIRequestContext):
    response = api_context.get(
        "/api/users/2", 
        params={"project_id": "8567"}
    )
    
    if response.status != 200:
        print(f"\nDETALLE DEL ERROR: {response.text()}")
        
    assert response.status == 200

# --- POST: Crear usuario ---
def test_create_new_user(api_context: APIRequestContext):
    user_payload = {
        "name": "Prueba Milton",
        "job": "QA Automation"
    }
    
    response = api_context.post(
        "/api/users", 
        data=user_payload,
        params={"project_id": "8567"}
    )
    
    assert response.status == 201