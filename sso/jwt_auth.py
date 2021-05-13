import jwt


class JwtUser:
    @staticmethod
    def get_jwt_user(auth_header: str, secret_key: str):
        auth_token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(auth_token, secret_key)
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            raise ValueError('Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            raise ValueError('Invalid token. Please log in again.')
