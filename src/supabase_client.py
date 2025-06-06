from supabase import create_client, Client

url: str = "https://xjgxgdghvdsszygtftms.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhqZ3hnZGdodmRzc3p5Z3RmdG1zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDkxNjk0MjMsImV4cCI6MjA2NDc0NTQyM30.mXR-2OSCwXHqxqOiRT3iR9jRwDpo2ozKwAQaTWsej78"
supabase: Client = create_client(url, key)
