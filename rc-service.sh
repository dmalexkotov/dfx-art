#!/bin/sh                                                                                                                                                                                                                                                                      
#                                                                                                                                                                                                                                                                              
# PROVIDE: gunicornd                                                                                                                                                                                                                                                           
#                                                                                                                                                                                                                                                                              
# Filename: gunicornd                                                                                                                                                                                                                                                          
# Author: Frederic DELBOS - fred.delbos@gmail.com                                                                                                                                                                                                                              
# Created: Sat Sep 17 00:29:58 2011 (+0200)                                                                                                                                                                                                                                    
# Last-Updated: Sat Sep 17 02:04:02 2011 (+0200)                                                                                                                                                                                                                               
#           By: Frederic DELBOS - fred.delbos@gmail.com                                                                                                                                                                                                                        
#     Update #: 15                                                                                                                                                                                                                                                             
#                                                                                                                                                                                                                                                                              
#                                                                                                                                                                                                                                                                              


. /etc/rc.subr
name="gunicornd"
rcvar=`set_rcvar`
start_cmd="${name}_start"
stop_cmd=":"

load_rc_config $name

gunicornd_start()
{
    if checkyesno ${rcvar}; then
        /bin/su -c "/usr/local/bin/gunicorn --chdir /home/user/dfx_art --workers=4 --bind=0.0.0.0:8000 dfx_art.wsgi" - user
    fi
}

load_rc_config $name
run_rc_command "$1"