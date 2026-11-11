#!/bin/bash
cd $1
rm -rf $DIR/*
for f in `ls *.txt`; do echo $f; done
