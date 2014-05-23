#!/usr/bin/env bash
#
# Create BNew Modules Template
# Written by: levi Nachamni (levi0x0)
# Date: 21-05-2014

TEMP="../api/module_template.py"
EDITOR=`which vim`

create_module() {
	cp $TEMP "../modules/${module_name}.py"
	if [ -z $EDITOR ];then
		echo "[ERROR] vim Not Found, EDITOR = nano"
		EDITOR="nano"
	fi
	$EDITOR "../modules/${module_name}.py"
	echo "Done Saved to ../modules/${module_name}.py"
}

if [ -z $1 ];then
	echo -e "\nUsage: ./new_modules.sh [MODULE_NAME]"
	echo -e "\n\tExample: ./new_module.sh mymodule"
	exit
else
	module_name=$1
	create_module
fi


