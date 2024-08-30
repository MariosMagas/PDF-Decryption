import pikepdf

def main(path, password):
    if path == '':
        result = 'No file selected'
        return result
    
    new_file = f'{path[:-4]}_unlocked'
    try:
        with pikepdf.open(path, password=password) as pdf:
            pdf.save(f'{new_file}.pdf')
    except Exception as e:
       _removed_path = str(e).split(': ') # e = python file path + error msg. Display of the entire path would force the app window to become unnecessarily wide. 
       result = f'Error : {_removed_path[1]}'
       return result

    result = 'Hooray!!!'
    return result