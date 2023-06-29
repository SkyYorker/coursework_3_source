from flask import current_app

import calendar
import datetime


from project.services.users_service import UsersService
import jwt


class AuthService:
    def __init__(self, dao: UsersService) -> None:
        self.user_service = dao


    
    def generate_token(self, email):
        user = self.user_service.get_by_email(email)
        if not user:
            raise Exception("Не найден пользователь")


        
        data = {
            'email': user.email,
            # 'username': user["name"],
            
        }


        min15 = datetime.datetime.utcnow() + datetime.timedelta(current_app.config['TOKEN_EXPIRE_MINUTES'])
        data['exp'] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, current_app.config['SECRET_KEY'])

        day130 = datetime.datetime.utcnow() + datetime.timedelta(current_app.config['TOKEN_EXPIRE_DAYS'])
        data['exp'] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, current_app.config['SECRET_KEY'])
        
        return {"access_token":access_token, "refresh_token":refresh_token}

    def refresh_token(self,refresh_token):
        data = jwt.decode(refresh_token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        email = data.get("email")
        user = self.user_service.get_by_email(email)

        if not user:
            raise Exception('плохой токен')

        return self.generate_token(email)  