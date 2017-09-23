#!/bin/bash
d=`date +%y-%m-%d-%H-%M-%S`


# just to have in on one place :)
git add .
git config user.name "mincaeuro"
git config user.email "mincaeuro@gmail.com"
git commit -m "update_$d"
git push
