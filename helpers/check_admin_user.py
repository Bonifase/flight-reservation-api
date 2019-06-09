from flights.models.user import User

def check_admin_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user.isAdmin:    
        assert False, "You are not authorised to perform this action"