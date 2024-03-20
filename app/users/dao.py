from app.dao.base import DAO
from app.users.models import Users

class UsersDAO(DAO):
    model = Users
