#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import glob

from config import host, server_workdir

def is_extension_contained(dir_path, ext_with_dot):
    file_name = os.path.join(dir_path, '*' + ext_with_dot)
    file_list = glob.glob(file_name)
    return len(file_list) > 0

def extract_last_element(fullpath, sp=os.sep):
    idx0 = fullpath.rfind(sp, 0, -1)
    return  fullpath[idx0 + len(sp) :]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        target_dir_path_local  = os.getcwd()
    else:
        # TODO: rm last /
        target_dir_path_local = sys.argv[1]

    if not is_extension_contained(target_dir_path_local, '.tex'):
        print("remotex: No file name specified, and I couldn't find any.")
        print('''Usage : ./remotex.py [target_dir_path_local]
        if there is no argument, this script looks in the directory
        which it called for .tex files.''')
    else:
        # transfers source files from local to remote
        rsync_texdir_command = 'rsync -auvz {0} {1}:{2}'\
                .format(target_dir_path_local, host, server_workdir)
        print('> ' + rsync_texdir_command)
        os.system(rsync_texdir_command)

        # executes latexmk remotely
        server_target_dir = extract_last_element(target_dir_path_local)
        target_dir_path_server = os.path.join(
                server_workdir, server_target_dir)
        ssh_latexmk_command = "ssh {0} 'cd {1}; latexmk'"\
                .format(host, target_dir_path_server)
        print('> ' + ssh_latexmk_command)
        os.system(ssh_latexmk_command)

        # receives a generated pdf file
        # TODO: receive only a target pdf file
        target_pdf_path_server = os.path.join(target_dir_path_server, '*.pdf')
        receive_pdf_command = 'scp {0}:{1} {2}'\
                .format(host, target_pdf_path_server, target_dir_path_local)
        print('> ' + receive_pdf_command)
        os.system(receive_pdf_command)

