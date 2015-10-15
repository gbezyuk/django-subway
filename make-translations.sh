#!/bin/sh
echo 'Compiling translations; you need to have gettext installed'
cd core
../manage.py makemessages -l ru
cd ..
cd subway
../manage.py makemessages -l ru
cd ..
echo '\n'
