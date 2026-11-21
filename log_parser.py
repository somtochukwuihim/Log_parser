import os
import sys


def failed_logins(file_path):
 
    counts = {}
    incomplete_log = []

    if not os.path.exists(file_path):
        return f'File not found. Check if the file is in the right directory.'
    if os.path.isdir(file_path):
        return f'This {file_path} points to a directory not a file.'

    try:
        with open(file_path, 'r') as f:
            log_book = f.readlines()
            
            for line in (log_book):
                line = line.strip()
                if 'LOGIN' in line and 'FAILED' in line and 'user=' not in line:
                    incomplete_log.append(line)
                else:
                    if 'LOGIN' in line and 'FAILED' in line and 'user=' in line:  
                        parts = line.split()

                        for part in parts:
                            if part.startswith('user='):
                                user = part.split('=')[1]
                                if not user:
                                    incomplete_log.append(line)
                                else:
                                    counts[user] = counts.get(user, 0) + 1

            print('***Failed User Count***')
            incomplete_logs ='\n'.join(incomplete_log)
            for user, count in counts.items():
                print(f'{user}: {count}')
            print(' ')
            print('***Incomplete log***')
            print(f'{incomplete_logs}')
            return ' '
    except PermissionError:
        return f'You do not have permission to view this file{file_path}.\nAsk admin for such permission.'

if __name__=='__main__':
    if len(sys.argv)<2:
        print('ERROR: Missing isnputs')
        print('Usage: python log_parser.py <path_to_log_file>')
        sys.exit()

file_path = sys.argv[1]
failed_logins(file_path)
    