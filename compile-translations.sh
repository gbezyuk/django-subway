#!/bin/sh
echo 'Compiling translations; you need to have gettext installed'
cd core
../manage.py compilemessages -l ru
cd ..
cd subway
../manage.py compilemessages -l ru
cd ..
echo '\n'
