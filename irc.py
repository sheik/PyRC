class IRCMessage:
    def __init__(self, message):
        self.message = message = message.replace('\r\n','')
        self.prefix = ''
        self.parameters = []

        pfx_end = -1

        # build prefix
        if message.startswith(':'):
            pfx_end = message.find(' ')
            self.prefix = message[1:pfx_end]

        # get trailing portion
        trail_start = message.find(' :')
        if trail_start >= 0:
            trailing = message[trail_start+2:]
        else:
            trail_start = len(message)

        # build command and parameters
        cmd_par = message[pfx_end+1:trail_start].split(' ')
        self.command = cmd_par[0]

        # populate parameters if they exist
        if len(cmd_par) > 1:
           self.parameters = cmd_par[1:]

        # If trailing exists, append to parameters
        if 'trailing' in locals():
            self.parameters.append(trailing)

