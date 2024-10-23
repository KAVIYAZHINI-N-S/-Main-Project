if city == 'Palladam':
            if blood_type == 'A+':
                donors = [
                    {'name': 'Arjun', 'contact': '9345******'},
                    {'name': 'Lakshmi', 'contact': '877861****'},
                    {'name': 'Selvaraj', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'A-':
                donors = [
                    {'name': 'Lee', 'contact': '9345******'},
                    {'name': 'Loi', 'contact': '877861****'},
                    {'name': 'Leo', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'O+':
                donors = [
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='O-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            else:
                donors = []  # Return an empty list for other blood types
            return donors