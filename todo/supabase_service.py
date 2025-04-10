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
    return r.json()

def add_task(title):
    url = f"{settings.SUPABASE_URL}/rest/v1/{settings.SUPABASE_TABLE_NAME}"
    payload = {"title": title, "completed": False}
    r = httpx.post(url, headers=HEADERS, json=payload)
    return r.json()

def delete_task(task_id):
    url = f"{settings.SUPABASE_URL}/rest/v1/{settings.SUPABASE_TABLE_NAME}?id=eq.{task_id}"
    r = httpx.delete(url, headers=HEADERS)
    return r.json()

def toggle_complete(task_id, status):
    url = f"{settings.SUPABASE_URL}/rest/v1/{settings.SUPABASE_TABLE_NAME}?id=eq.{task_id}"
    r = httpx.patch(url, headers=HEADERS, json={"completed": status})
    return r.json()
