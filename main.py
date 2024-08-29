import pikepdf
from pikepdf import PasswordError

def unlock_and_save(original_pdf, password):
    unlocked_pdf = 'unlocked.pdf'
    try:
        with pikepdf.open(original_pdf, password=password) as pdf:
            pdf.save(unlocked_pdf)
            print('OK!!!')
    except PasswordError:
        print('Wrong Password!!!')
    except Exception as e:
        print(f'Error: {e}')


unlock_and_save(original_pdf='1.pdf', password='maris')