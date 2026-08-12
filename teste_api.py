from routeros_api import RouterOsApiPool

pool = RouterOsApiPool(
    host="192.168.0.1",
    username="admin",
    password="",
    port=8728,
    plaintext_login=True
)

api = pool.get_api()

print(api.get_resource("/system/resource").get())

pool.disconnect()