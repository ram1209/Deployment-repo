#from resources.user import UserRegister
from werkzeug.security import safe_str_cmp
from models.user import UserModel

#users=[User(1,'bob','asdf')]



#username_mapping={u.username:u for u in users}
#userid_mapping={u.id:u for u in users }

def authenticate(username,password):
    print("user  is ", username)
    user=UserModel.find_by_username(username)
    #print("user  is ",user)
    #user=username_mapping.get(username,None)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id=payload['identity']
    #return userid_mapping.get(user_id,None)
    return UserModel.find_by_id(user_id)
def test():
    print("testing")
