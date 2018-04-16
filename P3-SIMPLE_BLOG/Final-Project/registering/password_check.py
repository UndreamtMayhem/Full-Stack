# Python dependencies
import re

def is_password_strong(password):
    target_score  = 1

    if len(password) <= 6 or len(password) > 14:
        return {
            'is_strong': False,
            'error_msg': "The password must be between 6 and 12 characters."
        }
    else:
        
        password_scores = {
            0:'Horrible', 
            1:'Weak', 
            2:'Medium', 
            3:'Strong'
        }

        password_strength = dict.fromkeys([
            'has_upper', 
            'has_lower', 
            'has_num'], 
            False
        )

        if re.search(r'[A-Z]', password):
            password_strength['has_upper'] = True

        if re.search(r'[a-z]', password):
            password_strength['has_lower'] = True

        if re.search(r'[0-9]', password):
            password_strength['has_num'] = True

        score = len([b for b in password_strength.values() if b])


        if score >= target_score:
            return {
                'is_strong': True,
                'score': password_scores[score]
            }
        else:
            return {
                'is_strong': False,
                'error_msg': "Password needs uppercase character, lowercase character and a number",
                'score': password_scores[score]
            }