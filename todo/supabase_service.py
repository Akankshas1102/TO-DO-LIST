import httpx
from django.conf import settings

HEADERS = {
    "apikey": settings.SUPABASE_API_KEY,
    "Authorization": f"Bearer {settings.SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

def get_tasks():
    url = f"{settings.SUPABASE_URL}/rest/v1/{settings.SUPABASE_TABLE_NAME}?select=*"
    r = httpx.get(url, headers=HEADERS)
    if r.status_code >= 400:
        print("Error:", r.status_code, r.text)
        return None

    try:
        return r.json()
    except Exception as e:
        print("JSON decode error:", e, "Response text:", r.text)
        return None

def add_task(title):
    url = f"{settings.SUPABASE_URL}/rest/v1/{settings.SUPABASE_TABLE_NAME}"
    payload = {"title": title, "completed": False}
    r = httpx.post(url, headers=HEADERS, json=payload)
    if r.status_code >= 400:
        print("Error:", r.status_code, r.text)
        return None

    try:
        return r.json()
    except Exception as e:
        print("JSON decode error:", e, "Response text:", r.text)
        return None

def delete_task(task_id):
    url = f"{settings.SUPABASE_URL}/rest/v1/{settings.SUPABASE_TABLE_NAME}?id=eq.{task_id}"
    r = httpx.delete(url, headers=HEADERS)
    if r.status_code >= 400:
        print("Error:", r.status_code, r.text)
        return None

    try:
        return r.json()
    except Exception as e:
        print("JSON decode error:", e, "Response text:", r.text)
        return None

def toggle_complete(task_id, status):
    url = f"{settings.SUPABASE_URL}/rest/v1/{settings.SUPABASE_TABLE_NAME}?id=eq.{task_id}"
    r = httpx.patch(url, headers=HEADERS, json={"completed": status})
    if r.status_code >= 400:
        print("Error:", r.status_code, r.text)
        return None

    try:
        return r.json()
    except Exception as e:
        print("JSON decode error:", e, "Response text:", r.text)
        return None
